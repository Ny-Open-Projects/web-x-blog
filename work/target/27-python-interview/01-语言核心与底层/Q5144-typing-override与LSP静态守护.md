---
title: "[Q5144] typing.override（PEP 698）与 LSP 静态守护演进"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5144 · typing.override（PEP 698）与 LSP 静态守护演进

难度：P6 ｜ 标签：typing、PEP 698、LSP、3.12+

**问**：Python 3.12 引入的 `typing.override` 解决什么问题？为什么重写父类方法时"拼错方法名静默变成新方法"是一类真实事故？它和 `Protocol` 的 `runtime_checkable` 有何不同？

**答**：
结论：`@override` 是**给类型检查器的声明**：标注"我是在重写父类（或基类协议）的已有成员"。运行时它也会做一次真实校验（找不到父成员抛 TypeError），但核心价值在静态层——父类改名/删方法后，子类里拼错的"重写"会立刻被 mypy/pyright 报错，而不是静默变成一个永远不会被调用的孤儿方法。此前生态只有 pyright 私有的 `# type: ignore[override]` 与文档约定，PEP 698 把它标准化并可从 `typing_extensions` 回移到 3.7+。

取舍：给存量代码全量补 `@override` 是低收益大噪音，落地策略是"新增重写必须标 + 触碰过的文件顺手标"；它不改变任何继承语义（非运行时强制 LSP，只校验"父类确实有这个成员"），参数逆变/返回协变仍靠检查器的 override 兼容性检查。

实战：在抽象基类/插件基类（`save`/`handle` 这类约定方法）上启用最严格 override 检查（pyright `reportImplicitOverride`），把"方法名拼错"从线上静默 bug 前移到 CI。兼容层统一走 `try: from typing import override except ImportError: from typing_extensions import override`。

```python
# Python 3.12+ 基线；<3.12 用 typing_extensions（pip install typing_extensions）
from typing import override

class Storage:
    def save(self, key: str, payload: bytes) -> str:
        raise NotImplementedError

    def health(self) -> bool:
        return True

class S3Storage(Storage):
    @override
    def save(self, key: str, payload: bytes) -> str:   # 合法重写
        return f"s3://{key}"

class BrokenStorage(Storage):
    @override
    def sve(self, key: str, payload: bytes) -> str:    # 拼错：静态报错 + 运行时 TypeError
        return "oops"

try:
    BrokenStorage()
except TypeError as e:
    print("runtime check:", e)

print(S3Storage().save("a", b"x"))

# 与 Protocol 的差异：override 校验"确实在重写"，Protocol 校验"结构上满足"
from typing import Protocol, runtime_checkable

@runtime_checkable
class SupportsSave(Protocol):
    def save(self, key: str, payload: bytes) -> str: ...

print(isinstance(S3Storage(), SupportsSave))  # 结构匹配 -> True
```

**追问一**：`@override` 运行时校验发生在什么时候、开销多大？——类创建时（`__set_name__`/装饰阶段向上扫 MRO 找成员），每类一次性 O(MRO 深度) 开销，与调用路径无关，热路径零成本。

**追问二**：重写时把参数名改了（`key` → `object_id`）为什么也算 LSP 违约？——Python 调用点常用关键字传参，改名后 `storage.save(key="a", payload=b"x")` 会 TypeError；pyright 的 override 检查覆盖参数名，这正是不该靠人眼的原因。

**追问三**：`@override` 与 `@abstractmethod` 能否叠加、语义差别？——可以且常见：`@override` 表示"父类已有此成员，我在定制"，`@abstractmethod` 表示"子类必须实现"；抽象层默认实现 + 子类 override 是标准组合。

## 背诵要点
- `@override` = 声明"这是重写"，静态层抓父类改名后拼错/漏改的孤儿方法，运行时类创建期也校验。
- 3.12 进 `typing`，旧版本走 `typing_extensions`；推荐 pyright `reportImplicitOverride` 配合。
- 它只查"父类有该成员"，不做参数逆变/返回协变的深度 LSP 判断（那是检查器 override 规则的职责）。

## 复盘追问
- 存量 20 万行仓库如何灰度启用 implicit-override 检查而不淹没 CI？（先报数不开错，分目录白名单渐进）
- `@override` 与鸭子类型的冲突怎么权衡？（内部基类用 override 收紧；对外开放的 Protocol 保持结构化，讨论两套契约的边界）
