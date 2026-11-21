import uuid
try:
    from fastapi import FastAPI, HTTPException
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
jobs: dict[str, dict] = {}

@app.post("/exports", status_code=202)
def create_export():
    job_id = uuid.uuid4().hex
    jobs[job_id] = {"status": "running", "progress": 40}  # 模拟异步推进
    return {"job_id": job_id, "status": "running"}

@app.get("/exports/{job_id}")
def get_export(job_id: str):
    job = jobs.get(job_id)
    if not job:
        raise HTTPException(404)
    return job

client = TestClient(app)
r = client.post("/exports")
print(r.status_code, r.json())
print(client.get(f"/exports/{r.json()['job_id']}").json())
print(client.get("/exports/nope").status_code)
