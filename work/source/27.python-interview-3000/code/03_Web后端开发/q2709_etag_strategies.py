"""ETag 生成的四种策略对比: 强度、成本与跨实例一致性(纯标准库)。"""
import hashlib
import json
import time


def etag_content(body):
    """内容哈希: 字节级强标签, 换实例也一致; 代价是每次全量哈希。"""
    return '"' + hashlib.sha256(body).hexdigest()[:32] + '"'


def etag_meta(mtime_ns, size):
    """mtime+size: 近乎零成本, 但秒级以下不敏感且多实例时钟难对齐, 只配弱标签。"""
    return 'W/"%x-%x"' % (mtime_ns // 1000, size)


def etag_version(version):
    """构建版本号: 部署期生成, 请求期零成本且跨实例绝对一致, 强标签。"""
    return '"v%s"' % version


def etag_semantic(obj, volatile=("updated_at",)):
    """语义指纹: 剔除易变字段并做键序归一后哈希, 字节不同但语义相同也算命中。"""
    cleaned = {k: v for k, v in obj.items() if k not in volatile}
    norm = json.dumps(cleaned, sort_keys=True, separators=(",", ":"))
    return 'W/"sem-' + hashlib.sha256(norm.encode("utf-8")).hexdigest()[:24] + '"'


BODY_A = b'{"id":1,"name":"a"}'
BODY_B = b'{"id":1,"name":"a"} '
assert etag_content(BODY_A) == etag_content(BODY_A)
assert etag_content(BODY_A) != etag_content(BODY_B), "一字节之差内容哈希必须不同"

obj1 = {"id": 1, "name": "a", "updated_at": "2026-01-01", "k2": "v2"}
obj2 = {"k2": "v2", "name": "a", "updated_at": "2026-06-01", "id": 1}
assert etag_semantic(obj1) == etag_semantic(obj2), "键序与易变字段不影响语义指纹"

t0 = time.perf_counter()
for _ in range(2000):
    etag_content(BODY_A)
t_hash = (time.perf_counter() - t0) / 2000 * 1e6
t0 = time.perf_counter()
for _ in range(2000):
    etag_meta(1762128000123456789, len(BODY_A))
t_meta = (time.perf_counter() - t0) / 2000 * 1e6
print("内容哈希 %.1f us/次, mtime+size %.2f us/次" % (t_hash, t_meta))
print("选型: 静态文件用 mtime+size 弱标签, 动态小响应用内容哈希,")
print("      有构建号的资源用版本号, 聚合列表用语义指纹")
