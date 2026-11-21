"""静态资源指纹命名: 内容哈希与不可变缓存(纯标准库)。"""
import hashlib
import os


def write(path, content):
    with open(path, "w") as fh:
        fh.write(content)


def fingerprint(path):
    with open(path, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()[:12]
    root, ext = os.path.splitext(path)
    return "{}.{}{}".format(root, digest, ext)


path = "/tmp/q2187_app.js"
write(path, "console.log('v1')")
f1 = fingerprint(path)
print("v1 指纹名:", f1)
write(path, "console.log('v2')")
f2 = fingerprint(path)
print("v2 指纹名:", f2)
assert f1 != f2
write(path, "console.log('v1')")
assert fingerprint(path) == f1                       # 同内容同名, CDN 副本可复用
print("重写回 v1 复用旧名:", fingerprint(path) == f1)
print("要点: 指纹是内容哈希不是时间戳; 缓存可写死 immutable, 入口 HTML 是整条缓存链的失效入口")
os.remove(path)
