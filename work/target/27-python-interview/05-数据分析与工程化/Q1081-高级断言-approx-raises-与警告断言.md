---
title: [Q1081] 高级断言 approx、raises 与警告断言
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1081 · 高级断言 approx、raises 与警告断言

> 难度:★★★☆ | 标签:pytest, 断言

**问**:浮点比较、异常断言、警告断言,pytest 的标准姿势分别是什么?

**答**:浮点用 `pytest.approx(0.3)`(默认相对容差 1e-6),杜绝 `==` 比浮点;异常用 `with pytest.raises(ValueError, match="正则")`,match 同时校验错误信息,防止"任意异常都算过";警告用 `with pytest.warns(DeprecationWarning)`,或在 `filterwarnings("error")` 下让警告直接变失败。工程规范:断言异常必须断言类型加信息,只写 `pytest.raises(Exception)` 等于没测;approx 对 NaN、列表、numpy 数组同样有效。

```python
# file: code/05_数据分析与工程化/q1081_assertions.py
import warnings

def approx(expected, tol=1e-9):
    return ("approx", expected, tol)

def assert_equal(actual, expected):
    if isinstance(expected, tuple) and expected[0] == "approx":
        _, exp, tol = expected
        assert abs(actual - exp) <= tol, f"{actual} != {exp} within {tol}"
    else:
        assert actual == expected, f"{actual} != {expected}"

def avg(xs):
    return sum(xs) / len(xs)

def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

if __name__ == "__main__":
    # pytest 写法:assert sum(x) == pytest.approx(0.3);with pytest.raises(ValueError, match="zero")
    assert_equal(sum([0.1, 0.2]), approx(0.3, tol=1e-9))
    try:
        divide(1, 0)
    except ValueError as e:
        assert "zero" in str(e)
        print("异常断言通过:", e)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warnings.warn("deprecated", DeprecationWarning)
        assert any(issubclass(x.category, DeprecationWarning) for x in w)
        print("警告断言通过")
```

**追问**:
- 追问 1:raises 里代码没抛异常会怎样?—— 测试失败,这正是想要的,否则断言形同虚设。
- 追问 2:approx 的 rel 和 abs 参数怎么选?—— 数值跨度大用 rel,跨零点或接近 0 用 abs 混合给出下限。
