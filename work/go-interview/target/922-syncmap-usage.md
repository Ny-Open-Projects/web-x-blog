# 922 sync.Map 的用法与它和普通 map 的五点区别

> 分类：Go 并发 | 难度：L2 | 题型：用法题 | 频率：高 | 关键词：**sync.Map、Store、Load、Range、LoadOrStore、LoadAndDelete、读写分离**

> 原文锚点：第 5~37 段「sync.Map 的使用非常简单，我们可以通过 Store 方法来存储键值对，读取的时候通过 Load 方法传入 key 来获取 value，如果 key 存在 ok 就是 true，不存在 ok 就是 false…遍历 map 我们可以使用 Range 方法…回调函数里面如果 return true 遍历就会继续，如果 return false 就会终止遍历…LoadOrStore 表示存在就返回原来的值，不存在就插入…LoadAndDelete 表示如果存在就删除这个 key 同时取出对应的 value」

## 一句话总述
`sync.Map` 是 Go 1.9 起标准库提供的**并发安全 map**，**声明即可用、无需初始化**，**可存不同类型的键值对**，但**只能通过指定方法读写**：`Store` 写、`Load` 读、`Delete` 删、`Range` 遍历、`LoadOrStore`（存在返回原值、不存在才插入）、`LoadAndDelete`（删除并返回原值）。它内部用**读写分离**减少锁操作，性能优于"普通 map + 锁"。

## 面试官视角
- 考察意图：是否真用过 `sync.Map`，尤其是 **`LoadOrStore` 的"已存在则不修改"语义**这个高频陷阱。
- 分档：P5 知道 `sync.Map` 并发安全；P6 能列出 `Store`/`Load`/`Range`；P7 能说清 **`LoadOrStore` 存在时不覆盖**、**`Range` 靠回调返回 bool 控制终止**、以及"**无并发冲突时优先用普通 map**"。
- 红旗答案：以为 `LoadOrStore` 会覆盖已存在的值（**不会**）；或以为 `sync.Map` 可以像普通 map 那样用 `m[k]` 下标访问。
- 惊艳点：`LoadOrStore` 实测——**key 已存在时传入新值也不会改写，返回的仍是旧值**，这是它常被误用的地方 `[源码]`。

## 主问答
**Q（面试官原话）：** `sync.Map` 怎么用？和普通 map 有什么区别？

1. **结论**：`sync.Map` 是 **Go 1.9 新增**的**并发安全 map**，**可以在多个 goroutine 之间安全地读取和更新数据，而不需要自己加锁**；用法上**只能通过指定方法读写** `[源码]`。
2. **基本读写**：**写入用 `Store`** 存键值对；**读取用 `Load`**，传入 key 取 value，**key 存在则 ok 为 true，不存在为 false**；**删除用 `Delete`** `[源码]`。
3. **遍历 `Range`**：**遍历用 `Range` 方法并配合一个回调函数**，回调参数是内部遍历出来的 key 与 value；**回调返回 `true` 表示继续遍历，返回 `false` 表示终止遍历**；**遍历结果是无序的** `[源码]`。
4. **`LoadOrStore`**：**存在就返回原来的值，不存在就插入**；返回的 `actual` 是**之前存储的该 key 对应的值**，`loaded` 表示**该 key 是否已存在**。**关键细节：key 已存在时不会修改数据**（实测传入新值 `v2` 后取到的仍是 `v1`）`[源码]`。
5. **`LoadAndDelete`**：**如果 key 存在就把它删除，同时取出对应的 value**；`existed` 表明该 key 是否存在 `[源码]`。
6. **与普通 map 的五点区别**：
   - **`sync.Map` 无需初始化，声明即可使用**；普通 map **必须先通过字面量或 `make` 初始化** `[源码]`。
   - **`sync.Map` 可以存储不同类型的数据**；普通 map 的**键和值类型在声明时必须指定，且所有键、所有值各自类型相同** `[源码]`。
   - **`sync.Map` 只能通过指定方法读写**；普通 map 可用下标 `[源码]`。
   - **性能**：`sync.Map` **对元素的访问使用了读写分离机制来减少锁操作**，**与普通 map 加锁实现相比性能更好、使用更简单** `[源码]`。
   - **选型**：**如果确定 map 不会存在并发冲突、或可以规避并发冲突，尽量优先使用普通 map**；**map 并发场景才考虑 `sync.Map`** `[源码]`。

**加分层：** `Range` 的终止依赖回调返回值而非 `break`——要在回调里 `return false` 才能中断，写惯 `for range` 的人很容易在这里踩坑。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | sync.Map 要 make 吗？ | 答出声明即用 |
| L2 | 怎么遍历？ | 答不出 Range + 回调 |
| L3 | 怎么终止遍历？ | 答不出 return false |
| L4 | LoadOrStore 存在时覆盖吗？ | 答出覆盖即错 |
| L5 | 什么时候该用普通 map？ | 答出无并发冲突时 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.9+ | 新增 `sync.Map` | 之前只能自己加锁 |
| Go 全版本 | 普通 map 非并发安全 | 并发写直接 fatal |
| Go 1.9+ | `LoadAndDelete` | 原子地取走并删除 |
| 所有版本 | 无冲突时优先普通 map | `sync.Map` 有额外开销 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	var m sync.Map // 无需初始化，声明即可用

	// 1) Store / Load
	m.Store(1, "v1")
	if v, ok := m.Load(1); ok {
		fmt.Println("load:", v) // v1
	}

	// 2) LoadOrStore：key 已存在时不覆盖，返回旧值
	actual, loaded := m.LoadOrStore(1, "v2")
	fmt.Println("actual:", actual, "loaded:", loaded) // v1 true —— 注意没有改成 v2

	// 3) 遍历无序；回调 return false 可终止
	m.Store(2, "v2")
	m.Store(3, "v3")
	m.Range(func(k, v any) bool {
		fmt.Println("range:", k, v)
		return k != 3 // 遇到 k==3 就终止
	})

	// 4) LoadAndDelete：删除并取出原值
	if v, existed := m.LoadAndDelete(1); existed {
		fmt.Println("deleted value:", v)
	}
	if _, ok := m.Load(1); !ok {
		fmt.Println("key 1 已删除")
	}
}
```

## 总结与追问预判
**最爱追问的是 `LoadOrStore` 与 `Store` 的差别**——`Store` 无条件覆盖，`LoadOrStore` **只在 key 不存在时写入**，因此它是实现"**只初始化一次**"语义（如懒加载缓存）的原子手段。追问常接"那为什么还要保留普通 map"——**`sync.Map` 为读写分离付出了额外结构与指针跳转成本**，无并发时纯属浪费；再往下就是实现原理（见 `922-syncmap-read-dirty`）。

## ⚠️ 原文纠错
1. 事实核校：`sync.Map` 为 Go 1.9 新增、无需初始化、可存不同类型、只能通过方法读写、`Store`/`Load`/`Delete`/`Range`/`LoadOrStore`/`LoadAndDelete` 语义、`Range` 回调返回 bool 控制继续或终止、遍历无序、`LoadOrStore` 已存在时不覆盖、读写分离优于 map 加锁、无冲突优先普通 map——均与 Go 标准库一致 `[经验]`。
2. 补充：`sync.Map` 的可存不同类型是因为其签名为 `any`（`interface{}`），**代价是编译期失去类型检查、并有装箱开销**；真实项目中优先用**泛型 + 互斥锁**或 `sync.Map` 配合类型断言 `[经验]`。
3. 崩坏词归一：源码将 sync.Map、goroutine、键值对、加锁、读写分离等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
