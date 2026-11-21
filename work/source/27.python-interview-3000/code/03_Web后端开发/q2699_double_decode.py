"""URL 双层解码陷阱: 每一段只允许解码一次(纯标准库)。"""
from urllib.parse import quote, unquote, unquote_plus

# %25 是 '%' 自身的编码: 攻击者把 ../ 编码两次, WAF 解一次看到的是无害的 %2e
raw = "/api/%252e%252e%252fadmin"
once = unquote(raw)
twice = unquote(once)
print("原始    ", raw)
print("解码一次", once)
print("解码两次", twice)
assert once == "/api/%2e%2e%2fadmin"
assert twice == "/api/../admin"


def double_decode_risk(raw_path):
    """解码一次之后若再解一次还会变化, 说明存在被二次解释的空间, 直接拒绝。"""
    once = unquote(raw_path)
    return unquote(once) != once


assert double_decode_risk("/api/%252e%252e/admin")
assert not double_decode_risk("/api/%e4%bd%a0%E5%A5%BD")  # 正常单层编码的中文
assert not double_decode_risk("/api/plain-path")

# 加号陷阱: 查询串里 '+' 表示空格, 路径里 '+' 就是加号, 两个解码器不能混用
assert unquote_plus("q=java+web") == "q=java web"
assert unquote("q=java+web") == "q=java+web"
assert unquote_plus("q=java%2Bweb") == "q=java+web"  # %2B 永远是字面加号
# 编码再解码必须还原: quote 的缺省 safe='/' 会放过斜杠, 安全场景应 safe=''
assert quote(unquote("/a b", errors="strict"), safe="") == "%2Fa%20b"
print("单层语义稳定: 加号按段解释, 编码解码可还原")
