try:
    from fastapi import FastAPI, Depends, HTTPException
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
logs: list[str] = []

def db_session():
    logs.append('session open')
    session = {'in_tx': True}
    try:
        yield session                     # 注入给路由
        session['in_tx'] = False          # 正常结束:提交
        logs.append('commit')
    except Exception:
        logs.append('rollback')           # 路由抛异常:回滚
        raise
    finally:
        logs.append('session close')      # 无论成败都清理

@app.get('/ok')
def ok(session: dict = Depends(db_session)):
    return {'data': 'ok'}

@app.get('/boom')
def boom(session: dict = Depends(db_session)):
    raise HTTPException(400, 'bad request')
# 连续请求 /ok、/boom 后 logs 依次为 open->commit->close / open->rollback->close
