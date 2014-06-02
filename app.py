from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config.from_pyfile('local_settings.py')

@app.route('/')
def index():
    return render_template('indx.html')


if __name__ == '__main__':
    app.run()
