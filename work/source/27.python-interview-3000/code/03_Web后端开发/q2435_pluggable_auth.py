"""可插拔认证层: 方案注册、逐级协商与质询(纯标准库)。"""
import base64
import binascii
import hashlib
import hmac

TOKENS = {"tok-alice-1": "alice"}
USERS = {"alice": "wonderland"}


class AuthLayer:
    def __init__(self):
        self.schemes = []                       # (名称, 解析函数, 质询串)

    def register(self, name, resolver, challenge):
        self.schemes.append((name.lower(), resolver, challenge))
        return self                             # 链式注册

    def authenticate(self, headers):
        """按 Authorization 头的 scheme 前缀分派, 返回 principal 或 None。"""
        raw = headers.get("Authorization", "")
        scheme, _, credential = raw.partition(" ")
        for name, resolver, _ in self.schemes:
            if scheme.lower() == name:
                return resolver(credential)
        return None

    def www_authenticate(self):
        """401 响应的 WWW-Authenticate 值: 列出全部已注册方案。"""
        return ", ".join(ch for _, _, ch in self.schemes)


def bearer_resolver(credential):
    return TOKENS.get(credential)


def basic_resolver(credential):
    try:
        decoded = base64.b64decode(credential).decode()
        user, _, pwd = decoded.partition(":")
    except (binascii.Error, UnicodeDecodeError):
        return None
    expected = USERS.get(user)
    if expected and hmac.compare_digest(expected, pwd):
        return user
    return None


def apikey_resolver(credential):
    return ("service-" + credential[3:7]) if credential.startswith("sk-") else None


auth = (AuthLayer()
        .register("Bearer", bearer_resolver, 'Bearer realm="api"')
        .register("Basic", basic_resolver, 'Basic realm="api"')
        .register("ApiKey", apikey_resolver, "ApiKey"))

cases = [
    ({"Authorization": "Bearer tok-alice-1"}, "alice"),
    ({"Authorization": "Basic " + base64.b64encode(b"alice:wonderland").decode()}, "alice"),
    ({"Authorization": "Basic " + base64.b64encode(b"alice:wrong").decode()}, None),
    ({"Authorization": "ApiKey sk-demo123"}, "service-demo"),
    ({"Authorization": "Digest aaa"}, None),
    ({}, None),
]
for headers, expect in cases:
    got = auth.authenticate(headers)
    label = headers.get("Authorization", "无头")
    print("{:24s} -> {}".format(label[:24], got))
    assert got == expect, (label, got, expect)

status = 401 if auth.authenticate({}) is None else 200
assert status == 401
print("401 响应头 WWW-Authenticate:", auth.www_authenticate())
print("要点: 认证层只做 身份解析 不做授权, 新方案注册即用; "
      "401 必须回带 WWW-Authenticate 告知客户端支持的方案")
