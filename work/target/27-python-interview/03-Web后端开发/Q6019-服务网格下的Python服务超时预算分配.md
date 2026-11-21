---
title: [Q6019] 服务网格下的超时预算分配
date: 2026-11-19
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6019 · 服务网格下的超时预算分配

> 难度:★★★ | 标签:超时, Istio, 事故复盘

**问**：调用链 A→B→C，C 挂 5s、B 配了 10s 重试 2 次、A 配了 8s——为什么用户 30 秒才拿到错误？「超时预算」怎么自上而下分配，mesh（Istio/Envoy）的超时重试与应用内超时为什么必须协同，否则出「重试放大」？

**答**：事故拆解：B 的超时（10s）> A 的预算（8s），且 B 重试 2 次 → 最坏 A 等到 10s×2+ 提前失败——**下层超时必须小于上层剩余预算**，否则上层先断、下层白干（客户端已放弃，服务端还在烧资源）。预算分配方法：① 自上而下：入口总预算（如 8s）= 自身处理 0.5s + 逐层递减分配（B 得 4s、C 得 2s），每层留 50% 给失败快速返回与重试余量；② 每层写死：mesh 层 timeout（Envoy route timeout）≤ 应用层 timeout ≤ 上游剩余预算；③ 重试预算：每层重试次数 × 单次超时 ≤ 该层预算的一半（重试不超预算），且配重试预算熔断（A101）；④ **deadline 传递**：A 把剩余预算写进 header（如 `X-Deadline`/grpc deadline）传下去，每层取 `min(自己配置, 剩余)`——这是消灭「上层先断下层白干」的根本手段。mesh 与应用协同：Envoy 的 timeout 对「应用正在处理的请求」也生效（连接被 mesh 切断），应用却不知道 → 出现「应用认为成功、上游已失败」的幽灵写；写操作必须等应用层事务真正完成或配幂等重试。

```python
# 全部标准库；demo 实现预算分配器与 deadline 传递
import time

class Budget:
    """超时预算：自上而下分配，每层取 min(配置, 剩余)。"""
    def __init__(self, total: float):
        self.total = total
        self.remaining = total

    def allocate(self, share: float, hard_cap: float) -> float:
        """给下游分配预算：份额 + 硬上限，两层取小。"""
        grant = min(self.remaining * share, hard_cap)
        self.remaining -= grant
        return grant

def plan_budgets(total=8.0):
    b = Budget(total)
    a_self = b.allocate(0.06, 0.5)      # A 自身处理 6%
    b_budget = b.allocate(0.5, 4.0)     # B 拿一半
    c_budget = b.allocate(0.9, 2.0)     # B 的 90% 给 C（留余量）
    print(f"total={total}s → A自身={a_self}s B={b_budget}s C={c_budget}s 剩余={b.remaining:.1f}s")
    # 重试约束：重试次数×单次超时 ≤ 预算一半
    c_timeout, c_retries = 1.2, 2
    assert c_timeout * (c_retries + 1) <= c_budget, "重试超预算"
    print(f"C 重试 {c_retries} 次 × {c_timeout}s ≤ {c_budget}s ✅")
    return {"a": a_self, "b": b_budget, "c": c_budget}

def deadline_header(budget_left: float) -> dict:
    """deadline 传递：A 层生成，下游每层取 min(自己的配置, 剩余)。"""
    return {"X-Deadline-Ms": str(int(budget_left * 1000 + time.time() * 1000))}

def effective_timeout(cfg: float, headers: dict) -> float:
    left = float(headers["X-Deadline-Ms"]) / 1000 - time.time()
    return max(0.05, min(cfg, left))     # 不超上游剩余；至少留 50ms 快速返回

if __name__ == "__main__":
    plan = plan_budgets()
    h = deadline_header(plan["b"])       # B 层视角：剩余 = b 预算
    print("C 层生效超时 =", effective_timeout(2.0, h), "s（min(配置, 剩余)）")
    # 幽灵写防线：mesh 切断连接后应用仍在写 → 写接口必须幂等或等事务提交再返回
```

**追问**：1) 重试为什么要「预算内」而不是固定次数？——固定次数在慢下游时重试总耗时超上层预算，上层已返回错误而重试还在继续（浪费 + 重试风暴）；预算内重试保证资源有界。2) grpc 的 deadline 传播和 HTTP 头方案差异？——grpc deadline 是协议字段（metadata `grpc-timeout`）自动跨层传播；HTTP 要手动约定 header 且每个中间件都要尊重它——工程一致性是难点。3) 熔断（A106）和预算什么关系？——预算管「单请求内部怎么花」，熔断管「下游整体病了别去了」；两者互补，预算分配好能减少触发熔断的频率。

## 背诵要点
1. 铁律：下层超时 < 上层剩余预算；每层实际超时 = min(自身配置, deadline 头剩余)。
2. 重试约束：次数 × 单次超时 ≤ 层预算一半；重试预算熔断联动 A101。
3. mesh 幽灵写：Envoy 切断后应用不知道——写操作幂等或等事务提交。

## 复盘追问
1. 为什么入口总预算不能给满（如 8s 全给 B）？（提示：无余量则任何抖动都触发上游失败；50% 原则留快速失败空间）
2. deadline 到期瞬间，正在执行的写事务怎么办？（提示：应用侧 deadline 响应与事务提交解耦——先返回超时但事务可能成功，需幂等与对账，参考 A102）
