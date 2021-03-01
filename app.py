from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def hello():
    ret = open("templates/index.html").read()
    return render_template('index.html')

@app.route("/blog")
def blog():
    ret = open("templates/blog.html").read()
    from data import blog
    return render_template('blog.html', blog = blog)

if __name__ == '__main__':
    app.run(debug=True)