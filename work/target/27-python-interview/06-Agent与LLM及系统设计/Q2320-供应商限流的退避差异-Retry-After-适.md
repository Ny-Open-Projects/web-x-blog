---
title: [Q2320] 供应商限流的退避差异:Retry-After 适配
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2320 · 供应商限流的退避差异:Retry-After 适配

> 难度:★★★☆ | 标签:LLM 运维, 限流, 重试

**问**:两家供应商都限流,一家返回 Retry-After 头,一家只返回 429,退避策略能通用吗?

**答**:不能一刀切,按供应商建退避档案:有 Retry-After 的尊重它的指示值——服务器最清楚自己什么时候有空位,但指示值也要受自家上限保护,防止对方下发离谱数值把我方请求冻结几小时;没有指示头的按该供应商的退避曲线走,曲线参数(基值、倍率、上限)逐家配置,激进供应商用短基值快重试,保守供应商用长基值少打扰。计次按 vendor 加请求键隔离,成功后清零,不让一次历史失败影响新请求的退避起点。退避日志要记录"用了哪种模式",复盘限流损失时能分清是没遵守指示还是曲线设错。

```python
# file: code/06_Agent与LLM及系统设计/q2320_backoff_profiles.py
"""供应商限流退避适配:有 Retry-After 就按它的来,没有则用该供应商的退避曲线,退避有上限。"""
PROFILES = {
    "vendorA": {"base": 1.0, "factor": 2.0, "max": 30.0},
    "vendorB": {"base": 2.0, "factor": 1.5, "max": 10.0},
}


class BackoffPlanner:
    def __init__(self, profiles):
        self.profiles = profiles
        self.attempts = {}

    def next_delay(self, vendor, key, retry_after=None):
        k = (vendor, key)
        self.attempts[k] = self.attempts.get(k, 0) + 1
        if retry_after is not None:
            return min(float(retry_after), self.profiles[vendor]["max"]), "respect-retry-after"
        p = self.profiles[vendor]
        d = min(p["base"] * (p["factor"] ** (self.attempts[k] - 1)), p["max"])
        return d, "profile"

    def reset(self, vendor, key):
        self.attempts.pop((vendor, key), None)


if __name__ == "__main__":
    planner = BackoffPlanner(PROFILES)
    d1, s1 = planner.next_delay("vendorA", "chat")
    d2, _ = planner.next_delay("vendorA", "chat")
    d3, _ = planner.next_delay("vendorA", "chat")
    assert (d1, d2, d3) == (1.0, 2.0, 4.0) and s1 == "profile", "vendorA 指数退避"
    d4, s4 = planner.next_delay("vendorA", "chat", retry_after=120)
    assert d4 == 30.0 and s4 == "respect-retry-after", "Retry-After 也受自家上限保护"
    d5, s5 = planner.next_delay("vendorB", "chat", retry_after=5)
    assert d5 == 5.0 and s5 == "respect-retry-after", "合理 Retry-After 照单全收"
    d6, _ = planner.next_delay("vendorB", "mail")
    assert d6 == 2.0, "vendorB 曲线不同 base 2.0"
    planner.reset("vendorA", "chat")
    assert planner.next_delay("vendorA", "chat")[0] == 1.0, "成功后计数清零"
    print("退避差异通过:按供应商曲线 Retry-After 适配 上限保护 成功清零")
```

**追问**:
- 多实例下退避计次怎么共享? 答:计次进 Redis 按供应商汇总,否则每台机器各自全速重试,集群层面的退避形同虚设
- 429 和 5xx 的退避一样吗? 答:不一样,429 是限流按指示退,5xx 是故障走熔断与故障转移,不要用同一条曲线糊弄
