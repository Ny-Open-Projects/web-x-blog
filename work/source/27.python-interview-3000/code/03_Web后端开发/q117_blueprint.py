try:
    from flask import Flask, Blueprint, jsonify, url_for
except ImportError:
    print("该题演示需要第三方库 flask:pip install flask,原理见正文")
    raise SystemExit(0)

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

@users_bp.get('')
def list_users():
    return jsonify([{'id': 1, 'name': 'alice'}])

@users_bp.get('/<int:uid>')
def get_user(uid: int):
    return jsonify({'id': uid, 'name': 'alice'})

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(users_bp)
    with app.test_request_context():
        print(url_for('users.get_user', uid=42))  # /api/users/42
    return app

if __name__ == '__main__':
    create_app().run(port=5000)
