---
title: "[Q5261] 递归 __repr__ 的守卫：reprlib.recursive_repr 的线程隔离与 fillvalue"
date: 2026-11-25
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5261 · 递归 __repr__ 的守卫：reprlib.recursive_repr 的线程隔离与 fillvalue

难度：P6 ｜ 标签：repr、recursive_repr、递归、线程隔离、日志、调试

基线：CPython 3.12.2，纯标准库；用自引用对象复现 `RecursionError`，用 `threading` 验证守卫键里的线程标识。

**问**：日志 SDK 要打印一条链路追踪对象，span 树里父子互相引用。上线后日志线程偶发 `RecursionError`，整个进程的日志被拖死；同事在 `__repr__` 上加了一个全局 `set` 去重，压测时两个线程同时打印不同请求的对象，结果对方的对象被误判成"递归"，字段直接变成 `...`，排查时完全看不出请求内容。为什么自引用 `repr` 会炸？`reprlib.recursive_repr` 到底按什么键去重？为什么它不会把另一个线程的对象误判成递归？

**答**：

- **结论**：`repr(obj)` 会递归调用子对象的 `__repr__`，自引用对象没有终止条件，必然一路压栈直到 `RecursionError`。`reprlib.recursive_repr(fillvalue='...')` 的原理是给被装饰函数加一个"正在执行"的集合，键是 **`(id(self), 当前线程 ident)`**：进入时 `add`，`finally` 里 `discard`，再次遇到同一个对象（同一线程）就直接返回 `fillvalue`，不再进函数。键里带线程 ident 是关键——A 线程正在打印对象 X 时，B 线程打印 X 不会被误判为递归，两个线程各自拿到完整结果。3.12 的实现就是 `key = (id(self), get_ident())`，所以它是"按对象 + 线程"隔离，而不是全局去重。
- **取舍**：`fillvalue` 用 `"..."` 还是 `"<cycle>"` 是语义选择：`...` 兼容 `repr` 的惯例、短；`<cycle>` 明确告诉读者"这里有环"，但会污染日志字段。守卫应该加在**真正递归的 `__repr__`** 上，而不是加在外层格式化函数上——加错层只挡住一次调用，子树仍然会炸。另一个取舍是 `id(self)` 的复用风险：对象在 `__repr__` 执行期间不可能被回收（`self` 还被栈引用），所以执行期内 `id` 不会复用；但不要把守卫集合持久化到函数外，否则会泄漏 id。最后，守卫只解决"打印不炸"，不解决"对象图有环"——生产上更该在建模时用弱引用或显式 `parent_id` 打破环。
- **实战**：事故对象是 `Span`，`parent.children` 与 `child.parent` 双向引用，`__repr__` 直接 f-string 拼 `children`。修复分两步：① 给 `Span.__repr__` 加 `@recursive_repr("<cycle>")`，保证任何日志路径都不会炸；② 日志序列化改为 `to_dict(max_depth=8)`，超过深度输出 `"__truncated__"`，不再依赖 `repr` 做结构化输出。压测时 16 个线程并发打印 2000 个对象，修复前偶发 `RecursionError` 与字段串号，修复后零异常；单次 `repr` 多了一次 `get_ident()` 和一次 set 操作，微基准约 0.6 微秒，可忽略。

下面先复现无守卫的递归，再验证守卫的 `fillvalue`、嵌套不同对象、以及两个线程并发打印同一对象时的隔离。

```python
# 递归 __repr__: 无守卫 -> RecursionError; recursive_repr -> 按 (id(self), 线程) 去重
import reprlib
import threading
import time


class Bad:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __repr__(self):
        return f"Bad({self.name!r}, {self.next!r})"


bad = Bad("a")
bad.next = bad
try:
    repr(bad)
    raise AssertionError("自引用对象本应触发 RecursionError")
except RecursionError:
    print("[1] 无守卫的自引用 repr -> RecursionError（符合预期）")


class Good:
    def __init__(self, name):
        self.name = name
        self.next = None

    @reprlib.recursive_repr("<cycle>")
    def __repr__(self):
        return f"Good({self.name!r}, {self.next!r})"


g = Good("root")
g.next = g
text = repr(g)
print("[2] 守卫后:", text)
assert "<cycle>" in text

# 守卫按对象隔离: 嵌套两个不同对象, 内层不应该被误判
a, b = Good("a"), Good("b")
a.next = b
nested = repr(a)
print("[3] 不同对象嵌套:", nested)
assert "<cycle>" not in nested and "Good('b'" in nested

# 守卫键包含线程 ident: 两个线程同时打印同一个自引用对象, 都应拿到完整结构
class Slow(Good):
    @reprlib.recursive_repr("<cycle>")
    def __repr__(self):
        time.sleep(0.05)          # 放大并发窗口
        return f"Slow({self.name!r}, {self.next!r})"


s = Slow("shared")
s.next = s
results = []
lock = threading.Lock()


def worker():
    value = repr(s)
    with lock:
        results.append(value)


threads = [threading.Thread(target=worker) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("[4] 两线程结果:", results)
assert results == ["Slow('shared', <cycle>)"] * 2, "跨线程被误判为递归"
print("[5] 守卫键 = (id(self), get_ident())，同对象跨线程互不干扰")
```

**追问一**：为什么不能用 `if self in seen` 做守卫？—— 因为 `in` 会调用 `__eq__`/`__hash__`，而很多业务对象的 `__eq__` 本身就要遍历子字段，等于是用递归去检测递归，可能在进入守卫前就再次炸栈；即使没炸，`__eq__` 的语义也可能把"值相等"误当成"同一个对象正在打印"。用 `id(self)` 是身份判断，O(1) 且不触发用户代码，这才是守卫该用的键。代价是 `id` 只在对象存活期内唯一，所以集合必须用 `finally` 及时清理，不能跨调用缓存。

**追问二**：`fillvalue` 返回 `...` 会不会让日志"看起来正常但实际丢数据"？—— 会，这是守卫的固有取舍：它保证不崩，但不保证完整。正确做法是把 `repr` 定位成"调试用、可截断"的表示，结构化日志走单独的 `to_dict`/`to_json`，并在截断处显式标记（如 `"<cycle>"`、`"<max-depth>"`）。如果业务要求日志必须完整，就不能靠 `repr` 递归，而要在建模层用 `parent_id` 或 `weakref` 打断环，从根上消除自引用。

## 背诵要点

- 无守卫的自引用 `__repr__` 必然 `RecursionError`；`reprlib.recursive_repr(fillvalue)` 在 `finally` 中清理，保证异常路径也不泄漏守卫状态。
- 3.12 的键是 `(id(self), get_ident())`：按对象 + 线程隔离，跨线程并发打印同一对象不会互相误判。
- 守卫只保证"不炸"，日志完整性要靠 `to_dict(max_depth=...)` 或建模层断环，不能靠调大递归深度。

## 复盘追问

- 如果 `__repr__` 里的递归不是经过 `self`，而是经过一个全局注册表，`recursive_repr` 还能挡住吗？（键只看第一个参数，间接环需要自己按对象 id 建守卫）
- 为什么守卫集合必须在 `finally` 里 `discard`，而不是在正常返回时删？（`__repr__` 中途抛异常时，残留的 id 会让同一对象的后续打印永远返回 `fillvalue`）
