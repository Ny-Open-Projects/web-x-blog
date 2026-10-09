# 109 用 channel 串行化实现并发安全的 Slice

> 分类：Go/并发 | 难度：L3 | 题型：方案题 | 频率：中 | 关键词：**channel串行化**/**actor模型**/**request封装**/**匿名函数**/**run loop**
> 原文锚点：第 31~54 段「request 结构体封装操作(set 传索引+值/range 传 any 匿名函数)、run for-range 串行处理、range 转回函数遍历切片键值」

## 一句话总述
并发安全 slice 的第二种实现是 **channel 串行化（actor 模型）**：把所有对 slice 的操作封装成 `request` 结构体（set 操作传索引+值；range 操作把遍历函数以 `any` 存入 value），由单一 goroutine 的 `run` 循环 `for range` 读取 request **串行**执行——因不并发访问底层数组而天然安全。读频繁场景效率不如 RWMutex。

## 面试官视角
- 考察意图：能否用「单协程 + channel」把并发访问串行化，并理解 range 用匿名函数回调的 trick。
- 分档：P5 知 channel 可串行化；P6 能写 request+run 循环；P7 知 range 用 any 传函数、读多不如 RWMutex。
- 红旗答案：多个 goroutine 直接读 request channel 仍并发；range 不用回调却想拿到每元素。
- 惊艳点：点出「所有操作经一个 goroutine 串行、天然无竞争」，以及「range 把匿名函数塞进 value、处理时转回函数类型遍历键值」 [经验]。

## 主问答
**Q（面试官原话）：** 除了加锁，还能怎么让 slice 并发安全？
**A：**
1. **request 封装操作**：定义 `request` 结构体统一封装操作；set 传索引+值，range 把遍历函数以 `any` 存入 `value` [经验]。
2. **单协程 run 串行**：开 goroutine 跑 `run`，`for range` 读 request 串行处理 slice——不并发访问底层数组，天然安全 [经验]。
3. **range 回调 trick + 读多劣势**：range 时把匿名函数转回函数类型遍历切片键值；但读频繁场景串行化效率不如 RWMutex [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | channel 咋做？ | 思路 | 串行化访问 | P5 |
| L2 | 结构？ | 封装 | request+run | P6 |
| L3 | range 咋传？ | trick | any 存函数 | P6 |
| L4 | 读多？ | 选型 | 不如 RWMutex | P7 |
| L5 | 生产者多？ | 工程 | 单消费者瓶颈 | P7+ |

## 版本与兼容性
- 本卡只讲 channel 串行化；slice 非并发本质见 109、RWMutex 封装见 109 [边界]。
- channel 当锁/串行化见 609、actor 模型见并发模式——本卡只引不重述 [边界]。

## 关键代码

```go
// channel 串行化：所有操作经单 goroutine 串行执行，天然并发安全
type request struct {
    op    string
    index int
    value any // set 存值；range 存匿名函数
}
type ChanSlice struct {
    ch   chan request
    data []int
}
func (c *ChanSlice) run() {
    for r := range c.ch { // 单协程串行处理
        switch r.op {
        case "set":
            if r.index >= 0 && r.index < len(c.data) {
                c.data[r.index] = r.value.(int)
            }
        case "range":
            fn := r.value.(func(int, int)) // 转回函数类型遍历键值
            for i, v := range c.data {
                fn(i, v)
            }
        }
    }
}
// 调用方只往 c.ch 写 request，不直接碰 data —— 无竞争
```

## 总结与追问预判
channel 串行化是「以串行换安全」的典型 actor 思路，逻辑简单但单消费者成瓶颈。读多写少优先 RWMutex，写多或需统一审计可用 channel。

## ⚠️ 原文纠错
1. 事实核校： [经验] request 封装、单协程 run 串行、range 用 any 存匿名函数、读多不如 RWMutex——均正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（channel、协程、串行化、匿名函数、切片等）。
