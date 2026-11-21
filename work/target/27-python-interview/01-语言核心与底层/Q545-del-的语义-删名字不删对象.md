---
title: [Q545] del 的语义:删名字不删对象
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q545 · del 的语义:删名字不删对象

> 难度:★★☆☆ | 标签:del, 引用

**问**:del x 之后对象被释放了吗?del 对 dict 条目、切片、属性分别做什么?

**答**:del 只做「解绑名字/引用」:从命名空间、容器、属性里移除一个引用,引用计数减一;对象是否立即释放取决于是否还有其他引用——别名存在就活着。变体:del dict[k] 删条目、del list[i:j] 删切片(等价赋空切片)、del obj.attr 调用 __delattr__、del 局部变量让后续访问 NameError(函数内还用于「声明此名不再使用」配合 nonlocal)。它与「清空容器」不同:del lst[:] 才清内容,del lst 只删名字。GC 时序依赖(del 即释放)在 CPython 成立,跨实现不保证——资源释放永远用 with。

```python
# file: code/01_语言核心与底层/q545_del_semantics.py
import sys

data = [1, 2, 3]
alias = data
del data                                  # 只删名字
print("object alive via alias:", alias)

holder = {"k": [1, 2, 3]}
ref = holder["k"]
del holder["k"]                           # 删条目,对象由 ref 继续持有
print("value survives:", ref, "refcount > 1:", sys.getrefcount(ref) > 1)

nums = [0, 1, 2, 3, 4]
del nums[1:3]                             # 删切片
print("slice deleted:", nums)

def scope_demo():
    x = 1
    del x
    try:
        print(x)
    except NameError as e:
        print("unbound inside function:", e)

if __name__ == "__main__":
    scope_demo()
```

**追问**:1) 为什么函数里 del 局部变量后编译器把它当未绑定?——del 在字节码层是 DELETE_FAST,移除局部槽的绑定;编译期就知道该名字在后续不可用,访问直接抛 UnboundLocalError 语义的 NameError。2) del 的三重语义?——删名字(解除绑定)、容器项(调 __delitem__)、属性(调 __delattr__);都不直接释放对象——引用归零才回收,del 只是「拆引用」的语法。3) 字节码层?——DELETE_FAST/DELETE_GLOBAL/DELETE_NAME 分别处理局部/全局/名字表;del 后同一函数里再赋值同一名字,编译器把它视为普通局部变量。4) 生产陷阱?——以为 del 大对象立即释放内存(闭包/全局引用还在);想强制回收用 gc.collect();del 列表切片 vs clear() 的语义差异(前者重建索引后者原地清空)。
