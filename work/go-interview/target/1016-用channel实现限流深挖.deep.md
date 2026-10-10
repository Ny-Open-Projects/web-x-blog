# 1016 用 channel 实现限流 深挖

> 覆盖源 10-16 全文：channel 令牌桶限速、goroutine 发起与协程池、最快响应与取消。主卡已拆成令牌桶实现、最快响应、令牌桶 vs 信号量三张，本附录做横向串联与取舍。

## 思路与架构

```mermaid
graph TD
A[channel 限流] --> B[令牌桶: 容量=峰值+定时写令牌]
A --> C[信号量: 容量=并发数]
B --> B1[读令牌才放行=限速率]
B --> B2[goroutine 发起+协程池防端口耗尽]
A --> D[最快响应: 容量1 channel]
D --> D1[只留最先返回]
D --> D2[close 广播取消其余]
D --> D3[真实 HTTP 用 context 取消]
```

## 方案取舍
- **令牌桶 vs 信号量**：令牌桶控「每周期请求数」、允许积存令牌短时突发；信号量只卡在飞数、不平滑速率。选型看要「多快」还是「多少」。
- **goroutine 发起**：必须，否则请求耗时拉长实际速率；但无协程池会堆积 goroutine、拥堵致本地端口耗尽。
- **最快响应 vs 限速**：两者都是 channel 妙用，前者竞速收敛（谁先谁赢）、后者恒定节流；生产常组合（限速发 + 竞速取）。

## 答题技巧
- 被问「channel 限速」先定位语义（速率 or 并发），再给实现，比直接甩代码显体系 [经验]。
- 主动边界到 `1015`(信号量)/`108`(分布式)/`158`(微服务限流)/`711`(协程池)，构成限流全栈 [边界]。

## 细节与核心 API

**令牌桶（控速率，允许积存令牌短时突发）vs 信号量（只卡在飞数）**：

```go
// 令牌桶：容量=峰值，定时写令牌；读令牌才放行=限速率
type TokenBucket struct{ tokens chan struct{}; tick *time.Ticker }
func NewTokenBucket(rate, burst int) *TokenBucket {
    tb := &TokenBucket{tokens: make(chan struct{}, burst)}
    for i := 0; i < burst; i++ { tb.tokens <- struct{}{} } // 预充突发额度
    tb.tick = time.NewTicker(time.Second / time.Duration(rate))
    go func() {
        for range tb.tick.C { select { case tb.tokens <- struct{}{}: default: } } // 满则丢弃
    }()
    return tb
}
func (tb *TokenBucket) Allow() bool {
    select { case <-tb.tokens: return true; default: return false } // 拿不到=限流
}

// 信号量：容量=并发数（不平滑速率，只限同时在飞）
sem := make(chan struct{}, N)
for i := 0; i < M; i++ { sem <- struct{}{}; go func() { defer func() { <-sem }(); doReq() }() }

// 协程池：防 goroutine 堆积致本地端口耗尽
pool := make(chan struct{}, maxConns)
for _, t := range tasks { pool <- struct{}{}; go func(t Task) { defer func() { <-pool }(); worker(t) }(t) }

// 最快响应：容量 1 channel 只留最先返回（buffer=1 写入不阻塞其余退出）
respCh := make(chan string, 1)
for _, u := range urls { go func(u string) { respCh <- fetch(u) }(u) }
first := <-respCh // 只取最先返回；真实 HTTP 改用 context 取消其余在飞请求
```

> 边界：信号量限并发见 1015；分布式限流见 108；微服务限流见 158；协程池见 711。
