try:
    from fastapi import FastAPI, Depends
    from fastapi.testclient import TestClient
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

def get_current_user():
    return {'user': 'real'}

@app.get('/me')
def me(user: dict = Depends(get_current_user)):
    return user

client = TestClient(app)

def test_me():
    resp = client.get('/me')
    assert resp.status_code == 200
    assert resp.json() == {'user': 'real'}

def test_me_mocked():
    app.dependency_overrides[get_current_user] = lambda: {'user': 'fake'}
    try:
        resp = client.get('/me')
        assert resp.json() == {'user': 'fake'}
    finally:
        app.dependency_overrides.clear()   # 用完清理,防止影响其他用例

test_me()
test_me_mocked()
print('all tests passed')
