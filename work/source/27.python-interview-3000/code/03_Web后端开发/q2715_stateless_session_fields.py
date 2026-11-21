"""无状态会话的字段取舍与体积预算: 进什么留什么(纯标准库)。"""
import base64
import hashlib
import hmac
import json

SECRET = b"session-key"
HEADER_BUDGET = 3800  # Cookie 全长 4KB, 留出属性与转义余量


def encode_session(payload, secret=SECRET):
    """紧凑编码: JSON 定长分隔符 + urlsafe base64 + 截断 HMAC。

    截断到 16 字节 hex 对会话完整性足够; 关键是 payload 本身必须瘦身。
    """
    raw = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")
    sig = hmac.new(secret, raw, hashlib.sha256).hexdigest()[:16]
    return base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=") + "." + sig


def decode_session(token, secret=SECRET):
    b64, sig = token.rsplit(".", 1)
    raw = base64.urlsafe_b64decode(b64 + "=" * (-len(b64) % 4))
    if not hmac.compare_digest(hmac.new(secret, raw, hashlib.sha256).hexdigest()[:16], sig):
        raise ValueError("签名不符")
    return json.loads(raw)


SLIM = {"sub": "u1", "roles": ["user"], "ver": 3, "exp": 1794192000, "iat": 1794105600}
BLOATED = dict(
    SLIM,
    cart=[{"sku": "s%02d" % i, "qty": 2, "note": "x" * 80} for i in range(40)],
    profile={"addr": "某市某区某街道 100 号 2 栋 301", "phone": "13800000000", "real_name": "张三"},
    recent_views=["p%03d" % i for i in range(100)],
)

t_slim = encode_session(SLIM)
t_fat = encode_session(BLOATED)
assert len(t_slim) <= HEADER_BUDGET, len(t_slim)
assert len(t_fat) > HEADER_BUDGET, len(t_fat)
assert decode_session(t_slim) == SLIM
try:
    bad = t_slim[:-2] + "zz"
    decode_session(bad)
except ValueError as e:
    print("篡改拒绝:", e)
print("瘦身令牌 %dB, 塞满工作数据的令牌 %dB, 预算 %dB" % (len(t_slim), len(t_fat), HEADER_BUDGET))
print("取舍: 身份与授权事实可进; 购物车/浏览历史等工作数据进服务端; PII 一律不进")
