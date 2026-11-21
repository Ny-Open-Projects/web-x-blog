try:
    from fastapi import FastAPI, Response
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

@app.post('/login')
def login(username: str, password: str, response: Response):
    # 实际:校验密码后签发 session id 或 JWT
    response.set_cookie(
        key='sessionid',
        value='fake-session-id',
        httponly=True,       # 防 XSS 读取
        secure=True,         # 仅 HTTPS
        samesite='lax',      # 防 CSRF,允许顶级导航
        max_age=3600,        # 1 小时
        path='/',
    )
    return {'msg': 'logged in'}

@app.post('/logout')
def logout(response: Response):
    response.delete_cookie('sessionid', path='/')
    return {'msg': 'logged out'}
