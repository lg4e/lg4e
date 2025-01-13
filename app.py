from flask import Flask, render_template
from markupsafe import Markup
import os
import markdown
from markdown.extensions import fenced_code, tables
from config import CARDS

app = Flask(__name__)

# 全局标题变量
SITE_TITLE = "⇒ LG4E - Logic For Everybody"

# 将全局变量传递给所有模板
@app.context_processor
def inject_globals():
    return {
        "site_title": SITE_TITLE,
        "cards": CARDS,  # 传递所有卡片数据，用于动态导航
    }

# 自定义 404 错误页面
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', title="404 - Page Not Found"), 404

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
    # 获取卡片数据
    card_data = CARDS.get(card_slug)
    if not card_data:
        return render_template('404.html', title="404 - Not Found"), 404

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
    # 获取卡片数据
    card_data = CARDS.get(card_slug)
    if not card_data:
        return render_template('404.html', title="404 - Not Found"), 404

    # 获取章节数据
    chapter_title = card_data["chapters"].get(chapter_id)
    if not chapter_title:
        return render_template('404.html', title="404 - Not Found"), 404

    # 确保路径安全
    safe_card_slug = card_slug.replace("/", "").replace("\\", "")
    markdown_file = os.path.join("content", f"{safe_card_slug}_chapter_{chapter_id}.md")

    # 加载 Markdown 文件
    if os.path.exists(markdown_file):
        with open(markdown_file, 'r', encoding='utf-8') as file:
            md_content = file.read()
        # 使用 markdown 渲染内容，并支持其他扩展
        html_content = markdown.markdown(
            md_content,
            extensions=[
                fenced_code.FencedCodeExtension(),  # 支持代码块
                tables.TableExtension()           # 支持表格
            ]
        )
    else:
        html_content = "<p>Content not available yet. Stay tuned!</p>"

    # 渲染章节页面
    return render_template(
        'chapter.html',
        title=f"{card_data['title']} - {chapter_title}",
        chapter_title=chapter_title,
        chapter_id=chapter_id,
        content=Markup(html_content),
    )

@app.route('/tutorials/<card_slug>/references')
def references(card_slug):
    # 获取卡片数据
    card_data = CARDS.get(card_slug)
    if not card_data:
        return render_template('404.html', title="404 - Not Found"), 404

    # 确保路径安全
    safe_card_slug = card_slug.replace("/", "").replace("\\", "")
    markdown_file = os.path.join("content", f"{safe_card_slug}_references.md")

    # 加载 Markdown 文件
    if os.path.exists(markdown_file):
        with open(markdown_file, 'r', encoding='utf-8') as file:
            md_content = file.read()
        html_content = markdown.markdown(
            md_content,
            extensions=[
                fenced_code.FencedCodeExtension(),
                tables.TableExtension()
            ]
        )
    else:
        html_content = "<p>参考书籍内容尚未添加。</p>"

    # 渲染参考书籍页面
    return render_template(
        'references.html',
        title=f"{card_data['title']} - 参考书籍",
        content=Markup(html_content),
    )

if __name__ == '__main__':
    app.run(debug=True)

