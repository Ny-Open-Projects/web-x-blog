try:
    from fastapi import FastAPI, HTTPException
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
users: dict[int, dict] = {}

@app.get('/users')                       # 列表:GET /users?page=1&size=10
def list_users(page: int = 1, size: int = 10):
    ids = sorted(users)[(page - 1) * size: page * size]
    return {'total': len(users), 'items': [users[i] for i in ids]}

@app.get('/users/{user_id}')             # 详情:GET /users/1
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(404, 'user not found')
    return users[user_id]

@app.post('/users', status_code=201)     # 创建:POST /users
def create_user(user: dict):
    uid = max(users or {0: 0}) + 1
    users[uid] = {'id': uid, **user}
    return users[uid]

@app.delete('/users/{user_id}', status_code=204)  # 删除:DELETE /users/1
def delete_user(user_id: int):
    users.pop(user_id, None)
