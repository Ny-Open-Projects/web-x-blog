---
title: [Q758] Range 断点续传下载
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q758 · Range 断点续传下载

> 难度:★★★★ | 标签:FastAPI, HTTP 协议

**问**:大文件下载中断了要能续传,Range 请求的服务端逻辑怎么写?

**答**:三步:首响应带 `Accept-Ranges: bytes` 告知支持分段;收到 `Range: bytes=start-end` 头时返回 **206** + `Content-Range: bytes start-end/total`,只回对应切片;区间非法(start 越界或 start>end)返回 **416** 并附 `Content-Range: bytes */total`。文件可能被替换时要配 **ETag/If-Range**:版本变了拒绝续传旧区间,防止客户端拼出混合版本。生产上大文件优先交给 Nginx 的 sendfile 或对象存储签名 URL,应用只做鉴权。

```python
# file: code/03_Web后端开发/q758_range_download.py
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
```

**追问**:
- Content-Range 里 end 是闭区间吗?——是,包含 end 本身,和 Python 切片的右开区间不同,手写时最容易错这里。
- If-Range 匹配失败返回什么?——返回完整 200 响应,客户端丢弃已下载部分重新开始。
