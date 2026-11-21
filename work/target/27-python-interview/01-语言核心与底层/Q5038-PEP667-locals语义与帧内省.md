---
title: [Q5038] PEP 667：3.13 的 locals() 一致性语义与调试器
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5038 · PEP 667：3.13 的 locals() 一致性语义与调试器

> 难度:★★★★ | 标签:PEP 667, locals, 版本演进, 调试器

**问**：函数内调用 `locals()` 返回什么？为什么 3.13 之前"改 locals() 返回的 dict 想修改变量"不可靠？PEP 667 把语义统一成了什么？

**答**：历史上 `locals()` 的行为**按上下文分裂**：模块级返回真全局字典（改它真的生效）；函数级每次调用**从帧的 fast locals 拷贝一份新 dict**（Q1258：局部变量存在槽里不在 dict 里），改它不影响真实变量，且两次调用得到两个独立快照——这也是"为什么调试器里手动赋值经常不生效"的根源。PEP 667（3.13）统一语义：帧对象新增 `f_locals` 的**写回视图**（FrameLocalsProxy）——`frame.f_locals["x"] = 1` 或函数内 `locals()["x"] = 1` 现在是**定义良好的写回操作**（内部通过 `PyFrame_UpdateLocals` 同步到槽），且同一个帧的视图是同一对象、实时反映变量变化。影响面：pdb/调试器的"改局部变量"从赌运气变成可靠；`sys._getframe().f_locals` 这类自省代码不再需要 `exec` hack；同时 `locals()` 在函数内仍是快照语义？——**不是**，3.13 起函数内 locals() 返回的也是这个实时视图（同一帧同一代理）。代价：每次访问视图都有同步成本，热循环里把 `locals()` 当 dict 用本来就是反模式。与 PEP 667 配套的还有 PEP 749（FrameType/TracebackType API 规范化）与 3.14 的延迟注解（Q5003）共同重塑自省生态。

```python
# file: code/01_语言核心与底层/q5038_pep667_locals.py
import sys

# 1) 语义探测: 函数内 locals() 是否为实时写回视图
def probe() -> tuple:
    x = 1
    locs = locals()
    same = locs is locals()            # PEP 667: 同帧同视图 -> True
    try:
        locs["y"] = 2                  # PEP 667: 写回真实局部变量
        return same, y                 # y 已成为真实变量 (3.13+)
    except NameError:
        return same, "(3.12-: 快照, 写回无效)"

same, y = probe()
print(f"两次 locals() 同一对象: {same} | 写回的 y: {y}")
print("(3.13+: True/2; 3.12-: False/快照)")

# 2) 帧级写回: 调试器修改变量的可靠路径 (3.13+)
def demo() -> int:
    a = 10
    frame = sys._getframe()
    try:
        frame.f_locals["a"] = 42       # 3.13 定义良好的写回
    except TypeError:                  # 3.12-: f_locals 是只读 dict 快照
        pass
    return a

print("帧级写回后 a =", demo(), "(3.13+: 42; 3.12-: 10)")

# 3) 模块级: 一向是真字典
mod_locals = locals()
print("模块级 locals() 是 globals:", mod_locals is globals())

# 4) 版本守卫写法: 兼容 3.12- 的调试器代码
def guarded_write(frame, name: str, value) -> None:
    if sys.version_info >= (3, 13):
        frame.f_locals[name] = value   # PEP 667 视图
    else:
        frame.f_locals                # 3.12- 只读快照, 需 eval hack(不推荐展示)
    # 3.12- 的历史方案: frame.f_locals 后跟 exec(f"{name}=value") —— 语义脆弱
    frame.clear()

f = sys._getframe()
print("版本:", sys.version_info[:3], "| 守卫写入已按版本分派")
```

**追问**：1) 为什么函数局部变量不能直接就是 dict？——LOAD_FAST/STORE_FAST 按槽索引访问（快且编译期确定），dict 是运行时结构；PEP 667 是在"槽"之上建了一个同步代理，而不是反过来把槽变成 dict。2) PEP 667 对 sys.settrace 调试器意味着什么？——trace 事件里拿到的 frame.f_locals 变成一致的读写视图，断点处修改变量不再需要"重新绑定帧"的黑魔法，覆盖率/时旅调试工具的实现复杂度下降。3) 视图和 dict 的 API 差异？——它是只读视图类 FrameLocalsProxy 的写回版，不支持 `.update()` 以外的批量操作语义完全等同 dict？实际上是接近 dict 的代理：支持 in、len、迭代与单键读写，但不是 dict 子类，`copy()` 出来的才是真 dict。

## 背诵要点
- 3.13 前函数内 locals() 是拷贝快照，改它无效且两次调用不同对象；模块级一直是真 globals。
- PEP 667：frame.f_locals 与 locals() 返回实时写回视图（FrameLocalsProxy），同帧同对象。
- 写回 = 定义良好的操作，调试器修局部变量从 hack 变可靠；热代码里别拿视图当 dict。

## 复盘追问
- 为什么 CPython 长期容忍"locals() 修改无效"这种半定义行为？统一它的代价是什么？
- 你线上有哪些代码依赖"locals() 是快照"的旧行为？升级 3.13 前怎么扫描？
