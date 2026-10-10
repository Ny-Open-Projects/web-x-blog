# 1011 atomic.Pointer 与 atomic.Value 区别

> 分类：并发模型 | 难度：L3 | 题型：对比题 | 频率：中 | 关键词：**atomic.Value** / **类型安全** / **容器并发**

> 原文锚点：第 70~80 段「atomic.Value 存任意类型，但不能解决 map 单 key 并发」

## 一句话总述
`atomic.Pointer[T]` 类型安全、专管单个指针；`atomic.Value` 存任意类型但要求类型一致且只能整体读写，无法解决 map 等容器"单 key"并发——两者解决不同层问题。一句话背法：**「atomic.Pointer[T] 类型安全管单指针；atomic.Value 存任意类型但须类型一致且整体读写，不解决 map 单key并发」**。

## 面试官视角
这是考察"按类型固定 vs 任意类型""单元素 vs 整体"选型的题。
- **P5**：知道两者都免锁。
- **P6**：说清 atomic.Value 类型一致约束与整体读写。
- **P7**：知道容器并发需内部加锁或分片。
- **红旗**：以为 atomic.Value 能解决 map 并发（它只能整体换 map）；混用不同类型 Store 进同一 Value。
- **惊艳点**：`atomic.Value.Store` 类型须与后续 Load 一致，否则 panic——而 `atomic.Pointer[T]` 编译期就卡死 `[源码]` sync/atomic。

## 主问答
**Q（面试官原话）：** atomic.Pointer 和 atomic.Value 怎么选？

**先铺垫（由浅入深第 1 层）**：两者都让你"免锁换数据"，但粒度不同。`Pointer[T]` 锁死一个具体指针类型，编译期就防错；`Value` 更灵活能存任意类型，但灵活带来运行时约束——类型一致性得自己保证。

1. **结论（第 2 层·机制）**：类型固定且是单个指针 → `atomic.Pointer[T]`；需存任意/未知类型 → `atomic.Value` `[源码]`。
2. **机制（第 3 层）**：atomic.Value 只能整体 Store/Load，对 map 只能换整张表，不能原子改单 key；Pointer 直接换一个 `*T`，粒度更细 `[源码]`。
3. **边界（第 4 层）**：atomic.Value 的 Store 类型必须恒定（首次决定，后不一致 panic）；它不解决容器内部并发，单 key 写入仍要锁 `[源码]`。
4. **选型（第 5 层）**：固定类型用 Pointer（类型安全、免断言）；任意类型/配置热更新用 Value（但首次类型定终身）`[经验]`。
5. **进阶（第 6 层）**：map/切片等容器"单 key 并发写"两者都不直接解决，需 `sync.Map`、分片或内部 Mutex（见 1011 指针原子 vs 锁）`[边界]`。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 区别 | 类型/粒度不同 | — |
| L2 | Value 约束 | 类型必须一致 | 停 L2：判 P5 |
| L3 | map 并发 | 只能整体读写 | 停 L3：判 P6 |
| L4 | 选型 | 固定用 Pointer | 停 L4：判 P6+ |
| L5 | 容器方案 | 分片/内部锁 | 停 L5：判 P7 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| Go 1.19 起 | `atomic.Pointer[T]` 泛型引入 |
| atomic.Value | 长期存在（Go 1.4+），任意类型但类型一致 |
| 选型 | 固定类型用 `atomic.Pointer[T]`，任意类型用 `atomic.Value` `[源码]` |
| 关联 | 泛型 API 见 1011；CAS 比地址见 1011；与锁选型见 105 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync/atomic"
)

func main() {
	// atomic.Pointer[T]：类型安全，管单个指针
	type User struct{ Name string }
	var p atomic.Pointer[User]
	p.Store(&User{Name: "a"})
	u := p.Load() // *User，无需转换
	fmt.Println("pointer load:", u.Name)

	// atomic.Value：存任意类型，但首次 Store 的类型决定后续类型（否则 panic）
	var v atomic.Value
	m := map[string]int{"a": 1}
	v.Store(m) // 之后 Load 必须也是 map[string]int
	got := v.Load().(map[string]int)
	fmt.Println("value load:", got)

	// atomic.Value 只能整体换 map，不解决单 key 并发
	// 并发改 m["a"] 仍需额外锁
}
```

## 总结与追问预判
**背这三句就够**：① **Pointer[T] 类型安全、专管单个指针**；② **Value 存任意类型但须类型一致、只能整体读写**；③ **容器单 key 并发二者都不直接解决（需锁/分片）**。
**预判追问**：
- 「Value 首次能存 nil 吗？」→ 不能，nil 会导致后续 Load 拿不到东西（见 1010）。
- 「指针 CAS 比什么？」→ 比地址非内容（见 1011 原子指针 CAS）。
- 「和锁怎么选？」→ 单变量原子、多变量组合用锁（见 105）。

## ⚠️ 原文纠错
原文第 70~80 段「atomic.Value 只能整体 Store/Load、不能解决 map 单 key 并发」表述准确，未发现错误。本卡补充一处源文未提的硬约束：`atomic.Value.Store` 首次写入的类型决定后续类型，类型不一致会 panic（go 运行时行为，长期稳定）`[源码]` sync/atomic。
