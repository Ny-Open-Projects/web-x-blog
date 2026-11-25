---
title: "[Q6270] 无状态会话 Cookie：HMAC 签名、时间戳与密钥轮换"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6270 · 无状态会话 Cookie：HMAC 签名、时间戳与密钥轮换

难度：P7 ｜ 标签：Cookie、HMAC、签名、密钥轮换、会话、compare_digest

基线：CPython 3.12.2，纯标准库；用 `hmac`/`hashlib`/`base64`/`json` 实现签名与校验，覆盖篡改、过期、密钥轮换与 payload 可读性。

**问**：一个边缘服务为了"无状态"，把 `uid`、`role`、`iat` 用 `base64(json)` 放进 Cookie，末尾拼 `sha256(secret + payload)` 当签名。上线后偶发"随机用户被踢下线"，排查发现不同 worker 的 JSON 键顺序/空格不一致，签名对不上；安全审计还指出 `sha256(secret + payload)` 存在长度扩展风险，且签名比较用了 `==`。另一个团队轮换密钥时直接替换，导致所有在线用户瞬间登出。无状态 Cookie 应该怎么签？为什么必须 HMAC？密钥怎么轮换才不踢人？

**答**：

- **结论**：无状态会话 Cookie 的标准做法是 `base64url(payload) + "." + base64url(HMAC-SHA256(key, base64url(payload)))`。**签名必须覆盖最终参与传输的那串字节**（编码后的 payload），而不是"重新序列化后的 dict"——否则键顺序、空格、Unicode 转义一变，签名就漂移。用 `hmac.new(key, msg, hashlib.sha256)` 而不是 `sha256(key + msg)`：后者是"秘密前缀 MAC"，对 Merkle–Damgård 哈希存在长度扩展攻击，攻击者可以在不知道 key 的情况下追加数据并算出合法签名；HMAC 有专门的结构证明，标准库直接提供。校验用 `hmac.compare_digest` 做常量时间比较，避免逐字节比较的时序侧信道；`==` 在 Python 里虽然对 bytes 有短路，但不保证常量时间。
- **取舍**：HMAC 只保证**完整性**，不保证**机密性**——payload 只是 base64，任何人都能解出 `uid/role`；需要隐藏内容要额外加密（标准库没有 AEAD，生产可用 `cryptography` 的 Fernet/AES-GCM，或干脆只放不透明的 session id）。无状态 token 难以**单点吊销**：签发后到期前都有效，要支持"立即踢人"必须维护 `jti` 黑名单或改用服务端 session；短 TTL + refresh token 是折中。密钥轮换要用 `kid`（key id）标识，验签时按 `kid` 选 key，新 token 用新 key，旧 token 在过期前继续用旧 key；直接把旧 key 删掉就会全员登出。
- **实战**：事故的签名函数对 `json.dumps(payload)` 签名，校验时又 `json.loads` 后重新 `dumps`，两个 worker 的 `sort_keys`/`separators` 配置不同，签名随机不匹配。修复：① 签发时先 `b64e(canonical_json)`，签名只针对这个字符串，校验时**不重新序列化**，直接对收到的 `body` 验签；② 换成 HMAC-SHA256 + `compare_digest`；③ token 加 `kid`，密钥表保留 current/previous 两把，轮换窗口 24h；④ 加 `exp`，并对 `iat` 做未来时间容差（±60s）。上线后随机掉线归零，轮换零感知。

下面实现签发/校验，验证篡改、过期、密钥轮换、payload 可读与 URL-safe 编码。

```python
# 无状态会话 Cookie: HMAC-SHA256 覆盖编码后的 payload, kid 支持密钥轮换
import base64
import hashlib
import hmac
import json


def b64e(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


def b64d(text: str) -> bytes:
    padding = "=" * (-len(text) % 4)
    return base64.urlsafe_b64decode(text + padding)


def sign(payload: dict, key: bytes, kid: str) -> str:
    body = b64e(json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8"))
    message = f"{kid}.{body}".encode("ascii")
    signature = b64e(hmac.new(key, message, hashlib.sha256).digest())
    return f"{kid}.{body}.{signature}"


class BadToken(Exception):
    pass


def verify(token: str, keys: dict, now: int, max_age: int = 3600) -> dict:
    try:
        kid, body, signature = token.split(".")
    except ValueError as exc:
        raise BadToken("malformed token") from exc
    if kid not in keys:
        raise BadToken(f"unknown kid: {kid}")
    expected = b64e(hmac.new(keys[kid], f"{kid}.{body}".encode("ascii"), hashlib.sha256).digest())
    if not hmac.compare_digest(expected, signature):
        raise BadToken("bad signature")
    payload = json.loads(b64d(body))
    if now - payload["iat"] > max_age:
        raise BadToken("expired")
    if payload["iat"] - now > 60:
        raise BadToken("issued in the future")
    return payload


keys = {"v1": b"old-secret-32-bytes-long-000000", "v2": b"new-secret-32-bytes-long-000000"}
token = sign({"uid": 7, "role": "admin", "iat": 1000}, keys["v1"], "v1")
print("[1] token:", token)
assert token.count(".") == 2
assert "=" not in token and "+" not in token and "/" not in token

payload = verify(token, keys, now=1050)
print("[2] 校验通过:", payload)
assert payload["uid"] == 7 and payload["role"] == "admin"

# payload 只是 base64, 不是加密
leaked = json.loads(b64d(token.split(".")[1]))
print("[3] 任何人都能读出 payload:", leaked)
assert leaked["role"] == "admin"

# 篡改 body -> 签名失败
kid, body, sig = token.split(".")
forged_body = b64e(json.dumps({"uid": 1, "role": "admin", "iat": 1000}, separators=(",", ":"), sort_keys=True).encode())
try:
    verify(f"{kid}.{forged_body}.{sig}", keys, now=1050)
    raise AssertionError("篡改应失败")
except BadToken as exc:
    print("[4] 篡改 ->", exc)

# 过期
try:
    verify(token, keys, now=1000 + 3601)
    raise AssertionError("过期应失败")
except BadToken as exc:
    print("[5] 过期 ->", exc)

# 密钥轮换: 旧 token 用 v1, 新 token 用 v2, 两把都在 keys 里
new_token = sign({"uid": 8, "role": "user", "iat": 2000}, keys["v2"], "v2")
print("[6] 新 token kid:", new_token.split(".")[0])
assert verify(token, keys, now=1050)["uid"] == 7
assert verify(new_token, keys, now=2000)["uid"] == 8
print("[7] 轮换窗口内新旧 token 都可用")

# 去掉旧 key 后, 旧 token 立即失效
try:
    verify(token, {"v2": keys["v2"]}, now=1050)
    raise AssertionError("旧 key 移除后应失败")
except BadToken as exc:
    print("[8] 旧 key 移除 ->", exc)

print("[9] 结论: HMAC 覆盖编码字节 + compare_digest + kid 轮换; payload 不加密")
```

**追问一**：为什么不能对 `json.dumps(payload)` 签名、校验时再 `json.loads` 后重新 `dumps`？—— JSON 不是规范化的：键顺序、空格、`ensure_ascii`、浮点格式、Unicode 转义都可能不同；不同语言/版本的默认行为也不一样。签名必须针对"实际传输的字节"（base64 后的 body），校验时直接对收到的 body 验签，**不要反序列化再序列化**。如果确实要对结构化数据签名，先定义 canonical JSON（排序键、固定分隔符、固定转义），并在所有实现里共用同一套规范化函数。

**追问二**：`sha256(secret + payload)` 的长度扩展具体怎么利用？—— SHA-256 是 Merkle–Damgård 结构，给定 `H(secret || payload)` 和 `len(secret || payload)`，攻击者可以在不知道 secret 的情况下构造 `H(secret || payload || padding || extra)`，从而给追加后的消息伪造签名。HMAC 用 `H(key ⊕ opad || H(key ⊕ ipad || msg))` 的双层结构避免了这个问题。另一个常见错误是用 `hash()` 或 `random` 当密钥：`hash()` 受 `PYTHONHASHSEED` 影响、不是密码学哈希；密钥必须来自 `secrets.token_bytes` 或 KMS。

## 背诵要点

- 签名覆盖**编码后的 payload 字节**，不要反序列化后重签；HMAC-SHA256 防长度扩展，`compare_digest` 防时序侧信道。
- HMAC 只保证完整性，payload 可被 base64 解码；要机密性需额外加密或改用不透明 session id。
- 轮换用 `kid` + current/previous 双 key，旧 token 到期前继续可验；直接删旧 key 会全员登出。

## 复盘追问

- 为什么无状态 token 难以"立即踢人"？（签发后到期前都有效，除非维护 jti 黑名单或服务端 session）
- `iat` 在未来时间为什么要拒绝/容差？（时钟漂移会导致刚签发的 token 被判无效；但放太宽会削弱过期语义）
