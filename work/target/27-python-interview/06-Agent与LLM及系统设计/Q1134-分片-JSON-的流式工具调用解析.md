---
title: [Q1134] 分片 JSON 的流式工具调用解析
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1134 · 分片 JSON 的流式工具调用解析

> 难度:★★★★ | 标签:流式, 结构化输出

**问**:工具调用的参数 JSON 是分片下发的,怎么在流中实时展示参数进度?完整参数怎么保证正确?

**答**:做法是维护一个字符串缓冲,每收到一片就尝试"补全闭合"做渐进解析——即统计未闭合的括号与引号,补上结尾后再 `json.loads`,成功则能拿到"目前已生成的部分参数"。这个技巧用于 UI 实时回显;而真正执行工具必须等 done 且用原始完整缓冲解析,渐进解析的结果只作展示,不落库。

```python
# file: code/06_Agent与LLM及系统设计/q1134_partial_json_stream.py
"""分片 JSON 流式解析:补全闭合括号实现渐进解析,仅用于展示,执行用完整缓冲。"""


def try_partial_parse(buf: str):
    """把不完整 JSON 补闭合后尝试解析;引号内的花括号不参与配对。"""
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
    patched = buf + ('"' if in_str else "") + "".join("}" if c == "{" else "]" for c in reversed(stack))
    try:
        return patched, json.loads(patched)
    except Exception:
        return None, None


import json

if __name__ == "__main__":
    deltas = ['{"city": ', '"北京", ', '"days": ', '3}']
    buf = ""
    for d in deltas:
        buf += d
        patched, obj = try_partial_parse(buf)
        print(f"收到分片 {d!r:>12} -> 渐进解析: {obj}")
    final = json.loads(buf)  # done 后用完整缓冲解析
    assert final == {"city": "北京", "days": 3}
    print("最终参数:", final, "可安全执行工具")
```

**追问**:
- 渐进解析出的部分参数能直接执行工具吗?答:绝对不能,执行必须以 done 后的完整解析为准,渐进结果只用于 UI 回显,避免截断值入库。
- 补闭合在嵌套数组 + 未闭合字符串时怎么验证正确?答:用文中的扫描状态机记录栈与引号状态,恢复顺序是"先关引号、再逆序关括号",可用随机分片顺序做性质测试。
