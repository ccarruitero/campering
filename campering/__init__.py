from flask import Flask, render_template, url_for, make_response
from roads import roads_app
from campering.shared.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('local_settings.py')
    db.init_app(app)
    return app

app = create_app()
app.register_blueprint(roads_app, url_prefix='/api/v0.1/roads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('index.html'), 302)

if __name__ == '__main__':
    app.run()
