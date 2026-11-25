---
title: [A160] 跨服务日志关联：trace_id 与采样联动
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A160 · 跨服务日志关联

> 难度:★★☆ | 标签:trace_id, 日志, 可观测性

**问**（笔试·编程+场景题）：用户报障「订单失败」，三个服务的日志分散三处——trace_id 怎么贯穿（入口生成/透传/落日志），日志里除了 trace_id 还要什么字段才能「一条日志定位问题」（user_id/request 参数/版本号），采样（Q6015）和 trace_id 怎么联动（错误 trace 全留但日志采样丢了怎么办），「trace_id 缺失的服务」（老服务没接）怎么补关联？

**答**：① trace_id 贯穿：入口（网关）生成 → 透传（header）→ 每个服务的每条日志带 trace_id（中间件自动注入，Q7015 structlog 上下文绑定）——**缺失的服务**：没有 trace_id 传入时按「时间窗口+user_id+接口」弱关联（尽力而为），长期方案是改造接入（ instrumentation 有成本，按服务重要性排期）。② 日志关键字段五件套：trace_id、user_id、request 参数摘要（脱敏）、服务版本、本地 span 耗时——「一条日志定位」的标准：不用再查其他日志就知道发生了什么+属于谁+哪个版本。③ 采样联动：trace 全留（tail-based，错误强制保留）但**日志**按比例采——错误 trace 的日志会被采样掉 → 联动规则：**日志采样以 trace_id 为粒度**（同一 trace 的日志同进同出——采样决策在 trace 层做，日志跟随）；错误 trace 的日志 100% 保留。④ 老服务补关联兜底：网关层把 trace_id 写进发给老服务的请求，老服务返回时带上（哪怕只 echo）→ 网关侧聚合关联——「不改老服务也能关联」的网关代理模式。

```python
# 全部标准库；demo 实现「trace 粒度采样联动 + 弱关联兜底」
import time, random
from collections import defaultdict

class TraceAwareSampler:
    """日志采样以 trace_id 为粒度：错误 trace 全留，成功按比例。"""
    def __init__(self, sample_rate: float = 0.1):
        self.rate = sample_rate
        self.decisions: dict[str, bool] = {}      # trace_id -> 是否保留（trace 层决策）
        self.logs: list[dict] = []
        self.errors = 0
    def trace_finish(self, trace_id: str, had_error: bool):
        keep = had_error or random.random() < self.rate
        self.decisions[trace_id] = keep
        if had_error: self.errors += 1
    def log(self, trace_id: str, service: str, msg: str, **fields):
        keep = self.decisions.get(trace_id, True)  # 未决策的（进行中）先保留
        if keep:
            self.logs.append({"trace_id": trace_id, "svc": service, "msg": msg, **fields})

def weak_correlate(logs_by_service: dict[str, list[dict]], user_id: str,
                   endpoint: str, window_s: float = 5.0) -> dict[str, list]:
    """老服务无 trace_id：按 user_id+endpoint+时间窗弱关联。"""
    out = defaultdict(list)
    for svc, logs in logs_by_service.items():
        for lg in logs:
            if lg.get("user_id") == user_id and lg.get("endpoint") == endpoint:
                out[svc].append(lg)
    # 时间窗收敛：只保留最早日志 ±window 内的
    if out:
        base = min(min(l["ts"] for l in v) for v in out.values())
        for svc in out:
            out[svc] = [l for l in out[svc] if abs(l["ts"] - base) <= window_s]
    return dict(out)

if __name__ == "__main__":
    random.seed(4)
    s = TraceAwareSampler(sample_rate=0.1)
    s.trace_finish("t-err-1", had_error=True)
    s.log("t-err-1", "order", "下单失败: 库存服务超时", user_id="u1", version="v2.3")
    s.trace_finish("t-ok-1", had_error=False)
    s.log("t-ok-1", "order", "正常下单")
    s.trace_finish("t-ok-2", had_error=False)
    s.log("t-ok-2", "order", "正常下单")
    assert any(l["trace_id"] == "t-err-1" for l in s.logs)   # 错误 trace 日志全留
    print("trace 粒度采样：错误 trace 日志 100% 保留 ✅")
    now = time.time()
    services = {
        "gateway": [{"ts": now, "user_id": "u1", "endpoint": "/order", "msg": "502"}],
        "legacy-billing": [{"ts": now - 1, "user_id": "u1", "endpoint": "/order",
                            "msg": "charge failed"}],        # 无 trace_id 的老服务
    }
    corr = weak_correlate(services, "u1", "/order")
    assert "legacy-billing" in corr
    print("弱关联兜底：无 trace_id 老服务按 user+endpoint+时间窗关联 ✅", list(corr))
    # 口径：trace_id 入口生成透传；日志五件套（trace/user/参数/版本/耗时）；
    # 采样决策在 trace 层、日志跟随；老服务网关代理模式补关联。
```

**追问**：1) 为什么采样决策要在 trace 层而不是日志层各自决定？——日志层各自按比例采会把同一 trace 的日志打散（一半有一半无），trace 断裂无法排查；trace 粒度决策保证「留下的 trace 是完整的」——完整比全量重要。2) 弱关联的误关联风险？（提示：同 user 同 endpoint 并发两次请求会误关联——时间窗收紧 + 加请求参数指纹（金额/商品 id）二次过滤——弱关联是兜底不是精确手段，结论需人工确认）3) 「网关代理模式」的侵入成本？（提示：零侵入老服务（不改代码），网关响应时注入 trace echo；但老服务内部多段日志还是关联不了（只能关联入口/出口）——精度有限，长期还是要 instrumentation 排期改造）

## 背诵要点
1. trace_id 贯穿：入口生成 → header 透传 → 中间件自动注入日志；缺失服务按 user+endpoint+时间窗弱关联兜底。
2. 日志五件套：trace_id/user_id/参数摘要/服务版本/耗时——「一条日志定位问题」的标准。
3. 采样决策在 trace 层（错误全留成功按比例），日志跟随同进同出——完整比全量重要。

## 复盘追问
1. trace_id 全链路有了，但日志还是难排查——多数是什么问题？（提示：日志内容质量（缺参数摘要/错误信息只有「failed」）——trace_id 解决「找到日志」，五件套解决「看懂日志」；两件事都要）
2. 老服务 20 个，改造成本评估怎么排优先级？（提示：按「故障频率×影响面」排——高频故障链路上的老服务优先 instrumentation（Q123 依赖图 + 事故统计），边缘服务用弱关联兜底——改造成本是投资，投给回报大的）
