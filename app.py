from flask import Flask
from flask import request,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def hello():
    return render_template('hello.html')

@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


if __name__ == '__main__':
    app.run(debug=True,port=1200)
