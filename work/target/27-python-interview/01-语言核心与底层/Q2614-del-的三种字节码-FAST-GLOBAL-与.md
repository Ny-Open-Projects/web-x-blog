---
title: [Q2614] del 的三种字节码:FAST、GLOBAL 与 DEREF 的删除语义
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2614 · del 的三种字节码:FAST、GLOBAL 与 DEREF 的删除语义

> 难度:★★★☆☆ | 标签:del, 字节码, 作用域

**问**:`del x` 删的是对象还是名字?不同作用域里的 del 在字节码上有什么区别?

**答**:`del` 删的是名字(或容器的槽位),不是对象;对象由引用计数和 GC 兜底回收。字节码上按名字所在层级分派四种指令:局部变量 `DELETE_FAST`(清槽位并标记未绑定)、模块级 `DELETE_NAME`(删模块字典键)、全局函数里删全局名 `DELETE_GLOBAL`、闭包变量 `DELETE_DEREF`(清 cell)。容器形态另有两条:`del lst[0]` 编译为删除下标加 `DELETE_SUBSCR`,`del obj.attr` 是 `DELETE_ATTR`。删未绑定的名字抛 UnboundLocalError 或 NameError,这常被用作「快速失败」的手段。理解 del 是删名字,才能解释 `del` 之后为什么别处引用的对象还活着。

```python
# file: code/01_语言核心与底层/q2614_del_bytecode.py
"""del 的字节码家族:DELETE_FAST、DELETE_NAME、DELETE_DEREF 与容器形态。"""
import dis

module_var = 1


def del_fast():
    a = 1
    del a                       # DELETE_FAST
    return a                    # 已未绑定


def make_closure():
    x = 10

    def inner():
        nonlocal x
        del x                   # DELETE_DEREF
    return inner


def del_global():
    global module_var
    del module_var              # DELETE_GLOBAL


if __name__ == "__main__":
    print("del 局部变量:")
    dis.dis(del_fast)

    print("del 闭包变量:")
    dis.dis(make_closure())

    lst = [1, 2, 3]

    class Box:
        pass

    b = Box()
    b.v = 1

    def del_container():
        del lst[0]              # DELETE_SUBSCR
        del b.v                 # DELETE_ATTR
    dis.dis(del_container)
```

**追问**:1) `except E as e` 结束后为什么 `e` 没了?——解释器在 except 块结束时会隐式 `DELETE` 这个名字,防止 traceback 通过 `e.__traceback__` 造成引用滞留。2) 三种 DELETE 的语义差异?——DELETE_FAST 拆局部槽、DELETE_GLOBAL 删全局名、DELETE_DEREF 拆闭包 cell;共同点:删名字不删对象(Q545);del 后同函数内再赋值回到普通局部。3) 隐式删除的工程含义?——块外用 e 必须「先转存」且注意 __traceback__ 引用链(Q2643);闭包捕获 e 同样失效。4) 生产陷阱?——日志函数闭包捕获 e 后 NameError;保留异常对象钉住整条调用链;以为 del 会立即释放(引用在别处)。
