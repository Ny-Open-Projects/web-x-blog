# 1114 堆/互斥锁/阻塞 Profile

> 分类：性能与排障 | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**heap** / **allocs** / **mutex** / **block**
> 原文锚点：第 15~22 段、第 42~49 段「内存每千次分配采样、mutex 竞争默认关、block 记录阻塞」

## 一句话总述
heap/allocs 看内存分配、mutex 看锁竞争、block 看阻塞；heap 默认按字节率采样(`MemProfileRate`≈512KB)，mutex 由 `SetMutexProfileFraction` 开，默认都关；allocs 含已释放、heap 仅存活。

## 面试官视角
- 意图：是否分得清三类 profile 的采样对象与开启方式，知 allocs/heap 差异。
- P5 知三类名 / P6 说清默认关闭项与 heap 采样机制 / P7 知 allocs vs heap、误开 mutex 的代价。
- 红旗：以为 heap 默认每 1000 次分配采一次；以为 mutex rate=1 与内存分配有关。
- 惊艳点：`allocs` profile 含已释放对象、`heap` 仅当前存活；排查"分配多但存活少"看 allocs —— 验证 `runtime.MemProfile` `[源码]`。

## 主问答
**Q（面试官原话）：** 内存、互斥锁、阻塞这三类 profile 怎么采？有什么不同？
**A：**
1. **结论**：heap/allocs 记内存分配（默认按 `runtime.MemProfileRate`≈512KB 字节率采样）；mutex 记锁竞争、默认关；block 记 channel/锁/IO 阻塞时间 `[源码]`。
2. **机制**：mutex 用 `runtime.SetMutexProfileFraction(n)` 开（1=全采、0=关），与内存无关；可用 `pprof.Lookup("mutex")/("block").WriteTo(f,0)` 落盘；heap 是 `runtime.MemProfile` 的存活快照 `[源码]`。
3. **边界**：`allocs` 含已分配又释放的对象、`heap` 只含当前存活；二者都来自同一分配流但口径不同。
**加分层：** mutex 默认关是因为竞争采样有全局开销，只在怀疑锁瓶颈时开启。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 三类有啥 | 概念 | heap/mutex/block | 换题 |
| L2 | 谁默认关 | 机制 | mutex/block | 判 P5 |
| L3 | allocs vs heap | 边界 | 含释放vs存活 | 判 P6 |
| L4 | 怎么开mutex | 权衡 | SetFraction | 判 P6+ |
| L5 | 误开代价 | 实战 | 全局开销 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 `[源码]` | `MemProfileRate` 默认 512KB | heap 字节率采样；mutex 默认关需开 |

## 关键代码
```go
// 示意，未验证：开启 mutex 采样并落盘
// runtime.SetMutexProfileFraction(1) // 1=全采，0=关
// f, _ := os.Create("mutex.prof")
// pprof.Lookup("mutex").WriteTo(f, 0)
```

## 总结与追问预判
- heap 字节率采样、mutex 默认关、allocs 含释放 heap 仅存活。
- 预判：CPU 原理 → 见 1114；分析命令 → 见 1114。

## ⚠️ 原文纠错
原文第 15 段称堆采样"默认每千次分配采一次"，实际由 `runtime.MemProfileRate`（默认 512*1024 字节≈512KB）按字节率采样，并非按分配次数。第 43~45 段把 `SetMutexProfileFraction(1)` 描述为"每分配一次内存采一次"，互斥锁竞争采样比例与内存分配无关（rate=1 表示全采竞争事件，0 关闭）。allocs/heap 区别原文未提，已按 `runtime.MemProfile` 事实补入。核对范围：通读全文并重点核对采样率与 mutex 接口；仅做机翻解码（如 勾浪→Go 等），技术结论已更正两处。
