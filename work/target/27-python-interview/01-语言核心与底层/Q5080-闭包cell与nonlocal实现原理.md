---
title: [Q5080] 闭包 cell 与 nonlocal 的实现原理
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5080 · 闭包 cell 与 nonlocal 的实现原理

> 难度:★★★★ | 标签:原理深挖, 闭包, 字节码

**问**：`LOAD_DEREF`/`STORE_DEREF` 与 cell 对象是什么关系？为什么闭包里写 `x += 1` 不加 nonlocal 会报 UnboundLocalError 而读没问题？late-binding 的 `lambda` 循环陷阱在 cell 层面如何解释、`default=` 与 `functools.partial` 两种修法在机制上差在哪？

**答**：结论：Python 的闭包实现是**二级名字体系**：内层函数引用外层局部变量时，编译器把该变量放进一个 `cell` 对象（一格可变容器），外层帧用 `STORE_DEREF` 写 cell、内层用 `LOAD_DEREF` 读 cell——函数捕获的是 **cell 引用**而不是值的快照，这就是"闭包记住的是变量本身"的机制根源。规则细节：a) **判断写不写 nonlocal** 的依据是编译期作用域分析：内层函数对名字有赋值语句（含 `+=`，它编译成 STORE）就把这个名字归为**本地名**，运行时 `LOAD_FAST` 读本地槽位、未赋值即 UnboundLocalError；只读的名字才归为闭包名走 LOAD_DEREF；b) late-binding 陷阱的 cell 解释：循环里 `lambda: i` 的三份 lambda 共享**同一个 cell**（循环体每轮 STORE_DEREF 更新 cell 内容），循环结束 cell 里是最后值，三个 lambda 调用都读到它；`lambda i=i: i` 的修法是把值放进**参数默认值**——默认值在函数对象创建时求值一次存进 `__defaults__`，与 cell 无关，所以是早绑定；`partial(f, i)` 同理是构造时固定参数；c) 成本与工具：cell 多一层间接，访问略慢于本地槽，但可忽略；调试用 `func.__closure__`（cell 元组）+ `cell.cell_contents` 查看捕获内容，改 cell_contents（3.7+ 可写）甚至能"从外部改闭包变量"。实战：并发场景下闭包捕获共享 cell 变量要当锁内共享对待（多线程写同一 cell 与普通变量同样有竞态）；循环提交任务的最常见事故就是共享 cell。

```python
# file: code/01_语言核心与底层/q5080_closure_cell.py
import sys, dis

def outer():
    n = 0
    def inner():
        nonlocal n          # 有赋值 -> 必须 nonlocal 才归为闭包名
        n += 1
        return n
    def reader():           # 只读 -> 自动走 cell
        return n
    return inner, reader

inc, rd = outer()
print("读写共享同一 cell:", inc() == 1 and inc() == 2 and rd() == 2)
print("inner.__closure__:", inc.__closure__, "| cell 内容:", inc.__closure__[0].cell_contents)

# 1) 字节码: STORE_DEREF/LOAD_DEREF(nonlocal 写) 与 LOAD_DEREF(闭包读)
print("== inner 的字节码(含 nonlocal 写) ==")
dis.dis(inc, depth=0)

# 2) 写不加 nonlocal -> 名字被归为本地 -> UnboundLocalError
def broken():
    x = 1
    def bump():
        x += 1              # 编译期判定 x 是本地名
        return x
    return bump
try:
    broken()()()
except UnboundLocalError as e:
    print("无 nonlocal 的赋值:", e)

# 3) late-binding 陷阱与两种修法的机制差异
lams = [lambda: i for i in range(3)]
print("共享 cell -> 全是最后值:", [f() for f in lams])
cells = {id(f.__closure__[0]) for f in lams}
print("三个 lambda 捕获的是同一个 cell 吗:", len(cells) == 1)

lams2 = [lambda i=i: i for i in range(3)]          # 默认值: 创建时求值, 存 __defaults__
print("default 早绑定:", [f() for f in lams2],
      "| defaults:", [f.__defaults__ for f in lams2])

from functools import partial
lams3 = [partial(lambda v: v, i) for i in range(3)]
print("partial 固定参数:", [f() for f in lams3])

# 4) 3.7+ 可从外部改 cell
inc.__closure__[0].cell_contents = 100
print("外部改 cell 后再 inc:", inc())
print("python:", sys.version.split()[0])
```

**追问**：1) `cell_contents` 可写有什么工程风险？——它绕过 nonlocal 声明直接改闭包状态，适合测试注入与补丁，但生产代码里用它等于制造"函数对象带隐藏可变状态"，可测试性看似变好、可维护性变差；比它更正规的方式是显式传上下文对象。2) class 体内的推导式为什么访问不到类属性？——类体作用域**不进入**嵌套作用域链（推导式是隐函数），其中引用类属性会落到全局查找失败；这正是推导式里 `lambda` 捕获需要 default 参数的又一案例。3) `__closure__` 为 None 何时发生？——内层函数没有引用任何外层自由变量（比如只用了全局），就没有 cell；`func.__code__.co_freevars` 列出自由变量名，空即无闭包。

## 背诵要点
- 闭包=捕获 cell 引用：外层 STORE_DEREF 写、内层 LOAD_DEREF 读，捕获变量而非值快照；`__closure__`/`cell_contents` 可检视（3.7+ 可写）。
- 赋值语句（含 +=）让编译期把名字归为本地 → UnboundLocalError，必须 nonlocal；只读名自动走 cell。
- late-binding 根因=循环共享同一 cell；default= 是创建时存 `__defaults__` 的早绑定，partial 是构造时固定参数，两者都与 cell 无关。

## 复盘追问
- 你们代码里循环提交任务（线程池/事件循环回调）用的是哪种捕获方式？出过"回调全拿到最后一个变量"的事故吗？（提示：三类修法里 default= 最轻，但注意默认值是可变对象时共享的二级陷阱）
- 闭包捕获大对象（模型、连接）时，生命周期由谁持有？（提示：内层函数存活多久，cell 就持多久；排查内存不释放时把 `__closure__` 检查加进泄漏工具链，见 Q5071）
