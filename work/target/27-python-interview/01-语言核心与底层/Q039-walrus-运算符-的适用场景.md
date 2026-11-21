---
title: [Q039] walrus 运算符 := 的适用场景
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q039 · walrus 运算符 := 的适用场景

> 难度:★☆☆ | 标签:语法, Python 3.8

**问**:海象运算符解决什么问题?哪里不该用?

**答**:`:=` 在表达式内完成赋值并返回值,消除「计算一次、判断一次、再用一次」的重复,典型场景:while 读取循环条件、推导式中的过滤计算、if 中复用一次昂贵调用。它不是替代 `=` 的通用赋值,过度使用会降低可读性,不能用于模块级简单赋值语句位置,也有作用域例外(推导式中的目标绑定到外层作用域)。

```python
# file: code/01_语言核心与底层/q039_walrus.py
import random

def fetch():
    return random.randint(0, 5)

if __name__ == "__main__":
    random.seed(7)

    # 旧写法:先算一次赋给变量,再在 while 条件里反复判断
    while (chunk := fetch()) != 0:
        print("got", chunk)
    print("loop ended on zero")

    values = [10, 25, 3, 40]
    big = [trimmed for v in values if (trimmed := v - 20) > 0]
    print(big)               # [5, 20],计算一次并复用

    if (n := len(values)) > 3:
        print(f"{n} items, more than three")
```

**追问**:1) 推导式里 := 绑定到哪个作用域?——PEP 572 规定绑定到包含推导式的作用域,这是特例,便于过滤条件与输出表达式共享计算。2) 推导式里用 := 有什么意外行为?——赋值目标绑定到包含推导式的作用域(PEP 572 特例),循环结束后变量仍存在;目标名还不能与推导式的迭代变量同名,否则 SyntaxError。3) 什么场景不该用 :=?——为省一行把赋值嵌进复杂条件导致可读性下降;团队规范通常只允许 while 读取循环与简单 if 提取两类用法。
