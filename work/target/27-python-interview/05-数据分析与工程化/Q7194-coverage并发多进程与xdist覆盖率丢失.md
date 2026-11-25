---
title: "[Q7194] coverage 并发多进程与 xdist 覆盖率丢失复盘"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7194 · coverage 并发多进程与 xdist 覆盖率丢失复盘

难度：P6 ｜ 标签：事故复盘、coverage.py、pytest-xdist、CI 门禁

基线：Python 3.12；coverage.py 7+；pytest-xdist；json 标准库演示数据合并。

**问**：CI 里 `pytest -n 4` 跑完，coverage 报告只剩 20%，本地单进程跑却有 80%。测试明明都执行了，覆盖率为什么塌了？

**答**：
- **结论**：coverage.py 默认只测量**主进程**的执行。`pytest-xdist` 把测试分发到多个 worker 子进程，子进程里的代码执行没被 tracer 记录，于是大量行被判为"未覆盖"。正确做法两步：(1) 在 `.coveragerc` 里声明 `concurrency = multiprocessing,thread`（coverage 7.x），并通过 `COVERAGE_PROCESS_START` + `sitecustomize.py` 让每个子进程启动时自动开始测量；(2) 跑完用 `coverage combine` 把各 worker 写出的 `.coverage.hostname.pid.random` 数据文件合并成一份，再 `coverage report`。
- **取舍**：多进程测量有额外 tracer 开销、数据文件合并多一步 CI 配置；fork 与 spawn 启动方式不同，钩子注入方式也不同（Windows/macOS 默认 spawn）。若分支覆盖率要求高，还要开 `branch = True`。
- **实战**：把 `COVERAGE_PROCESS_START` 和 `coverage combine` 固化进 CI 脚本；合并后校验 `coverage report --fail-under=XX` 才让门禁生效；定期核对"报告行数 vs 实际执行测试数"，防止再次静默漏测。

```python
import json


def combine(coverage_files: list[str]) -> set[str]:
    """模拟 coverage combine：合并各 worker 的覆盖数据（取并集）。"""
    seen: set[str] = set()
    for path in coverage_files:
        with open(path, encoding="utf-8") as f:
            seen.update(json.load(f)["lines"])
    return seen


if __name__ == "__main__":
    for i, lines in enumerate(
        (["a.py:1", "a.py:2"], ["a.py:2", "b.py:1"]), 1
    ):
        with open(f"/tmp/q7194_w{i}.json", "w", encoding="utf-8") as f:
            json.dump({"lines": lines}, f)
    merged = combine(["/tmp/q7194_w1.json", "/tmp/q7194_w2.json"])
    print("merged lines:", sorted(merged))
    # 不做 combine：只看单个 worker，覆盖率被低估。
```

**追问一**：为什么子进程默认不被 coverage 测量？
→ 解析：coverage 的 tracer 是在进程启动时安装的，只作用于当前进程；xdist worker 是 fork/spawn 出来的新进程，没有自动继承 tracer，需要在子进程启动时通过 `sitecustomize` 钩子重新启动测量。

**追问二**：合并后出现"覆盖率反而超过 100%"或数据异常怎么办？
→ 解析：通常是 data 文件版本不一致、不同源码路径映射到同一文件、或残留上次的 `.coverage.*` 未清理。CI 里先删旧数据文件、固定源码路径映射，再 combine。
