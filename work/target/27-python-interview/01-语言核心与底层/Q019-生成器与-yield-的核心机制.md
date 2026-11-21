---
title: [Q019] 生成器与 yield 的核心机制
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q019 · 生成器与 yield 的核心机制

> 难度:★★☆ | 标签:生成器

**问**:生成器和普通函数有什么不同?yield 执行到一半的函数状态存在哪里?

**答**:含 `yield` 的函数调用时并不执行函数体,而是返回生成器对象;每次 `next()` 执行到下一个 yield 暂停,局部变量、指令指针保存在生成器对象的栈帧里,而非线程栈。生成器惰性求值,天然适合流式处理超大文件、无限序列,内存占用与数据量无关。结束抛出 StopIteration,函数 return 值放在其 value 属性中。

```python
# file: code/01_语言核心与底层/q019_generator.py
def countdown(n):
    while n > 0:
        yield n
        n -= 1
    return "done"

if __name__ == "__main__":
    gen = countdown(3)
    print(next(gen))  # 3
    print(next(gen))  # 2
    for rest in gen:  # for 自动处理 StopIteration
        print(rest)   # 1

    try:
        next(gen)
    except StopIteration as e:
        print("return value:", e.value)  # done

    big = (x * x for x in range(10**8))  # 立即返回,不占内存
    print(next(big))
```

**追问**:1) 生成器可以被多次遍历吗?——不能,一次性消耗,重复遍历第二个必然为空;需要多次就重新调用生成函数或用 `itertools.tee`。2) 生成器靠什么「记住」执行位置?——栈帧分配在堆上而非线程栈,保存指令指针与局部变量,暂停时帧不销毁,`next()` 从 yield 处恢复——这正是协程的机制基础。3) 生成器抛异常后还能继续 next 吗?——不能,异常使其进入关闭状态,再 next 只会抛 StopIteration;`close()` 在挂起点注入 GeneratorExit,`throw()` 注入任意异常,都要求生成器做清理。
