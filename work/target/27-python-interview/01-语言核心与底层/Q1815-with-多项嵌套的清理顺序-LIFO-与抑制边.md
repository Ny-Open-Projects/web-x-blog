---
title: [Q1815] with 多项嵌套的清理顺序:LIFO 与抑制边界
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1815 · with 多项嵌套的清理顺序:LIFO 与抑制边界

> 难度:★★★☆☆ | 标签:with, 清理顺序, __exit__

**问**:`with A() as a, B() as b:` 的进入与退出顺序是什么?某个环节出错时资源会漏吗?

**答**:多项 with 是嵌套的语法糖:进入按书写顺序 A→B,退出严格 LIFO B→A——先开的资源后关,栈式配对。异常路径也按栈展开:体里抛错时先 B.__exit__ 再 A.__exit__,每个 __exit__ 都能看到异常并决定抑制(返回 True,Q449)或放行;第二个 CM 的 __enter__ 失败时,第一个已经进入、仍会收到清理机会,只有「还没进入」的资源无需清理——demo 里内层 enter 失败,外层照样执行 exit。两个边界:__exit__ 自身抛新异常会顶掉正在传播的旧异常(旧异常进 __context__);抑制是逐层决策,默认 False 放行,没有「全局抑制开关」。

```python
# file: code/01_语言核心与底层/q1815_with_lifo.py
"""with 多项嵌套的清理顺序:LIFO 与抑制边界。"""


class Tracer:
    def __init__(self, name, fail_enter=False):
        self.name = name
        self.fail_enter = fail_enter

    def __enter__(self):
        if self.fail_enter:
            raise RuntimeError(self.name + " 进入失败")
        print("enter " + self.name)
        return self

    def __exit__(self, exc_type, exc, tb):
        seen = exc_type.__name__ if exc_type else "无"
        print("exit  " + self.name + " | 顺带看到异常: " + seen)
        return False                     # 不抑制


def order_demo():
    with Tracer("外层"), Tracer("内层"):
        print("body 执行")


def body_error_order():
    try:
        with Tracer("外层"), Tracer("内层"):
            raise ValueError("业务异常")
    except ValueError as e:
        print("捕获:", e)


def enter_fail_still_cleans():
    # 第二个 CM 的 __enter__ 失败:第一个已进入,仍会收到清理机会
    try:
        with Tracer("外层"), Tracer("内层", fail_enter=True):
            print("body 不会执行")
    except RuntimeError as e:
        print("捕获:", e)


if __name__ == "__main__":
    print("--- 正常路径:进入顺序 A-B,退出顺序 B-A ---")
    order_demo()
    print("--- 体异常:先出内层再出外层,异常最后交给外层 ---")
    body_error_order()
    print("--- 第二个 enter 失败:第一个仍被清理 ---")
    enter_fail_still_cleans()
```

**追问**:1) 需要非固定顺序的动态清理怎么办?——contextlib.ExitStack 统一压栈,Q448 讲动态数量,本题的 LIFO 语义就是它的底层保证。2) 多项 with 的语义细节?——`with a as x, b as y` 等价嵌套:进入顺序 a→b,退出逆序 b→a;某层 __enter__ 失败,已进入的外层照常退出。3) 抑制边界?——内层 __exit__ 返回 True 吞掉异常,外层看不到——「内层 suppress 外层不知道」是排查诡异行为的常见原因;资源间有依赖时,清理逆序正好保证「先关后代再关祖先」。4) 生产陷阱?——依赖正序清理的代码写反了嵌套顺序;内层吞异常让外层事务语义失效;多项 with 拆成多行后顺序被无意调换。
