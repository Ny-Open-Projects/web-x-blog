try:
    from fastapi import FastAPI
    from pydantic import BaseModel
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
db = {1: {'name': 'alice', 'email': 'a@x.com', 'age': 20}}

class UserIn(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None

@app.put('/users/{uid}')            # 全量替换:未传字段被置为 None
def replace_user(uid: int, body: UserIn):
    db[uid] = {'name': body.name, 'email': body.email, 'age': body.age}
    return db[uid]

@app.patch('/users/{uid}')          # 部分更新:只改传入的字段
def patch_user(uid: int, body: UserIn):
    patch = body.model_dump(exclude_unset=True)
    db[uid].update(patch)
    return db[uid]
