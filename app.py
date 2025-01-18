from flask import Flask, render_template, request
from markupsafe import Markup
import os
import markdown
from markdown.extensions import fenced_code, tables
from config import CARDS
import logging

# 初始化 Flask 应用
app = Flask(__name__)

# 配置日志
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# 全局常量
SITE_TITLE = "(∀) LG4E - Logic For Everybody"
DEFAULT_404_TEMPLATE = "404.html"
DEFAULT_500_TEMPLATE = "500.html"
MARKDOWN_EXTENSIONS = [
    fenced_code.FencedCodeExtension(),
    tables.TableExtension()
]

# 将全局变量传递给所有模板
@app.context_processor
def inject_globals():
    return {
        "site_title": SITE_TITLE,
        "cards": CARDS,  # 传递所有卡片数据，用于动态导航
    }

# 通用函数：渲染 Markdown 文件
def render_markdown_file(file_path):
    if os.path.exists(file_path):
        logging.info(f"Rendering Markdown file: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                md_content = file.read()
            return markdown.markdown(md_content, extensions=MARKDOWN_EXTENSIONS)
        except Exception as e:
            logging.error(f"Failed to render Markdown file {file_path}: {e}")
            return "<p>Failed to load content. Please try again later.</p>"
    logging.warning(f"Markdown file not found: {file_path}")
    return "<p>Content not available yet. Stay tuned!</p>"

# 通用函数：获取卡片数据或返回 404
def get_card_or_404(card_slug):
    card_data = CARDS.get(card_slug)
    if not card_data:
        logging.warning(f"Card not found: {card_slug}")
        return render_template(DEFAULT_404_TEMPLATE, title="404 - Not Found"), 404
    return card_data

# 自定义 404 错误页面
@app.errorhandler(404)
def not_found(e):
    logging.warning(f"404 error occurred: {request.path}")
    return render_template(DEFAULT_404_TEMPLATE, title="404 - Page Not Found"), 404

# 自定义 500 错误页面
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"500 error occurred: {str(e)}")
    return render_template(DEFAULT_500_TEMPLATE, title="500 - Internal Server Error"), 500

# 首页
@app.route('/')
def home():
    logging.info("Home page accessed.")
    return render_template('index.html')

# Tutorials 页面
@app.route('/tutorials')
def tutorials():
    logging.info("Tutorials page accessed.")
    return render_template('tutorials.html', cards=CARDS)

# 卡片页面（显示章节列表）
@app.route('/tutorials/<card_slug>')
def card(card_slug):
    logging.info(f"Card page accessed: {card_slug}")
    card_data = get_card_or_404(card_slug)
    if isinstance(card_data, tuple):
        return card_data

    # 动态传递章节信息
    chapters = card_data["chapters"]
    template_path = f'{card_slug}.html'
    if not os.path.exists(os.path.join("templates", template_path)):
        logging.warning(f"Template for card not found: {template_path}")
        return render_template('404.html', title="404 - Not Found"), 404

    # 渲染卡片目录页面
    return render_template(
        template_path,
        title=card_data["title"],
        card_slug=card_slug,
        chapters=chapters,
    )

# 章节页面（显示 Markdown 内容）
@app.route('/tutorials/<card_slug>/chapter/<int:chapter_id>')
def chapter(card_slug, chapter_id):
    logging.info(f"Chapter page accessed: {card_slug} - Chapter {chapter_id}")
    card_data = get_card_or_404(card_slug)
    if isinstance(card_data, tuple):
        return card_data

    chapter_title = card_data["chapters"].get(chapter_id)
    if not chapter_title:
        logging.warning(f"Chapter not found: {chapter_id} in card {card_slug}")
        return render_template(DEFAULT_404_TEMPLATE, title="404 - Not Found"), 404

    markdown_file = os.path.join("content", f"{card_slug}_chapter_{chapter_id}.md")
    html_content = render_markdown_file(markdown_file)

    return render_template(
        'chapter.html',
        title=f"{card_data['title']} - {chapter_title}",
        chapter_title=chapter_title,
        content=Markup(html_content),
    )

if __name__ == '__main__':
    logging.info("Starting Flask application.")
    app.run(debug=True)

