---
title: "[Q7799] Agent 循环终止条件：最大步数、预算与无进展检测三件套"
date: 2026-11-25
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7799 · Agent 循环终止条件：最大步数、预算与无进展检测三件套

难度：P6 ｜ 标签：Agent、主循环、终止条件、最大步数、预算、无进展检测、熔断

基线：库知识库外知识卡，代码用标准库模拟——用动作签名与观测哈希实现三种终止闸门，不调用外部 API。

**问**：一个 ReAct Agent 半夜跑飞，反复调用同一个搜索工具 27 次，烧了 40 美元，最后因为上游限流才停。事后加了 `max_steps=10`，结果另一个需要读 15 个文件的长任务每次都被误杀。只靠最大步数显然不够——终止条件到底该有哪几个？无进展怎么判定？三个闸门同时触发时谁优先？

**答**：

- **结论**：终止条件要三件套，各自防不同的失败模式。① **最大步数**（硬上限）：防止无限循环/代码 bug 导致的失控，最简单但最粗暴，步数定小了会误杀合法长任务；② **预算**（token/金额/时间，硬上限）：直接对应成本与 SLO，比步数更贴近业务，但管不住"低成本空转"（每步很便宜、但重复 100 次）；③ **无进展检测**（软闸）：看**动作签名**是否重复（同一工具+同一参数）、**观测哈希**是否不变（返回内容一样）、**目标距离**是否不降（任务状态没有前进），连续 N 次即判定停滞。三者关系是"硬闸保底、软闸提质"：硬闸（步数/预算）到点必须停，软闸（无进展）可以先触发一次"换策略提示"，再不停才终止。
- **取舍**：无进展的 `patience` 是最难调的参数。太小（2 次）会把"重试一次就成功"的瞬时故障误判为停滞；太大（10 次）则浪费预算。经验是 3 次，并且**区分可重试动作**（网络抖动、限流退避、外部状态未就绪）与**不可重试动作**（同一查询、同一文件、同一 API 同参数）——前者不该计入停滞，后者才计。另一个取舍是"终止后的收场"：直接抛错会让用户丢失已有进展，正确做法是返回**部分结果 + 终止原因 + 建议**（"已达到预算上限，已完成 A/B，C 未完成"），并保留可续跑的状态。
- **实战**：一次调研 Agent 对同一个关键词反复搜索 27 次，因为每次返回的摘要略有不同（观测哈希不同），动作签名相同但没做去重——只加了"观测不变"检测，漏掉了"动作重复"。修复后同时看两个信号：动作签名连续 3 次相同 → 停滞；观测哈希连续 3 次相同 → 停滞。另一条文件处理链路把"读同一文件"误判为停滞，实际是在等异步导出完成——把 `read_file` 加入"可重试白名单"，并给等待动作单独的退避预算。上线后跑飞归零，长任务误杀率从 18% 降到 2%。

下面用动作签名 + 观测哈希实现三件套，跑三种典型轨迹看谁先触发。

```python
# Agent 终止三件套: 步数 / 预算 / 无进展(动作签名 + 观测哈希)
import hashlib


def run(actions, max_steps=12, budget=1000, patience=3):
    """actions: [(action_sig, cost, observation)]"""
    used = 0
    sigs, obs = [], []
    for i, (sig, cost, ob) in enumerate(actions, 1):
        if i > max_steps:
            return "max_steps", i - 1, used
        used += cost
        if used > budget:
            return "budget", i, used
        sigs.append(sig)
        if len(sigs) >= patience and len(set(sigs[-patience:])) == 1:
            return "no_progress_action", i, used
        obs.append(hashlib.md5(ob.encode()).hexdigest())
        if len(obs) >= patience and len(set(obs[-patience:])) == 1:
            return "no_progress_obs", i, used
    return "done", len(actions), used


# A: 反复同一个搜索, 观测内容略有不同(摘要抖动)
loop = [("search:退款政策", 30, f"结果摘要 v{i}") for i in range(10)]
# B: 合法的长任务: 15 个不同文件, 每步都前进
long_task = [(f"read:file{i}.md", 50, f"内容 {i}") for i in range(15)]
# C: 每步都不同但很贵, 预算先到
expensive = [(f"call:api{i}", 90, f"resp {i}") for i in range(30)]

for name, acts in (("A 重复搜索", loop), ("B 长任务", long_task), ("C 高成本", expensive)):
    reason, steps, used = run(acts)
    print(f"[1] {name}: 终止原因={reason}, 步数={steps}, 消耗={used}")
    if name.startswith("A"):
        assert reason == "no_progress_action" and steps == 3
    if name.startswith("B"):
        assert reason == "max_steps" and steps == 12, "合法长任务被步数上限误杀"
    if name.startswith("C"):
        assert reason == "budget" and used > 1000
print("    → 实测 三种闸门各自先触发; max_steps 会误杀长任务, 需要与预算配合调")

# 观测不变但动作不同: 换着法儿查同一件事, 动作签名检测不到
same_obs = [(f"search:q{i}", 20, "完全相同的空结果") for i in range(6)]
reason, steps, _ = run(same_obs)
print(f"[2] 动作不同但观测相同: {reason}, 步数 {steps}")
assert reason == "no_progress_obs" and steps == 3
print("    → 实测 只去重动作签名不够; 观测哈希能抓住'换关键词但没新信息'")

# 可重试动作白名单: 等待外部状态不算停滞
def run_with_retryable(actions, retryable, patience=3):
    streak = 0
    for i, (sig, cost, ob) in enumerate(actions, 1):
        if sig.split(":")[0] in retryable:
            continue                      # 等待型动作不计入停滞
        streak = streak + 1 if ob == "无变化" else 0
        if streak >= patience:
            return "no_progress", i
    return "done", len(actions)


waiting = [("poll:export", 10, "无变化") for _ in range(8)]
print(f"[3] poll 等待型动作: {run_with_retryable(waiting, {'poll'})}, "
      f"不白名单: {run_with_retryable(waiting, set())}")
assert run_with_retryable(waiting, {"poll"})[0] == "done"
print("    → 实测 无进展检测要区分'重复无效'与'合理等待', 否则误杀异步任务")

# 优先级: 预算/步数是硬闸, 先于软闸判定
reason, steps, used = run([("search:x", 600, "a")] * 5, budget=500)
print(f"[4] 单步就超预算: {reason} (第 {steps} 步, 已用 {used}); 软闸尚未触发")
assert reason == "budget"
print("    → 实测 硬闸先算账再判停滞; 终止后返回部分结果与原因, 而不是直接抛异常")
```

**追问一**：最大步数应该设多大？有没有公式？—— 没有通用公式，但可以按"任务的必要步骤数分布"定：取历史成功任务步数的 P99 再乘 2～3 倍作为 `max_steps`，同时用预算兜底。比如 95% 的任务在 8 步内完成、P99 是 15 步，`max_steps=40` 既能覆盖长尾又不会让跑飞的任务烧太久。更重要的是**分层**：不同任务类型（检索/代码/多轮工具）用不同的上限，而不是全局一个数；并在触发时记录"卡在哪一步、最后几个动作"，用于迭代 prompt 或工具设计——多数跑飞不是模型笨，而是工具返回了模型无法理解的错误，导致它反复重试。

**追问二**：无进展检测为什么不能只看"目标距离"？—— 因为"目标距离"通常需要一个可靠的评分器（LLM judge 或规则），本身有噪声和成本；每步都打分既贵又可能误判（分数抖动被当成"没前进"或"前进了"）。动作签名与观测哈希是**廉价、确定性**的代理信号，适合高频检测；目标距离适合低频（每 3～5 步）或在终止前做一次最终判断。三者组合：廉价信号触发"疑似停滞"→ 让模型自检/换策略→ 仍无进展再用目标距离或直接终止。只用目标距离会被评分器噪声牵着走，只用签名会漏掉"动作不同但原地打转"。

## 背诵要点

- 三件套：`max_steps`（防失控）、预算（token/金额/时间，防烧钱）、无进展（动作签名重复 / 观测哈希不变 / 目标距离不降）。
- 硬闸优先（先算预算与步数），软闸可先触发一次"换策略提示"再终止；`patience` 经验值 3，需区分可重试动作。
- 终止后返回部分结果 + 原因 + 可续跑状态；`max_steps` 按任务类型分层，取历史 P99 的 2～3 倍。

## 复盘追问

- Agent 反复搜同一个词 27 次，为什么"观测不变"检测没拦住？（每次摘要略有不同，哈希变了；要同时看动作签名，二者是独立信号）
- 为什么无进展检测要设"可重试动作白名单"？（轮询/等待外部状态是合理重复，计入停滞会误杀异步任务）
