"""请求日志脱敏中间件: 查询串与头部的密钥遮罩(纯标准库)。"""
import re
from urllib.parse import urlsplit, parse_qsl, urlencode

SENSITIVE_KEYS = {"password", "passwd", "token", "access_token", "secret",
                  "api_key", "apikey", "signature", "code"}
SENSITIVE_HEADERS = {"authorization", "cookie", "set-cookie", "proxy-authorization"}


def mask_value(value, keep=4):
    """部分遮罩: 保留末尾 4 位用于排障对照, 其余打星。"""
    if len(value) <= keep:
        return "***"
    return "***" + value[-keep:]


def mask_query(url):
    """脱敏查询串: 键保留可见, 敏感值遮罩; 键名本身不进入敏感名单除外。"""
    parts = urlsplit(url)
    pairs = []
    for k, v in parse_qsl(parts.query, keep_blank_values=True):
        if k.lower() in SENSITIVE_KEYS:
            pairs.append((k, mask_value(v)))
        else:
            pairs.append((k, v))
    return urlencode(pairs)


def mask_headers(headers):
    """脱敏头部: 白名单类整值遮罩, 其余仅遮疑似长令牌。"""
    out = {}
    for k, v in headers.items():
        if k.lower() in SENSITIVE_HEADERS:
            out[k] = mask_value(v)
        elif re.search(r"(?i)(token|key|secret)", k):
            out[k] = mask_value(v)
        else:
            out[k] = v
    return out


url = "/search?q=redis&page=2&access_token=eyJhbGciOiJIUzI1Nnk9w&api_key=sk-live-9f3ab777"
print("原始:  " + url)
print("脱敏:  " + mask_query(url))
assert "9f3ab777" not in mask_query(url) and "q=redis" in mask_query(url)

headers = {"Authorization": "Bearer eyJhbGciOi.eyJzdWIi.7d8fa9c0",
           "X-Request-Id": "req-42", "X-Api-Key": "abcd1234efgh",
           "User-Agent": "curl/8.4"}
print("头部脱敏:", mask_headers(headers))
masked = mask_headers(headers)
assert masked["X-Request-Id"] == "req-42"
assert masked["Authorization"].startswith("***") and "eyJhbGciOi" not in masked["Authorization"]

print("要点: 中间件在写日志前统一过这一层, 键名可见值不可见, 排障所需的对照尾巴只留 4 位")
