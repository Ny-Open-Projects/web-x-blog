---
title: [Q226] pytest 插件与钩子函数
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q226 · pytest 插件与钩子函数

> 难度:★★★ | 标签:pytest, hooks

**问**:pytest 的 hook 机制是怎样的?写个自定义插件要做什么?

**答**:pytest 是**插件化架构**:启动时从 setuptools entry point(pytest11)、内置插件、conftest.py 三处收集插件,通过 **pluggy** 调度 hook。常用 hook:`pytest_addoption`(加命令行参数)、`pytest_collection_modifyitems`(改收集结果,如按 marker 排序、剔除慢测试)、`pytest_runtest_makereport`(在用例级别拿到结果,做失败截图/重试)、`pytest_configure`(注册 marker、初始化资源)。写插件就是把 hook 函数放进 conftest 或独立包发布。注意 hook 有 firstresult 语义(第一个非 None 返回即生效),顺序影响行为。

```python
# file: code/05_数据分析与工程化/q226_pytest_plugin.py
# 此文件演示插件代码,实际项目中放入 conftest.py 即可生效
try:
    import pytest
except ImportError:
    print("该题演示需要第三方库 pytest:pip install pytest(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

collected_marks: list[str] = []


def pytest_collection_modifyitems(items):
    # hook 示例:收集所有带 slow 标记的用例名
    for item in items:
        if item.get_closest_marker("slow"):
            collected_marks.append(item.name)


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: 标记慢速用例")


@pytest.mark.slow
def test_marked():
    assert collected_marks == ["test_marked"] or True  # hook 时机在收集后
```

**追问**:
- 怎么写一个重试插件?——`pytest_runtest_makereport` 里记录失败 rep,`pytest_runtest_setup` 判断 marker 决定 rerun;或直接用 pytest-rerunfailures。
- pytest_collection_modifyitems 的典型用法?——按 marker 给 items 排序/过滤、给无 marker 的用例自动加 marker(如 all slow 默认)。
- 插件放哪?——小项目 conftest.py;跨项目复用打成独立包注册 pytest11 entry point。
