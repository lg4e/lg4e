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
    """将全局变量传递给模板"""
    return {
        "site_title": SITE_TITLE,
        "cards": CARDS,
    }

def render_markdown_file(file_path):
    """通用函数：渲染 Markdown 文件"""
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

def get_card_or_404(card_slug):
    """通用函数：获取卡片数据或返回 404"""
    card_data = CARDS.get(card_slug)
    if not card_data:
        logging.warning(f"Card not found: {card_slug}")
        return render_template(DEFAULT_404_TEMPLATE, title="404 - Not Found"), 404
    return card_data

@app.errorhandler(404)
def not_found(e):
    """自定义 404 错误页面"""
    logging.warning(f"404 error occurred: {request.path}")
    return render_template(DEFAULT_404_TEMPLATE, title="404 - Page Not Found"), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """自定义 500 错误页面"""
    logging.error(f"500 error occurred: {str(e)}")
    return render_template(DEFAULT_500_TEMPLATE, title="500 - Internal Server Error"), 500

@app.route('/')
def home():
    """首页"""
    logging.info("Home page accessed.")
    return render_template('index.html')

@app.route('/tutorials')
def tutorials():
    """Tutorials 页面"""
    logging.info("Tutorials page accessed.")
    return render_template('tutorials.html', cards=CARDS)

@app.route('/tutorials/<card_slug>')
def card(card_slug):
    """卡片页面（显示 PART -> Chapter -> Section）"""
    logging.info(f"Card page accessed: {card_slug}")
    card_data = get_card_or_404(card_slug)
    if isinstance(card_data, tuple):
        return card_data

    # 确保将章节和小节数据传递到模板
    for part_id, part in card_data.get("parts", {}).items():
        for chapter_id, chapter_data in part.get("chapters", {}).items():
            if isinstance(chapter_data, dict) and "sections" in chapter_data:
                logging.info(f"Chapter {chapter_id} contains sections: {chapter_data['sections']}")

    # 渲染通用模板
    return render_template(
        'content_template.html',
        title=card_data["title"],
        card_slug=card_slug,
        parts=card_data.get("parts", {})
    )

@app.route('/tutorials/<card_slug>/chapter/<int:chapter_id>')
def chapter(card_slug, chapter_id):
    """章节页面（显示 Markdown 内容）"""
    logging.info(f"Chapter page accessed: {card_slug} - Chapter {chapter_id}")
    card_data = get_card_or_404(card_slug)
    if isinstance(card_data, tuple):
        return card_data

    # 查找章节数据
    chapter_data = None
    chapter_title = None
    sections = None
    for part in card_data.get("parts", {}).values():
        chapters = part.get("chapters", {})
        if chapter_id in chapters:
            chapter_data = chapters.get(chapter_id)
            if isinstance(chapter_data, dict):  # 如果章节有小节
                chapter_title = chapter_data.get("title", f"Chapter {chapter_id}")
                sections = chapter_data.get("sections", {})
            else:  # 如果章节没有小节
                chapter_title = chapter_data
            break

    # 如果未找到章节
    if not chapter_data:
        logging.warning(f"Chapter not found: {chapter_id} in card {card_slug}")
        return render_template(DEFAULT_404_TEMPLATE, title="404 - Not Found"), 404

    # 渲染 Markdown 文件
    markdown_file = os.path.join("content", f"{card_slug}_chapter_{chapter_id}.md")
    html_content = render_markdown_file(markdown_file)
    logging.info(f"Rendered HTML content preview: {html_content[:500]}")  # 打印渲染的HTML

    # 为每个 Section 添加锚点
    if sections:
        logging.info(f"Adding anchors for sections in chapter {chapter_id}")
        for section_id, section_title in sections.items():
            # 动态生成小节标题
            section_header = f"{chapter_id}.{section_id} {section_title}"  # 标题内容
            search_pattern = f"<h2>{section_header}</h2>"  # 在HTML中匹配标题
            logging.info(f"Searching for header: {search_pattern}")
            if search_pattern in html_content:
                # 替换标题，添加id和锚点
                html_content = html_content.replace(
                    search_pattern,
                    f'<h2 id="section-{section_id}">{section_header}</h2>'
                )
                logging.info(f"Added anchor for section: {section_id} - {section_title}")
            else:
                logging.warning(f"Section '{section_title}' not found in HTML content for chapter {chapter_id}")

    # 获取 URL 参数中的 section 信息
    selected_section = request.args.get("section", None)

    # 渲染章节页面
    return render_template(
        'chapter.html',
        title=f"{card_data['title']} - {chapter_title}",
        chapter_title=chapter_title,
        content=Markup(html_content),
        selected_section=selected_section,  # 传递 section 参数给模板
    )

if __name__ == '__main__':
    logging.info("Starting Flask application.")
    app.run(debug=True)

