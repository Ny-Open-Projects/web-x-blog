---
title: [Q7694] LLM 配额 RPM/TPM 与并发请求的容量账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7694 · LLM 配额 RPM/TPM 与并发请求的容量账

难度：P6 ｜ 标签：容量规划、速率限制、RPM、TPM、配额

基线：Python 3.9+；OpenAI/兼容平台组织级 RPM/TPM 配额；429 退避。

**问**：产品要做 500 并发用户的客服 agent，单请求平均输入 3k token、输出 500 token、耗时 8 秒。供应商给的组织配额是 10000 RPM / 200 万 TPM。这笔并发容量账怎么算？会撞哪个限制？撞了怎么办？

**答**：
- **结论**：两个限制分别算：RPM 口径——每请求平均 8s，一个"并发槽"每分钟发起 60/8 ≈ 7.5 个请求，500 并发 ≈ 3750 RPM < 10000，RPM 不是瓶颈；TPM 口径——每分钟 3750 请求 × (3k 输入+500 输出) ≈ 1312 万 token，**远超 200 万 TPM**，瓶颈是 TPM（常见误区：只看 RPM）。TPM 瓶颈下的有效并发 = TPM / (每请求 token / 8s × 60s) ≈ 200 万 / 26 万×... 即并发上限约 76。撞限的形态是 429 突刺——峰值时刻集中失败，而不是平滑降速。
- **取舍**：应对梯度：(1) 客户端令牌桶按 TPM/RPM 双桶限流，主动排队而不是打过去吃 429（429 本身也消耗配额窗口）；(2) 降每请求 token（上下文压缩、输出长度上限）；(3) 申请提额或多 key/多供应商池化（注意成本与一致性）；(4) 削峰——非实时任务走 Batch API。另外退避要带 jitter，避免集群同步重试造成"重试风暴二次打满"。
- **实战**：监控三指标：配额水位（当前分钟已用/上限）、429 率、排队时长 P95；容量规划时按 P95 请求体积算而不是均值（长尾大请求撞 TPM 最快）。

```python
# RPM/TPM 双桶容量账（标准库可运行）。
def capacity(users: int, think_s: float, in_tok: int, out_tok: int,
             rpm_limit: int, tpm_limit: int) -> dict:
    rpm_need = users * (60 / think_s)                 # 每分钟发起的请求数
    tpm_need = rpm_need * (in_tok + out_tok)          # token 口径
    max_users_rpm = rpm_limit * think_s / 60
    max_users_tpm = tpm_limit * think_s / 60 / (in_tok + out_tok)
    return {
        "RPM需求": round(rpm_need), "RPM余量": f"{rpm_limit / max(rpm_need,1):.1f}x",
        "TPM需求": int(tpm_need), "TPM超限比": f"{tpm_need / tpm_limit:.1f}x",
        "RPM瓶颈最大并发": int(max_users_rpm),
        "TPM瓶颈最大并发": int(max_users_tpm),   # 有效并发取 min
    }

if __name__ == "__main__":
    r = capacity(users=500, think_s=8, in_tok=3000, out_tok=500,
                 rpm_limit=10000, tpm_limit=2_000_000)
    for k, v in r.items():
        print(f"{k}: {v}")
    # RPM余量 2.7x（不撞）；TPM超限比 6.6x（撞）；
    # TPM 瓶颈最大并发 ~76 -> 500 并发需提额/降 token/削峰三管齐下。
```

**追问**：
- 一层：为什么按"平均 8 秒耗时"折算 RPM 是错的（或至少危险）？→ 提示：耗时随输出长度波动，P95 更长；且突发到达（整点活动）会让瞬时 RPM 远超均值，限流器必须按突发容量（burst）设计。
- 二层：429 重试风暴是怎么形成的？→ 提示：N 个客户端同时失败同时重试，Retry-After 窗口再次同步打满；解法是 jitter + 指数退避 + 全局单飞（single-flight）排队器。

**背诵要点**：
1. 双桶账：RPM 看"并发×60/单请求耗时"，TPM 看"RPM×每请求 token"；本案 TPM 超限 6.6 倍才是真瓶颈。
2. 有效并发 = min(RPM 瓶颈并发, TPM 瓶颈并发)；规划按 P95 请求体积。
3. 撞限应对：客户端双桶限流主动排队 > 降 token > 提额/多池 > Batch API 削峰；退避必须加 jitter。

**复盘追问**：
1. 为什么压测没撞限、上线撞了？提示：压测环境配额不同或请求体积偏小；压测必须带真实上下文体积分布。
2. 多供应商池化后账怎么变？提示：故障切换时另一家的 schema/价格/配额都不同，池化要按供应商分别记账。
