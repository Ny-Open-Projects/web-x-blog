---
title: [Q7511] ReAct 循环的步数预算推导与死循环熔断
date: 2026-11-19
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7511 · ReAct 循环步数预算与熔断

> 难度:★★★ | 标签:Agent, ReAct, 熔断

**问**：Agent 循环「最多跑 N 步」的 N 怎么定才不是拍脑袋——预算从哪几项成本推导？「模型在同一个工具上反复失败」怎么熔断（同错误签名计数），熔断后的兜底（降级回答 vs 人工接管）怎么选？重复检测除了精确匹配还要看什么？

**答**：① 预算推导四项：**任务步数上限**（复杂任务的步骤树深 × 每步平均工具调用，典型 10-30）、**成本上限**（max_tokens × 步数 × 单价 ≤ 预算，倒推步数）、**延迟上限**（用户容忍墙钟时间 ÷ 每步耗时）、**错误预算**（失败重试不无限涨——预算与重试分开记账）。四项取最小才是 N，写进配置可调，不是常量。② 同错误熔断：对「工具名+错误类型+关键参数」做错误签名，签名计数 ≥3 直接停止该工具路径（换路或降级）——防止「参数错→重试→再错」的无限打转。③ 重复检测：精确匹配（相同 tool+args）只是第一层；**语义重复**（参数微调重试同一意图，如 search("python gil") → search("python GIL") → search("gil python")）要用相似度（哈希归一化 + 编辑距离）兜住。④ 熔断后兜底选择：任务可降级（部分结果仍有用）→ 返回部分结果+明确声明未完成；任务必须完整（写库操作）→ 拒绝执行转人工/队列，**绝不静默编造完成**。

```python
# 全部标准库；demo 实现预算记账 + 错误签名熔断 + 语义重复检测
import hashlib, re, time

class Budget:
    """四项预算取最小：步数/成本/墙钟/错误。"""
    def __init__(self, max_steps=30, max_cost=2.0, max_wall=120.0, max_errors=5):
        self.limits = {"steps": max_steps, "cost": max_cost,
                       "wall": max_wall, "errors": max_errors}
        self.used = {"steps": 0, "cost": 0.0, "wall": 0.0, "errors": 0}
        self.t0 = time.monotonic()
    def remaining_budget(self) -> int:
        """每步开始前问一次：还允许几步（四项各自倒推取最小）。"""
        wall_left = max(0, self.limits["wall"] - (time.monotonic() - self.t0))
        by_cost = max(0, int((self.limits["cost"] - self.used["cost"]) / 0.05))  # 0.05$/步
        by_wall = max(0, int(wall_left / 2.0))                                    # 2s/步
        return min(self.limits["steps"] - self.used["steps"], by_cost, by_wall)
    def record_step(self, cost: float, error: bool = False):
        self.used["steps"] += 1
        self.used["cost"] += cost
        if error: self.used["errors"] += 1

def err_signature(tool: str, args: dict, err: str) -> str:
    """错误签名：tool + 归一化参数 + 错误类型。"""
    norm = re.sub(r"\d+", "#", str(sorted(args.items())))   # 数字归一化（页码类参数）
    return hashlib.md5(f"{tool}|{norm}|{type(err).__name__ or err[:40]}".encode()).hexdigest()[:10]

def semantic_sig(query: str) -> str:
    """语义重复：去大小写/标点/词序无关的词集哈希。"""
    words = frozenset(re.findall(r"\w+", query.lower()))
    return hashlib.md5("|".join(sorted(words)).encode()).hexdigest()[:10]

class Circuit:
    def __init__(self, max_repeat: int = 3):
        self.err_count: dict[str, int] = {}
        self.seen_queries: dict[str, int] = {}
        self.max_repeat = max_repeat
    def check(self, tool: str, args: dict, prev_err: str | None) -> str:
        if prev_err:
            sig = err_signature(tool, args, prev_err)
            self.err_count[sig] = self.err_count.get(sig, 0) + 1
            if self.err_count[sig] >= self.max_repeat:
                return f"熔断：同错误签名 {self.max_repeat} 次，换路径或降级"
        ssig = semantic_sig(args.get("query", ""))
        self.seen_queries[ssig] = self.seen_queries.get(ssig, 0) + 1
        if self.seen_queries[ssig] > 3:
            return "熔断：语义重复搜索（参数微调刷次数）"
        return "ok"

if __name__ == "__main__":
    b = Budget(max_steps=10, max_cost=0.3)
    print("预算允许步数:", b.remaining_budget())
    c = Circuit()
    outcomes = []
    for i in range(4):
        verdict = c.check("db_query", {"query": "python gil", "page": i}, "TimeoutError")
        outcomes.append(verdict)
    assert outcomes[-1].startswith("熔断"), outcomes
    print("错误签名熔断:", outcomes[-1])
    c2 = Circuit()
    assert c2.check("search", {"query": "python GIL!"}, None) == "ok"
    assert c2.check("search", {"query": "GIL python"}, None) == "ok"
    v = c2.check("search", {"query": "python gil."}, None)
    print("语义重复检测（词序/标点不变）:", v)
    # 兜底口径：可降级任务返回部分结果 + 未完成声明；必须完整任务转人工——绝不静默编造完成。
```

**追问**：1) 为什么错误签名要「参数归一化」？——`page=1/2/3` 翻页重试本质同一失败（服务超时），数字归一化后签名一致才能计数；但把「查询词」也归一化会误伤合法变体——签名设计要按工具语义分层。2) 预算和错误熔断谁先生效？——都生效，取先到：预算防「合法但太贵」，熔断防「非法打转」；日志要记录触发的那个条件供复盘。3) 部分结果的「完成度声明」怎么做？——结构化输出 schema 加 `completed: bool` + `missing_steps` 字段，让下游消费者程序化处理不完整结果，而不是靠自然语言「可能没做完」。

## 背诵要点
1. 步数预算 = min(任务步数、成本倒推、墙钟倒推、错误预算)，四项分开记账。
2. 错误签名（tool+归一化参数+错误类型）计数 ≥3 熔断；语义重复用词集哈希兜参数微调刷次数。
3. 熔断兜底二选一：可降级 → 部分结果 + completed 声明；必须完整 → 转人工；绝不静默编造完成。

## 复盘追问
1. Agent 卡在「工具返回成功但语义失败」（如搜索命中垃圾结果）怎么破？（提示：结果质量评估层（相关性打分）进循环，连续低分视为错误签名触发熔断）
2. 预算超限与熔断的告警怎么区分处理？（提示：预算超限=常规运维指标（调预算）；熔断=异常信号（工具坏了/任务设计错），要单独告警复盘）
