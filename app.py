from flask import Flask, render_template, url_for, make_response

app = Flask(__name__)
app.config.from_pyfile('local_settings.py')

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('index.html'), 302)

if __name__ == '__main__':
    app.run()
