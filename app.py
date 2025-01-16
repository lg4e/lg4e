from flask import Flask, render_template
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

# 全局标题变量
SITE_TITLE = "(\u2200) LG4E - Logic For Everybody"

# 将全局变量传递给所有模板
@app.context_processor
def inject_globals():
    return {
        "site_title": SITE_TITLE,
        "cards": CARDS,  # 传递所有卡片数据，用于动态导航
    }

# 通用函数：渲染 Markdown 文件
def render_markdown_file(file_path):
    """渲染 Markdown 文件为 HTML"""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            md_content = file.read()
        return markdown.markdown(
            md_content,
            extensions=[
                fenced_code.FencedCodeExtension(),  # 支持代码块
                tables.TableExtension()            # 支持表格
            ]
        )
    return "<p>Content not available yet. Stay tuned!</p>"

# 通用函数：获取卡片数据或返回 404
def get_card_or_404(card_slug):
    """获取卡片数据或返回 404"""
    card_data = CARDS.get(card_slug)
    if not card_data:
        return render_template('404.html', title="404 - Not Found"), 404
    return card_data

# 自定义 404 错误页面
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', title="404 - Page Not Found"), 404

# 自定义 500 错误页面
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Error: {str(e)}")
    return render_template('500.html', title="500 - Internal Server Error"), 500

# 首页
@app.route('/')
def home():
    return render_template('index.html')

# Tutorials 页面
@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html', cards=CARDS)

# 卡片页面（显示章节列表）
@app.route('/tutorials/<card_slug>')
def card(card_slug):
    card_data = get_card_or_404(card_slug)
    if isinstance(card_data, tuple):  # 如果返回了 404 页面
        return card_data

    # 渲染卡片页面，显示章节列表
    return render_template(
        'card.html',
        title=card_data["title"],
        chapters=card_data["chapters"],
        card_slug=card_slug,  # 传递 card_slug 用于生成章节链接
    )

# 章节页面（显示 Markdown 内容）
@app.route('/tutorials/<card_slug>/chapter/<int:chapter_id>')
def chapter(card_slug, chapter_id):
    card_data = get_card_or_404(card_slug)
    if isinstance(card_data, tuple):
        return card_data

    chapter_title = card_data["chapters"].get(chapter_id)
    if not chapter_title:
        return render_template('404.html', title="404 - Not Found"), 404

    markdown_file = os.path.join("content", f"{card_slug}_chapter_{chapter_id}.md")
    html_content = render_markdown_file(markdown_file)

    return render_template(
        'chapter.html',
        title=f"{card_data['title']} - {chapter_title}",
        chapter_title=chapter_title,
        content=Markup(html_content),
    )

# 参考书籍页面
@app.route('/tutorials/<card_slug>/references')
def references(card_slug):
    card_data = get_card_or_404(card_slug)
    if isinstance(card_data, tuple):
        return card_data

    markdown_file = os.path.join("content", f"{card_slug}_references.md")
    html_content = render_markdown_file(markdown_file)

    return render_template(
        'references.html',
        title=f"{card_data['title']} - 参考书籍",
        content=Markup(html_content),
    )

if __name__ == '__main__':
    app.run(debug=True)
