from flask import Flask, render_template, request, abort, jsonify
from markupsafe import Markup
import os
import logging
from docutils.core import publish_parts
from config import CATEGORIES, BOOKS
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
# from functools import lru_cache  # 添加缓存装饰器
from pathlib import Path  # 使用 Path 处理路径

# 初始化 Flask 应用
app = Flask(__name__)

# 配置日志
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    encoding='utf-8'  # 明确指定编码
)

# 全局常量
class Config:
    SITE_TITLE = "(\u2200) LG4E - Logic For Everybody"
    DEFAULT_404_TEMPLATE = "404.html"
    DEFAULT_500_TEMPLATE = "500.html"
    CONTENT_DIR = Path(app.root_path) / 'content'  # 使用 Path 对象

# Sphinx配置
app.config.update(
    SPHINX_PROJECT='your_project_name',
    SPHINX_SOURCE=str(Config.CONTENT_DIR),
    SPHINX_BUILD=str(Path(app.root_path) / '_build')
)

@app.context_processor
def inject_globals():
    """将全局变量传递给模板"""
    return {
        "site_title": Config.SITE_TITLE,
        "categories": CATEGORIES,
    }

#@lru_cache(maxsize=100)  # 添加缓存装饰器
def render_rst_file(file_path: str) -> Markup:
 #   """通用函数：渲染 RST 文件，添加缓存以提高性能"""
    path = Path(file_path)
    if not path.exists():
        logging.warning(f"RST file not found: {file_path}")
        return Markup("<p class='text-warning'>Content not available yet. Stay tuned!</p>")

    try:
        content = path.read_text(encoding='utf-8')
        html_content = publish_parts(
            source=content,
            writer_name='html',
            settings_overrides={
                'math_output': 'MathJax',  # MathJax を有効化
                'math_opts': {             # 数式レンダリングオプション
                    'format': 'mathjax',
                    'font_encoding': 'UTF-8'
                },
                'input_encoding': 'utf-8',  # 入出力エンコーディング指定
                'output_encoding': 'utf-8',
                'halt_level': 4            # エラー制御を厳格化
            }
        )['html_body']
        return Markup(html_content)
    except Exception as e:
        logging.error(f"Failed to render RST file {file_path}: {e}")
        return Markup("<p class='text-danger'>Failed to load content. Please try again later.</p>")

def get_category_or_404(category_slug):
    """获取分类数据或返回 404"""
    category = CATEGORIES.get(category_slug)
    if not category:
        logging.warning(f"Category not found: {category_slug}")
        abort(404, description="Category not found")
    return category

def get_books_by_category(category_slug):
    """获取分类下的书籍列表"""
    books = BOOKS.get(category_slug, [])
    if not books:
        logging.warning(f"No books found for category: {category_slug}")
    return books

def get_book_or_404(category_slug, book_slug):
    """获取书籍数据或返回 404"""
    books = get_books_by_category(category_slug)
    for book in books:
        if book["slug"] == book_slug:
            return book
    logging.warning(f"Book not found: {book_slug} in category {category_slug}")
    abort(404, description="Book not found")

@app.errorhandler(404)
def not_found(e):
    """自定义 404 错误页面"""
    logging.warning(f"404 error occurred: {request.path}", exc_info=True)
    return render_template(Config.DEFAULT_404_TEMPLATE, title="404 - Page Not Found"), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """自定义 500 错误页面，添加更详细的错误日志"""
    logging.error(f"500 error occurred: {str(e)}", exc_info=True)
    return render_template(Config.DEFAULT_500_TEMPLATE, title="500 - Internal Server Error"), 500

@app.route('/')
def home():
    """首页"""
    logging.info("Home page accessed.")
    return render_template('index.html')

@app.route('/tutorials')
def tutorials():
    """分类页面"""
    logging.info("Tutorials page accessed.")
    return render_template('tutorials.html', categories=CATEGORIES)

@app.route('/tutorials/<category_slug>')
def category(category_slug):
    """显示特定分类下的书籍"""
    logging.info(f"Category page accessed: {category_slug}")

    category_data = CATEGORIES.get(category_slug)
    if not category_data:
        logging.error(f"Category not found: {category_slug}")
        return render_template(Config.DEFAULT_404_TEMPLATE, title="404 - Category Not Found"), 404

    books = BOOKS.get(category_slug, [])
    logging.info(f"Books under category '{category_slug}': {books}")

    return render_template('category.html', category_data=category_data, category_slug=category_slug, books=books, title=category_data["title"], description=category_data["description"])

@app.route('/api/category/<category_slug>/book/<book_slug>')
def get_book_data(category_slug, book_slug):
    """API 路由：返回书籍目录数据"""
    logging.info(f"Fetching book data for category '{category_slug}', book '{book_slug}'")

    category_data = CATEGORIES.get(category_slug)
    if not category_data:
        logging.warning(f"Category not found: {category_slug}")
        return jsonify({"error": "Category not found"}), 404

    books_in_category = BOOKS.get(category_slug, [])
    book_data = next((book for book in books_in_category if book['slug'] == book_slug), None)
    if not book_data:
        logging.warning(f"Book not found in category '{category_slug}': {book_slug}")
        return jsonify({"error": "Book not found"}), 404

    response_data = {
        "title": book_data.get("title", "Untitled"),
        "parts": book_data.get("parts", {})
    }

    return jsonify(response_data), 200

@app.route('/tutorials/<category_slug>/<book_slug>/preface')
def book_preface(category_slug, book_slug):
    """显示书籍前言（RST 解析）"""
    logging.info(f"Book preface page accessed: {category_slug}/{book_slug}")
    book = get_book_or_404(category_slug, book_slug)

    rst_file = os.path.join("content", category_slug, book_slug, "preface.rst")
    html_content = render_rst_file(rst_file)

    return render_template(
        'book_preface.html',
        book=book,
        title=f"{book['title']} - Preface",
        content=html_content
    )

@app.route('/tutorials/<category_slug>/<book_slug>/author')
def book_author(category_slug, book_slug):
    """显示书籍作者信息（RST 解析）"""
    logging.info(f"Book author page accessed: {category_slug}/{book_slug}")
    book = get_book_or_404(category_slug, book_slug)

    rst_file = os.path.join("content", category_slug, book_slug, "author.rst")
    html_content = render_rst_file(rst_file)

    return render_template(
        'book_author.html',
        book=book,
        title=f"{book['title']} - Author",
        content=html_content
    )

@app.route('/tutorials/<category_slug>/<book_slug>/chapter/<int:chapter_id>')
def chapter(category_slug, book_slug, chapter_id):
    """显示章节内容（RST 解析）"""
    logging.info(f"Chapter page accessed: {category_slug}/{book_slug} - Chapter {chapter_id}")
    
    # 获取书籍信息
    book = get_book_or_404(category_slug, book_slug)
    parts = book.get("parts", {})

    # 遍历获取章节和小节数据
    chapter_data = None
    for part in parts.values():
        chapters = part.get("chapters", {})
        if chapter_id in chapters:
            chapter_data = chapters[chapter_id]
            break

    if not chapter_data:
        logging.warning(f"Chapter {chapter_id} not found in book {book_slug}")
        abort(404, description="Chapter not found")

    # 渲染 RST 文件（替换 Markdown 方式）
    rst_file = os.path.join("content", category_slug, book_slug, f"chapter_{chapter_id}.rst")
    html_content = render_rst_file(rst_file)

    return render_template(
        'chapter.html',
        book_title=book["title"],
        chapter_title=chapter_data["title"],  # 章节标题仍然从 parts 数据获取
        chapter_id=chapter_id,
        sections=chapter_data.get("sections", {}),  # 保持原样
        content=Markup(html_content),
    )

@app.route('/about')
def about():
    """About 页面（静态内容）"""
    logging.info("About page accessed")
    return render_template('about.html', title="About LG4E")

if __name__ == '__main__':
    logging.info("Starting Flask application.")
    app.run(debug=True)

