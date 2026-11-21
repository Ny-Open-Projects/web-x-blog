---
title: [Q1652] JSON 深度限制防栈爆
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1652 · JSON 深度限制防栈爆

> 难度:★★★☆ | 标签:DoS 防护, JSON

**问**:一个几 KB 的 JSON 请求能把服务打挂?深度限制怎么实现?

**答**:JSON 解析是递归下降,嵌套深度超过解释器递归上限会抛 RecursionError——被捕获还算运气好;真正危险的是超深嵌套触发 C 栈溢出导致进程段错误,或解析超时占满 CPU,几 KB 的 body 就能打挂一个 worker,这是经典的解析器 DoS。防线在解析之前:用一次线性扫描统计最大嵌套深度(跟踪左右括号计数,跳过字符串字面量内部),超过阈值(64 层足够覆盖正常业务)直接以 400 拒绝,不给 json.loads 机会;再叠加 body 大小限制与解析超时。注意别用调大 recursionlimit 的方式修——那只会把 RecursionError 升级成不可恢复的段错误。

```python
# file: code/03_Web后端开发/q1652_json_depth.py
"""JSON 深度限制: 防 RecursionError 与 C 栈溢出(纯标准库)。"""
import json

MAX_DEPTH = 64


def measure_depth(text, limit=MAX_DEPTH):
    """迭代扫描嵌套深度, 字符串内的括号不算; 超限或结构非法返回 -1, 否则返回最大深度。"""
    depth, in_str, esc, maxd = 0, False, False, 0
    for ch in text:
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
        elif ch in "[{":
            depth += 1
            maxd = max(maxd, depth)
            if depth > limit:
                return -1
        elif ch in "]}":
            depth -= 1
            if depth < 0:
                return -1
    if depth != 0 or in_str:
        return -1
    return maxd


def safe_loads(text):
    if measure_depth(text) == -1:
        raise ValueError("JSON 嵌套超限或结构非法")     # 由调用处捕获
    return json.loads(text)


deep = "[" * 5000 + "]" * 5000
try:
    json.loads(deep)
except RecursionError:
    print("直接 loads 深度 5000: RecursionError, 默认递归上限 1000 是最后防线而非设计")

try:
    safe_loads(deep)
except ValueError as e:
    print("safe_loads 拦下:", e)

legit = json.dumps({"a": {"b": [1, 2, {"c": 3}]}})
print("正常载荷深度:", measure_depth(legit), "解析:", safe_loads(legit))
crafted = "[" * 65 + "]" * 65
print("深度 65 载荷被限制拦截:", measure_depth(crafted) == -1)
```

**追问**:
- 为什么不直接 try/except RecursionError?——能接住一次,但依赖解释器在 C 栈溢出前抛出,极端输入下会段错误,前置深度检查才是确定性防线。
- 阈值取多少合适?——64 层,正常业务 JSON 很少超过 10 层,配置中心类深结构单独评估放宽。
