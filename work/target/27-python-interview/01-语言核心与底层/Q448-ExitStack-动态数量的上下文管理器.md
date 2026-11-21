---
title: [Q448] ExitStack:动态数量的上下文管理器
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q448 · ExitStack:动态数量的上下文管理器

> 难度:★★★★ | 标签:上下文管理器, contextlib

**问**:with 语句只能写死的几层嵌套,如果要按运行时条件打开不定数量的资源怎么办?

**答**:contextlib.ExitStack 是上下文管理器的「栈容器」:`enter_context(cm)` 立即进入并登记退出回调,栈在 with 结束或异常时按逆序统一展开,等价于把 N 层 with 压平。它解决三类问题:动态数量(循环里 enter_context 打开任意多文件)、条件进入(需要时才 enter)、所有权移交(close 后的回调可以被 pop_all 搬走转交他人)。callback 还能注册任意清理函数,不只是上下文管理器。

```python
# file: code/01_语言核心与底层/q448_exitstack.py
import contextlib
import os
import tempfile

def open_many(paths):
    """打开任意数量文件,把清理权打包移交"""
    stack = contextlib.ExitStack()
    handles = [stack.enter_context(open(p, encoding="utf-8")) for p in paths]
    return stack, handles                 # 所有权随 stack 一起移交

def rollback_demo(paths):
    with contextlib.ExitStack() as stack:
        stack.callback(print, "cleanup 1 runs last")
        stack.callback(print, "cleanup 2 runs first")
        raise RuntimeError("boom")        # 异常时 callback 逆序执行

if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    paths = []
    for i in range(3):
        p = os.path.join(tmpdir, f"f{i}.txt")
        with open(p, "w", encoding="utf-8") as w:
            w.write("line\n" * (i + 1))
        paths.append(p)

    stack, handles = open_many(paths)
    print("total lines:", sum(1 for h in handles for _ in h))
    stack.close()                         # 逆序统一关闭

    try:
        rollback_demo(paths)
    except RuntimeError as e:
        print("caught:", e)
```

**追问**:1) pop_all 和 close 的区别?——pop_all 把已登记的清理动作搬进一个新 ExitStack 返回,实现「全部成功才提交」的事务模式;close 是立即就地逆序清理。2) callback 与 enter_context 的执行顺序?——同一栈统一按注册逆序展开;「后注册的先跑」与直觉相反,事务式的成功/失败双路径要用 pop_all 把回调搬到不同栈再分别触发。3) 展开时某回调抛异常怎么办?——ExitStack 继续展开剩余回调保证清理完整,最后异常经 __context__ 链上抛;这是「清理优先于单点失败」的设计,自定义栈容器应复刻该语义。4) 生产陷阱?——把 ExitStack 当长期资源池(它只管一次性清理不管复用);pop_all 移交所有权后忘记 close 新栈,泄漏点转移到新持有者且更隐蔽。
