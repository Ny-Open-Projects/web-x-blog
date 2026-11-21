import time
try:
    from flask import Flask, g, request
except ImportError:
    print("该题演示需要第三方库 flask:pip install flask,原理见正文")
    raise SystemExit(0)

app = Flask(__name__)
logs: list[str] = []

@app.before_request
def start_timer():
    g.start = time.perf_counter()
    logs.append(f'start {request.path}')

@app.after_request
def add_header(response):
    cost = round((time.perf_counter() - g.start) * 1000, 2)
    response.headers['X-Cost-Ms'] = str(cost)
    logs.append(f'end {request.path}')
    return response

@app.teardown_appcontext
def close_db(exc):
    logs.append('teardown app context')   # 关闭 g 中缓存连接的典型位置

@app.get('/')
def index():
    return {'ok': True}

if __name__ == '__main__':
    app.run(port=5000)
