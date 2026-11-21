---
title: [Q7552] Agent 多会话并发写冲突的复盘与工具层乐观锁
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7552 · Agent 多会话并发写冲突的复盘与工具层乐观锁

难度：P6 | 标签：并发控制、乐观锁、工具设计、事故复盘

**问**：两个运营同时让 Agent 改同一个广告预算，一个"加 10 元"一个"改 50 元"，结果 10 元的修改凭空消失。为什么 Agent 的工具调用天然容易丢更新？工具层怎么加乐观锁？冲突了让谁决策？

**答**：
- **结论**：工具调用的典型形态是读-改-写（read current → compute new → write），两个会话并发时都基于同一初始值计算，后写覆盖前写。防线在工具层而不是模型层：资源记录带版本号，写请求必须携带"读到的版本"，不匹配即冲突——返回最新状态让调用方重读重试（CAS 语义）。冲突分两类：版本冲突可自动重试（重读后 delta 仍适用）；语义冲突（两个人意图冲突，如"预算上限 100"vs"改成 200"）必须回给模型重新规划或升级人工——自动重试会违背某个用户的意图。
- **取舍**：工具层全量加锁会拖慢并发吞吐，合理的粒度是"按资源键"加版本校验（只在真有并发写的热点资源上启用）；重试次数要有上限（本例 1 次），超过上限说明冲突风暴，应该转人工而不是无限循环。模型本身不知道并发存在——把它暴露给模型（工具返回 conflict + 最新状态）比在提示词里写"注意并发"有效得多。
- **实战**：落地清单：① 可变资源工具（更新配置/下单/改配额）强制携带 `expected_version` 参数；② 工具返回结构统一：`{ok, reason: conflict|policy_violation, current}`，模型据此决定重试还是上报；③ 审计日志记录两个会话的完整读写序列，复盘丢更新时能还原时序。

```python
"""Agent 多会话并发写冲突：无锁丢更新 vs 工具层乐观锁与冲突分类。"""
import threading

class ToolStore:
    """工具层的资源存储：记录带版本号（写前必须带上读到的版本）。"""

    def __init__(self):
        self.data = {"ad_budget": {"amount": 100, "ver": 1}}
        self.lock = threading.Lock()
        self.conflicts = 0

    def write_optimistic(self, key: str, amount: int, expect_ver: int) -> dict:
        with self.lock:
            cur = self.data[key]
            if cur["ver"] != expect_ver:
                self.conflicts += 1
                return {"ok": False, "reason": "conflict",
                        "current": dict(cur)}          # 冲突：带最新状态回去重读
            self.data[key] = {"amount": amount, "ver": expect_ver + 1}
            return {"ok": True, "ver": expect_ver + 1}

    def write_naive(self, key: str, amount: int) -> None:
        """无版本校验：读-改-写直接覆盖（丢更新）。"""
        with self.lock:
            self.data[key] = {"amount": amount, "ver": self.data[key]["ver"] + 1}

# 场景一：无锁——两个会话基于同一初始值 100，后写覆盖前写
store_a = ToolStore()
res_a: list = []
def naive_worker(delta: int):
    store_a.write_naive("ad_budget", 100 + delta)
    res_a.append(store_a.data["ad_budget"]["amount"])
threads = [threading.Thread(target=naive_worker, args=(d,)) for d in (10, 50)]
[t.start() for t in threads]; [t.join() for t in threads]
print(f"无锁并发写：最终 {store_a.data['ad_budget']['amount']} 元"
      f"（正确应为 160，丢失了 +10 的更新）")

# 场景二：工具层乐观锁——两边先各自读到 ver1，随后竞争写，必然一方冲突重试
store_b = ToolStore()
res_b: list = []
barrier = threading.Barrier(2)
def optimistic_worker(delta: int):
    cur = store_b.data["ad_budget"]          # 两个会话读到的都是 (amount=100, ver=1)
    barrier.wait()                           # 双方都读完才放行写入 -> 制造真实竞争
    r = store_b.write_optimistic("ad_budget", cur["amount"] + delta, cur["ver"])
    if not r["ok"] and r["reason"] == "conflict":
        cur2 = r["current"]                  # 重新读最新状态，把 delta 作用其上
        r = store_b.write_optimistic("ad_budget", cur2["amount"] + delta, cur2["ver"])
    res_b.append(r)

threads = [threading.Thread(target=optimistic_worker, args=(d,)) for d in (10, 50)]
[t.start() for t in threads]; [t.join() for t in threads]
print(f"乐观锁并发写：最终 {store_b.data['ad_budget']['amount']} 元，"
      f"冲突 {store_b.conflicts} 次且经重读自动恢复")
print("冲突分类：版本冲突可重试（重读即可）；语义冲突（超出策略边界）要回给模型重规划")
```

**追问链**：
1. 追问一层：为什么这个防线不能做在"让模型小心"上？——模型看不到真实的并发时序（工具结果到达时状态可能已变），提示词的"注意并发"是猜测；版本校验是存储层的原子判定，确定性 100%。经验法则：凡是"数据正确性"问题都下沉到工具/存储层，凡是"决策质量"问题才交给模型。
2. 追问二层：如果 delta 操作不可交换（比如"设置价格=X"而不是"加 10 元"），重试重读还有意义吗？——"设置"型写入重试没有意义（后写者赢就是合理语义，冲突提示反而该转人工确认）；只有"增量/条件更新"型（+10、状态机推进）重试才有价值。工具 schema 里应区分 set 与 delta 两类写语义。

**背诵要点**：
1. 工具调用是读-改-写，多会话并发必然丢更新；防线在工具层版本校验（CAS），不在提示词。
2. 冲突分类：版本冲突自动重读重试；语义冲突回给模型重规划或升级人工。
3. 可变资源工具 schema 强制 expected_version；返回结构统一 ok/reason/current。

**复盘追问**：
1. 复盘时怎么证明"确实丢了更新而不是用户改主意"？（工具调用审计：两个会话的读值、写值、时间戳时序——A 读 100 写 110，B 读 100 写 150，B 后写覆盖，铁证）
2. 为什么重试上限设 1 次而不是 5 次？（冲突风暴说明热点资源上有持续并发写，重试只是排队加剧；1 次解决偶发竞争，持续冲突转人工/队列串行化）
