try:
    from flask import Flask, current_app, g, request
except ImportError:
    print("该题演示需要第三方库 flask:pip install flask,原理见正文")
    raise SystemExit(0)

app = Flask(__name__)
app.config['DB'] = 'sqlite:///:memory:'

def get_db():
    if 'db' not in g:                      # g 生命周期:一个请求
        g.db = current_app.config['DB']    # 请求内缓存连接
    return g.db

@app.get('/who')
def who():
    return {'db': get_db(), 'path': request.path}

# 离线/测试脚本中必须手动推上下文
with app.app_context():
    print(current_app.config['DB'])

with app.test_request_context('/who'):
    print(get_db(), request.path)
