from flask import Flask
from db.init_db import init_db
from routes.todos import todo_bp

# Flaskアプリを作成・設定する
def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_bp)
    init_db()
    return app


if __name__ == "__main__":
    
    app = create_app()
    app.run(debug=True)