---
title: "[Q5083] random 生成 token 被预测的事故与 secrets 的演进"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5083 · random 生成 token 被预测的事故与 secrets 的演进

难度：★★★☆☆ ｜ 标签：安全 / random / secrets / 事故复盘 / 版本演进

**问**：某服务用 `random.random()` 派发重置密码 token，攻击者拿到了几个 token 后成功预测出他人的 token。为什么会这样？`random.seed()` 不设种子不是"真随机"吗？这个能力缺口是怎么在 Python 版本里被补上的？

**答**：
- **结论**：`random` 模块的默认 Random 实例用 **Mersenne Twister (MT19937)**，它是确定性 PRNG：不播种时用系统熵做一次种子，但输出序列完全可由内部状态推出——观察 624 个连续 32 位输出即可重建状态、预测后续所有"随机数"。token 属于安全敏感值，必须用 CSPRNG。3.6 起标准库给出 `secrets` 模块（封装 os.urandom），并在文档与 lint 生态里持续把 `random` 用于安全场景标为反模式（S311 类检查）。
- **取舍**：`os.urandom` / `secrets` 直接读内核熵池，不可预测但无分布调参能力；`random` 提供可复现、可采样、可控分布——用于仿真、压测造数是对的。演进线：3.6 `secrets` 落地 → 3.9 `randbytes` 补齐 → 3.11+ 各类 lint 规则成熟 → 3.12+ `random` 文档顶部加"不要用于安全目的"红字。同时 `secrets.compare_digest` 顺带解决时序侧信道比较。
- **实战**：事故复盘三步：1）token 生成的所有调用点排查（grep `random.`）；2）已有 token 全量作废重发（状态泄露不可撤销，只能换库）；3）CI 加规则禁止安全目录 import random。注意 `uuid.uuid4()` 底层也是 urandom，可用于标识但拼接业务语义（时间戳+计数器）会削弱随机性。

```python
"""random 可预测性演示 + secrets 正确用法（Python 3.9+）"""
import random, secrets, string

# 1) MT19937 的可复现性：同种子同序列（攻击者预测的原理）
random.seed(2026)
a = [random.random() for _ in range(3)]
random.seed(2026)
b = [random.random() for _ in range(3)]
print("同种子序列完全一致:", a == b)

# 2) getrandbits 是状态直接输出：收集 624 个 32 位字即可重建 MT 状态
#    （untempering 是公开算法，这里演示"输出即状态暴露面"）
words = [random.getrandbits(32) for _ in range(624)]
print("收集到状态暴露面字数:", len(words))

# 3) 正确做法：secrets（os.urandom 封装）
token = secrets.token_urlsafe(32)          # 256 bit 熵，URL 安全
api_key = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(40))
print("token   :", token)
print("api_key :", api_key)

# 4) 常数时间比较，防时序侧信道
ref = secrets.token_hex(16)
probe = secrets.token_hex(16)
print("compare_digest:", secrets.compare_digest(probe, ref))

# 5) 分工准则：random=可复现仿真（压测造数），secrets=一切安全敏感值
rng = random.Random(12345)   # 显式实例化，避免污染全局序列
print("压测样本:", [rng.randrange(100) for _ in range(5)])
```

**追问链**
1. 攻击者具体怎么从 624 个输出重建 MT 状态？
   1. MT19937 每次输出前做 tamper 变换（可逆），拿到 624 个连续 32 位输出后逆变换还原内部状态数组，即可推进生成器预测未来输出；这也是为什么"泄露部分 token + 知道偏移"就够。
   2. 追问：如果中间夹了 `random.random()`（53 位）会怎样？——random() 由两个 32 位字拼出，仍是同一状态流，不影响重建，只是换算方式不同。
2. `secrets.token_urlsafe(32)` 的 32 是什么单位？会话 token 该选多少熵？
   1. 单位是字节，32 字节 = 256 bit 熵；会话/重置 token 业界下限 128 bit（16 字节），API key 建议 160-256 bit，并用哈希落库防库泄露。
   2. 追问：token 存库要不要加密？——存 SHA-256 摘要即可（高熵不需要慢哈希），泄露库也无法反推 token。

## 背诵要点
- random 默认是 MT19937 确定性 PRNG，624 个 32 位输出即可重建状态预测未来，禁用于安全场景。
- 3.6 起 secrets（os.urandom 封装）是标准答案：token_urlsafe/choice/compare_digest（防时序）。
- 分工：random=仿真与造数（可复现），secrets=token/key/防侧信道比较；事故后 token 只能全量作废。

## 复盘追问
- 如何在 CI 层面系统性拦截"安全目录用 random"？规则误报（压测造数目录）怎么豁免？
- 如果 token 还被用作 URL 路径的一部分，日志脱敏和幂等重试之间有什么冲突要权衡？
