---
title: [Q1570] join vs += :拼接方式的实测与选型
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1570 · join vs += :拼接方式的实测与选型

> 难度:★★★☆☆ | 标签:str, 性能, 拼接

**问**:循环拼字符串,join 与 += 到底谁快?CPython 的 += 优化在什么条件下失效?选型的工程准则?

**答**:join 与 += 的实测结论:片段是已知列表时 ''.join 最稳——一次分配总长缓冲,任何实现近似 O(n);CPython 的 += 有针对性特化(左值是唯一引用的局部串时原地扩容,近似 O(n),Q425 讲机制),但条件苛刻:多一个别名引用、挂在异常帧、非 CPython 实现都退化为 O(n²) 的反复重建。io.StringIO 适合流式逐步构造(边产边写),性能居中。选型准则:① 片段已知可迭代 → join;② 流式累积 → StringIO;③ 个位数次拼接 → f-string/+= 无所谓,可读性优先;④ 热路径先在目标版本实测(Q430 的 timeit 规范)再固化,别把 += 特化当跨平台保证。

```python
# file: code/01_语言核心与底层/q1570_join_vs_concat.py
import io
import timeit

PIECES = ["line-%04d\n" % i for i in range(4000)]


def by_join(parts):
    return "".join(parts)


def by_plus(parts):
    out = ""
    for p in parts:
        out += p                # CPython 特化路径:左值无别名
    return out


def by_stringio(parts):
    buf = io.StringIO()
    write = buf.write
    for p in parts:
        write(p)
    return buf.getvalue()


def by_plus_aliased(parts):
    out = ""
    alias = out                 # 多余引用让 refcount 恒大于 1
    for p in parts:
        out += p                # 特化失效:每轮新建字符串
    return alias, out


if __name__ == "__main__":
    assert by_join(PIECES) == by_plus(PIECES) == by_stringio(PIECES)
    n = 20
    t_join = timeit.timeit(lambda: by_join(PIECES), number=n) / n
    t_plus = timeit.timeit(lambda: by_plus(PIECES), number=n) / n
    t_io = timeit.timeit(lambda: by_stringio(PIECES), number=n) / n
    print("join     : %6.3f ms" % (t_join * 1000))
    print("+=       : %6.3f ms   # 唯一引用时享受原地扩容" % (t_plus * 1000))
    print("StringIO : %6.3f ms" % (t_io * 1000))

    # 别名破坏 += 特化:多一个引用就退化为反复重建
    t_alias = timeit.timeit(lambda: by_plus_aliased(PIECES), number=5) / 5
    print("+= 别名版: %6.3f ms   # 特化失效, 显著变慢" % (t_alias * 1000))

    alias, result = by_plus_aliased(PIECES)
    print("alias stays old:", alias == "",
          "| result correct:", result == by_join(PIECES))
```

**追问**:1) 生成器能直接喂 join 吗?——能,join 会先内部物化一遍再计算总长;片段本身就是列表时 join 最省,两次遍历成本可以忽略。2) 实测选型结论?——大量片段:join(一次精确分配);少量插值:f-string(编译期字节码);流式不可知总量:io.StringIO;CPython 的 += 在 refcount==1 时有原地优化但不可移植(Q1264)。3) 测量方法?——timeit 取 min 对比;注意量级切换点(几段 vs 几十万段);3.11+ 特化让小拼接差距进一步缩小。4) 生产陷阱?——对巨型生成器 join(先物化,内存峰值=全量);循环内 += 在非 CPython 或多引用场景 O(n²);为「看起来快」牺牲语义清晰度。
