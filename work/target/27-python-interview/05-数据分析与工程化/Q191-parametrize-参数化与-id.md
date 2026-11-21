---
title: [Q191] parametrize 参数化与 id
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q191 · parametrize 参数化与 id

> 难度:★★☆ | 标签:pytest, parametrize

**问**:怎么用参数化避免写一堆重复测试?如何让失败用例的名字更好认?

**答**:`@pytest.mark.parametrize("输入,期望", [(...), (...)])` 会把一个测试函数展开为多个独立用例,任一失败互不影响、报告里逐条展示。通过 `ids` 参数(传列表或回调函数)自定义用例名,失败时一眼看出是哪个场景;用 `pytest.param(..., marks=pytest.mark.xfail)` 可对个别用例打标记。参数化还支持**堆叠**:多个装饰器做笛卡尔积,适合覆盖"输入组合 × 配置组合"这类矩阵场景。

```python
# file: code/05_数据分析与工程化/q191_parametrize.py
try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

@pytest.mark.parametrize(
    "year,expected",
    [
        pytest.param(2000, True, id="整百年能整除400"),
        pytest.param(1900, False, id="整百年不能整除400"),
        pytest.param(2024, True, id="普通闰年"),
        pytest.param(2023, False, id="普通平年"),
    ],
)
def test_is_leap(year, expected):
    assert is_leap(year) is expected

@pytest.mark.parametrize("a", [1, 2])
@pytest.mark.parametrize("b", [10, 20])
def test_cartesian(a, b):
    # 2x2 共 4 个用例
    assert a + b == b + a
```

**追问**:
- 参数化和 fixture 能一起用吗?——可以,fixture 通过 `request.param` 间接参数化(`params=[...]`),适合「环境矩阵」;直接数据矩阵用 parametrize。
- ids 为什么重要?——失败报告按 id 展示,默认显示参数值,复杂对象可读性差;业务化的 id 让 CI 失败一眼定位场景。
- 怎么给个别参数打标记?——`pytest.param(v, marks=pytest.mark.xfail)`;组合 xfail/skip 与参数化是处理已知 bad case 的正路。
