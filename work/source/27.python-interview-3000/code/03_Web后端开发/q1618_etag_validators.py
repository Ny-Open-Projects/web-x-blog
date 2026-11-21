"""ETag 强/弱校验器: 生成策略与两种比较语义(纯标准库)。"""
import hashlib


def strong_etag(body):
    """内容哈希生成强标签: 字节级一致才相等。"""
    return '"' + hashlib.sha256(body).hexdigest()[:32] + '"'


def weak_etag(mtime, size):
    """mtime+size 生成弱标签: 语义等价即可, 类似 Nginx 的 W/"mtime-size"。"""
    return 'W/"%x-%x"' % (mtime, size)


def strip_weak(tag):
    return tag[2:] if tag.startswith("W/") else tag


def strong_eq(a, b):
    """强比较: 都必须是强标签且完全一致。"""
    return not a.startswith("W/") and not b.startswith("W/") and a == b


def weak_eq(a, b):
    """弱比较: 忽略 W/ 前缀, 只比标签本体。"""
    return strip_weak(a) == strip_weak(b)


e1 = strong_etag(b"hello")
print("强标签:", e1)
print("同内容重算一致:", e1 == strong_etag(b"hello"), "强比较:", strong_eq(e1, e1))
w1 = weak_etag(1730000000, 5)
plain = '"%x-%x"' % (1730000000, 5)
print("弱标签:", w1, "与无前缀版本弱比较:", weak_eq(w1, plain), "但强比较:", strong_eq(w1, plain))
w2 = weak_etag(1730000999, 5)
print("mtime 变了:", w2, "弱比较:", weak_eq(w1, w2))
print("规则: If-None-Match 用弱比较, If-Match 与 If-Range 必须强比较")
