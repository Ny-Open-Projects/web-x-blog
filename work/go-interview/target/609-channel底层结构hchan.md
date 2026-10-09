# 609 channel 底层结构 hchan

> 分类：Go 并发 | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**hchan**/**环形缓冲区**/**qcount**/**sendx/recvx**
> 原文锚点：第 6~36 段「channel 底层数据结构…结构体字段含义」

## 一句话总述
channel 底层是 **hchan 结构体**：核心字段 `qcount`(元素数)/`dataqsiz`(缓冲容量)/`buf`(缓冲指针)/`elemsize`/`closed`/`sendx`/`recvx`(环形下标)/`recvq`/`sendq`(等待队列)/`lock`；`buf` 是**环形缓冲区(ring buffer)**，而非链表。

## 面试官视角
- 考察意图：是否真看过 `runtime/chan.go` 的 hchan，而非只背"channel 是引用类型"。
- 分档：P5 知 channel 有锁和缓冲；P6 能说出 hchan 主要字段；P7 能讲清环形缓冲 + 等待队列 + 锁的协作。
- 红旗答案：把 buf 说成"双向链表"、或不知道 sendx/recvx 是环形下标。
- 惊艳点：**纠正"双向链表"误传——Go 用环形缓冲(buf+sendx/recvx 模运算)，收发是 O(1) 环形移动** `[经验]`。

## 主问答
**Q（面试官原话）：** channel 底层数据结构是什么？
**A：**
1. **结论**：hchan 结构体 + 环形缓冲 + 两把等待队列 + 一把锁。
2. **机制**：`buf` 指向一块按 `elemsize` 连续排布的环形队列；`sendx`/`recvx` 是读写**环形下标**（到尾回绕）；`qcount` 记当前元素数，`dataqsiz` 是缓冲容量（0=无缓冲）。`recvq`/`sendq` 才是阻塞等待者的 sudog 双向链表。
3. **边界**：源称"双向链表 + 头尾取放"不精确——**收发走环形缓冲**，只有阻塞的等待者才用 sudog 链表管理。

**加分层：** hchan 定义在 `runtime/chan.go`；无缓冲 channel 的 buf 为 nil、dataqsiz=0。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | channel 是什么？ | 基础 | hchan 结构体 | P5 |
| L2 | 主要字段？ | 结构 | qcount/buf/lock | P6 |
| L3 | buf 是链表？ | 纠偏 | 环形缓冲 | P6 |
| L4 | sendx/recvx？ | 机制 | 环形下标 | P7 |
| L5 | 源码位置？ | 进阶 | runtime/chan.go | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0+（hchan 长期稳定） | 无 | 答"hchan: buf 环形缓冲 + qcount/dataqsiz/sendx/recvx + recvq/sendq + lock" |

## 关键代码
```go
// runtime/chan.go 节选
type hchan struct {
    qcount   uint            // 当前元素数
    dataqsiz uint            // 缓冲容量
    buf      unsafe.Pointer  // 环形缓冲起始地址
    elemsize uint16
    closed   uint32
    sendx    uint            // 下次发送的位置(环形)
    recvx    uint            // 下次接收的位置(环形)
    recvq    waitq           // 等待接收的 sudog 队列
    sendq    waitq           // 等待发送的 sudog 队列
    lock     mutex
}
```

## 总结与追问预判
hchan = 环形缓冲 + 等待队列 + 锁；源"双向链表"应纠正为环形缓冲。追问接"发送/接收流程"与"等待队列 sudog"。

## ⚠️ 原文纠错
1. 机翻崩坏词归一：`killcount`→**qcount**；`datacaresize`→**dataqsiz**；`buffer`→**buf**；`reservex`/`reervex`→**recvx**；`send的s`→**sendx**；`receivecill`→**recvq**；`senandlill`→**sendq**；`look`→**lock(mutex)**；`CHIN`/`CHAN`→**chan**；`嵌点go`→**chan.go**；`五杠九`→**5-9**(示例目录)。事实正确，仅术语崩坏，本卡已归一 `[经验]`。
2. **精度纠错（重要）**：原文称 channel "由一个双向链表和一个锁组成、头部取数据尾部加数据"——**不准确**。Go 实际用 **环形缓冲区(ring buffer)**：`buf` 指向环形队列，`sendx`/`recvx` 为环形下标，收发是 O(1) 环形移动；sudog 双向链表只用于管理**阻塞等待者**(recvq/sendq)，并非数据本体。
