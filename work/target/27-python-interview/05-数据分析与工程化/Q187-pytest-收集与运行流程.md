---
title: [Q187] pytest 收集与运行流程
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q187 · pytest 收集与运行流程

> 难度:★★☆ | 标签:pytest, 收集规则

**问**:pytest 是怎么找到测试的?为什么我的 test_xxx.py 里的函数没被执行?

**答**:pytest 从命令行给定的路径(默认当前目录)开始**递归收集**:目录无 `__init__.py` 时按文件名作顶层模块,遵循 `python_files = test_*.py *_test.py`、函数 `test_*`、类 `Test*`(且类不能有 `__init__`)的默认规则。常见"收集不到"的原因:文件名不符合规则、类名不带 Test 前缀、fixture 名与函数名冲突导致 skip、收集期有 import 错误(collect-only 可以提前看)。用 `pytest --collect-only` 检查收集结果,是最快的排查手段。

```python
# file: code/05_数据分析与工程化/q187_collect_rules.py
class TestCart:
    # 类名必须以 Test 开头,且不能定义 __init__
    def test_total(self):
        assert 2 + 2 == 4

    def helper(self):
        # 没有 test_ 前缀,不会被当作测试收集
        return "helper"

def test_top_level():
    assert TestCart().helper() == "helper"
```

**追问**:
- 收集时报 collection import error 怎么办?——先 `pytest --collect-only` 定位,通常是模块顶层代码抛异常或 conftest 导入失败。
- pytest 怎么改默认收集规则?——pyproject.toml 的 `[tool.pytest.ini_options]` 里 python_files/python_functions;团队统一约定防止测试被漏收集。
- 为什么测试目录要避免 __init__.py?——无 init 时根目录入 sys.path 更灵活;加了 init 则要保证包名唯一,两种模式不能混用。
- 怎么只跑一个用例?——`pytest path::file::func` 精确定位;`-k` 表达式按名字模糊过滤,调试时最常用。
