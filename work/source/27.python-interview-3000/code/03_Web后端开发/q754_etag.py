import hashlib
try:
    from fastapi import FastAPI, Request, Response
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

@app.get("/report")
def report(request: Request):
    payload = b"report-version-7"
    etag = '"' + hashlib.md5(payload).hexdigest() + '"'
    if request.headers.get("if-none-match") == etag:
        return Response(status_code=304, headers={"ETag": etag})
    return Response(content=payload, media_type="text/plain", headers={"ETag": etag})

client = TestClient(app)
r1 = client.get("/report")
print(r1.status_code, r1.headers["etag"])
r2 = client.get("/report", headers={"If-None-Match": r1.headers["etag"]})
print(r2.status_code, len(r2.content))
