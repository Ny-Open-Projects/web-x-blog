---
title: "[Q7804] 多 Agent 的静默终止：所有 Agent 都空闲但任务没做完"
date: 2026-11-25
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7804 · 多 Agent 的静默终止：所有 Agent 都空闲但任务没做完

难度：P7 ｜ 标签：多 Agent、quiescence、静默终止、依赖缺失、编排

基线：库知识库外知识卡，用纯 Python 的任务依赖图与调度循环模拟"无在飞任务、无可运行任务、目标未达成"的静默终止。

**问**：一条多 Agent 流水线：抓取 → 解析 → 摘要 → 审核 → 发布。上线后有一次整条链路卡住 40 分钟，监控显示 5 个 Agent 全部 `idle`，没有任何报错，直到上游超时重试才恢复。事后发现"审核" Agent 因为配置错误没注册，`发布` 任务一直在等一个永远不会出现的依赖。为什么系统自己发现不了"全体空闲但没干完"？单 Agent 超时为什么不够？静默终止该怎么检测？

**答**：

- **结论**：每个 Agent 只知道自己"没活干"，不知道"全局还有任务没完成"。当依赖图里缺了一条边/一个节点，等待方永远不满足前置条件，也不会进入"运行中"，于是**没有超时可以触发**：超时通常挂在"正在执行的任务"上，而这里是"从未开始"。这叫**静默终止/quiescence**：`in_flight == 0`、`runnable == 0`、但 `completed != all`。必须在**编排层**做全局检测，而不是指望单个 Agent 的 watchdog。
- **取舍**：① 全局静默检测：每轮调度后检查"三条件"，O(任务数)，最直接；② 依赖图静态校验：提交前拓扑排序 + 检查每个依赖是否存在，能在启动时抓住"缺节点"，但抓不住运行时动态依赖；③ 超时兜底：给整个 workflow 设 deadline，简单但发现晚、损失大；④ 心跳/租约：Agent 定期上报"我还活着但没活干"，能区分"空闲"与"卡死"，代价是额外心跳流量。
- **实战**：① 提交前校验依赖图：所有 `deps` 必须存在于任务表，环检测拒绝；② 每轮调度后跑 quiescence 检测，三条件同时满足就标记 `STALLED` 并输出"卡在哪个任务、等哪个依赖"；③ 区分 `STALLED`（依赖缺失/环）与 `DONE`（全部完成）与 `FAILED`（有任务失败），不要用同一个状态；④ 监控"空闲 Agent 数 / 未完成任务数"，两者同时 >0 且持续 N 轮就是静默终止前兆。

下面构造一个缺失依赖的任务图，对比"单 Agent 超时"与"全局静默检测"的发现时机。

```python
# quiescence: 无在飞、无可运行、目标未达成 -> 静默终止
TASKS = {
    "fetch":     {"deps": [],         "status": "done"},
    "parse":     {"deps": ["fetch"],  "status": "done"},
    "summarize": {"deps": ["parse"],  "status": "done"},
    "publish":   {"deps": ["review"], "status": "pending"},   # review 未注册
}


def runnable(tasks):
    return [k for k, v in tasks.items()
            if v["status"] == "pending" and all(
                tasks.get(d, {}).get("status") == "done" for d in v["deps"])]


def step(tasks):
    ready = runnable(tasks)
    if not ready:
        return "STALLED"
    for k in ready:
        tasks[k]["status"] = "done"
    return "PROGRESSED"


tick = 0
state = "PROGRESSED"
while state == "PROGRESSED" and tick < 10:
    tick += 1
    state = step(TASKS)

pending = [k for k, v in TASKS.items() if v["status"] != "done"]
print(f"[1] 第 {tick} 轮: 状态={state}, 在飞=0, 未完成={pending}")
assert state == "STALLED" and pending == ["publish"]
assert tick == 1, "全局检测应在第一轮就发现"

# 单 Agent 超时: 只挂在'运行中'的任务上, 从未开始的任务没有超时
PER_AGENT_TIMEOUT = 30
print(f"[2] 单 Agent 超时要 {PER_AGENT_TIMEOUT} 轮才触发, 全局检测在第 {tick} 轮")
assert tick < PER_AGENT_TIMEOUT


# 区分三种终态: DONE / FAILED / STALLED
def final_state(tasks, failed=()):
    if failed:
        return "FAILED"
    if all(v["status"] == "done" for v in tasks.values()):
        return "DONE"
    if not runnable(tasks):
        return "STALLED"
    return "RUNNING"


print(f"[3] 当前={final_state(TASKS)}, 全部完成={final_state({'a': {'deps': [], 'status': 'done'}})}, "
      f"有失败={final_state(TASKS, failed={'publish'})}")
assert final_state(TASKS) == "STALLED"
assert final_state({"a": {"deps": [], "status": "done"}}) == "DONE"
assert final_state(TASKS, failed={"publish"}) == "FAILED"

# 静态校验: 提交前发现缺失依赖
def validate(tasks):
    problems = []
    for k, v in tasks.items():
        for d in v["deps"]:
            if d not in tasks:
                problems.append(f"{k} 依赖不存在的 {d}")
    return problems


print(f"[4] 提交前校验: {validate(TASKS)}")
assert validate(TASKS) == ["publish 依赖不存在的 review"]
print("    → 实测 静态校验能提前拦住缺节点; 运行时 quiescence 兜住动态漏网")
```

**追问一**：静默终止和死锁有什么区别？—— 死锁是**等待图成环**（A 等 B、B 等 A），每个参与者都在等一个持锁方；静默终止是**可运行集合为空**，可能因为环，也可能因为依赖缺失、条件永远不满足、事件丢失。环检测只能抓前者；`in_flight=0 && runnable=0 && not done` 能同时抓两者，是更通用的兜底。

**追问二**：为什么不能只给整个 workflow 设一个 40 分钟 deadline？—— 能兜底，但发现太晚：40 分钟里可能已经烧了 token、占用了并发配额、下游报表延迟。静默检测在第一轮就能报"publish 等一个不存在的 review"，定位到具体依赖；deadline 只能告诉你"超时了"，还要人工排查。两者是"快速失败"与"最终兜底"的关系。

## 背诵要点

- 静默终止三条件：`in_flight == 0`、`runnable == 0`、`completed != all`；单 Agent 超时抓不到"从未开始"的任务。
- 提交前做依赖存在性 + 环检测；运行时每轮做 quiescence 检测，输出卡住的任务与缺失依赖。
- 终态要区分 `DONE`/`FAILED`/`STALLED`，不要用同一个状态掩盖"没干完"。

## 复盘追问

- 如果依赖是运行时动态产生的（如 Agent 临时决定调用另一个 Agent），静态图校验还够吗？
- 心跳能区分"空闲"与"卡死"，但心跳本身也可能丢；怎样避免把"网络抖动"误判成静默终止？
