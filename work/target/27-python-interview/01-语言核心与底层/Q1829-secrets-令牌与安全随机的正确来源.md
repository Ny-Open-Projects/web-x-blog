---
title: [Q1829] secrets:令牌与安全随机的正确来源
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1829 · secrets:令牌与安全随机的正确来源

> 难度:★★★☆☆ | 标签:secrets, 安全随机, 令牌

**问**:生成 API token、找回密码链接、短信验证码,随机源该怎么选?

**答**:一律 secrets,不碰 random:random 的 Mersenne Twister 状态可被观测输出反推,不适合任何对抗场景。四个常用面:① token_urlsafe/token_hex 生成 nbytes 字节熵的令牌,前者 URL 安全可直接进链接;② choice 从字母表逐位选,拼验证码与密码;③ compare_digest 常数时间比较,校验令牌时防时序侧信道——普通 == 逐字节短路,时序差会泄露匹配前缀长度;④ 熵意识:16 字节约 128 bit,6 位数字验证码只有约 20 bit,靠限流与有效期补足。与 Q1567 的随机源注入互补:业务代码把 secrets 用法收口到可注入的 provider,测试才可控。

```python
# file: code/01_语言核心与底层/q1829_secrets_tokens.py
"""secrets:令牌与安全随机的正确来源。"""
import secrets
import string


def url_token(nbytes=16):
    return secrets.token_urlsafe(nbytes)    # URL 安全,长度约 1.3 倍 nbytes


def hex_token(nbytes=16):
    return secrets.token_hex(nbytes)


def otp_code(digits=6):
    return "".join(secrets.choice(string.digits) for _ in range(digits))


def constant_time_compare():
    a = secrets.token_bytes(16)
    b = secrets.token_bytes(16)
    return secrets.compare_digest(a, b)     # 常数时间比较,防时序侧信道


def password(pool=None, length=12):
    pool = pool or (string.ascii_letters + string.digits)
    return "".join(secrets.choice(pool) for _ in range(length))


if __name__ == "__main__":
    print("token_urlsafe:", url_token())
    print("token_hex    :", hex_token())
    print("6 位验证码    :", otp_code())
    print("常数时间比较(不同值):", constant_time_compare())
    print("随机密码:", password())
```

**追问**:1) token_urlsafe 的字符数为什么不是 nbytes 的 2 倍?——base64 编码 3 字节变 4 字符,去填充后约 1.3 倍;16 字节出 22 字符,长度按字节算不按字符算。2) 为什么必须 secrets 而不是 random?——random 是 Mersenne Twister,可预测、非加密安全;secrets 用 OS 熵源(os.urandom);密码学语义(secrets.compare_digest 防时序比较)配套。3) 熵的估算?——n 字节 = 8n bit 熵;按「碰撞概率」反推长度;token_hex/urlsafe 的后缀字母表不同不影响熵。4) 生产陷阱?——用 random.randint 生成验证码/令牌;截断 token(熵骤降);令牌进日志或 URL query(泄露面);用 == 比较密文(时序攻击,要 compare_digest)。
