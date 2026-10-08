# 1010 sync/atomic 五个方法的 API 语义：Store / Add / Load / Swap / CAS

> 分类：Go/并发 | 难度：L3 | 题型：对比题 | 频率：高 | 关键词：**sync/atomic**/**Store**/**Add**/**Load**/**Swap**/**CompareAndSwap**/**atomic.Value**/**unsafe.Pointer**
> 原文锚点：第 1~35 段「原子操作主要是通过 Go 对底层原子操作进行封装之后提供的 atomic 标准库来实现的，支持的类型包括 int32/int64/uint32/uint64/uintptr 以及 unsafe 包装的 pointer…第一个参数都需要传指针类型…原子操作是根据指针定位到这个值的内存地址」
> [边界] 本文只讲**五个方法的签名语义（参数与返回值）**：原子操作的本质与 CPU 指令见 `104-atomic-essence`，适用类型与保护范围见 `105-atomic-types-scope`，五个使用陷阱见 `104-atomic-pitfalls`，atomic 与锁的选型见 `105-atomic-vs-lock-when`，均不重述。

## 一句话总述
`sync/atomic` 只有五个动作，**务必分清各自返回什么**：**Store 无返回值**（纯写入）、**Load 返回当前值**、**Add 返回加完之后的新值**、**Swap 返回被替换掉的旧值**、**CompareAndSwap 返回是否替换成功（bool）**。所有方法的**第一个参数都是目标变量的指针**——原子操作靠这个指针定位内存地址再操作地址上的数据。

## 面试官视角
- 考察意图：这是**手写无锁代码的入场券**。CAS 的返回值/参数顺序搞反，写出来的自旋锁和无锁队列一定错。
- 分档：P5 知道有 atomic 包；P6 能背下五个方法名；P7 能**准确说出每个方法返回什么**（尤其 Add 返回新值、Swap 返回旧值）、能写出正确的 CAS 重试循环，并知道 **Go 1.19+ 推荐类型化 API**（`atomic.Int64`）而非老式函数调用。
- 红旗答案：「Swap 是把两个值互换」——**错**。Swap(addr, new) 是**写入新值并返回旧值**，是单向赋值，不是交换两个数。
- 惊艳点：主动补「**源码里的例子我跑过**：x=1 → Add(+1)=2 → Add(-1)=1 → Swap(2) 返回旧值 1 → CAS(3,4) 失败 false → CAS(2,3) 成功 true、x=3，与源码第 35/38 行输出完全一致」[实测]。

## 主问答
**Q（面试官原话）：** 用 atomic 做计数和状态位，Store/Add/Load/Swap/CAS 这几个分别怎么用，返回值是什么？

**A：**
1. **统一前提：第一个参数必须是指针**。原子操作要**按指针定位到目标值的内存地址**，再操作这块地址上的数据，所以传的一定是被操作值的地址 [源码]。
2. **Store（写）**：`atomic.StoreInt64(&x, 1)` —— 把值写进去，**没有返回值**。布尔类型也有对应的 `Store` [源码]。
3. **Add（增减）**：`atomic.AddInt64(&x, 1)` —— 第二个参数是**增量**，传**正数就是加、传负数就是减**（传 -1 即减一）。注意：**Add 返回的是加完之后的新值**，不是旧值 [实测]。
4. **Load（读）**：`atomic.LoadInt64(&x)` —— 返回当前值。并发读写同一个变量时，读也必须走 Load，**不能直接用 `x`**，否则不是原子读 [源码]。
5. **Swap（强制交换）**：`atomic.SwapInt64(&x, 2)` —— 把新值写进去，**返回被替换掉的旧值**。它和 Store 类似，但**多一个旧值返回值**，适合"抢占式替换并保留旧值"的场景 [源码]。
6. **CompareAndSwap（比较并交换，CAS）**：`atomic.CompareAndSwapInt64(&x, old, new)` —— 只有当前值**等于 old** 时才把它替换成 new，**成功返回 true、失败返回 false**。它不是"比较然后随便换"，而是**条件写入** [源码]。
7. **实测走一遍源码的例子**：初值 1 → `Add(+1)` 返回 2 → `Add(-1)` 返回 1 → `Swap(2)` 返回旧值 **1**、此时 x=2 → `CAS(3,4)` 因为当前是 2 ≠ 3 所以 **false**、x 仍是 2 → `CAS(2,3)` 匹配成功 **true**、x=3。与源码第 35/38 行的输出完全一致 [实测]。
8. **布尔类型也有完整三件套**：`atomic.Bool` 提供 Store / Load / Swap / CompareAndSwap（`atomic.Bool`） [实测]。
9. **还能存任意值：`atomic.Value`**。可以先 Store 一个结构体，再用 Swap 设新值（返回旧结构体），也支持 CAS。但**有硬约束**：前后必须是**同一个具体类型**，否则 panic [实测]。
10. **保护粒度是"变量级"**：原子操作能保护单个变量的原子性，性能比互斥锁高；但如果需要保证的是**一段代码**的并发安全，就必须用互斥锁或读写锁 [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 第一个参数为什么传指针？ | 机制 | 按指针定位内存地址 | P5 停 |
| L2 | Add 返回新值还是旧值？ | 精度 | 新值；Swap 才返回旧值 | P6 停 |
| L3 | CAS 失败时当前值变了吗？ | 语义 | 没变，原样保留 | P6 停 |
| L4 | atomic.Value 换类型会怎样？ | 边界 | panic，类型必须一致 | P7 停 |
| L5 | Go 1.19 之后推荐怎么写？ | 版本意识 | 类型化 API `atomic.Int64` | P7+ 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本 | 五个方法的函数式 API 均可用 | 老代码仍在大量使用 |
| **Go 1.19+** | 新增**类型化**类型：`Int64/Bool/Pointer[T]` 等 | **新代码优先用类型化 API**，编译期防误用 |
| Go 全版本 | `atomic.Value` 自 Go 1.4 起提供 | 存任意值，但禁换类型 |
| Go 全版本 | `uintptr` / `unsafe.Pointer` 支持原子操作 | 但 **unsafe.Pointer 没有 Add** |
| Go 1.26.5（本机实测） | 类型化 API 行为与函数式一致 | 迁移时语义无需改写 |
| 32 位平台注意 | 64 位原子操作要求 **8 字节对齐** | 结构体首字段放 64 位量的经典坑 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync/atomic"
)

type user struct{ Name string }

func main() {
	// ---- 1) 老式函数式 API：逐个确认返回值语义 ----
	var x int64
	atomic.StoreInt64(&x, 1) // Store：写入，无返回值
	fmt.Printf("Store 后 Load=%d\n", atomic.LoadInt64(&x))
	fmt.Printf("Add(+1) 返回新值=%d\n", atomic.AddInt64(&x, 1))   // → 2
	fmt.Printf("Add(-1) 返回新值=%d\n", atomic.AddInt64(&x, -1))  // → 1（传负即减）
	fmt.Printf("Swap(2) 返回旧值=%d, x=%d\n", atomic.SwapInt64(&x, 2), atomic.LoadInt64(&x))
	fmt.Printf("CAS(3,4) 失败=%v, x=%d\n", atomic.CompareAndSwapInt64(&x, 3, 4), atomic.LoadInt64(&x))
	fmt.Printf("CAS(2,3) 成功=%v, x=%d\n", atomic.CompareAndSwapInt64(&x, 2, 3), atomic.LoadInt64(&x))

	// ---- 2) Go 1.19+ 类型化 API：推荐写法 ----
	var counter atomic.Int64
	counter.Store(1)
	fmt.Printf("[类型化] Add(1)=%d Swap(9)=%d CAS(9,10)=%v\n",
		counter.Add(1), counter.Swap(9), counter.CompareAndSwap(9, 10))

	var flag atomic.Bool
	flag.Store(true)
	fmt.Printf("[类型化] Bool Load=%v Swap(false)=%v\n", flag.Load(), flag.Swap(false))

	// ---- 3) CAS 重试循环：无锁累加的正确写法 ----
	var n atomic.Int64
	for i := 0; i < 100; i++ {
		go func() {
			for {
				old := n.Load()
				if n.CompareAndSwap(old, old+1) { // 只有一个 goroutine 能成功
					return
				}
				// 失败说明被别人抢了，重新读一次再试
			}
		}()
	}

	// ---- 4) atomic.Value：类型必须一致，否则 panic ----
	var v atomic.Value
	v.Store(user{Name: "u"})
	v.Store(user{Name: "u1"}) // 同类型 OK
	fmt.Printf("[类型化] Value 同类型 OK: %+v\n", v.Load())
	defer func() {
		if r := recover(); r != nil {
			fmt.Printf("[实测] 换类型 panic: %v\n", r)
		}
	}()
	v.Store(123) // ← 换成 int，panic
}
```

> 验证（`[实测]` 输出，macOS / go1.26.5）：
> ```text
> Store 后 Load=1
> Add(+1) 返回新值=2
> Add(-1) 返回新值=1
> Swap(2) 返回旧值=1, x=2
> CAS(3,4) 失败=false, x=2
> CAS(2,3) 成功=true, x=3
> [类型化] Add(1)=2 Swap(9)=2 CAS(9,10)=true
> [类型化] Bool Load=true Swap(false)=true
> [类型化] Value 同类型 OK: {Name:u1}
> [实测] 换类型 panic: sync/atomic: store of inconsistently typed value into Value
> ```
> 前六行与源码第 35/38 行的输出逐行吻合，可作为"五个方法返回值"的对照基准。

## 总结与追问预判
- 一句话收尾：**Store 无声、Load 取当前、Add 给新值、Swap 给旧值、CAS 给成败**。
- 大概率被追的三问：① CAS 循环要不要加 `runtime.Gosched()`（一般不要，失败重读即可；真高竞争反而该换锁）；② 为什么 CAS 失败后必须重新 Load（旧值已过期，拿它再 CAS 永远失败）；③ `atomic.Value` 首次 Store 能不能是 nil（不能，nil 会导致后续 Load 拿不到东西）。
- 反向加分：主动说「**别用 atomic 保护多个变量的组合一致性**——那是锁的活」。

## ⚠️ 原文纠错
1. 源码称 Swap 是「将第一个参数的值与第二个参数的值进行交换」——**不准确**：`Swap(addr, new)` 是**写入新值并返回旧值**，单向赋值，不是两数互换 [实测]。
2. 源码未强调 **Add 返回的是加完之后的新值**（很多人误以为是旧值），实测 diff 一次即可确认 [实测]。
3. 源码称支持类型含「ICF 包装的 point」——规范写法是 **`unsafe` 包定义的 `unsafe.Pointer`**，且它**不支持 Add（原子增减）** [经验]。
4. 源码类型列举被音译为「int 三十二的六十四」等，规范为 **int32 / int64 / uint32 / uint64 / uintptr** [经验]。
5. 源码**完全没有提到 Go 1.19+ 的类型化 API**（`atomic.Int64` / `atomic.Bool` / `atomic.Pointer[T]`），这是当前推荐写法 [源码]。
6. 源码演示了 `atomic.Value` 存取结构体，但**未提类型一致的硬约束**——实测换类型直接 panic：`sync/atomic: store of inconsistently typed value into Value` [实测]。
