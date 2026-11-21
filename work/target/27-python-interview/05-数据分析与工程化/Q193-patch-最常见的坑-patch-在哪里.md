---
title: [Q193] patch 最常见的坑:patch 在哪里
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q193 · patch 最常见的坑:patch 在哪里

> 难度:★★★ | 标签:mock, patch, 坑

**问**:为什么 `patch("mymodule.add")` 之后被测函数还在调真实现?

**答**:因为 patch 替换的是**某个命名空间里的名字绑定**。如果被测模块 `mymodule/utils.py` 写了 `from utils import add`,那它自己的命名空间里有一个指向原函数的引用;此时你去 patch `utils.add`,改的是 utils 模块的绑定,utils_module 里那份引用不受影响。正确做法是 **patch 被测模块中的引用位置**:`patch("mymodule.utils.add")`。另一个高频坑:多个 patch 装饰器**自下而上**应用,参数顺序相反;以及 patch 类时默认返回的是"类实例的 Mock",需要 `patch(...).return_value` 才能配置实例方法。

```python
# file: code/05_数据分析与工程化/q193_patch_path.py
from unittest.mock import patch

def _now():
    return "real"

def greet():
    # 关键:这里引用的是本模块命名空间里的 _now
    return f"hello at {_now()}"

def test_patch_local_namespace():
    # 正确:patch 被测函数所在的模块名下的引用
    with patch("__main__._now", return_value="fake"):
        assert greet() == "hello at fake"

def test_real_function_untouched():
    with patch("__main__._now", return_value="fake"):
        pass
    # 作用域退出后恢复原实现
    assert greet() == "hello at real"
```

**追问**:
- 多个 patch 装饰器的参数顺序?——自下而上应用,参数也自下而上注入;记不住就用 with 嵌套或 pytest-mock 的 mocker.patch 链。
- patch 类方法会影响所有实例吗?——会,patch 的是类属性;只要替换一个实例就 `patch.object(instance, 'method')`。
- patch 和依赖注入怎么取舍?——能 DI 就别 patch:显式传参可测性更好;patch 留给改不了的第三方与全局状态。
