"""对象存储的签名直传与回调确认: 应用不经手文件字节(纯标准库)。"""
import hashlib
import hmac


def presign(bucket, key, method, expires, secret, now):
    """签名覆盖方法、桶、键与到期时间; 客户端拿到的 URL 换任何一项都验不过。"""
    exp = now + expires
    material = "\n".join([method, bucket, key, str(exp)])
    sig = hmac.new(secret, material.encode("utf-8"), hashlib.sha256).hexdigest()[:32]
    return {"method": method, "bucket": bucket, "key": key, "expires": exp, "sig": sig}


def verify_presign(grant, method, bucket, key, secret, now, max_size, declared_size):
    """校验顺序: 到期 -> 方法与对象匹配 -> 重算签名 -> 尺寸上限。"""
    if now > grant["expires"]:
        return "expired"
    if method != grant["method"] or bucket != grant["bucket"] or key != grant["key"]:
        return "mismatch"
    material = "\n".join([grant["method"], grant["bucket"], grant["key"], str(grant["expires"])])
    want = hmac.new(secret, material.encode("utf-8"), hashlib.sha256).hexdigest()[:32]
    if not hmac.compare_digest(want, grant["sig"]):
        return "bad_signature"
    if declared_size > max_size:
        return "too_large"
    return "ok"


SECRET = b"storage-key"
MAX_SIZE = 10 * 1024 * 1024
clock = {"t": 1000.0}
now = lambda: clock["t"]

grant = presign("media", "upload/u1/report.pdf", "PUT", 900, SECRET, now())
assert verify_presign(grant, "PUT", "media", "upload/u1/report.pdf", SECRET, now(), MAX_SIZE, 2048) == "ok"
assert verify_presign(grant, "PUT", "media", "upload/u2/other.pdf", SECRET, now(), MAX_SIZE, 1) == "mismatch", "换 key 即失效"
assert verify_presign(grant, "DELETE", "media", "upload/u1/report.pdf", SECRET, now(), MAX_SIZE, 1) == "mismatch"
assert verify_presign(grant, "PUT", "media", "upload/u1/report.pdf", b"wrong", now(), MAX_SIZE, 1) == "bad_signature"
clock["t"] = 1901.0
assert verify_presign(grant, "PUT", "media", "upload/u1/report.pdf", SECRET, now(), MAX_SIZE, 1) == "expired"


class UploadRecord:
    """直传后凭存储回调关单: 校验回调签名与尺寸, 才把记录从 pending 置 ready。"""

    def __init__(self, secret):
        self.secret = secret
        self.records = {}

    def pending(self, key):
        self.records[key] = "pending"

    def confirm(self, key, size, etag, sig):
        if self.records.get(key) != "pending":
            return "unknown_key"
        want = hmac.new(self.secret, ("%s|%d|%s" % (key, size, etag)).encode("utf-8"),
                        hashlib.sha256).hexdigest()[:16]
        if not hmac.compare_digest(want, sig):
            return "bad_callback_signature"
        if size > MAX_SIZE:
            return "too_large"
        self.records[key] = "ready"
        return "ready"


rec = UploadRecord(SECRET)
rec.pending("upload/u1/report.pdf")
sig = hmac.new(SECRET, b"upload/u1/report.pdf|2048|etag1", hashlib.sha256).hexdigest()[:16]
assert rec.confirm("upload/u1/report.pdf", 2048, "etag1", sig) == "ready"
assert rec.confirm("upload/u1/report.pdf", 2048, "etag1", sig) == "unknown_key", "ready 后重复回调忽略"
print("直传链: 预签名(到期+方法+对象+尺寸) -> PUT -> 回调验签 -> pending 置 ready")
