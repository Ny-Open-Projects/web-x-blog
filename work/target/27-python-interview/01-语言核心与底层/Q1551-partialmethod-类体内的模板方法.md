---
title: [Q1551] partialmethod:类体内的模板方法
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1551 · partialmethod:类体内的模板方法

> 难度:★★★☆☆ | 标签:functools, partialmethod, 类设计

**问**:functools.partialmethod 解决什么问题?为什么在类体里直接用 partial 不行?

**答**:partial 不是描述符:放进类体后,实例访问它不会绑定 self,拿到的是裸 partial 对象,调用时缺 self 直接 TypeError;partialmethod 是给类体设计的包装——实现 __get__,属性访问时绑定实例,等价「一个基方法派生多个语义化方法」的生成器(Q519 讲函数层的 partial,本题讲类体层)。工程用法:① 移动/配置类语义方法(move_up/move_down/fast/safe)复用同一实现;② 给带默认参数的方法生成快捷变体;③ 类体内批量生成同构方法,避免复制粘贴。要点:① __doc__ 与 functools 的语义保留配套;② 3.9 不能与 classmethod/staticmethod/abstractmethod 叠放(3.11 起支持),需要类方法版就手工包一层;③ 纯函数场景(不在类体)继续用 partial。

```python
# file: code/01_语言核心与底层/q1551_partialmethod.py
from functools import partial, partialmethod


class Robot:
    def _move(self, dx, dy, label):
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        return "%s: now at %s" % (label, self.pos)

    move_up = partialmethod(_move, 0, 1, label="up")
    move_down = partialmethod(_move, 0, -1, label="down")

    def _set_mode(self, mode):
        self.mode = mode
        return "mode -> " + mode

    fast = partialmethod(_set_mode, "fast")
    safe = partialmethod(_set_mode, "safe")

    # 反例:partial 不是描述符,这样写调用时会炸(仅作展示)
    broken = partial(_move, 0, 0, label="broken")


if __name__ == "__main__":
    r = Robot()
    r.pos = (0, 0)
    print(r.move_up())
    print(r.move_down())
    r.fast()
    print(r.move_up())
    r.safe()
    print("mode:", r.mode)

    try:
        r.broken()
    except TypeError as err:
        print("partial in class ->", type(err).__name__, "-", err)
```

**追问**:1) partialmethod 能叠 @classmethod 吗?——3.11 起支持,3.9 会行为异常;需要类方法版就手工包一层 def cls_method(cls): return _impl(...)。2) partialmethod 的机制?——descriptor 包装 partial:类体内定义模板方法,访问时绑定 self 再拼预置参数;这是它与裸 partial 的本质差——partial 放类属性不绑定 self。3) 模板方法的典型场景?——一个 _impl(params) 派生多个语义化方法(set_x/get_x);Django 风格的 convenience 方法;减少样板代码。4) 生产陷阱?——把 partial 直接放类里当方法(不绑定,调用报缺 self);3.9 叠 classmethod 异常;模板方法太多掩盖「该抽象基类」的设计信号。
