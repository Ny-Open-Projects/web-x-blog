---
title: "[Q6176] Pydantic after 校验中赋值与 validate_assignment 递归"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6176 · Pydantic after 校验中赋值与 validate_assignment 递归

难度：P6-P7 ｜ 标签：Pydantic v2、model_validator、validate_assignment、递归、规范

**问**：Pydantic v2 里开了 `validate_assignment=True`（为了"任何赋值都重新校验"），又在 `@model_validator(mode="after")` 里把字段规整一下：`self.name = self.name.strip().upper()`。为什么一构造模型就 `RecursionError`/栈溢出？`mode="after"` 拿到的是模型实例，赋值为什么会再触发自己？这和 Q721（model_validator 跨字段校验）的边界在哪？正确的规整姿势是什么？

**答**：
结论：`validate_assignment=True` 时，对模型属性的任何赋值都会走一遍"校验 + 重新运行 after validator"；而 after validator 里又给 `self.name` 赋值，于是形成"赋值 → 校验 → after → 赋值"的无限递归，直到 `RecursionError`。`mode="after"` 的语义是"模型已经构造完成，做跨字段断言/只读检查"，不是"再改字段"；Pydantic 文档也建议 after 里不要改 `self`。Q721 讲"跨字段校验怎么写、before/after 各拿什么"，本题专攻"after + 赋值校验"的组合陷阱。

取舍：规整/归一化放 `mode="before"`（拿原始 dict，改完返回，不触发实例赋值），或放字段级 `field_validator(mode="before")`；after 只做断言。确实需要在 after 里改，用 `object.__setattr__(self, "name", ...)` 绕过 `validate_assignment`（但会跳过后续校验，需自己保证合法），或者用 `model_copy(update={...})` 返回新实例（注意 after 返回新对象时 Pydantic 的语义）。也可以对"规整字段"关掉赋值校验、只对关键字段开，但配置是模型级的，粒度有限。

实战：事故形态是"迁移到 v2 后为了安全开了 `validate_assignment=True`，某个 normalizer 在 after 里统一大小写，单测只测了构造成功，线上遇到带空格的输入直接 500/栈溢出"。下面用等价的 Python 对象模拟这条链：`__setattr__` 在非 `_validating` 时调用 `after_validate`，after 里再赋值 → `RecursionError`；用 `object.__setattr__` 绕过则正常，且后续外部赋值仍会触发校验。

```python
class RecursiveModel:
    def __init__(self, **data):
        object.__setattr__(self, "_validating", True)
        for key, value in data.items():
            object.__setattr__(self, key, value)
        object.__setattr__(self, "_validating", False)
        self.after_validate()

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        if not getattr(self, "_validating", False):
            self.after_validate()          # 模拟 validate_assignment=True

    def after_validate(self):
        if hasattr(self, "name"):
            self.name = self.name.strip().upper()   # after 阶段赋值


try:
    RecursiveModel(name="  apple ")
except RecursionError:
    print("after 校验里赋值 + 赋值校验 -> RecursionError")


class SafeModel(RecursiveModel):
    def after_validate(self):
        object.__setattr__(self, "name", self.name.strip().upper())


m = SafeModel(name="  apple ")
print("绕过 __setattr__ 后:", repr(m.name))
print("再次赋值仍会触发校验:", end=" ")
m.name = " pear "
print(repr(m.name))
```

**追问一**：为什么 `mode="before"` 不会递归？——before validator 接收的是**原始输入**（dict/任意对象），返回的也是输入，不涉及模型实例的属性赋值；它运行在模型构造之前，不会触发 `validate_assignment`。把"去空格/大小写/别名归一"放在 before，既避免递归，也让 after 只处理"字段之间的约束"（如 start < end），职责更清晰。

**追问二**：`object.__setattr__` 绕过赋值校验安全吗？——它跳过 `validate_assignment`，也就跳过了类型/约束校验；如果你在 after 里写的值一定合法（比如 `strip().upper()` 保持 str），可以接受；否则应改用 `model_copy(update=...)` 或把规整逻辑前移。另一个坑：`frozen=True` 的模型连 `object.__setattr__` 都可能被 Pydantic 的 `__setattr__` 拦截/不被支持，规整必须在 before 做。

## 背诵要点
- `validate_assignment=True` 下，after validator 里给 `self.x` 赋值会再次触发校验 → 递归到 `RecursionError`。
- after 只做断言/只读检查；归一化放 `mode="before"` 或字段级 before validator。
- 必须改时用 `object.__setattr__`（跳过校验，自担合法性）或 `model_copy(update=...)`；frozen 模型更受限。

## 复盘追问
- 开 `validate_assignment` 后构造模型栈溢出，如何定位是 after validator 自赋值？（赋值→校验→after 循环、before 迁移）
- `object.__setattr__` 绕过校验有什么风险？frozen 模型为什么连这招都可能不行？（跳过约束、Pydantic 拦截）
