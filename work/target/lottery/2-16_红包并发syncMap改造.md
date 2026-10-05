# Go 企业级抽奖项目: 红包并发安全问题与 sync.Map 改造

## 纲要

- 压测发红包时发现金额分配不均衡，需按红包数量分级调整随机上限 `rmax`（>1000→0.01，>100→0.1，>10→0.3，否则 0.55）。
- 直接对普通 `map` 做并发读写会触发 `fatal error: concurrent map read and write`，必须改造为线程安全结构。
- 除互斥锁外，可用 `sync.Map` 替代普通 `map`：`sync.Map` 内部基于 `atomic.Value` 实现，适合"读多写少"场景。
- `sync.Map` 接口与普通 `map` 不同：`Range`（回调遍历）、`Store(key, value)`、`Load(key)`、`Delete(key)`，需相应改造读写删逻辑。
- 当红包集合达到千万级时 `sync.Map` 效率会相对偏低，需结合后续散列拆分优化。

## 金额分配的均衡优化

基础随机算法（`rmax=0.55`）在红包数量较大时容易让金额"一边倒"。解决办法是按红包个数分级收紧随机上限：数量越多，单个红包能拿走的比例越小，整体更均衡。

```go
// AdjustRmax 根据红包个数调整随机上限，使分配更均衡
func AdjustRmax(num int) float64 {
	switch {
	case num > 1000:
		return 0.01
	case num > 100:
		return 0.1
	case num > 10:
		return 0.3
	default:
		return 0.55
	}
}
```

调小 `rmax` 后重新压测，分布会比"全靠 0.55"更平缓。

## 普通 Map 的并发危机

压测未做并发保护的发红包接口时，会直接报错——Go 的普通 `map` 不是线程安全的，并发读写会触发 `fatal error`。下面这段来自课程 `_demo/threadsafe/mainMap.go` 的示例，直观对比了"不安全"与"加互斥锁安全"两种写法。

```go
/**
 * 并发编程，map的线程安全性问题
 */
package main

import (
	"fmt"
	"sync"
	"time"
)

var data map[int]int = make(map[int]int)
var wgMap sync.WaitGroup = sync.WaitGroup{}
var muMap sync.Mutex = sync.Mutex{}

func main() {
	// 并发启动的协程数量
	max := 100000
	fmt.Printf("map add num=%d\n", max)
	wgMap.Add(max)
	time1 := time.Now().UnixNano()
	for i := 0; i < max; i++ {
		go modifyNotSafe(i)
	}
	wgMap.Wait()
	time2 := time.Now().UnixNano()
	fmt.Printf("map len=%d, time=%d ms\n", len(data), (time2-time1)/1000000)

	// 覆盖后再执行一次
	data = make(map[int]int)
	fmt.Printf("new map add num=%d\n", max)
	wgMap.Add(max)
	time3 := time.Now().UnixNano()
	for i := 0; i < max; i++ {
		go modifySafe(i)
	}
	wgMap.Wait()
	time4 := time.Now().UnixNano()
	fmt.Printf("new map len=%d, time=%d ms\n", len(data), (time4-time3)/1000000)
}

// 线程不安全的方法
func modifyNotSafe(i int) {
	data[i] = i
	wgMap.Done()
}

// 线程安全的方法，增加了互斥锁
func modifySafe(i int) {
	muMap.Lock()
	data[i] = i
	muMap.Unlock()
	wgMap.Done()
}
```

`modifyNotSafe` 在十万并发下几乎必然触发 `concurrent map writes`；`modifySafe` 通过 `sync.Mutex` 加锁后则安全，但最终 `len(data)` 能稳定等于并发数。注意：加锁版本虽安全，但锁竞争会拖慢性能。

## 改用 sync.Map

`sync.Map` 内部用 `atomic.Value` 存储和读取数据，对外提供的是另一套接口。它适合"大量并发读、少量写入"的场景；但如果 `packageList` 非常大（如一千万红包），其效率会相对偏低，此时再结合散列拆分更有效。

将红包集合从普通 `map` 改为 `sync.Map` 后，读写删都要相应改造：

```go
package main

import (
	"fmt"
	"sync"
)

// PackageList 线程安全的红包集合
var PackageList sync.Map // key=int(红包ID), value=[]int(金额切片)

// StorePacket 写入红包
func StorePacket(id int, amounts []int) {
	PackageList.Store(id, amounts)
}

// LoadPacket 读取红包，返回切片与是否存在
func LoadPacket(id int) ([]int, bool) {
	v, ok := PackageList.Load(id)
	if !ok {
		return nil, false
	}
	return v.([]int), true
}

// SumPackets 遍历汇总所有红包数量与总金额（回调式 Range）
func SumPackets() (count, money int) {
	PackageList.Range(func(key, value interface{}) bool {
		count++
		for _, m := range value.([]int) {
			money += m
		}
		return true // 返回 false 可提前终止遍历
	})
	return
}

// DeletePacket 删除空红包
func DeletePacket(id int) {
	PackageList.Delete(id)
}
```

改造要点：

- 遍历：`sync.Map` 没有 `for range`，改用 `Range(func(key, value interface{}) bool)` 回调，回调内做类型断言 `value.([]int)`。
- 写入：`Store(key, value)`，不再是 `m[key] = v`。
- 读取：`Load(key)` 返回 `(value, ok)`，需类型断言后才能使用。
- 删除：`Delete(key)`。

## API 速览

- `AdjustRmax(num int) float64`：按红包数量分级返回随机上限系数。
- `sync.Map.Store(key, value)` / `Load(key)` / `Range(f)` / `Delete(key)`：线程安全集合的增、查、遍历、删。
- `SumPackets() (count, money int)`：基于 `Range` 汇总红包个数与总金额。

## Demo 示例

运行说明：`mainMap.go` 可直接 `go run` 复现"普通 map 并发崩溃 vs 互斥锁安全"的对比；`sync.Map` 示例则需替代原 `packageList` 后配合发/抢红包接口联调。

代码说明：`sync.Map` 用原子值实现读多写少的高效并发，但接口与普通 `map` 不兼容，所有读写删都要改写；大规模集合建议叠加散列拆分。

技术点总结：并发集合有两套成熟方案——互斥锁（通用但竞争重）与 `sync.Map`（读多写少高效）。选型的依据是读写比例与集合规模。

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/lottery/_demo/threadsafe/mainMap.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：95%。是否需要继续：是。代码是否可运行：是。
