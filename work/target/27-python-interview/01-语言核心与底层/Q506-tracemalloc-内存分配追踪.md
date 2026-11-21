---
title: [Q506] tracemalloc:内存分配追踪
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q506 · tracemalloc:内存分配追踪

> 难度:★★★★ | 标签:内存, 调试

**问**:RSS 涨了但对象不多,tracemalloc 能看到什么?快照对比怎么定位泄漏点?

**答**:tracemalloc 记录每次 Python 层分配的调用栈:take_snapshot 抓取当前全部分配,compare_to 对比两个快照给出「按行号增长最多的分配」,statistics 按文件/行聚合,get_traced_memory 给当前与峰值。工作流:服务启动后 start + 抓基线 → 运行一段时间再抓 → compare_to 排序看 top 增长行,基本能直接指认泄漏代码。开销不低(约 2 倍内存 + 时间),只用于排查不常驻;与 gc.get_objects(区分「对象泄漏」)和 objgraph(引用链)互补——tracemalloc 看内存,gc 看对象。

```python
# file: code/01_语言核心与底层/q506_tracemalloc.py
import tracemalloc

def allocate_big():
    return [bytes(1024) for _ in range(50)]      # 约 50 KB

if __name__ == "__main__":
    tracemalloc.start()
    before = tracemalloc.take_snapshot()

    keep = allocate_big()                         # 持有引用,模拟泄漏

    after = tracemalloc.take_snapshot()
    for stat in after.compare_to(before, "lineno")[:3]:
        print(stat)
    current, peak = tracemalloc.get_traced_memory()
    print("current KB:", current // 1024, "peak KB:", peak // 1024)
    tracemalloc.stop()
```

**追问**:1) tracemalloc 能看到 C 扩展的分配吗?——不能,它只追踪 Python 内存分配器层;numpy 大数组这类绕过 pymalloc 的分配要用 RSS 对比或 valgrind/massif 排查。2) 追踪的代价与控制手段?——给每次分配挂钩栈记录,速度大约减半、内存随 trace 表增长;start(nframe) 限制栈深,快照对比(take_snapshot + compare_to)定位增长点,用完必须 stop()。3) 底层挂钩位置?——记录发生在 pymalloc 分配路径(记录指针→大小+栈);CPython 分配器分层 obmalloc→malloc→mmap,tracemalloc 只覆盖最上层。4) 生产陷阱?——生产常开(慢且贵),应短窗口采样;把 numpy/PyTorch 显存增长误判为 Python 泄漏;忘了 stop 导致 trace 表常驻。
