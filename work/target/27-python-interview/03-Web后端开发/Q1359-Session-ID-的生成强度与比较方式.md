---
title: [Q1359] Session ID 的生成强度与比较方式
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1359 · Session ID 的生成强度与比较方式

> 难度:★★ | 标签:会话安全, 密码学

**问**:Session ID 用 `random` 生成行不行?比较两个 SID 用 `==` 有什么问题?

**答**:不行:Python 的 `random` 是 Mersenne Twister,不是密码学安全的,攻击者观察到少量输出就能预测后续状态,必须用 `secrets`(底层 os.urandom)。强度上 SID 至少 128 位熵,`secrets.token_urlsafe(32)` 提供 256 位,配合足够长过期策略可以认为不可穷举。比较时用 `hmac.compare_digest` 恒定时间比较,防止逐字节短路带来的计时侧信道(单独看收益小,但这是零成本的正确习惯)。另外 SID 永远不要出现在 URL 里,只走 HttpOnly + Secure Cookie。

```python
# file: code/03_Web后端开发/q1359_sid_strength.py
"""Session ID 的生成强度与恒定时间比较(纯标准库)。"""
import hmac
import secrets

# 弱示例:顺序号完全可预测,仅作对照
weak_sids = [f"SID-{i:08d}" for i in range(3)]
print("弱 SID 可预测:", weak_sids)

strong = secrets.token_urlsafe(32)          # 32 字节 = 256 位熵
print("强 SID 示例:", strong[:16], "... 熵 bits:", 32 * 8)

# 恒定时间比较:避免逐字节短路带来的计时侧信道
a, b = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
print("compare_digest 自身:", hmac.compare_digest(strong, strong))
print("compare_digest 他人:", hmac.compare_digest(strong, b))
```

**追问**:
- 用 uuid4 做 SID 行吗?——可以,uuid4 底层也是 CSPRNG,122 位熵达标;自增 ID、时间戳、uuid1 绝对不行。
- 为什么不在 SID 里编码用户信息?——SID 必须是不透明随机串,任何可读结构都给攻击者提供信息。
