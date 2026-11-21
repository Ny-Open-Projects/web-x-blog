try:
    from fastapi import Depends, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
ids = []

def shared_token():
    ids.append("shared")
    return object()

def per_call_token():
    ids.append("fresh")
    return object()

def cached(a=Depends(shared_token), b=Depends(shared_token)):
    return a is b

def uncached(x=Depends(per_call_token), y=Depends(per_call_token, use_cache=False)):
    return x is not y

@app.get("/cached")
def cached_ep(v: bool = Depends(cached)):
    return {"same_instance": v}

@app.get("/uncached")
def uncached_ep(v: bool = Depends(uncached)):
    return {"different_instance": v}

client = TestClient(app)
print(client.get("/cached").json())
print(client.get("/uncached").json())
print("依赖调用次数:", ids)
