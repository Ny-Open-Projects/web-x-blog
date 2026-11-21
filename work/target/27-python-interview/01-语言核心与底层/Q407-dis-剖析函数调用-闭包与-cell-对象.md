---
title: [Q407] dis 剖析函数调用:闭包与 cell 对象
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q407 · dis 剖析函数调用:闭包与 cell 对象

> 难度:★★★★★ | 标签:dis, 闭包, 字节码

**问**:闭包变量和全局变量、局部变量在字节码层面有什么本质区别?`cell` 对象是什么?为什么闭包捕获的是"变量"而不是"值"?

**答**:CPython 为每层作用域使用不同的加载指令:`LOAD_FAST`(栈上局部,数组下标访问)、`LOAD_GLOBAL`(模块字典查找,3.11 起有内联缓存加速)、`LOAD_DEREF`(经 cell 对象间接访问)。内层函数引用外层函数变量时,编译器把该变量提升为 cell——一个堆上小盒子,内外两层函数都通过 `LOAD_DEREF`/`STORE_DEREF` 读写它,所以闭包捕获的是变量的**存储位置**而非快照值,这也是 `for i in ...: fs.append(lambda: i)` 全部读到末值的根源。`__closure__` 属性暴露这些 cell。这解释了闭包的三大行为:延迟绑定、闭包内赋值需要 `nonlocal`、以及循环变量共享。

```python
# file: code/01_语言核心与底层/q407_closure_deref.py
import dis

def outer():
    x = 10
    def inner():
        return x + 1        # x 是自由变量,经 cell 访问
    return inner

f = outer()
print(f())                 # 11
print(f.__closure__)       # cell 对象元组
print(f.__closure__[0].cell_contents)   # 10,可读也可写(cell_contents 可赋值)

print("---- inner bytecode ----")
dis.dis(f)                 # 看到 LOAD_DEREF 而非 LOAD_FAST/LOAD_GLOBAL

# 经典坑:lambda 捕获变量本身
fs = [lambda: i for i in range(3)]
print([g() for g in fs])   # [2, 2, 2]
fs2 = [lambda i=i: i for i in range(3)]
print([g() for g in fs2])  # [0, 1, 2],默认参数在 def 时固化
```

**追问**:1) 为什么闭包读到循环末值?——所有 lambda 共享同一个 cell,循环结束时 cell 里是 2。2) Python 3.11+ 的 `LOAD_GLOBAL` 缓存存在哪里?——adaptive interpreter 把指令改写成特化形式,缓存内嵌在字节码流里,这是 3.11 提速的核心手段之一。
