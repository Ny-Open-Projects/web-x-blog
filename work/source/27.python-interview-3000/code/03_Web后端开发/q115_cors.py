try:
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://app.example.com'],  # 明确列出前端域名
    allow_credentials=True,                      # 允许携带 cookie
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['Authorization', 'Content-Type'],
)

@app.get('/data')
def data():
    return {'ok': True}
