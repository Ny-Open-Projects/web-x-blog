---
title: [Q405] 小整数缓存与字符串 intern:is 比较的坑
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q405 · 小整数缓存与字符串 intern:is 比较的坑

> 难度:★★★★☆ | 标签:CPython, 对象缓存, str

**问**:为什么 `256 is 256` 为 True 而 `257 is 257` 可能是 False?为什么两个内容相同的字符串有时 `is` 为 True 有时为 False?这些"缓存"的边界到底在哪?

**答**:CPython 解释器初始化时预先创建 -5 到 256 的 `PyLong` 对象并在全解释器共享,所以小整数 `is` 恒真;257 这类超出缓存范围的字面量,在同一 code object 内会被**常量去重**(co_consts 中合并为同一对象)所以 is 也可能为 True,但跨 code object(如交互式逐行执行、不同模块)就是两个独立对象;小整数缓存 [-5,256] 只保证该范围内跨编译单元共享。注意「常量去重」与「常量折叠」(编译期求值,如 "hello"+"_world")是两个不同概念。字符串方面,只由 ASCII 字母、数字、下划线组成的**编译期字面量**会被自动 intern(标识符长得像,方便按指针比较属性名),而运行期拼接产生的字符串(含空格、动态结果)不会。结论:`is` 只该用于单例比较(`x is None`),数值/字符串相等一律用 `==`;对字面量用 `is` 还会触发 SyntaxWarning("is" with a literal),这本身就是反模式信号;把 `is` 当优化手段依赖的是实现细节,Python 3.12 的 immortal objects 和 PEP 683 进一步改变了这些边界。

```python
# file: code/01_语言核心与底层/q405_intern_cache.py
import sys

# 同一 code object 内:相同字面量常量去重(257 也共享)
print(256 is 256)               # True
print(257 is 257)               # 同一 code object 内 True(常量去重,不是常量折叠)
x, y = 257, 257                 # 局部变量仍指向同一常量池对象
print(x is y)                   # True,因为同一函数编译单元

# 字符串:编译期字面量自动 intern,运行期拼接不会
a = "hello_world"
b = "hello_world"
print(a is b)                   # True,字面量 intern
c = "hello" + "_world"
print(c is a)                   # True!常量折叠在编译期完成
d = "".join(["hello", "_world"])
print(d is a, d == a)           # False True,运行期产生不 intern

print(sys.intern("py" + "thon") is sys.intern("python"))  # 手动 intern
```

**追问**:1) `sys.intern` 的真正用途是什么?——让大量重复字符串(如协议字段名)共享同一对象,dict 查找退化为指针比较,同时省内存;CPython 内部 dict 键比较正是先比 `hash` 再比指针再比内容。2) `float`/`tuple` 有类似缓存吗?——没有,只有小整数和部分单例(`None`/`True`/`False`)以及空 tuple 有共享。
