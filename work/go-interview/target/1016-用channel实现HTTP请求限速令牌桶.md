# 1016 用 channel 实现 HTTP 请求限速（令牌桶）

> 分类：Go/并发 | 难度：L3 | 题型：方案题 | 频率：高 | 关键词：**channel限速**/**令牌桶**/**定时器写令牌**/**goroutine发起**/**协程池**
> 原文锚点：第 1~20 段「两常量(周期/峰值) + handleRequest 声明容量=rateLimit 的 channel + goroutine+timer 按速率写空 struct 令牌 + 处理前读 channel 放行」

## 一句话总述
用 channel 实现**令牌桶限流器**：声明一个容量等于「单位时间峰值」的 channel 当令牌桶，另开 goroutine 用定时器按 `周期/个数` 的速率向里写空 struct 令牌；处理请求前先从 channel 读令牌，有才放行、无则阻塞到定时器写入——天然等价于恒定速率限流。请求用 goroutine 发起、高并发配协程池防端口耗尽。

## 面试官视角
- 考察意图：能否把「限速」映射成「固定容量 channel + 定时写令牌」，并讲清为什么用 goroutine 发起。
- 分档：P5 知 channel 当令牌桶、定时写；P6 能写 handleRequest 读放行逻辑；P7 知 goroutine 发起避免耗时拖累速率、协程池防端口耗尽。
- 红旗答案：把速率限制说成「sleep 每秒」而非恒定令牌流；忽略请求耗时会拖慢实际速率。
- 惊艳点：点出「定时器按 周期/请求数 写令牌、读即消费，等价于令牌桶算法」，以及「请求耗时 > 间隔时必须 goroutine 发起否则速率被拉长」 [经验]。

## 主问答
**Q（面试官原话）：** 怎么用 channel 对 HTTP 请求做限速？
**A：**
1. **容量即令牌桶**：声明容量为 rateLimit（单位时间峰值）的 channel 当桶；另开 goroutine 用 timer，按 `周期/请求个数` 的速率向 channel 写空 struct 令牌 [经验]。
2. **读即放行**：处理请求前从 channel 读令牌，有令牌才放行，无令牌阻塞至 timer 写入——恒定速率限流 [经验]。
3. **goroutine 发起 + 协程池**：用 goroutine 发真实请求，避免单请求耗 1 秒把「1 秒 100 请求」拖成 1 秒 1 请求；高并发需协程池限制 goroutine 数，否则拥堵致本地端口耗尽 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | channel 咋限速？ | 映射 | 容量=桶+定时写 | P5 |
| L2 | 怎么放行？ | 逻辑 | 读令牌才放行 | P6 |
| L3 | 为啥 goroutine？ | 速率 | 耗时拖累速率 | P6 |
| L4 | 高并发坑？ | 工程 | 协程池防端口耗尽 | P7 |
| L5 | 分布式？ | 扩展 | Redis 令牌桶 | P7+ |

## 版本与兼容性
- 本卡只覆盖「channel 令牌桶限流」；最快响应模式见 1016、令牌桶 vs 信号量区分见 1016 [边界]。
- 信号量限并发见 1015、协程池见 711/`711-ants`、分布式限流见 108、微服务限流隔离见 158——本卡只引不重述 [边界]。

## 关键代码

```go
// channel 令牌桶限流：容量=峰值，goroutine 按速率写空 struct 令牌
const (
    rateLimitPeriod = time.Second // 限速时间段
    rateLimit       = 1           // 该时间段内最大请求数（例：1 秒 1 请求）
)

func handleRequest(reqCh chan interface{}) {
    quota := make(chan struct{}, rateLimit) // 容量=单位时间峰值，当令牌桶
    go func() {
        tick := time.NewTicker(rateLimitPeriod / rateLimit) // 按速率生成令牌
        for range tick.C {
            quota <- struct{}{} // 恒定速率写入令牌
        }
    }()
    for req := range reqCh {
        <-quota // 无令牌则阻塞，直到 timer 写入才放行
        go func(r interface{}) { // goroutine 发起，避免请求耗时拖累速率
            doHTTP(r) // 真实 HTTP 请求（生产应限协程池数量）
        }(req)
    }
}
```

## 总结与追问预判
channel 令牌桶是「单机固定速率」限流的最简实现。面试常追问「分布式多实例怎么一致」（答 Redis+令牌桶/滑动窗口）、「突发流量怎么缓冲」（漏桶/桶容量允许积压）。

## ⚠️ 原文纠错
1. 事实核校： [经验] 容量=峰值、定时写令牌、读即放行、goroutine 发起、协程池防端口耗尽——均正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（令牌、定时器、goroutine、协程池、通道等）。
