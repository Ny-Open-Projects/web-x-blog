try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

def get_db():
    raise RuntimeError("测试中不应触达真库")

app = FastAPI()

@app.get("/users")
def users(db: str = Depends(get_db)):
    return {"db": db}

app.dependency_overrides[get_db] = lambda: "fake-db"

client = TestClient(app)
print(client.get("/users").json())
app.dependency_overrides.clear()
