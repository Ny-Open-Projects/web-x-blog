---
title: [Q199] 慢测试、skip、xfail 与 marker
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q199 · 慢测试、skip、xfail 与 marker

> 难度:★★☆ | 标签:pytest, marker, skip

**问**:怎么把慢测试和快测试分开跑?skip 和 xfail 的语义区别?

**答**:自定义 marker(需在 pyproject.toml 注册,否则告警)如 `@pytest.mark.slow`,配合 `pytest -m "not slow"` 在日常开发只跑快集,CI 每晚跑全量。语义区分:`skip` 表示**已知无法/不应执行**(如仅 Windows),无条件跳过或条件 `skipif`;`xfail` 表示**会执行但预期失败**,万一通过了会报 XPASS,提醒你更新预期。`skip` 用于环境不匹配,`xfail` 用于记录已知 bug 待修复,两者都不能滥用成"测试红着不管"的借口。

```python
# file: code/05_数据分析与工程化/q199_markers.py
import sys

try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

@pytest.mark.slow
def test_heavy_computation():
    # pytest -m "not slow" 会跳过它
    assert sum(range(1000)) == 499500

@pytest.mark.skipif(sys.platform == "win32", reason="仅 POSIX 行为")
def test_posix_only():
    assert "/" + "" == "/"

@pytest.mark.xfail(reason="已知 bug ISSUE-123")
def test_known_bug():
    # 预期失败:当前实现有 bug,修复后这里变 XPASS 提醒摘掉标记
    assert 1 / 0 == float("inf")

def test_fast():
    assert 2 + 2 == 4
```

**追问**:
- marker 没注册会怎样?——PytestUnknownMarkWarning,且 `-m` 过滤不可靠;在 pyproject.toml 的 markers 列表注册并写明用途。
- xfail(strict=True) 是什么?——一旦 XPASS 直接算失败,强制你更新预期;防 xfail 堆积成垃圾场。
- 怎么组织快慢测试?——slow marker + CI 分层:PR 只跑快集,nightly 跑全量;慢测试进了 PR 红灯链路就是灾难。
