# 610 channel 的创建、容量与零值

> 分类：Go 并发 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**make**/**nil channel**/**容量**
> 原文锚点：第 11~20 段「容量为零是非缓冲…零值用预声明的 leo…make 第二参是容量」

## 一句话总述
channel 零值是 `nil`（收发都永久阻塞）；非零 channel 必须用 `make` 创建，`make(chan T, n)` 的第二参数是容量，默认 0 即无缓冲，非零即缓冲。

## 面试官视角
- 考察意图：是否清楚 channel 必须 make、nil channel 的阻塞特性，以及容量参数的语义。
- 分档：P5 知 channel 要 make；P6 懂容量=0 无缓冲、nil 零值；P7 知 nil channel 在 select 中永不选中。
- 红旗答案：以为 channel 变量声明即可用（实际 nil 阻塞）；把容量说成"元素个数上限"误用。
- 惊艳点：**nil channel 在 `select` 中对应的 case 永远不被选中**——这一特性常被用来动态"关闭"某个分支 `[源码]`。

## 主问答
**Q（面试官原话）：** channel 怎么创建？容量是什么？
**A：**
1. **结论**：非零 channel 必须用 `make(chan T, cap)` 创建；第二参数 `cap` 是缓冲区容量，省略即 0（无缓冲），非零即缓冲。
2. **机制**：未 make 的 channel 变量是其**零值 `nil`**，对 nil channel 收发都会永久阻塞；`make` 才分配底层 `hchan` 结构 `[源码]`。
3. **边界**：`cap` 是"缓冲区可暂存的元素数上限"，不是总吞吐上限；capacity 固定后不可改，想扩容只能新建并迁移。

**加分层：** `nil` channel 在 select 中永不触发，可用来在运行期"禁用"某个 case（如控制是否监听某路信号）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | channel 要 make 吗？ | 基础 | 必须，否则 nil | P5 |
| L2 | 容量默认多少？ | 语义 | 0=无缓冲 | P6 |
| L3 | nil channel 收发？ | 零值 | 永久阻塞 | P6 |
| L4 | nil 在 select 中？ | 进阶 | 永不选中 | P7 |
| L5 | 容量能改吗？ | 深度 | 不可，需新建 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0+ | 无翻转 | 答"make 创建、第二参容量、零值 nil、nil 在 select 永不选中" |

## 关键代码
```go
var ch chan int        // 零值 nil
// ch <- 1             // 对 nil channel 写 → 永久阻塞
ch = make(chan int, 3) // 容量 3 的有缓冲 channel
ch <- 1
```

## 总结与追问预判
channel 必须 make，零值 nil 永久阻塞，容量是缓冲上限；nil 在 select 的妙用是动态禁用分支。追问接底层 hchan 深挖。

## ⚠️ 原文纠错
1. 原文"channel 类型的零值用预声明的 **leo** 来表示"——`leo` 是机翻崩坏，正确标识符是 **`nil`**；其余（非零 channel 必须 `make` 创建、第二参数是容量且默认 0）均准确 `[源码]`。
