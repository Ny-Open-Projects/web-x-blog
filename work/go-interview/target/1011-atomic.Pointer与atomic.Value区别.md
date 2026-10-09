# 1011 atomic.Pointer 与 atomic.Value 区别

> 分类：并发模型 | 难度：L3 | 题型：对比题 | 频率：中 | 关键词：**atomic.Value** / **类型安全** / **容器并发**
> 原文锚点：第 70~80 段「atomic.Value 存任意类型，但不能解决 map 单 key 并发」

## 一句话总述
`atomic.Pointer[T]` 类型安全、专管单个指针；`atomic.Value` 存任意类型但要求类型一致且只能整体读写，无法解决 map 等容器"单 key"并发——两者解决不同层问题。

## 面试官视角
- 意图：能否根据"类型固定 vs 任意类型""单元素 vs 整体"选型。
- P5 知两者都免锁 / P6 说清 atomic.Value 类型一致约束与整体读写 / P7 知容器并发需内部加锁或分片。
- 红旗：以为 atomic.Value 能解决 map 并发（它只能整体换 map）；混用不同类型 Store 进同一 Value。
- 惊艳点：`atomic.Value.Store` 类型须与后续 Load 一致，否则 panic——而 `atomic.Pointer[T]` 编译期就卡死 `[源码]` sync/atomic。

## 主问答
**Q（面试官原话）：** atomic.Pointer 和 atomic.Value 怎么选？
**A：**
1. **结论**：类型固定且是单个指针 → `atomic.Pointer[T]`；需存任意/未知类型 → `atomic.Value`。
2. **机制**：atomic.Value 只能整体 Store/Load，对 map 只能换整张表，不能原子改单 key；Pointer 直接换一个 `*T`，粒度更细。
3. **边界**：atomic.Value 的 Store 类型必须恒定（首次决定，后不一致 panic）；它不解决容器内部并发，单 key 写入仍要锁 `[源码]`。
**加分层：** 用 atomic.Value 存 map 治标不治本，并发写单 key 照样竞态。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 区别 | 概念 | 类型/粒度 | 换题 |
| L2 | Value 约束 | 机制 | 类型一致 | 判 P5 |
| L3 | map 并发 | 边界 | 整体读写 | 判 P6 |
| L4 | 选型 | 权衡 | 固定用Pointer | 判 P6+ |
| L5 | 容器方案 | 实战 | 分片/内部锁 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.19 起（Pointer） | atomic.Value 长期存在 | 固定类型用 `atomic.Pointer[T]`，任意类型用 `atomic.Value` `[源码]` |

## 关键代码
```go
// 示意，未验证：atomic.Value 只能整体换 map，不解决单 key 并发
var v atomic.Value
m := map[string]int{"a": 1}
v.Store(m) // 之后 Load 必须也是 map[string]int，否则 panic
// 并发改 m["a"] 仍需额外锁，atomic.Value 管不了
```

## 总结与追问预判
- Pointer 管单个类型安全指针；Value 管任意类型整体；容器单 key 并发二者都不直接解决。
- 预判：指针原子 vs 锁 → 见 1011；对比 105。

## ⚠️ 原文纠错
原文第 70~80 段「atomic.Value 只能整体 Store/Load、不能解决 map 单 key 并发」表述准确，未发现错误。本卡补充一处源文未提的硬约束：`atomic.Value.Store` 首次写入的类型决定后续类型，类型不一致会 panic（go 运行时行为，长期稳定）`[源码]` sync/atomic。
