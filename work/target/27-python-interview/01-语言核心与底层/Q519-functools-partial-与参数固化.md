---
title: [Q519] functools.partial 与参数固化
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q519 · functools.partial 与参数固化

> 难度:★★☆☆ | 标签:functools, 函数式

**问**:partial 和 lambda 的区别?partial 固化关键字参数有什么讲究?

**答**:partial(func, *args, **kwargs) 返回可调用对象,调用时「新参数接在固化参数之后」;与 lambda 相比:partial 是类实例、可 repr、可被 deepcopy、有 __name__ 可用性更好,且意图明确(「固定前几个参数」);lambda 更灵活(可重排参数)但匿名且闭包语义易踩 late binding。固化关键字参数时注意:后续调用传同名关键字会覆盖固化的值(partial 不锁死);回调注册(线程池 executor.submit、signal)、便捷构造器、把多参函数适配成单参回调是三大甜点区。

```python
# file: code/01_语言核心与底层/q519_partial.py
import functools
import operator

def send_email(to, subject, body, *, dry_run=False):
    return f"[{subject}] to {to}: {body}{' (dry)' if dry_run else ''}"

if __name__ == "__main__":
    notify_admin = functools.partial(send_email, "admin@corp.local")
    crash_alert = functools.partial(notify_admin, subject="CRASH", dry_run=True)
    print(crash_alert(body="worker died"))

    int2 = functools.partial(int, base=2)     # 固化关键字参数
    print(int2("1010"))

    double = functools.partial(operator.mul, 2)
    print(list(map(double, [1, 2, 3])))
    print("overridable:", crash_alert.keywords["dry_run"])   # partial 元数据可见
```

**追问**:1) partial 固化的关键字参数能被覆盖吗?——能,调用时传同名 kwargs 以调用方为准;要「锁死不可覆盖」就再包一层函数把参数收窄到剩余项。2) partial 与闭包/默认参数的差别?——partial 在调用时拼参数、不改函数定义;闭包捕获变量(晚绑定,循环变量坑);默认参数在定义时求值(早绑定);partial 返回可调用对象,参数结构可 introspect(func/args/keywords 属性)。3) 底层与衍生?——C 实现的 functools.partial 存 (func, args, keywords) 在 __call__ 时拼接;partialmethod 适配描述符协议,可在类里当方法用。4) 生产陷阱?——晚绑定混淆:partial 固化的是求值后的值,闭包固化的是变量名,两者混用出「循环里全是同一个值」的经典 bug;partial 链式套太多层可读性崩,显式 wrapper 更好。
