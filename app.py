from flask import Flask, render_template, request, abort
from markupsafe import Markup
import os
import markdown
from config import CATEGORIES, BOOKS, MARKDOWN_EXTENSIONS
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
SITE_TITLE = "(\u2200) LG4E - Logic For Everybody"
DEFAULT_404_TEMPLATE = "404.html"
DEFAULT_500_TEMPLATE = "500.html"

@app.context_processor
def inject_globals():
    """将全局变量传递给模板"""
    return {
        "site_title": SITE_TITLE,
        "categories": CATEGORIES,
    }

def render_markdown_file(file_path):
    """通用函数：渲染 Markdown 文件"""
    if os.path.exists(file_path):
        logging.info(f"Rendering Markdown file: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                md_content = file.read()
            
            # 使用 Markdown 解析，支持多种扩展
            html_content = markdown.markdown(md_content, extensions=MARKDOWN_EXTENSIONS)
            
            # 确保 HTML 代码不会被 Jinja2 过滤
            return Markup(html_content)

        except Exception as e:
            logging.error(f"Failed to render Markdown file {file_path}: {e}")
            return Markup("<p class='text-danger'>Failed to load content. Please try again later.</p>")
    
    logging.warning(f"Markdown file not found: {file_path}")
    return Markup("<p class='text-warning'>Content not available yet. Stay tuned!</p>")

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
    """分类页面"""
    logging.info("Tutorials page accessed.")
    return render_template('tutorials.html', categories=CATEGORIES)

@app.route('/tutorials/<category_slug>')
def category(category_slug):
    """显示特定分类下的书籍"""
    logging.info(f"Category page accessed: {category_slug}")

    # 从 CATEGORIES 提取分类数据
    category_data = CATEGORIES.get(category_slug)
    if not category_data:
        logging.error(f"Category not found: {category_slug}")
        return render_template(DEFAULT_404_TEMPLATE, title="404 - Category Not Found"), 404

    # 获取该分类下的书籍
    books = BOOKS.get(category_slug, [])
    logging.info(f"Books under category '{category_slug}': {books}")

    # 渲染模板
    return render_template('category.html', category_data=category_data, category_slug=category_slug, books=books, title=category_data["title"], description=category_data["description"])

@app.route('/api/category/<category_slug>/book/<book_slug>')
def get_book_data(category_slug, book_slug):
    """API 路由：返回书籍目录数据"""
    logging.info(f"Fetching book data for category '{category_slug}', book '{book_slug}'")

    # 检查分类数据
    category_data = CATEGORIES.get(category_slug)
    if not category_data:
        logging.warning(f"Category not found: {category_slug}")
        return {"error": "Category not found"}, 404

    # 检查书籍数据
    books_in_category = BOOKS.get(category_slug, [])
    book_data = next((book for book in books_in_category if book['slug'] == book_slug), None)
    if not book_data:
        logging.warning(f"Book not found in category '{category_slug}': {book_slug}")
        return {"error": "Book not found"}, 404

    # 确保返回的数据结构一致
    response_data = {
        "title": book_data.get("title", "Untitled"),
        "parts": book_data.get("parts", {})  # 如果 parts 为空，则返回空字典
    }

    return response_data, 200

@app.route('/tutorials/<category_slug>/<book_slug>/preface')
def book_preface(category_slug, book_slug):
    """显示书籍详细信息，包括从 Markdown 文件加载内容"""
    logging.info(f"Book preface page accessed: {category_slug}/{book_slug}")
    
    # 获取书籍信息
    book = get_book_or_404(category_slug, book_slug)
    
    # 构建 Markdown 文件路径
    markdown_file = os.path.join("content", category_slug, book_slug, "preface.md")
    
    # 渲染 Markdown 文件内容
    html_content = render_markdown_file(markdown_file)
    
    # 如果 Markdown 文件加载失败，返回默认内容
    if html_content.startswith("<p>Failed to load content"):
        html_content = "<p>No preface content is available for this book.</p>"
    
    # 渲染模板
    return render_template(
        'book_preface.html',
        book=book,
        title=f"{book['title']} - Perface",
        content=Markup(html_content)  # 将 HTML 内容传递给模板
    )

@app.route('/tutorials/<category_slug>/<book_slug>/author')
def book_author(category_slug, book_slug):
    """显示书籍作者信息，包括从 Markdown 文件加载内容"""
    logging.info(f"Book preface page accessed: {category_slug}/{book_slug}")
    
    # 获取书籍信息
    book = get_book_or_404(category_slug, book_slug)
    
    # 构建 Markdown 文件路径
    markdown_file = os.path.join("content", category_slug, book_slug, "author.md")
    
    # 渲染 Markdown 文件内容
    html_content = render_markdown_file(markdown_file)
    
    # 如果 Markdown 文件加载失败，返回默认内容
    if html_content.startswith("<p>Failed to load content"):
        html_content = "<p>No author content is available for this book.</p>"
    
    # 渲染模板
    return render_template(
        'book_author.html',
        book=book,
        title=f"{book['title']} - Author",
        content=Markup(html_content)  # 将 HTML 内容传递给模板
    )


@app.route('/tutorials/<category_slug>/<book_slug>/chapter/<int:chapter_id>')
def chapter(category_slug, book_slug, chapter_id):
    """显示章节内容并支持小节跳转"""
    logging.info(f"Chapter page accessed: {category_slug}/{book_slug} - Chapter {chapter_id}")
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

    # 渲染 Markdown 文件
    markdown_file = os.path.join("content", category_slug, book_slug, f"chapter_{chapter_id}.md")
    html_content = render_markdown_file(markdown_file)

    return render_template(
        'chapter.html',
        book_title=book["title"],
        chapter_title=chapter_data["title"],
        chapter_id=chapter_id,
        sections=chapter_data.get("sections", {}),
        content=Markup(html_content),
    )

if __name__ == '__main__':
    logging.info("Starting Flask application.")
    app.run(debug=True)

