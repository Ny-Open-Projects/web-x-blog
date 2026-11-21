---
title: [Q1078] 自定义 marker 注册与过滤
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1078 · 自定义 marker 注册与过滤

> 难度:★★★☆ | 标签:pytest, marker

**问**:`-m "slow and not db"` 这种表达式过滤是怎么工作的?为什么自定义 marker 要注册?

**答**:marker 是挂在测试函数上的标签集合,pytest 收集后按 `-m` 布尔表达式筛选。自定义 marker 必须在 `pytest.ini`/`pyproject.toml` 的 `markers` 里注册,否则报警告且无法文档化,团队也发现不了拼写错误(如 sloe 混过过滤)。进阶做法:用 `pytest_collection_modifyitems` 钩子强制校验(未注册/误用直接 fail),或按 marker 自动加 skip 条件,让"慢测试 CI 夜里跑、数据库测试本地默认跳"成为基础设施而非口头约定。

```python
# file: code/05_数据分析与工程化/q1078_custom_marker.py

TESTS = []

def marker(*names):
    def deco(fn):
        fn.marks = set(names)
        TESTS.append(fn)
        return fn
    return deco

@marker("slow", "db")
def test_backup():
    return "backup done"

@marker("slow")
def test_big_report():
    return "report done"

@marker("fast")
def test_add():
    return "2"

def run(only=None, skip=None):
    only, skip = set(only or []), set(skip or [])
    for t in TESTS:
        if t.marks & skip:
            continue
        if only and not (t.marks & only):
            continue
        print("RUN", t.__name__, "->", t())

if __name__ == "__main__":
    # pytest.ini: markers = slow: 超过 1s 的测试;db: 依赖数据库
    # -m "slow and not db" 的等价过滤:
    print("== slow and not db ==")
    run(only=["slow"], skip=["db"])
```

**追问**:
- 追问 1:未注册 marker 的后果只是警告吗?—— 还包括 IDE/文档不可见、拼写错误静默失效,所以 CI 里建议 `--strict-markers` 把警告变错误。
- 追问 2:addini 之外怎么给 marker 附加元数据?—— `pytest_configure` 里 `config.addinivalue_line("markers", "slow: desc")`,或直接在 ini 声明。
