try:
    from fastapi import BackgroundTasks, FastAPI
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

done = []
app = FastAPI()

def send_email(to: str):
    done.append(f"mail->{to}")

@app.post("/signup")
def signup(email: str, bg: BackgroundTasks):
    bg.add_task(send_email, to=email)
    return {"queued": True}

client = TestClient(app)
print(client.post("/signup?email=a@b.c").json())
print("任务已执行:", done)  # TestClient 请求完成后后台任务已同步跑完
