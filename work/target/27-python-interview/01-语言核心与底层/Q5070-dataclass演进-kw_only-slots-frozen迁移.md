---
title: [Q5070] dataclass 演进：kw_only/slots/frozen 的版本迁移
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5070 · dataclass 演进：kw_only/slots/frozen 的版本迁移

> 难度:★★★☆ | 标签:版本演进, dataclass, 3.10, 工程迁移

**问**：团队代码里 `@dataclass` 大多是裸用，升级 3.10+ 后哪些新参数值得全量开启？`kw_only` 解决什么继承陷阱？`slots=True`（3.10）与 `frozen=True` 的收益和冲突是什么？从裸 dataclass 迁移要注意哪些破坏性变化？

**答**：结论：裸 `@dataclass` 只生成 `__init__/__repr__/__eq__`，3.10 填上了三个工程化缺口：a) **`kw_only=True`**：字段强制关键字传参——根治"同类型位置参数传错位"事故（坐标对调、两个 str 字段互相传反），更重要的是解决**继承陷阱**：父类有默认值字段、子类新增无默认值字段时，普通 dataclass 直接 TypeError（默认值必须跟在非默认后），把父类字段标 `kw_only` 后顺序约束解除；b) **`slots=True`**：自动生成 `__slots__`，每实例省一个 `__dict__`（百万实例省数百 MB，key-sharing 的对比见既有 Q1262），副作用：不再支持动态加属性、与多继承某些带自己 slots 的类冲突（见既有 Q559）；c) **`frozen=True`**：`__setattr__` 抛 FrozenInstanceError，可哈希（配合 eq=True）能进 set/当 dict key，适合值对象/配置对象。迁移破坏点：a) 开 slots 后**类变量与字段同名冲突**（slots 描述符会撞类属性默认值）、dataclass 继承链所有父类也要 slots 才真省内存；b) kw_only 改签名 = 破坏所有位置传参调用方，要按"内部类型先改、对外 API 走版本化"；c) frozen 改动点：所有就地修改（`obj.x = 1`、`list.append` 不算、但 `obj.lst.append` 算改内容不算改引用）要换成 `dataclasses.replace()`。实战：新代码默认 `@dataclass(slots=True, frozen=True, kw_only=True)` 三开，需要可变状态的对象显式去掉 frozen 并注释理由——把"不可变优先"变成默认决策。

```python
# file: code/01_语言核心与底层/q5070_dataclass_evolution.py
import dataclasses, sys
from dataclasses import dataclass, field

# 1) 继承陷阱: 父类有默认值, 子类新字段无默认值 -> 裸版直接 TypeError
@dataclass
class BaseBad:
    tag: str = "t"
try:
    @dataclass
    class ChildBad(BaseBad):
        n: int                # 非默认跟在默认后
    @dataclass
    class ChildBad(BaseBad):
        n: int = 1
    print("裸版绕过: 给子类字段塞默认值(掩盖问题)")
except TypeError as e:
    print("裸版继承炸:", e)

# 2) 3.10+ kw_only 解除顺序约束
@dataclass(kw_only=True)
class Base:
    tag: str = "t"
@dataclass(kw_only=True)
class Child(Base):
    n: int                    # 无默认值也合法
print("kw_only 继承 OK:", Child(n=3))

# 3) kw_only 防位置传参错位: 位置参数直接炸
@dataclass(kw_only=True)
class Money:
    amount: int
    currency: str
try:
    Money(100, "CNY")
except TypeError as e:
    print("位置传参被禁:", e)
print("正确:", Money(amount=100, currency="CNY"))

# 4) slots=True 内存账: 无 __dict__
@dataclass(slots=True)
class P1:
    x: int; y: int
print("slots 实例有 __dict__ 吗:", hasattr(P1(1, 2), "__dict__"))
try:
    p = P1(1, 2); p.z = 3
except AttributeError as e:
    print("动态加属性被禁:", e)

# 5) frozen: 不可变值对象, 可哈希
@dataclass(frozen=True)
class Point:
    x: int; y: int
ps = {Point(1, 2), Point(1, 2)}
print("frozen 可入 set 去重:", len(ps))
try:
    Point(1, 2).x = 9
except dataclasses.FrozenInstanceError as e:
    print("就地改被禁:", e)
print("replace 生成新对象:", dataclasses.replace(Point(1, 2), y=5))

print("推荐基线:", sys.version_info >= (3, 10) and "@dataclass(slots=True, frozen=True, kw_only=True)")
```

**追问**：1) slots=True 与默认值类属性为什么冲突？——slots 描述符和"字段默认值=类属性"同占一个名字，dataclass 生成时需要把默认值挪走，字段默认值要用 `field(default=)` 场景谨慎；slots 类同时不能再有 `__dict__` 意味着 **ClassVar 之外的动态元编程（如 ORM 的 lazy attr）失效**，迁移前要 grep `setattr`。2) frozen 和 slots 能同时开吗？——3.10 初版两者同开有 bug（slots 重建类丢 frozen 语义），3.10.7+ 修复，升级日志里这是显式验证点；同开的类是真正不可变值对象，性能上 slots 读属性还更快。3) kw_only 怎么灰度？——先只对"历史上出过错位的类型"开启 + mypy 检查位置调用，mypy `--strict` 下 position-only 调用会报错，CI 拦截后逐模块放开。

## 背诵要点
- 3.10 dataclass 三参数：kw_only 解继承顺序约束并禁位置传参错位；slots=True 免 `__dict__` 省内存但禁动态属性；frozen 不可变+可哈希。
- 迁移破坏点：slots 与字段默认值类属性冲突、继承链父类也要 slots、frozen 修改改用 `dataclasses.replace()`。
- 新代码默认三开（slots/frozen/kw_only），可变对象显式豁免；同开 frozen+slots 需 3.10.7+。

## 复盘追问
- 你们的 dataclass 有没有发生过"两个同类型字段位置传反"的事故？（提示：找 repr 出来的怪数据反推，把高频误用类型 kw_only 化并在 CI 用 mypy 拦位置调用）
- 百万级实例的模型类开 slots 后内存降了多少？有没有 ORM/动态属性依赖被 slots 弄坏的回归？（提示：对照 Q1262 的 key-sharing 账；setattr 相关用例全量回归）
