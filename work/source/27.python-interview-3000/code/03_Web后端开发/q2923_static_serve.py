"""静态文件的安全伺服: 路径校验 + 类型白名单 + 安全响应头(纯标准库)。"""
import os
import tempfile
from urllib.parse import unquote

MIME = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".txt": "text/plain; charset=utf-8",
    ".ico": "image/x-icon",
}


class StaticError(Exception):
    def __init__(self, status, reason):
        self.status = status
        self.reason = reason


def serve_static(root, url_path):
    """url_path 应已完成百分号解码; 本函数只信任规范化后的结果。"""
    if "\x00" in url_path:
        raise StaticError(400, "路径含空字节")
    rel = os.path.normpath(url_path.lstrip("/"))
    if rel in ("", "."):
        rel = "index.html"
    if rel.startswith("..") or os.path.isabs(rel):
        raise StaticError(403, "路径越界")
    root_real = os.path.realpath(root)
    full = os.path.realpath(os.path.join(root_real, rel))
    if full != root_real and not full.startswith(root_real + os.sep):
        raise StaticError(403, "软链或别名逃逸出根目录")
    if os.path.isdir(full):
        full = os.path.join(full, "index.html")  # 目录回退到 index, 不开目录列表
    if not os.path.isfile(full):
        raise StaticError(404, "文件不存在")
    ext = os.path.splitext(full)[1].lower()
    if ext not in MIME:
        raise StaticError(415, "类型不在白名单, 不猜测不伺服")
    with open(full, "rb") as f:
        data = f.read()
    return {
        "status": 200,
        "body": data,
        "headers": {
            "Content-Type": MIME[ext],
            "Content-Length": str(len(data)),
            "X-Content-Type-Options": "nosniff",
            "Cache-Control": "public, max-age=3600",
        },
    }


tmp = tempfile.mkdtemp()
root = os.path.join(tmp, "public")
os.makedirs(os.path.join(root, "css"))
with open(os.path.join(root, "index.html"), "w") as f:
    f.write("<h1>ok</h1>")
with open(os.path.join(root, "css", "app.css"), "w") as f:
    f.write("body{margin:0}")
with open(os.path.join(root, "evil.exe"), "w") as f:
    f.write("MZ binary junk")
outside = os.path.join(tmp, "secret.txt")
with open(outside, "w") as f:
    f.write("top secret")
os.symlink(outside, os.path.join(root, "leak.txt"))
os.symlink("/etc/passwd", os.path.join(root, "passwd"))

hit = serve_static(root, "/index.html")
print("正常伺服:", hit["headers"]["Content-Type"], len(hit["body"]), "字节")
assert hit["status"] == 200 and hit["body"] == b"<h1>ok</h1>"
assert hit["headers"]["X-Content-Type-Options"] == "nosniff"

hit = serve_static(root, "/css/app.css")
assert hit["headers"]["Content-Type"].startswith("text/css")
hit = serve_static(root, "/")
assert hit["body"] == b"<h1>ok</h1>", "根路径回退 index.html"

attacks = [
    ("/../etc/passwd", "点段上跳"),
    ("/css/../../../etc/passwd", "多层点段"),
    (unquote("/%2e%2e/etc/passwd"), "编码点段, 进函数前已解码一次"),
    ("/leak.txt", "软链指向根外"),
    ("/passwd", "软链指向系统文件"),
]
for path, why in attacks:
    try:
        serve_static(root, path)
        raise AssertionError("应当拦截: %s" % why)
    except StaticError as e:
        print("拦截 [%s] -> %s %s" % (why, e.status, e.reason))
        assert e.status in (403, 404)

try:
    serve_static(root, "/nope.html")
except StaticError as e:
    print("缺失文件 ->", e.status)
    assert e.status == 404
try:
    serve_static(root, "/evil.exe")
except StaticError as e:
    print("类型不在白名单 ->", e.status)
    assert e.status == 415
print("静态文件安全伺服演示通过")
