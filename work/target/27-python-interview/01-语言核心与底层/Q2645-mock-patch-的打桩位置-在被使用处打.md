---
title: [Q2645] mock.patch 的打桩位置:在被使用处打,不是定义处
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2645 · mock.patch 的打桩位置:在被使用处打,不是定义处

> 难度:★★★★☆ | 标签:mock, 测试, 打桩

**问**:`patch("module_a.get_data")` 打了桩,被测代码却调了原函数,为什么?

**答**:`from module_a import get_data` 把名字**复制**进了使用方模块的命名空间,之后两个模块各持一份引用;patch 替换的是「某个命名空间里的名字」,打在定义处(module_a)不影响使用方已有的那份,必须打在**被使用的命名空间**上(`patch("module_b.get_data")`),这正是「在哪里使用就在哪里打桩」的口诀。推论:被测代码若用 `import module_a; module_a.get_data()`,打桩 module_a 就有效,因为使用方每次都通过模块属性查找。所以库的 import 风格直接影响可测性:模块属性访问风格对 patch 最友好,from-import 风格则要求精确知道打桩点。

```python
# file: code/01_语言核心与底层/q2645_mock_patch_site.py
"""mock.patch 的打桩位置:from-import 复制名字 vs 模块属性访问。"""
import sys
import types
from unittest import mock

# 构造两个演示模块:a 定义,b 用 from-import 引入
mod_a = types.ModuleType("fake_a")
mod_a.get_data = lambda: "real"
sys.modules["fake_a"] = mod_a

mod_b = types.ModuleType("fake_b")
exec("from fake_a import get_data\ndef use():\n    return get_data()",
     mod_b.__dict__)
sys.modules["fake_b"] = mod_b

if __name__ == "__main__":
    print("未打桩:", mod_b.use())

    # 打在定义处:使用方手里的旧引用不受影响
    with mock.patch("fake_a.get_data", return_value="stubbed-a"):
        print("patch 定义处:", mod_b.use(), "(仍是 real)")

    # 打在使用处:生效
    with mock.patch("fake_b.get_data", return_value="stubbed-b"):
        print("patch 使用处:", mod_b.use())

    # 属性访问风格:定义处打桩有效
    mod_c = types.ModuleType("fake_c")
    exec("import fake_a\ndef use():\n    return fake_a.get_data()",
         mod_c.__dict__)
    sys.modules["fake_c"] = mod_c
    with mock.patch("fake_a.get_data", return_value="stubbed-c"):
        print("属性访问风格:", mod_c.use())
```

**追问**:1) 怎么避免这种坑在团队里反复发生?——约定被测模块统一 `import mod` 属性访问,或测试里只 patch 使用方命名空间;code review 时核对 patch 路径与被测代码的 import 语句。2) 打桩位置的原理?——from m import f 把 f 绑进使用者命名空间,patch m.f 不影响已绑定的名字;patch "使用方.f" 或统一 import mod 后 mod.f 才生效(Q1812)。3) 与注入的取舍?——patch 是「别人的库」工具(Q1565);自家代码统一属性访问让 patch 路径可预测;或者干脆依赖注入免 patch。4) 生产陷阱?——patch 定义处(本题核心);patch 泄漏(用 fixture 自动还原);patch 私有函数路径升级即断。
