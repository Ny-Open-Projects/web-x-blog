try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

calls = []
app = FastAPI()

def dep_db():
    calls.append("db")
    return "db-conn"

def dep_auth(db: str = Depends(dep_db)):
    calls.append("auth")
    return f"user@{db}"

def dep_perm(user: str = Depends(dep_auth)):
    calls.append("perm")
    return f"perm[{user}]"

@app.get("/only-auth")
def only_auth(user: str = Depends(dep_auth)):
    return {"user": user}

@app.get("/with-perm")
def with_perm(p: str = Depends(dep_perm), user: str = Depends(dep_auth)):
    return {"p": p, "user": user}

client = TestClient(app)
print(client.get("/only-auth").json())
print(client.get("/with-perm").json())
print("解析顺序:", calls)  # 同一请求内 db 与 auth 只解析一次
