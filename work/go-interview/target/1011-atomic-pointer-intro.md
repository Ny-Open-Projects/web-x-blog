# 1011 atomic.Pointer 泛型 API 总览

> 分类：并发模型 | 难度：L3 | 题型：八股题 | 频率：高 | 关键词：**atomic.Pointer** / **go1.19** / **类型安全**
> 原文锚点：第 1~8 段「automatic 包对指针值提供 load/store/CS/swip 四种方法」

## 一句话总述
Go 1.19 引入泛型 `atomic.Pointer[T]`，提供 `Load/Store/Swap/CompareAndSwap` 四个类型安全方法，操作 `*T` 而非裸 `unsafe.Pointer`；旧写法用 `atomic.LoadPointer` 等配 `unsafe.Pointer`。

## 面试官视角
- 意图：是否跟进了 go1.19 的原子指针泛型化，而非停留在 unsafe 旧写法。
- P5 知有四个方法 / P6 说清泛型返回 `*T`、免转换 / P7 知旧 unsafe 写法与迁移代价。
- 红旗：把 `atomic.Pointer[T]` 当 `atomic.Value` 用；在 go1.19+ 仍手搓 `unsafe.Pointer` 转换。
- 惊艳点：`atomic.Pointer[T].Load()` 直接返回 `*T`，旧 `LoadPointer` 返回 `unsafe.Pointer` 需显式转 `[源码]` sync/atomic。

## 主问答
**Q（面试官原话）：** 指针值怎么原子操作？有几种方法？
**A：**
1. **结论**：用 `atomic.Pointer[T]`（go1.19+），四个方法 Load/Store/Swap/CompareAndSwap 操作 `*T`。
2. **机制**：泛型在编译期固化类型，`Load` 返回 `*T`、`Store` 收 `*T`，免去 `unsafe.Pointer` 互转与类型断言。
3. **边界**：go1.19 之前没有泛型版本，只能用 `atomic.LoadPointer(addr *unsafe.Pointer)` 等，返回值需 `(*T)(unsafe.Pointer(...))` 转换。
**加分层：** 类型安全减少 nil/类型错配 bug，是无锁结构首选。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 有几种 | 概念 | 四方法 | 换题 |
| L2 | 泛型收益 | 机制 | 免转换 | 判 P5 |
| L3 | 旧写法 | 边界 | unsafe.Pointer | 判 P6 |
| L4 | 何时用 | 权衡 | 无锁结构 | 判 P6+ |
| L5 | 迁移代价 | 实战 | 改写点 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.19 起新增 | go1.19 引入 `atomic.Pointer[T]` 泛型 | 新代码用 `atomic.Pointer[T]`；维护老代码认 `LoadPointer` `[源码]` |

## 关键代码
```go
// 示意，未验证：atomic.Pointer[T] 泛型用法（go1.19+）
type User struct{ Name string }
var p atomic.Pointer[User]
p.Store(&User{Name: "a"})
u := p.Load() // *User，无需转换
```

## 总结与追问预判
- `atomic.Pointer[T]` 四方法类型安全；旧版用 `unsafe.Pointer` + `atomic.LoadPointer`。
- 预判：CAS 比较的是什么 → 见 1011-atomic-pointer-cas。

## ⚠️ 原文纠错
原文使用历史写法 `atomic.LoadPointer`/`StorePointer`/`SwapPointer`/`CompareAndSwapPointer` 操作 `unsafe.Pointer`（对应 Go<1.19）。本卡按 Go 1.19+ 的 `atomic.Pointer[T]` 泛型类型安全 API 重写：源文「loadpoint/storepoint/swip/CS」即上述四个方法。结论与 API 行为一致，仅补充了版本边界（go1.19 引入泛型）。
