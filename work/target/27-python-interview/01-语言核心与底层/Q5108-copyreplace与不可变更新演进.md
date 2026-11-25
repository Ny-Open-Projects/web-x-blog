---
title: [Q5108] copy.replace 与不可变更新演进
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5108 · copy.replace 与不可变更新演进

> 难度:★★★★☆ | 标签:版本演进, 不可变, copy.replace

**问**:3.13 新增的 `copy.replace()` 解决了什么问题？和 dataclass `replace`、frozen 更新各是什么关系？

**答**:结论：不可变对象"改一个字段"过去没有统一协议——dataclass 有 `dataclasses.replace`，namedtuple 有 `_replace`，datetime 有 `datetime.replace`，各自命名、泛型代码没法通用。PEP 734 相关演进里，3.13 在 `copy` 模块新增 `copy.replace(obj, **changes)`，把"带参不可变克隆"上升为通用协议：对象实现 `__replace__` 即可被替换。取舍：dataclass 自动获得该协议（3.13 起）；namedtuple/datetime 3.13 内置支持；自研 frozen 类要自己实现 `__replace__` 才能接入。工程收益：仓储/领域模型的"纯函数式更新"从此可以写成与类型无关的通用代码。基线：仅 3.13+，降级方案是按类型分支调 `dataclasses.replace` 或 `_replace`。

```python
import sys, copy
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int = 0

p = Point(1, 2)

if sys.version_info >= (3, 13):
    q = copy.replace(p, y=9)              # 通用协议
else:                                     # 降级：dataclass 专属 API
    from dataclasses import replace
    q = replace(p, y=9)
print(q)                                  # Point(x=1, y=9)
print(p)                                  # Point(x=1, y=2) 原对象不动

# frozen 下没有 __setattr__，所以"改"必然是"造新"，replace 是唯一正道
try:
    p.y = 9
except Exception as e:
    print(type(e).__name__)               # FrozenInstanceError

# 自研 frozen 类接入通用协议（3.13+ 才生效，3.12 走降级分支）
class Tag:
    __slots__ = ("name",)
    def __init__(self, name): object.__setattr__(self, "name", name)
    def __setattr__(self, *a): raise AttributeError("frozen")
    def __replace__(self, **changes):
        merged = {"name": self.name, **changes}
        return Tag(**merged)

t = Tag("v1")
print(copy.replace(t, name="v2").name if sys.version_info >= (3, 13) else "3.12: 手写 with_ 方法")
```

**追问一层**:为什么协议选 `__replace__` 实例方法而不是模块级钩子？slots/frozen 类实现要注意什么？
**追二层**:`dataclasses.replace` 对含字段默认工厂/InitVar 的深嵌套更新有什么坑？

**背诵要点**
- 3.13 copy.replace 统一"不可变带参克隆"协议，靠 `__replace__`。
- dataclass/namedtuple/datetime 3.13 起原生接入；旧版本走各自专属 API。
- frozen 更新=造新对象，replace 是函数式更新的通用入口。

**复盘追问**
- 深层嵌套 frozen 结构做"改叶子"时，沿路径逐层 replace 的代码怎么收（lens 思想）？
- 版本降级分支放在库里还是调用方？提示：兼容 shim 模块与 Q5058 的迁移经验。
