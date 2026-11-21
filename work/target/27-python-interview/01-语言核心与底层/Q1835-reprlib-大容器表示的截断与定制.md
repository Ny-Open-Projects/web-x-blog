---
title: [Q1835] reprlib:大容器表示的截断与定制
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1835 · reprlib:大容器表示的截断与定制

> 难度:★★☆☆☆ | 标签:reprlib, repr, 日志

**问**:日志里打个 list 一百万元素直接把日志打爆,stdlib 有没有现成的截断表示?

**答**:reprlib 就是干这个的:reprlib.repr(obj) 按内置限额截断容器(maxlist/maxdict/maxstring/maxlevel 等),demo 里上百项的列表只显示前几项加省略号;自己实例化 Repr 可调各项限额。定制两点:① 继承 Repr 覆写 repr_<type> 方法(repr_str/repr_dict)给特定类型定制表示——demo 里长字符串只报尺寸不落内容;② maxlevel 控制嵌套深度,深结构只展开前两层。与 Q513 的手写 __repr__ 分工:模型类该有自己的 repr(字段名=值),reprlib 管「任意未知大对象」的兜底表示,日志管道、调试输出、异常消息里都该用它而不是裸 repr。

```python
# file: code/01_语言核心与底层/q1835_reprlib_truncate.py
"""reprlib:大容器表示的截断与定制。"""
import reprlib


def default_truncate():
    big = list(range(100)) + [{"k": i} for i in range(3)]
    r = reprlib.Repr()
    r.maxlist = 6                    # 列表最多显示 6 项
    r.maxdict = 2
    r.maxstring = 12
    return r.repr(big)


class QuietRepr(reprlib.Repr):
    def __init__(self):
        super().__init__()
        self.maxlevel = 2            # 嵌套深度上限
        self.maxother = 24

    def repr_str(self, s, level):
        return "str<" + str(len(s)) + "字节>"    # 长字符串只报尺寸


def log_friendly(obj):
    return QuietRepr().repr(obj)


if __name__ == "__main__":
    print("原生 repr 会全量展开:", repr(list(range(40)))[:44], "……")
    print("reprlib 截断:", default_truncate())
    payload = {"users": ["u" * 500], "meta": {"deep": {"deeper": [1, 2, 3]}}}
    print("日志友好表示:", log_friendly(payload))
```

**追问**:1) reprlib 的省略号安全吗?——截断表示不再是合法表达式,不能 eval 回来;需要无损快照走 pickle/json,「表示」与「序列化」是两件事。2) Repr 的定制面?——Repr 实例按类型配置 maxdict/maxlist/maxlevel 等;repr(obj) 自动截断嵌套;aRepr.maxstring 控制长串;这是调试器/日志框架防「repr 卡死」的标准手段(Q513)。3) 与 sys.getsizeof 的配合?——repr 截断解决「打印太大」,深大小解决「占用多大」(Q556);两者都是把无限嵌套变成有限展示。4) 生产陷阱?——把截断表示存档当数据(信息已丢);repr 副作用对象进日志;调试大结构没配 reprlib 直接卡死。
