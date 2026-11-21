---
title: [Q1294] except as 的隐式 del:名称在块外消失
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1294 · except as 的隐式 del:名称在块外消失

> 难度:★★☆☆☆ | 标签:异常, 作用域, 疑难杂症

**问**:`except ValueError as e:` 结束后 e 还能用吗?为什么 Python 要故意删掉它?

**答**:except 块结束时,解释器隐式执行 `del e`(3.0 起),块外再引用 e 抛 NameError——但注意删的是「这个名字」,函数外层的同名变量会幸存,作用域语义与 Q527 一脉相承。动机是异常对象持有 traceback,traceback 持有整条调用链的帧:如果 e 长期存活(比如绑到 self、闭包、全局),等于把异常发生时的整条栈钉在内存里(Q424 的内存滞留场景),隐式 del 是语言层的自动保险。需要保留时,把 `str(e)`、`type(e)` 或 `e.args` 摘出来,或者显式 `traceback.print_exc()` 后再保留消息;直接 `keep = e` 会连 traceback 一起留下,建议 `keep = e.with_traceback(None)`。

```python
# file: code/01_语言核心与底层/q1294_except_as_del.py


def show():
    try:
        raise ValueError("boom")
    except ValueError as e:
        print("inside block:", e)
    try:
        print(e)                        # 块外:名称已被隐式删除
    except NameError as err:
        print("outside block ->", type(err).__name__)

    kept = None
    try:
        raise ValueError("persist")
    except ValueError as e:
        kept = e.with_traceback(None)   # 摘掉 traceback 再保存
    print("kept message:", kept, "| traceback detached")


if __name__ == "__main__":
    show()
```

**追问**:1) Python 2 为什么没这个问题?——py2 不做隐式 del,e 长期存活导致著名泄漏案例,PEP 3110 在 py3 里统一改成隐式删除,这是「异常即资源」的历史注脚。2) 隐式 del 删的是什么?——只删 except 绑定的名字,异常对象是否回收取决于其他引用;traceback 链挂在 e.__traceback__ 上,长期持有异常对象会钉住整条调用链(Q1256)。3) 块外怎么办?——隐式 del 后名字未绑定,再访问 NameError;要在块外用就先绑定到别的变量,并且必要时清掉 __traceback__。4) 生产陷阱?——闭包/lambda 捕获 e 同样在块外失效;日志系统缓存异常对象导致内存滞留;重抛用裸 raise 保留原 traceback,新 raise 会重置(除非显式传)。
