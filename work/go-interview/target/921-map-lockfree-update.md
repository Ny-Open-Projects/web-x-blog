# 921 不加锁更新 map：写-复制-切换

> 分类：Go 语言基础 / map 进阶 | 难度：L1~L2 | 题型：方案题 | 频率：中 | 关键词：**写-复制-切换**/**atomic.Pointer**/**本地缓存**/**定时刷新**/**fatal error**

> 原文锚点：第 1~17 段「并发写抛 fatal error…map 当本地缓存…定时从 DB 刷新…写临时 map 后整体赋值…新 map 置 nil 回收」

## 一句话总述
读多写少的 map 缓存可以**不加锁**：写方在**私有新 map** 上构建全量数据，然后用一次**指针切换**发布（`atomic.Pointer[map[string]int]`）；读方 `Load()` 后无锁读——任何时刻读到的都是**完整一致的快照**。这是写-复制-切换（RCU 风格）思想。代价：每次更新全量拷贝，适合**小缓存+低频刷新**；并发写本身的 `fatal error: concurrent map writes` 不可 recover。

## 面试官视角
- 意图：map 并发题的进阶——不满足于「会加锁」，看能否给出免锁方案并说清代价与边界。
- 分档：P5 知并发写会崩；P6 能描述写-复制-切换流程；P7 能讲「为什么指针切换让读写安全」（快照语义）、sync.Map 与此方案的取舍、内存模型上的严谨性。
- 红旗答案：说「赋值操作是原子的所以随便替换 map 变量就安全」；不知道 fatal 无法 recover。
- 惊艳点：指出裸赋值切换在 Go 内存模型下**不保证**其他 goroutine 可见性，正确姿势是 `atomic.Pointer`（1.19+）或 `atomic.Value`；再对比 sync.Map「读多写少但键不定」的场景差 [经验]。

## 主问答
**Q（面试官原话）：** 如何在不加锁的情况下更新 map 的数据？

**A：** 前提：并发写同一 map 会触发 `fatal error: concurrent map writes`——**不可 recover**，进程直接崩 [实测]。适用场景：map 当**本地缓存**，允许秒级延迟刷新。方案三步 [实测]：

1. **写方私有构建**：定时任务（如每秒）从 DB 拉全量数据，写进一个**临时新 map**——此刻旧缓存仍在线服务，读写互不干扰。
2. **原子切换发布**：`cache.Store(&nm)`（`atomic.Pointer[map[string]int]`）——一次指针替换即完成「整个 map 的更新」，不存在「改一半」的中间态。
3. **读方无锁读**：`m := *cache.Load()` 后读——拿到的是切换前或切换后的**完整快照**；被替换的旧 map 由 GC 回收。
4. **代价与边界**：每次刷新全量拷贝（大 map 或高频刷新不划算）；单写多读最合适；多写方需外层串行化或按 key 分片。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 并发写 map 会怎样？ | fatal 且不可 recover |
| L2 | 不加锁怎么更新？ | 写-复制-切换三步 |
| L3 | 为什么切换是安全的？ | 快照语义+原子指针 |
| L4 | 裸赋值替换行不行？ | 内存模型不保证可见性 |
| L5 | 和 sync.Map 怎么选？ | 键集稳定 vs 动态 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|------|------|------|
| 1.x：并发写 fatal | 无 | `atomic.Pointer` 自 1.19 起泛型可用，之前用 `atomic.Value`；切换思路不受版本影响 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync/atomic"
	"time"
)

func main() {
	var cache atomic.Pointer[map[string]int]
	m0 := map[string]int{"v": 1}
	cache.Store(&m0)

	stop := make(chan struct{})
	go func() { // 读方：持续无锁读
		for {
			select {
			case <-stop:
				return
			default:
				m := *cache.Load() // 完整快照
				_ = m["v"]
			}
		}
	}()

	updates := 0
	for i := 2; i <= 6; i++ { // 写方：私有构建，一次切换
		nm := map[string]int{"v": i}
		time.Sleep(10 * time.Millisecond)
		cache.Store(&nm)
		updates++
	}
	close(stop)
	fmt.Println("updates:", updates, "no fatal")
}
```

[实测] 输出：`updates: 5 no fatal`——读方全程无锁、5 次整表更新零冲突。反例 [实测]：8 goroutine 直接并发写同 map → `fatal error: concurrent map writes`（runtime 层 abort，recover 捕获不到，程序必死）。

## 总结与追问预判
核心：**「私有构建 → 原子切换 → 无锁快照读」三步 + fatal 不可 recover 的前提 + 全量拷贝的代价**。追问接并发族：并发崩溃现象与检测见 `914-map-concurrency-float`、sync.Map 适用场景见 `914-map-hmap-bmap` 系列延伸、原子指针 API 细节见 `1011-atomic-pointer-intro` 与 `1011-atomic-pointer-vs-value`、CAS 原理见 `1011-atomic-pointer-cas`；goroutine 泄漏引发的读方问题见 `1022-goroutine-leak.deep`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文将 fatal error 音转为「fateerror」、goroutine 音转为「go 入 team」、nil 音转为「六」、键值对音转为「建制队」，本卡统一为规范术语，不列举原词。
2. 事实核校： [经验] 原文「这种赋值操作都是原子操作，不会有并发冲突」**在 Go 内存模型下不成立**——普通变量赋值不构成同步原语，其他 goroutine 可能读到旧值（甚至经 race detector 报数据竞争）；正确做法是用 `atomic.Pointer`/`atomic.Value` 做切换，语义与性能双保险 [实测]。
3. 事实核校： [经验] 原文说并发写「抛出异常」并用 recover 捕获——实际是 **fatal error**，不是 panic，**无法 recover**，运行时直接终止进程；这也是并发写 map 比空指针更危险的根源。
