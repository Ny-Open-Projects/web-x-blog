---
title: [Q018] nonlocal 与 global 的区别
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q018 · nonlocal 与 global 的区别

> 难度:★★☆ | 标签:作用域, 闭包

**问**:在嵌套函数里给外层变量赋值为什么报 UnboundLocalError?两种声明怎么选?

**答**:Python 用 LEGB 作用域查找规则,但赋值语句会让名字被编译期判定为局部变量,除非显式声明。`global` 绑定模块级名字,`nonlocal`(Python 3)绑定最近的封闭函数作用域,要求该名字在外层已存在。优先避免可变全局状态,需要跨层写变量时局部闭包用 `nonlocal`。

```python
# file: code/01_语言核心与底层/q018_nonlocal.py
counter_value = 0

def bad_counter():
    counter_value += 1   # UnboundLocalError,赋值使它成为局部

def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

if __name__ == "__main__":
    c = make_counter()
    print(c(), c(), c())   # 1 2 3,各闭包独立

    d = make_counter()
    print(d())             # 1,与 c 互不影响
```

**追问**:1) 不写 nonlocal、直接对外层 list 做 append 可以吗?——可以,因为这是方法调用而非名字重绑定,不触发局部判定;这也是「可变容器绕过作用域限制」的常见写法。2) nonlocal 找不到外层绑定会怎样?——编译期直接 SyntaxError: no binding for nonlocal;而 global 不要求先存在,首次赋值才创建模块级名字。3) 类体作用域在 LEGB 里算哪层?——不算,类体是独立的临时命名空间,方法内不会查找类体名字,必须通过 self 或类名访问;这是推导式/默认值引用类属性报 NameError 的常见来源。
