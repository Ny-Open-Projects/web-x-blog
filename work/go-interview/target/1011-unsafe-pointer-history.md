# 1011 历史写法 unsafe.Pointer 原子

> 分类：并发模型 | 难度：L3 | 题型：对比题 | 频率：低 | 关键词：**unsafe.Pointer** / **LoadPointer** / **go1.19 前**
> 原文锚点：第 9~22 段「用 unsafe 定义指针值，storepoint 把对象地址存入，loadpoint 取出再转引用」

## 一句话总述
Go 1.19 之前没有泛型原子指针，只能用 `atomic.LoadPointer/StorePointer/SwapPointer/CompareAndSwapPointer` 操作 `*unsafe.Pointer`，拿到的 `unsafe.Pointer` 须显式转回 `*T`——类型安全靠人肉保证。

## 面试官视角
- 意图：能否读懂老代码里的 `unsafe.Pointer` 原子写法，理解它与新泛型的映射。
- P5 知有四个 LoadPointer 等 / P6 说清 unsafe.Pointer 与 *T 互转 / P7 知新项目应迁移到 atomic.Pointer[T]。
- 红旗：把 `unsafe.Pointer` 当普通指针隐式用（转换必须显式）；以为历史写法有类型检查。
- 惊艳点：`(*T)(p)` 与 `unsafe.Pointer(t)` 是互转唯一合法桥；漏转或错转会编译不过或崩溃 `[源码]` unsafe。

## 主问答
**Q（面试官原话）：** 老代码里 atomic.LoadPointer 怎么用？
**A：**
1. **结论**：`atomic.LoadPointer(addr *unsafe.Pointer) unsafe.Pointer`，需 `(*T)(unsafe.Pointer(...))` 转回具体类型。
2. **机制**：底层操作的是 `*unsafe.Pointer`；`StorePointer` 写入、`CompareAndSwapPointer` 比地址，与泛型版语义一致。
3. **边界**：转换无编译期类型校验，写错 `*T` 运行期才暴露；go1.19+ 应优先 `atomic.Pointer[T]` 消除此类风险。
**加分层：** unsafe 转换零运行时开销，但把安全责任全压给开发者。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 有哪些 | 概念 | LoadPointer 等 | 换题 |
| L2 | 怎么转 | 机制 | unsafe 互转 | 判 P5 |
| L3 | 风险 | 边界 | 无类型检查 | 判 P6 |
| L4 | 迁移 | 权衡 | Pointer[T] | 判 P6+ |
| L5 | 崩溃排查 | 实战 | 错转定位 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go<1.19 主用 | go1.19 起推荐 `atomic.Pointer[T]` | 老代码认 `LoadPointer`；新代码用泛型 `[源码]` sync/atomic |

## 关键代码
```go
// 示意，未验证：go1.19 前的 unsafe.Pointer 原子写法
var ptr unsafe.Pointer
atomic.StorePointer(&ptr, unsafe.Pointer(&user))
u := (*User)(atomic.LoadPointer(&ptr)) // 显式转回 *User
```

## 总结与追问预判
- 旧写法 `*unsafe.Pointer` + LoadPointer 等，转换靠手；新代码改用 atomic.Pointer[T]。
- 预判：现代 API 总览 → 见 1011-atomic-pointer-intro。

## ⚠️ 原文纠错
原文整篇采用历史写法 `unsafe.Pointer` + `atomic.LoadPointer`/`StorePointer`/`SwapPointer`/`CompareAndSwapPointer`（对应 Go<1.19），API 行为描述正确，未发现事实错误。本卡点明：go1.19 起应迁移到 `atomic.Pointer[T]`；源文 `PTR` 零值为 nil（"new"系机翻）亦正确还原为指针零值 nil。
