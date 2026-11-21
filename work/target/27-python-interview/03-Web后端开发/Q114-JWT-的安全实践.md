---
title: [Q114] JWT 的安全实践
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q114 · JWT 的安全实践

> 难度:★★★ | 标签:JWT, 安全

**问**:JWT 有哪些安全风险?生产中要注意哪些实践?

**答**:JWT 默认只防篡改不防泄露,且签发后在过期前无法撤销。实践要点:1) 短有效期 + refresh token 轮换;2) 使用 `alg` 白名单校验,防止 `alg=none` / 算法混淆攻击;3) HS256 密钥足够强,或改用 RS256 非对称签名让验证方只持公钥;4) payload 只放非敏感信息(它是 Base64 可读,不是加密);5) 需要主动注销时引入服务端黑名单或版本号,配合 Redis 存储失效状态。

```python
# file: code/03_Web后端开发/q114_jwt_best_practice.py
try:
    from jose import jwt, JWTError
except ImportError:
    print("该题演示需要第三方库 python-jose:pip install python-jose(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

SECRET = 'a-very-long-random-secret-key-at-least-32-bytes'
ALLOWED_ALGS = ['HS256']            # 显式白名单,防算法混淆

def decode_token(token: str) -> dict:
    try:
        # algorithms 白名单必传;verify_exp 默认校验过期
        payload = jwt.decode(token, SECRET, algorithms=ALLOWED_ALGS)
    except JWTError as e:
        raise PermissionError(f'invalid token: {e}')
    if 'sub' not in payload:
        raise PermissionError('missing sub')
    return payload

def revoke(token: str, blacklist: set[str]):
    payload = decode_token(token)
    blacklist.add(token)            # 简化示例:生产用 Redis + TTL

blacklist: set[str] = set()
```

**追问**:
- Session 和 JWT 撤销的本质区别?——Session 服务端有状态可随时删除;JWT 无状态只能靠黑名单或短过期补救。
- alg 混淆攻击是什么?——攻击者把 RS256 token 改标 HS256,用公钥当 HMAC 密钥骗过校验;库必须显式白名单 algorithms=['RS256']。
- JWT payload 能放敏感信息吗?——不能,Base64 只是编码;要敏感信息就得 JWE 加密或干脆服务端存会话。
- 登出即失效怎么做?——jti/版本号写 Redis 黑名单,校验依赖多查一次;或者短过期(5-15min)让风险窗口可控。
