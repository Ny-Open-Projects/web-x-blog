try:
    from fastapi import FastAPI
    from fastapi.responses import StreamingResponse
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

def chunk_file(total_kb: int, chunk_kb: int = 8):
    for _ in range(0, total_kb, chunk_kb):
        yield b"x" * (chunk_kb * 1024)

@app.get("/download")
def download():
    return StreamingResponse(
        chunk_file(32),
        media_type="application/octet-stream",
        headers={"Content-Disposition": 'attachment; filename="blob.bin"'},
    )

client = TestClient(app)
r = client.get("/download")
print(r.status_code, len(r.content), r.headers["content-type"])
