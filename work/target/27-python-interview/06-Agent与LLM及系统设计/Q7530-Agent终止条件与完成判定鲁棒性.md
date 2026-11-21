---
title: [Q7530] Agent 终止条件与任务完成判定的鲁棒性
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7530 · Agent 的"任务完成"怎么判定？模型说 done 就算 done 吗？

> 难度:★★★★ | 标签:Agent, 终止条件, 可靠性

**问**：Agent 循环里模型输出 `"status": "done"` 就结束任务。实践中出现两类事故：模型第二页就宣称"列表已全部处理"（实际还有 50 页），以及"done 了但验收标准没达成"。终止条件怎么设计才鲁棒？

**答**：结论：终止判定必须是**多重门**，模型自述只是其中之一：① **显式验收断言**——任务定义时就写出机器可检查的完成条件（目标计数达成、产出文件存在且校验通过、状态机终态），这是事实层判定；② **进度信号**——连续 N 步无状态变化（工具结果指纹不变/指标不动）判定停滞，强制模型给出"还差什么"或终止；③ **预算门**——步数/时间/token 三重上限，任一触顶即终止并进入收尾（partial result + 原因说明），绝不静默续跑。模型自述 done 只有在验收断言通过时才被接受，否则转化成一次"拒绝理由"反馈驱动下一轮。

机理与实战：
- "宣称完成"的对抗性：模型有系统性提前收尾倾向（尤其任务冗长时），防御是把完成判定从生成侧移到校验侧——像工具参数校验一样，done 声明要附带机器可验证证据（`{"done": true, "evidence": {"processed": 432, "expected": 500}}`），校验不过自动回喂"还差 68 项，继续"。这与参数自愈同构：错误声明也是结构化反馈。
- 停滞检测的实现：每步记录"状态指纹"（关键变量的哈希 + 工具响应摘要），连续 3 步指纹不变即触发停滞分支——比纯步数预算早发现死循环，也比步数预算更能区分"慢但在进展"与"在空转"。
- 终态的输出契约：任何终止路径（正常/预算触顶/停滞/错误）都要产出结构化终态：`completed | partial | failed` + 原因 + 已完成部分清单。partial 是被严重低估的终态——大多数超预算任务已完成了 80% 工作，扔掉重来不如带着断点续跑（检查点在 Q5516 结构化并发与任务分片中有基础）。

```python
# 基线:Python 3.9+ 纯标准库 ;演示多重终止门与结构化终态
import hashlib
import json
from dataclasses import dataclass, field


@dataclass
class LoopState:
    steps: int = 0
    max_steps: int = 50
    processed: list[int] = field(default_factory=list)
    fingerprint_streak: int = 0
    last_fp: str = ""


def state_fp(state: LoopState) -> str:
    return hashlib.sha256(json.dumps(state.processed).encode()).hexdigest()[:8]


def check_termination(state: LoopState, claim: dict, target: int) -> tuple[str, str]:
    """返回 (动作, 原因)。动作: continue / terminate / reject_claim。"""
    # 门1:预算
    if state.steps >= state.max_steps:
        return "terminate", "预算触顶(步数),转 partial 收尾"
    # 门2:停滞
    fp = state_fp(state)
    if fp == state.last_fp:
        state.fingerprint_streak += 1
        if state.fingerprint_streak >= 3:
            return "terminate", "连续 3 步状态无变化,判定停滞"
    else:
        state.fingerprint_streak = 0
        state.last_fp = fp
    # 门3:完成声明必须过验收断言
    if claim.get("done"):
        ev = claim.get("evidence", {})
        if ev.get("processed") == len(state.processed) == target:
            return "terminate", "验收断言通过,completed"
        missing = target - len(state.processed)
        return "reject_claim", f"完成声明与验收不符: 还差 {missing} 项,反馈继续"
    return "continue", ""


def main() -> None:
    st = LoopState(max_steps=50)
    target = 5
    # 模拟:模型第 2 步就宣称完成(实际只处理 2 项)
    st.processed = [1, 2]
    st.steps = 2
    claim = {"done": True, "evidence": {"processed": 2}}
    action, why = check_termination(st, claim, target)
    print("宣称完成 ->", action, "|", why)
    # 正常推进到满额
    st.processed = [1, 2, 3, 4, 5]
    st.steps = 6
    st.last_fp = state_fp(st)
    claim = {"done": True, "evidence": {"processed": 5}}
    action, why = check_termination(st, claim, target)
    print("真完成 ->", action, "|", why)
    # 停滞场景
    st2 = LoopState(max_steps=50)
    st2.processed = [1]; st2.steps = 9
    st2.last_fp = state_fp(st2)
    for _ in range(3):
        action, why = check_termination(st2, {"done": False}, target)
        st2.steps += 1
    print("空转 3 步 ->", action, "|", why)


if __name__ == "__main__":
    main()
```

**追问一**：验收断言对开放性任务（"调研并写一份报告"）怎么定义？
答：开放任务没有机器可算的完成条件，拆解为可验的代理断言（覆盖了 N 个指定要点、每节有引用、长度/结构满足 rubric）+ 终判交给 LLM-as-judge 或人工确认门。架构上区分"可机验的执行类任务"（多重门全自动）与"判断类任务"（自动门管过程，产出走评审通道），别试图用同一套门覆盖两类。

**追问二**：拒绝 done 声明会不会造成死循环（模型反复宣称完成反复被拒）？
答：会，所以要给拒绝计数：同一 claim 指纹被拒 2 次即转人工/终止并标记"验收器与模型认知冲突"——这通常意味着验收断言写得与任务不符（验收器 bug），而不是模型固执。拒绝事件是验收断言质量的重要反馈源。

**背诵要点**：
- 终止三重门：预算（步/时/token）、停滞（状态指纹连续不变）、验收断言（事实层判定）。
- done 声明必须带机器可验 evidence，校验不过转结构化反馈回喂，同参数自愈。
- 终态契约 completed/partial/failed + 原因 + 断点清单，partial 支持续跑。

**复盘追问**：
- 状态指纹应选取哪些变量（全量哈希太敏感于噪声）？
- partial 终态的断点清单如何与任务分片的幂等重跑衔接？

## 背诵要点
- 模型自述 done 是"申请"不是"判定"，验收断言才是判定。
- 停滞检测（指纹 streak）比步数预算更早发现死循环。
- 拒绝同一声明 2 次即升级人工，冲突指向验收器质量问题。

## 复盘追问
- 验收断言的 DSL（断言类型：计数/存在/校验和/引用）怎么设计？
- 长任务的检查点粒度（每步 vs 每里程碑）如何权衡？
