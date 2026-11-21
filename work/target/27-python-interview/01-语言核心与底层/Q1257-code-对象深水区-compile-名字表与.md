---
title: [Q1257] code 对象深水区:compile、名字表与 code.replace
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1257 · code 对象深水区:compile、名字表与 code.replace

> 难度:★★★★☆ | 标签:code 对象, 字节码, 动态执行

**问**:compile 返回的 code 对象里有哪些「名字表」?code.replace 能安全地改什么?同一个 code 怎么变成新函数?

**答**:code 对象的几张表各管一类名字:`co_varnames` 是局部槽位(含参数,顺序即槽位顺序)、`co_cellvars`/`co_freevars` 是闭包相关变量、`co_names` 是全局名与属性名、`co_consts` 是常量池(嵌套函数的 code 对象也在里面)。`compile(src, filename, mode)` 是运行时造 code 的正规入口,mode 取 exec/eval/single。3.8 起的 `code.replace(**kwargs)` 可以以不可变方式派生新 code(改 co_name、co_filename 等),比手拼 types.CodeType 的参数列表安全得多;典型玩法是给 `__code__` 换血实现热修复或重命名,前提是槽位布局兼容。Q547 讲函数对象与 code 的分离,本题补的是 code 自身的表结构与派生工具。

```python
# file: code/01_语言核心与底层/q1257_code_replace.py
import dis
import types

SRC = """
def hello(name):
    return "hello " + name
"""

if __name__ == "__main__":
    module_code = compile(SRC, "<demo>", "exec")
    print("module co_names:", module_code.co_names)
    nested = [c for c in module_code.co_consts if isinstance(c, types.CodeType)]
    fn_code = nested[0]
    print("nested:", fn_code.co_name, "varnames:", fn_code.co_varnames)

    # eval 模式:表达式编译后可直接求值
    expr = compile("1 + 1", "<expr>", "eval")
    print("eval code result:", eval(expr))

    # 不可变派生:改名换文件名,字节码不动
    renamed = fn_code.replace(co_name="hello2", co_filename="<renamed>")
    ns = {}
    exec(module_code, ns)
    hello = ns["hello"]
    print("before swap:", hello("CPython"))
    hello.__code__ = renamed          # 槽位兼容,可以直接换
    print("after swap :", hello("CPython"), "| co_name:", hello.__code__.co_name)
    print("instruction count:", len(list(dis.get_instructions(renamed))))
```

**追问**:1) co_consts 里的嵌套 code 和外层 code 是什么关系?——编译期一次性生成、通过 MAKE_FUNCTION 在运行时绑上 globals 与默认值,这正是「同一份 code 组装多个函数」(Q547)的源头。2) code.replace 是干什么的?——3.8+ code 不可变,replace 返回改了 co_name/co_firstlineno 等字段的新 code,配合函数对象替换做度量与调试;不能改任意字节码语义的「危险开关」。3) 名字表怎么分工?——co_varnames 局部槽、co_cellvars/co_freevars 闭包、co_names 全局与属性名;dis 与静态分析工具都建立在这些表上。4) 生产陷阱?——marshal 持久化 code 跨版本不兼容(字节码随版本变);手动构造 code 对象是黑魔法;改 co_firstlineno 后 linecache 行号失配。
