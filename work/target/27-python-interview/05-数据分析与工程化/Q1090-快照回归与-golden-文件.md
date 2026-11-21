---
title: [Q1090] 快照回归与 golden 文件
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1090 · 快照回归与 golden 文件

> 难度:★★★☆ | 标签:快照测试, 回归

**问**:报表 SQL 输出 500 行,手写期望值不现实,这种输出怎么测?

**答**:golden/快照测试:首次运行把输出存成 golden 文件入库,之后每次运行与 golden 严格比对,不一致即失败;输出变更时用 `--update` 显式更新并走 code review,让"输出变化"成为人工审查对象。工程要点:序列化要稳定(排序键、固定浮点精度、去除时间戳等非确定字段);golden 文件按平台无关格式存;对比失败时输出 diff 而不是两个全文。适合渲染结果、生成的 SQL、报表内容这类"复杂但稳定"的输出。

```python
# file: code/05_数据分析与工程化/q1090_golden_snapshot.py
import json
import os
import tempfile

GOLDEN = os.path.join(tempfile.gettempdir(), "q1090_golden.json")

def render(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2)

def check(data, update=False):
    actual = render(data)
    if update or not os.path.exists(GOLDEN):
        with open(GOLDEN, "w", encoding="utf-8") as f:
            f.write(actual)
        return "golden 已写入/更新"
    with open(GOLDEN, encoding="utf-8") as f:
        expected = f.read()
    return "一致" if actual == expected else "不一致,请人工审查后 --update"

if __name__ == "__main__":
    print(check({"b": 1, "a": [1.0, 2.5]}))
    print(check({"b": 1, "a": [1.0, 2.5]}))
    print(check({"b": 1, "a": [1.0, 3.0]}))
    os.remove(GOLDEN)
```

**追问**:
- 追问 1:输出含时间戳怎么办?—— 序列化前做规范化钩子,替换成固定占位符,只测稳定部分。
- 追问 2:快照测试会不会让人无脑更新?—— 更新走独立 flag 加 review 流程,CI 中禁止自动更新,保证变化被看见。
