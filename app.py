from flask import Flask, render_template

app = Flask(__name__)

# 全局标题变量
SITE_TITLE = "⇒ LG4E - Logic For Everybody"

# 将全局变量传递给所有模板
@app.context_processor
def inject_site_title():
    return dict(site_title=SITE_TITLE)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/set-theory-and-logic')
def set_theory_and_logic():
    return render_template('set_theory_and_logic.html', title="Set theory and logic")

@app.route('/set-theory-and-logic/chapter/<int:chapter_id>')
def chapter(chapter_id):
    # 章节信息
    chapters = {
        1: "Fundamental Concepts",
        2: "Functions",
        3: "Relations",
        4: "The Integers and the Real Numbers",
        5: "Cartesian Products",
        6: "Finite Sets",
        7: "Countable and Uncountable Sets",
        8: "The Principle of Recursive Definition",
        9: "Infinite Sets and the Axiom of Choice",
        10: "Well-Ordered Sets",
        11: "The Maximum Principle",
    }

    # 获取章节标题
    chapter_title = chapters.get(chapter_id, "Chapter not found")
    if chapter_title == "Chapter not found":
        return render_template('404.html', title="404 - Not Found"), 404

    # 渲染章节页面
    return render_template('chapter.html', chapter_title=chapter_title, chapter_id=chapter_id)

@app.route('/logic-study-guide')
def logic_study_guide():
    return render_template('logic_study_guide.html', title="Logic Study Guide")

if __name__ == '__main__':
    app.run(debug=True)

