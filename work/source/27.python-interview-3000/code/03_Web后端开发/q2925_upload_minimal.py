"""文件上传的最小完整闭环: multipart 解析 + 校验 + 原子落盘 + 失败清理(纯标准库)。"""
import os
import re
import secrets
import tempfile

MAX_SIZE = 1024
ALLOWED = {".png": b"\x89PNG\r\n\x1a\n", ".jpg": b"\xff\xd8"}


class UploadError(Exception):
    def __init__(self, status, reason):
        self.status = status
        self.reason = reason


def parse_multipart(body, content_type):
    """最小单文件解析: 按 boundary 切段, 取第一个带 filename 的 part。

    生产环境请用框架解析器; 本实现假设 boundary 不出现在文件内容里。
    """
    m = re.search(r'boundary="?([^";]+)"?', content_type or "")
    if not m:
        raise UploadError(400, "Content-Type 缺少 boundary")
    boundary = m.group(1).encode()
    segments = body.split(b"--" + boundary)
    for seg in segments[1:]:
        if seg.startswith(b"--"):        # --boundary-- 结束标记
            break
        if seg.startswith(b"\r\n"):      # boundary 行后的 CRLF
            seg = seg[2:]
        if seg.endswith(b"\r\n"):        # 下一边界前的 CRLF
            seg = seg[:-2]
        head, sep, data = seg.partition(b"\r\n\r\n")
        if not sep:
            continue
        filename = None
        for line in head.decode("utf-8", "replace").split("\r\n"):
            if line.lower().startswith("content-disposition") and 'name="file"' in line:
                fm = re.search(r'filename="([^"]*)"', line)
                if fm:
                    filename = fm.group(1)
        if filename is not None:
            return filename, data
    raise UploadError(400, "请求中未找到文件部分")


def handle_upload(root, body, content_type):
    """校验三关 -> 随机名暂存 -> 原子替换; 任何一步失败都清理干净。"""
    filename, data = parse_multipart(body, content_type)
    if len(data) > MAX_SIZE:
        raise UploadError(413, "超过大小上限 %d 字节" % MAX_SIZE)
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ALLOWED:
        raise UploadError(415, "扩展名不在白名单")
    if not data.startswith(ALLOWED[ext]):
        raise UploadError(415, "魔数与扩展名不符, 疑似改名上传")
    os.makedirs(root, exist_ok=True)
    stored = os.path.join(root, secrets.token_hex(8) + ext)  # 永不使用客户端文件名
    tmp_path = stored + ".part"
    try:
        with open(tmp_path, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, stored)  # 同目录原子替换, 不会出现半截文件
    except BaseException:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)       # 失败清理, 不留 .part 垃圾
        raise
    return stored, len(data)


def multipart_body(filename, data, boundary=None):
    """构造测试用的 multipart/form-data 请求体。"""
    boundary = boundary or secrets.token_hex(16)
    part = (
        'Content-Disposition: form-data; name="file"; filename="%s"\r\n'
        "Content-Type: application/octet-stream\r\n\r\n" % filename
    ).encode()
    body = b"--" + boundary.encode() + b"\r\n" + part + data + b"\r\n"
    body += b"--" + boundary.encode() + b"--\r\n"
    return body, "multipart/form-data; boundary=%s" % boundary


tmp = tempfile.mkdtemp()
png = b"\x89PNG\r\n\x1a\n" + b"rest-of-png-bytes" * 10

body, ct = multipart_body("photo.png", png)
good_body, good_ct = body, ct
stored, size = handle_upload(tmp, body, ct)
print("合法上传落盘:", os.path.basename(stored), size, "字节")
assert stored.endswith(".png") and size == len(png)
with open(stored, "rb") as f:
    assert f.read() == png
assert os.path.basename(stored) != "photo.png", "客户端文件名只校验扩展名, 不用于落盘"

cases = [
    (multipart_body("big.png", png + b"x" * MAX_SIZE), "超过大小上限"),
    (multipart_body("shell.exe", png), "扩展名不在白名单"),
    (multipart_body("fake.png", b"MZ\x90\x00" + b"junk" * 10), "魔数与扩展名不符"),
    (b"not-multipart", "Content-Type: text/plain", "缺少 boundary"),
]
for case in cases:
    if len(case) == 2:
        (body, ct), why = case
    else:
        body, ct, why = case
    try:
        handle_upload(tmp, body, ct)
        raise AssertionError("应当被拒: %s" % why)
    except UploadError as e:
        print("拒绝 [%s] -> %s %s" % (why, e.status, e.reason))
        assert e.status in (400, 413, 415)

# 失败清理演示: 让 os.replace 模拟磁盘满, 验证 .part 不残留
real_replace = os.replace

def disk_full(src, dst):
    raise OSError(28, "模拟磁盘满")

os.replace = disk_full
try:
    handle_upload(tmp, good_body, good_ct)
except OSError as e:
    print("落盘失败:", e.strerror)
finally:
    os.replace = real_replace
leftover = [n for n in os.listdir(tmp) if n.endswith(".part")]
assert not leftover, "失败路径必须清理暂存文件"
print("失败清理后目录内容:", sorted(os.listdir(tmp)))
print("文件上传最小闭环演示通过")
