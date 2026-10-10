# 1011 atomic.Pointer 泛型 API 总览

> 分类：并发模型 | 难度：L3 | 题型：八股题 | 频率：高 | 关键词：**atomic.Pointer** / **go1.19** / **类型安全**

> 原文锚点：第 1~8 段「automatic 包对指针值提供 load/store/CS/swip 四种方法」

## 一句话总述
Go 1.19 引入泛型 `atomic.Pointer[T]`，提供 `Load/Store/Swap/CompareAndSwap` 四个类型安全方法，操作 `*T` 而非裸 `unsafe.Pointer`；旧写法用 `atomic.LoadPointer` 等配 `unsafe.Pointer`。一句话背法：**「Go1.19 引入泛型 atomic.Pointer[T]，四方法 Load/Store/Swap/CompareAndSwap 操作 *T，免 unsafe.Pointer 互转；旧写法用 LoadPointer」**。

## 面试官视角
这是考察"是否跟进了 go1.19 的原子指针泛型化"的题，而非停留在 unsafe 旧写法。
- **P5**：知道有四个方法。
- **P6**：说清泛型返回 `*T`、免转换。
- **P7**：知道旧 unsafe 写法与迁移代价。
- **红旗**：把 `atomic.Pointer[T]` 当 `atomic.Value` 用；在 go1.19+ 仍手搓 `unsafe.Pointer` 转换。
- **惊艳点**：`atomic.Pointer[T].Load()` 直接返回 `*T`，旧 `LoadPointer` 返回 `unsafe.Pointer` 需显式转 `[源码]` sync/atomic。

## 主问答
**Q（面试官原话）：** 指针值怎么原子操作？有几种方法？

**先铺垫（由浅入深第 1 层）**：在 Go 1.19 之前，原子操作指针只能拿 `unsafe.Pointer` 配 `atomic.LoadPointer` 等，每次都要类型断言，既丑又易错。1.19 的泛型 `atomic.Pointer[T]` 把类型钉死在编译期，彻底免转换。

1. **结论（第 2 层·机制）**：用 `atomic.Pointer[T]`（go1.19+），四个方法 Load/Store/Swap/CompareAndSwap 操作 `*T` `[源码]`。
2. **机制（第 3 层）**：泛型在编译期固化类型，`Load` 返回 `*T`、`Store` 收 `*T`，免去 `unsafe.Pointer` 互转与类型断言 `[源码]`。
3. **边界（第 4 层）**：go1.19 之前没有泛型版本，只能用 `atomic.LoadPointer(addr *unsafe.Pointer)` 等，返回值需 `(*T)(unsafe.Pointer(...))` 转换 `[源码]`。
4. **收益（第 5 层）**：类型安全减少 nil/类型错配 bug，是无锁结构首选（如原子换配置对象）`[经验]`。
5. **迁移（第 6 层）**：老代码维护要认 `LoadPointer`/`StorePointer`/`SwapPointer`/`CompareAndSwapPointer`；新代码一律 `atomic.Pointer[T]` `[经验]`。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 有几种方法 | 四方法 Load/Store/Swap/CAS | — |
| L2 | 泛型收益 | 免 unsafe 转换 | 停 L2：判 P5 |
| L3 | 旧写法 | unsafe.Pointer + LoadPointer | 停 L3：判 P6 |
| L4 | 何时用 | 无锁结构首选 | 停 L4：判 P6+ |
| L5 | 迁移代价 | 改写点 + 认旧 API | 停 L5：判 P7 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| Go 1.19 起 | 引入 `atomic.Pointer[T]` 泛型，四方法类型安全 |
| 旧写法 | `atomic.LoadPointer`/`StorePointer`/`SwapPointer`/`CompareAndSwapPointer` 配 `unsafe.Pointer` |
| 返回值 | 泛型 `Load()` 直接返回 `*T`；旧 `LoadPointer` 返回 `unsafe.Pointer` 需转 |
| 推荐 | 新代码用 `atomic.Pointer[T]`；维护老代码认 `LoadPointer` `[源码]` |
| 关联 | CAS 比地址见 1011；与 Value 区别见 1011；五方法语义见 1010 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync/atomic"
)

type User struct{ Name string }

func main() {
	var p atomic.Pointer[User]
	p.Store(&User{Name: "a"})
	u := p.Load() // *User，无需 unsafe.Pointer 转换
	fmt.Println("load:", u.Name)

	// 四方法类型安全
	old := p.Swap(&User{Name: "b"})
	fmt.Println("swap old:", old.Name)
	ok := p.CompareAndSwap(&User{Name: "b"}, &User{Name: "c"})
	fmt.Println("cas:", ok)
}
```

## 总结与追问预判
**背这三句就够**：① **Go 1.19 引入泛型 `atomic.Pointer[T]`**；② **四方法 Load/Store/Swap/CompareAndSwap 操作 `*T`**；③ **免 `unsafe.Pointer` 互转，类型安全**。
**预判追问**：
- 「CAS 比较什么？」→ 比地址非内容（见 1011 原子指针 CAS）。
- 「和 atomic.Value 怎么选？」→ 单指针用 Pointer，任意类型用 Value（见 1011 区别）。
- 「无锁结构首选？」→ 类型安全少 bug，配置热更新常用（见 1011 指针原子避免锁）。

## ⚠️ 原文纠错
原文使用历史写法 `atomic.LoadPointer`/`StorePointer`/`SwapPointer`/`CompareAndSwapPointer` 操作 `unsafe.Pointer`（对应 Go<1.19）。本卡按 Go 1.19+ 的 `atomic.Pointer[T]` 泛型类型安全 API 重写：源文「loadpoint/storepoint/swip/CS」即上述四个方法。结论与 API 行为一致，仅补充了版本边界（go1.19 引入泛型）。
