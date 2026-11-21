---
title: [Q212] GitHub Actions CI 流水线设计
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q212 · GitHub Actions CI 流水线设计

> 难度:★★★ | 标签:CI, GitHub Actions

**问**:设计一条 Python 项目的 CI 流水线,你会放哪些阶段?

**答**:一条务实的流水线:**lint/format → 类型检查 → 测试(带覆盖率)→ 构建 → (可选)安全扫描**,全部绿灯才允许 merge。关键工程点:用 `actions/setup-python` + `cache` 缓存 pip/uv 下载;矩阵跑多版本 Python(如 3.11/3.12);测试失败输出 junit/cov 报告;PR 触发只跑受影响路径(path filter)省时;secrets 走 Actions secrets 不进代码。失败要**快速且可读**——lint 先跑,几秒报错,别让开发者等 10 分钟测试才发现少个分号。

```yaml
# .github/workflows/ci.yml:非 python 文件
name: ci
on:
  push:
    branches: [main]
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install uv && uv sync
      - run: uv run ruff check .
      - run: uv run mypy src
      - run: uv run pytest --cov --cov-report=term
```

```python
# file: code/05_数据分析与工程化/q212_ci_gate.py
def ci_gate(results: dict[str, bool]) -> tuple[bool, str]:
    # CI 门禁逻辑:按阶段顺序短路,先挂先报
    order = ["lint", "typecheck", "test", "build"]
    for stage in order:
        if not results.get(stage, False):
            return False, f"failed at {stage}"
    return True, "all green"

def test_gate_order():
    assert ci_gate({"lint": True, "typecheck": True,
                    "test": True, "build": True}) == (True, "all green")
    assert ci_gate({"lint": False}) == (False, "failed at lint")
```

**追问**:
- 为什么 lint 放最前?——它最快,几秒内给出反馈,避免开发者等完整测试后才收到格式错误。
- 缓存怎么配?——`actions/setup-python` 内置 pip 缓存,uv 用 astral-sh/setup-uv 自带缓存;不缓存的 CI 每次全量下载,慢且打 PyPI 镜像。
- 矩阵构建什么时候值得?——库类项目要验证多 Python 版本;应用类跑目标版本即可,矩阵只增加时长。
- 失败报告怎么可读?——junit xml 上报到 PR checks,覆盖率徽章/摘要;只给「failed」三个字没人愿意修。
