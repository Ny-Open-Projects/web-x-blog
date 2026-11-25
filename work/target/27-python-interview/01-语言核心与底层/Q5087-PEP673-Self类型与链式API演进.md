---
title: "[Q5087] PEP 673 Self 类型：链式 API 与子类化的版本演进"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5087 · PEP 673 Self 类型：链式 API 与子类化的版本演进

难度：★★★☆☆ ｜ 标签：typing / PEP 673 / 版本演进 / 链式 API

**问**：链式 builder 每个方法都 `return self`，用 `-> "Base"` 标注后子类调用返回类型错了，历史上怎么绕，3.11 的 `Self` 为什么是正解？

**答**：
- **结论**：`return self` 的正确返回类型是"**当前类**"，不是声明处的类。3.11 前的三个绕法各有缺陷：字符串 `"Base"`（子类拿到父类类型，链断）；`TypeVar("T", bound="Base")`（需要方法写成类方法或泛型方法，实例方法上类型检查器推不出准确的 T）；`-> "Base"` + `cast`（运行时无感但代码噪音大）。PEP 673 引入 `typing.Self`（3.11+）：类型检查器把返回解析为**调用处实例的动态类型**，子类 `MyBuilder().set_x()` 的返回就是 `MyBuilder`。
- **取舍**：`Self` 还适用于 `__new__`/`__enter__`（返回 self 的上下文管理器）、classmethod 工厂（`cls()` 构造同类）。旧版本兼容：`typing_extensions` 提供 `Self`（基线 4.0+），代码里 `try: from typing import Self except ImportError: from typing_extensions import Self` 是标准降级写法。注意 `Self` 只能出现在"返回值/第一个位置参数是本类"的语境，不能用作字段类型注解（那是它和 `TypeVar` bound 方案的本质边界）。
- **实战**：迁移清单——链式 API 全量替换 `-> "Base"`；`__enter__` 返回类型标 `Self` 使 `with` 的目标类型随子类走；`from __future__ import annotations` 与 `Self` 无冲突（3.11+ 运行时已可用）。类型检查基线：mypy 1.0+/pyright 均完整支持。

```python
"""PEP 673 Self：链式 API 的返回类型随子类走（Python 3.11+）"""
from typing import Self

class QueryBuilder:
    def __init__(self, table: str):
        self._table = table
        self._wheres: list[str] = []

    def where(self, cond: str) -> Self:      # 返回"当前类"，不是 QueryBuilder
        self._wheres.append(cond)
        return self

    def build(self) -> str:
        sql = f"SELECT * FROM {self._table}"
        if self._wheres:
            sql += " WHERE " + " AND ".join(self._wheres)
        return sql

class SafeBuilder(QueryBuilder):
    def __init__(self, table: str):
        super().__init__(table)
        self._banned = {";"}                 # 子类新增校验

    def where(self, cond: str) -> Self:
        if any(b in cond for b in self._banned):
            raise ValueError("illegal condition")
        return super().where(cond)           # super() 返回 QueryBuilder，Self 语义保证外层仍是 SafeBuilder

q = SafeBuilder("users").where("id=1").where("age>18")
print(q.build())                             # 子类链式调用全程保持 SafeBuilder 类型

# classmethod 工厂 + __enter__ 也是 Self 的标准场景
class Ctx:
    def __enter__(self) -> Self:
        print("enter")
        return self
    def __exit__(self, *exc): print("exit")
    @classmethod
    def create(cls) -> Self:
        return cls()                          # 类型检查器知道返回的是 cls 的类型

with Ctx() as c:
    print("in block:", type(c).__name__)

# 3.11 前的降级：typing_extensions（基线 4.0+）
try:
    from typing_extensions import Self as SelfExt
    print("typing_extensions 可用，旧版本降级路径成立")
except ImportError:
    print("缺 typing_extensions：降级用字符串注解 + cast（损失子类精度）")
```

**追问链**
1. `Self` 和 `TypeVar("T", bound=Base)` 在类方法上的区别到底是什么？
   1. TypeVar 方案下 `T` 由调用点推断，实例方法上检查器往往把 T 绑死在声明类的接收者类型，链式调用跨子类时推断漂移；`Self` 是语言级"接收者类型"概念，语义精确且无需给每个方法重复声明泛型。
   2. 追问：何时仍必须用 TypeVar？——需要"返回另一个与本类相关但不同的类型"（如 `list[Self]` 也仍要用 Self 支持吗？3.11 里 `list[Self]` 合法但语义指"包含本类实例"，若要返回兄弟类组合则需要自定义泛型）。
2. `Self` 能用在协程方法上吗？
   1. 能，`async def fork(self) -> Self` 合法（PEP 673 明确覆盖 async）；检查器对协程返回类型解包为 Self。注意 `__enter__` 若是 async（`__aenter__`）同样支持。

## 背诵要点
- `return self` 用 `typing.Self`（3.11+），子类调用返回子类类型；旧版用 typing_extensions 4.0+ 降级。
- Self 适用于实例方法返回值、`__new__`/`__enter__`/`__aenter__`、classmethod `cls()` 工厂；不能作字段注解。
- 旧三绕法的缺陷：字符串注解链断、TypeVar bound 推断漂移、cast 噪音。

## 复盘追问
- 大型链式 API（如 ORM query builder）从字符串注解迁到 Self，迁移的风险点与验证方式？
- pyright 对 `Self` 在 `__enter__` 上的支持如果与运行时不一致，如何定位是注解问题还是实现问题？
