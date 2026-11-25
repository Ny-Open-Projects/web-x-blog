---
title: [Q5118] TypeIs 与类型收窄演进
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5118 · TypeIs 与类型收窄演进

> 难度:★★★★☆ | 标签:版本演进, PEP 742, typing

**问**:为什么 `def is_str(x) -> bool` 收窄不了类型，`-> TypeGuard[str]` 能收窄但"收窄方向"让人困惑，3.13 又为什么引入 `TypeIs`？三种写法的语义边界分别在哪？

**答**:结论：类型收窄靠**检查函数的返回类型注解**告诉类型检查器"返回 True 时 x 是什么"。演进三段：a) **bool**：无信息，检查器收不了窄；b) **TypeGuard[T]（PEP 647，3.10）**：返回 True 时把 x 收窄为 T——语义是**只添加**：收窄是"赋一个新假设"，不保留原有类型信息，也不能在 False 分支排除（对 `int | str` 判 `TypeGuard[str]`，False 分支仍是 `int | str`）；c) **TypeIs[T]（PEP 742，3.13）**：语义对齐 `isinstance`——True 收窄为 T 且**保持交集运算**（`int | str` 里判 `TypeIs[str]`，False 分支正确排除为 `int`），且要求 T 是参数类型的**子集**，签名不合法会被检查器拒绝。运行时行为：`TypeGuard`/`TypeIs` 注解在运行时只是别名标记，不改变函数执行——它们只给静态检查器（mypy/pyright）看。取舍：TypeIs 更符合直觉、误标更容易被查出，但要求"检查函数真的能排除"，而 TypeGuard 允许"宽进严出的自定义收窄"（如收紧字面量），这个自由度 TypeIs 没有了。降级：3.12 及以下从 `typing_extensions`（4.9+）导入同名类即可。

```python
import sys

# 运行时导入路径：3.13 用内置 typing，旧版本走 typing_extensions
try:
    from typing import TypeIs          # 3.13+（PEP 742）
    print("TypeIs 来源: typing (3.13+)")
except ImportError:
    try:
        from typing_extensions import TypeIs   # 第三方基线: typing_extensions>=4.9
        print("TypeIs 来源: typing_extensions（降级）")
    except ImportError:
        TypeIs = None
        print("无 TypeIs，仅演示 TypeGuard 语义")

from typing import TypeGuard, Union

def is_str_guard(x: Union[int, str]) -> TypeGuard[str]:
    return isinstance(x, str)

def is_str_is(x: Union[int, str]) -> TypeIs[str]:
    return isinstance(x, str)

def demo(x: Union[int, str]) -> None:
    if is_str_guard(x):
        reveal_type_guard = x
    else:
        # TypeGuard 语义：False 分支仍是 int | str，x 可能是 str！
        pass
    if is_str_is(x):
        reveal_type_is = x            # 收窄为 str
    else:
        reveal_type_is2 = x           # TypeIs 收窄为 int（正确排除）
    print("运行时无差别，只有检查器看注解:", type(x).__name__)

demo("a"); demo(1)

# 运行时可验证的事实：注解只是标记，函数体照常执行
import inspect
print(inspect.signature(is_str_guard).return_annotation)

# 运行时错误示例：TypeIs 约束 T 必须是入参类型的子集，
# def bad(x: int) -> TypeIs[str]  <- pyright/mypy 会报错（str 不是 int 的子集）
# 运行时不会拦，这是"静态契约靠检查器兜底"的典型分层。
```

**追问一层**:`TypeIs` 的 False 分支收窄按"差集"计算，那 T 是入参类型的真子集且入参还有第三种类型时（`int | str | bytes` 判 `TypeIs[str]`），False 分支收窄成什么？
**追二层**:PEP 742 为什么不直接改 TypeGuard 的语义、而是新增 TypeIs？存量 TypeGuard 代码在迁移到 TypeIs 时哪些场景会"变宽/变严"？

**背诵要点**
- bool 不收窄；TypeGuard=只添加假设（False 不排除）；TypeIs=isinstance 语义（交集+差集双向收窄）。
- TypeIs（3.13/typing_extensions 4.9+）要求 T 是入参类型子集，不合法签名检查器报错。
- 运行时两者都只是注解标记，行为零差异；收窄只存在于静态检查器。

**复盘追问**
- 存量 TypeGuard 工具函数迁 TypeIs 后 CI 类型检查突然报错，哪些是"真 bug 被暴露"？提示：False 分支本应排除却继续用被排除类型的代码。
- 团队规范何时该坚持 TypeGuard？提示：自定义收窄（如"非空字符串字面量"）无法用子集语义表达时。
