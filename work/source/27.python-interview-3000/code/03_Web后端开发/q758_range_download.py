try:
    from fastapi import FastAPI, Request, Response
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()
BLOB = bytes(range(256)) * 4  # 1024 字节模拟文件

@app.get("/file")
def get_file(request: Request):
    total = len(BLOB)
    headers = {"Accept-Ranges": "bytes", "Content-Type": "application/octet-stream"}
    rng = request.headers.get("range")
    if not rng:
        return Response(content=BLOB, headers=headers)
    start_s, end_s = rng.replace("bytes=", "").split("-")
    start = int(start_s or 0)
    end = int(end_s) if end_s else total - 1
    end = min(end, total - 1)
    if start > end or start >= total:
        return Response(status_code=416, headers={"Content-Range": f"bytes */{total}"})
    headers["Content-Range"] = f"bytes {start}-{end}/{total}"
    return Response(content=BLOB[start:end + 1], status_code=206, headers=headers)

client = TestClient(app)
print(client.get("/file").status_code, client.get("/file").headers.get("accept-ranges"))
r = client.get("/file", headers={"Range": "bytes=100-199"})
print(r.status_code, r.headers["content-range"], len(r.content))
