# 810 手动触发 GC：runtime.GC 与 debug.FreeOSMemory 的区别

> 分类：Go 运行时 / GC | 难度：L3 | 题型：机制题 | 频率：中 | 关键词：**runtime.GC** / **debug.FreeOSMemory** / **同步串行** / **STW** / **归还 OS**
> 原文锚点：第 13~23 段「手动触发:runtime.GC/debug.FreeOSMemory；手动=同步串行、执行中调度停止；FreeOSMemory 还额外清扫堆、立即还内存给OS(不保证成功)；仅特定场景用(释放大量内存/测试)」

## 一句话总述
手动触发 GC 有两个入口：`runtime.GC()` 做一次完整同步 GC 周期（STW）；`debug.FreeOSMemory()` 在 GC 之后**再清扫一次堆、并立即把已回收内存归还操作系统**（不保证成功，OS 可能拒绝/延迟）。二者都是同步串行、会停调度；自动调度则是异步并发。手动触发仅用于释放大量内存、或测试验证回收行为。

## 面试官视角
- 意图：区分两个手动入口的语义差异，以及"手动"与"自动"的并发模型差别。
- P5 知两者都能手动触发；P6 知 FreeOSMemory 额外清扫并还内存给 OS、不保证成功；P7 知手动同步 STW、自动异步并发、何时才该手动调。
- 红旗：以为 FreeOSMemory 一定能把内存还给 OS；或生产里频繁手动 GC（反而拖慢）。
- 惊艳点：点出"Go 运行时会缓存已回收内存复用，FreeOSMemory 才强制还 OS" `[边界]` 见 810-gc-trigger-timing（触发四分类）、1006-setmemorylimit（软限制与回收）、811-go-runtime-allocator（内存复用）。

## 主问答
**Q（面试官原话）：** runtime.GC 和 debug.FreeOSMemory 有什么区别？
**A：**
1. **都是手动同步触发**：二者都强制触发 GC 且同步串行执行，期间 goroutine 调度停止（STW），与自动调度的异步并发不同。
2. **FreeOSMemory 额外还内存**：`runtime.GC()` 只做回收；`debug.FreeOSMemory()` 在 GC 之后还会清扫堆内存，并强制把已回收内存立即归还操作系统。
3. **不保证成功**：归还 OS 可能被操作系统拒绝或延迟，并非调用就一定生效。
4. **仅特定场景用**：程序要释放大量内存、或测试验证回收正确性时才手动调；多数情况运行时自动管理，无需手动。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 两个入口 | 基础 | GC / FreeOSMemory | 判 P5 |
| L2 | 后者额外做啥 | 差异 | 清扫+还 OS | 判 P6 |
| L3 | 还 OS 保证吗 | 陷阱 | 不保证成功 | 判 P6+ |
| L4 | 手动 vs 自动 | 并发 | 同步STW vs 异步 | 判 P7 |
| L5 | 何时手动调 | 边界 | 大量释放/测试 | 判 P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 所有版本 | 无 | 两者手动同步 STW；FreeOSMemory 额外还 OS 不保证 |

## 关键代码
```go
package main

import (
	"runtime"
	"runtime/debug"
)

func main() {
	// 1) 仅做一次完整 GC 周期（同步 STW）
	runtime.GC()

	// 2) GC 后再清扫，并尽量把已回收内存归还操作系统
	//    注意：OS 可能拒绝/延迟，不保证一定释放
	debug.FreeOSMemory()
}
```

## 总结与追问预判
- 手动触发 = 同步 STW；FreeOSMemory 在 GC 后额外清扫并还 OS（不保证）；仅大量释放/测试用。
- 预判：触发四分类 → 见 810-gc-trigger-timing；软限制与回收 → 见 1006-setmemorylimit；降频参数 → 见 810-reduce-gc-frequency；分配器复用 → 见 811-go-runtime-allocator。

## ⚠️ 原文纠错
源码将若干专有名词音译为崩坏词（英文术语错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：runtime.GC 同步完整周期、FreeOSMemory 额外清扫并还 OS 且不保证成功、手动同步 STW 自动异步并发、仅特定场景手动调——均正确，未做更正。
