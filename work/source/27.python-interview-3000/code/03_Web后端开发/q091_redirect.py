try:
    from fastapi import FastAPI
    from fastapi.responses import RedirectResponse
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

@app.get('/old-api')
def old_api():
    # 308 永久且保持方法;上线一段时间确认无流量后可下线
    return RedirectResponse('/new-api', status_code=308)

@app.post('/login-legacy')
def login_legacy():
    # 307 保证 POST 方法与请求体原样转发到新地址
    return RedirectResponse('/login', status_code=307)

@app.get('/new-api')
def new_api():
    return {'msg': 'new api'}
