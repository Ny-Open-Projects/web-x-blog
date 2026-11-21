---
title: [Q5004] sys.monitoring（PEP 669）替代 sys.settrace 的成本模型
date: 2026-11-18
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5004 · sys.monitoring（PEP 669）替代 sys.settrace 的成本模型

> 难度:★★★ | 标签:PEP 669, sys.monitoring, 可观测性

**问**：3.12 的 `sys.monitoring` 为什么能把插桩开销从 settrace 的几十倍降到接近零？它的「事件 + 工具 ID」模型怎么用？调试器/覆盖率/APM 什么时候还必须退回 settrace？

**答**：结论：settrace 是**全局回调每行/每调用**——解释器每次执行都先问「tracer 在吗」，未插桩代码也要付检查成本，且 tracer 存在时关掉 3.11 的零开销优化，典型开销 3-50 倍。`sys.monitoring` 反过来：注册回调后解释器把「是否有人订阅此事件」**编译进字节码 specialize 路径**，无人订阅的指令零成本，有人订阅的事件回调也只在命中点触发；多工具用 `TOOL_ID`（0-5）隔离，各自订阅各自的事件，`EVAL_BREAKPOINT` 这类事件还能只对特定代码对象开。成本模型一句话：**你只为你订阅的事件付费，粒度到「代码对象 + 事件类型」**。事件覆盖 LINE_INSTRUCTION（对齐 3.11 指令级）、PY_START/PY_RESUME（协程恢复）、BRANCH_LEFT/RIGHT（覆盖率分支）、JUMP/RAISE 等。边界：monitoring 不是为「逐行暂停」设计的——没有「执行到一行就交还控制权给外部循环」的调度语义，断点单步调试仍走 settrace；`frame.f_lineno` 赋值跳行这类调试器魔法也只属于 settrace。实战：覆盖率工具 coverage 7.x 已切 monitoring 后端，分支覆盖成本显著下降；APM 用 PY_CALL/PY_RETURN 采样比 setprofile 稳定；诊断生产 CPU 用 `MONITORING` 订阅 instruction 采样仍不如 py-spy 旁路（不进进程），选型按「进程内低开销 vs 外部零侵入」分。

```python
# 基线:Python 3.12+(PEP 669)。3.11 及以下降级:sys.settrace(行为见注释)。
import sys

events_hit: list[str] = []

if sys.version_info >= (3, 12):
    TOOL_ID = 5   # 自定义工具 id(0-5 共 6 个槽位,0 被 ID_MAIN 固定占用,演示用 5)
    M = sys.monitoring
    M.use_tool_id(TOOL_ID, "demo-profiler")
    M.set_events(TOOL_ID, M.events.PY_START | M.events.PY_RETURN)

    # 注意:PY_START/PY_RETURN 的回调签名是 (code, instruction_offset),没有 event/arg
    def on_start(code, instruction_offset):
        events_hit.append(f"start:{code.co_name}")

    def on_return(code, instruction_offset, retval):   # PY_RETURN 额外带返回值
        events_hit.append(f"ret:{code.co_name}")
        return None  # monitoring 回调无控制权语义,不能像 settrace 那样"返回新 tracer"

    M.register_callback(TOOL_ID, M.events.PY_START, on_start)
    M.register_callback(TOOL_ID, M.events.PY_RETURN, on_return)

    def work(n):
        return sum(range(n))

    work(100)
    M.set_events(TOOL_ID, M.events.NO_EVENTS)   # 关掉:此后零成本
    M.free_tool_id(TOOL_ID)
    print(events_hit[:4], "... total:", len(events_hit))
else:
    print("3.11-: 无 sys.monitoring,退回 sys.settrace 全局逐行回调")
```

**追问**：
1) 为什么 monitoring 能做到「未订阅零成本」而 settrace 不行？——settrace 的协议要求解释器在每个可观测点检查全局 tracer 状态（还要每行构造 frame/回调）；monitoring 的订阅关系在注册时静态已知，解释器把回调检查合并进 3.11 的自适应指令 specialize 结果，订阅关闭时指令路径与未插桩一致。
2) 覆盖率工具怎么用 BRANCH_LEFT/RIGHT？——分支事件携带「走了哪个方向」，工具据此统计分支覆盖而无需像 settrace 时代那样对每行做差集推断；`coverage` 的 monitoring 后端行覆盖成本降到约原来的零头。
3) 同一进程多工具并存怎么不互相踩？——TOOL_ID 隔离：调试器、覆盖率、profiler 各占一个 id，`set_events` 互相独立；全局只有 6 个 id，抢不到时只能合并工具或退 settrace——这是生产上 APM 与调试器「二选一」的现实约束。
