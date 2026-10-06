# 815 p 的 GC / 定时器 / 抢占字段

> 分类：并发模型 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**gcw** / **timers** / **preempt** / **pad移除**
> 原文锚点：第 118~149 段「GCassistanttime 表示辅助分配花费的纳秒…pad 字段在 go1.20 已移除」

## 一句话总述
P 持 GC 辅助字段(gcAssistTime/gcMarkWorkerMode/gcw 写屏障缓冲)与定时器切片(timers，访问需 timelock)；preempt 标 P 应立即让出调度以保公平；旧的 pad 填充字段已在 go1.20 移除（结构体已缓存行对齐）`[源码]` runtime2.go。

## 面试官视角
- 考察意图：是否知道 P 还承载 GC 与定时器
- P5 知道 p 有 gcw/timers / P6 讲清 timelock 防并发 / P7 讲 preempt 实现抢占式调度
- 红旗：认为 timers 无锁可并发改；答不出 pad 为何被删
- 惊艳点：P 的 preempt 置位即"立刻进调度器"，即便当前 G 没跑完，防单 G 饿死其他 G `[源码]` runtime/proc.go

## 主问答
**Q：** P 上那些 GC/定时器/抢占字段干嘛？
**A：**
1. **GC 组**：gcAssistTime 记辅助分配纳秒，gcMarkWorkerMode 设标记模式，gcw 是写屏障缓冲 `[源码]`。
2. **timers + timelock**：timers 是定时器切片，增删须持 timelock 防竞态 `[源码]`。
3. **preempt / pad**：preempt 置位即立刻让出调度；pad 伪共享填充字段因结构体已对齐而在 go1.20 移除 `[源码]`。
**加分层：** preempt 是"协作式检查点"触发的入口，配合 G 的 stackguard0 完成抢占。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | gcw 是什么 | 概念 | P 的 GC 写屏障缓冲 | 换题 |
| L2 | timers 为何加锁 | 机制 | 防并发改切片 | 判 P5 |
| L3 | preempt 干嘛 | 边界 | 立即让出调度 | 判 P6 |
| L4 | pad 为何删 | 权衡 | 结构体已对齐、省内存 | 判 P6+ |
| L5 | 定时器性能调优 | 实战 | 看 timers 长度 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| pad 移除版本 `[存疑]` | 原文称"go1.20 移除 pad"，pad 具体引入/移除版本待核 `[存疑]` | 答"preempt 立即让出、pad 因对齐移除"并标存疑 |

## 关键代码
```go
// 示意，未验证：p 的 GC/定时器/抢占字段（节选）
type p struct {
	gcAssistTime     int64    // 辅助分配花费纳秒
	gcMarkWorkerMode int32    // 标记工作器模式
	gcw              gcWork   // 写屏障缓冲
	timers           []*timer // 定时器切片
	preempt          bool     // 立即让出调度
}
```

## ⚠️ 原文纠错
原文第 133~137 段称"pad 填充字段在 go1.20 已移除，用于解决伪共享"，方向正确(现代 p 结构体已足够大、缓存行对齐，无需 pad)；但"go1.20"这一具体版本号未核实，标 `[存疑]`，不臆断确切版本。

## 总结与追问预判
- P 承载 GC 辅助(gcw)、定时器(timers+timelock)与抢占(preempt)；pad 因对齐移除。
- 回顾「GMP 三者关系」见 813-gmp-model-overview。
