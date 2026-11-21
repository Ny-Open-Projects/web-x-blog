---
title: [Q2869] CQRS 读写分离概念:命令侧投影与读模型最终一致
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2869 · CQRS 读写分离概念:命令侧投影与读模型最终一致

> 难度:★★★☆ | 标签:分布式, CQRS, 架构

**问**:读写都在同一张表上,为什么大流量下要拆成命令侧和查询侧?拆开的代价是什么?

**答**:CQRS 把写路径和读路径彻底解耦:命令侧只做业务校验和追加事件,不管谁在读;查询侧用投影把事件折叠成查询友好的读模型——名单、计数、统计,一次查出来,不用每次现场聚合。收益是读写各自优化:写侧为不变量服务,读侧为查询模式服务,缓存、副本、索引随便加在投影上。代价必须讲清:投影是异步的,写入刚落、读模型未更新时,查到的是旧值,这是最终一致,不是 bug;业务上要么接受短暂旧读,要么提供读己之写的通道。投影是纯函数,事件日志在手随时重算,读模型坏了删了重建就行。适用边界也要会说:强一致交易类别硬上,读多写少、查询形状复杂的场景才划算。

```python
# file: code/06_Agent与LLM及系统设计/q2869_cqrs_projection.py
"""Q2869 CQRS 读写分离概念:命令侧校验 投影与读模型的最终一致。

命令侧只管校验和追加事件,读侧用投影把事件折成查询友好的读模型。
两边天然异步:写入刚落,读模型还没投影,查到的是旧值——这正是
CQRS 的代价,也是它把写负载与读负载彻底解耦的收益。
"""

CAPACITY = 2


def handle_command(cmd, events):
    """命令侧:校验通过才追加事件,拒绝不留痕。"""
    if cmd["action"] == "enroll":
        enrolled = sum(1 for e in events
                       if e[1] == cmd["course"] and e[0] != "cancel")
        if enrolled >= CAPACITY:
            return False, "课程已满"
    events.append((cmd["action"], cmd["course"], cmd["student"]))
    return True, "ok"


def project(events):
    """读侧投影:事件折叠成 course -> 学生名单 的读模型。"""
    model = {}
    for action, course, student in events:
        slot = model.setdefault(course, {"students": [], "count": 0})
        if action == "enroll":
            slot["students"].append(student)
            slot["count"] += 1
        elif action == "cancel":
            if student in slot["students"]:
                slot["students"].remove(student)
                slot["count"] -= 1
    return model


def main():
    events = []
    ok1, _ = handle_command({"action": "enroll", "course": "py",
                             "student": "alice"}, events)
    ok2, _ = handle_command({"action": "enroll", "course": "py",
                             "student": "bob"}, events)
    ok3, reason = handle_command({"action": "enroll", "course": "py",
                                  "student": "carol"}, events)
    assert (ok1, ok2) == (True, True) and ok3 is False, reason
    assert reason == "课程已满"
    handle_command({"action": "cancel", "course": "py",
                    "student": "bob"}, events)
    # 写入已落库,但读模型还是上次投影的旧值 —— 最终一致
    stale = {"py": {"students": ["alice", "bob"], "count": 2}}
    fresh = project(events)
    assert fresh == {"py": {"students": ["alice"], "count": 1}}, fresh
    assert stale != fresh
    # 查询只读投影,不碰事件日志:读路径廉价可缓存
    assert fresh["py"]["students"] == ["alice"]
    print("命令侧拒绝:", reason)
    print("事件日志:", events)
    print("投影后读模型:", fresh, "(bob 已取消,carol 未占座)")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:读己之写怎么做? 答:写后短窗口内把该用户的读路由到主侧或等投影追平,token 校验式回落是常用实现。
- 追问二:投影延迟怎么监控? 答:事件日志位点减投影位点就是滞后量,超阈值告警,滞后量也是限流的输入。
