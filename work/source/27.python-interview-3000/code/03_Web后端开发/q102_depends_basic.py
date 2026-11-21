try:
    from fastapi import FastAPI, Depends, HTTPException, Query
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

def pagination(page: int = Query(1, ge=1), size: int = Query(10, le=100)):
    return {'page': page, 'size': size}

def fake_db():
    return {'conn': 'db-conn'}

def get_current_user(token: str = Query(...), db: dict = Depends(fake_db)):
    if token != 'abc':
        raise HTTPException(401, 'invalid token')
    return {'user': 'alice', 'db': db}

@app.get('/items')
def list_items(pager: dict = Depends(pagination), user=Depends(get_current_user)):
    return {'pager': pager, 'user': user['user']}

@app.get('/admin', dependencies=[Depends(get_current_user)])  # 只校验不注入
def admin():
    return {'msg': 'ok'}
