try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

class Paginator:
    def __init__(self, max_size: int = 50):
        self.max_size = max_size

    def __call__(self, page: int = 1, size: int = 20):
        size = min(size, self.max_size)
        return {"offset": (page - 1) * size, "limit": size}

pager = Paginator(max_size=100)

def make_header_dependency(name: str):
    def dep():
        return {f"X-{name}-Limit": "60"}
    return dep

@app.get("/items", dependencies=[Depends(make_header_dependency("Quota"))])
def items(pg: dict = Depends(pager)):
    return pg

client = TestClient(app)
print(client.get("/items?page=3&size=999").json())
