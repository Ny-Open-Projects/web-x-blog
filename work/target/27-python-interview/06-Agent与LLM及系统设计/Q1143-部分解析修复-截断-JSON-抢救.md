---
title: [Q1143] 部分解析修复:截断 JSON 抢救
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1143 · 部分解析修复:截断 JSON 抢救

> 难度:★★★★ | 标签:结构化输出, 修复

**问**:模型输出超长被 max_tokens 截断,JSON 断在半截,怎么抢救?什么情况下不该抢救?

**答**:抢救器按扫描状态机统计未闭合的字符串与括号栈,补齐闭合符后尝试解析,能救回已生成的字段。两件事必须分清:抢救结果要打上 `truncated=true` 标记,下游按"部分数据"处理;若是关键字段(必填项)缺失,则不该带病执行,应走重试或降级。同时要处理转义引号断在半空的情况——状态机里 esc 标志负责这个。抢救是止损手段,根治靠约束解码 + 足够的输出预算。

```python
# file: code/06_Agent与LLM及系统设计/q1143_truncated_json_repair.py
"""截断 JSON 抢救:状态机补闭合符恢复部分字段,必填缺失时拒绝带病执行。"""
import json


def repair(buf):
    """返回 (repaired_obj, truncated, missing_reason)。"""
    stack, in_str, esc = [], False, False
    for ch in buf:
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch in "{[":
            stack.append(ch)
        elif ch in "}]":
            if stack:
                stack.pop()
    fixed = buf + ('"' if in_str else "") + "".join("}" if c == "{" else "]" for c in reversed(stack))
    try:
        obj = json.loads(fixed)
        return obj, True, None
    except json.JSONDecodeError as e:
        return None, True, str(e)


def is_safe(obj, required):
    if obj is None:
        return False
    return all(k in obj and obj[k] not in ("", None) for k in required)


if __name__ == "__main__":
    truncated = '{"order": "A1001", "amount": 99.5, "items": ["书", "笔'
    obj, flag, err = repair(truncated)
    print("抢救结果:", obj, "截断:", flag)
    assert obj == {"order": "A1001", "amount": 99.5, "items": ["书", "笔"]}

    required = ["order", "amount", "status"]      # status 没来得及生成
    safe = is_safe(obj, required)
    print("必填完整性:", "可执行" if safe else "拒绝执行,走重试")
    assert not safe, "缺 status 必须拒绝带病执行"

    hopeless = '{"a": {"b": [1, "x" 2'
    obj2, _, err2 = repair(hopeless)
    print("不可修复样例:", obj2, err2)
    assert obj2 is None
    print("抢救器通过")
```

**追问**:
- 抢救出的部分数据怎么入库才安全?答:整条记录打 partial 标记存隔离表,补全后合并上线,绝不与完整数据混用。
- 为什么截断常发生在中文长枚举?答:中文一个字可能是多 token 且枚举项多,输出预算估算用字符数会低估 token 数,应按估算器预留。
