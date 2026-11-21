try:
    from flask import Flask, jsonify, request
    from flask.signals import request_finished
except ImportError:
    print("该题演示需要第三方库 flask:pip install flask,原理见正文")
    raise SystemExit(0)

app = Flask(__name__)

@request_finished.connect_via(app)
def audit(sender, response, **extra):
    print(f'audit: {request.path} -> {response.status_code}')

class APIError(Exception):
    def __init__(self, message: str, status: int = 400):
        super().__init__(message)
        self.message = message
        self.status = status

@app.errorhandler(APIError)
def handle_api_error(e: APIError):
    return jsonify({'error': e.message}), e.status

@app.get('/items/<int:item_id>')
def get_item(item_id: int):
    if item_id > 100:
        raise APIError('item not found', 404)
    return jsonify({'id': item_id})

if __name__ == '__main__':
    app.run(port=5000)
