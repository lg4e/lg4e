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

@app.route('/logic-study-guide')
def logic_study_guide():
    return render_template('logic_study_guide.html', title="Logic Study Guide")

if __name__ == '__main__':
    app.run(debug=True)

