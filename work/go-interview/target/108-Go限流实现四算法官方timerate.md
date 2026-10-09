# 108 Go 限流实现（四算法 + 官方 time/rate）

> 分类：Go 并发 / 流量控制 | 难度：L3 | 题型：工程题 | 频率：高 | 关键词：**令牌桶** / **time/rate** / **漏桶** / **滑动窗口** / **固定窗口**
> 原文锚点：第 14~58 段「限流算法：固定窗口/滑动窗口/漏桶/令牌桶；官方 time/rate 用法；自实现 channel+ticker」

## 一句话总述
访问外部服务需限流防过载，常见四算法**固定窗口/滑动窗口/漏桶/令牌桶**；Go 官方 `golang.org/x/time/rate` 提供令牌桶：`rate.Limit` 设速率、`burst` 设桶容量、`Wait(ctx)` 在速率超限时阻塞（可超时放行）。

## 面试官视角
- 意图：是否会用限流保护下游，且能说清算法差异与官方库 API。
- 分档：P5 知令牌桶/漏桶；P6 能写 `rate.NewLimiter` + `Wait`；P7 能对比四算法优劣并自实现 channel+ticker。
- 红旗：把限流和"控制并发数"混为一谈；或只会 `time.Sleep` 硬控。
- 惊艳点：点出 `burst` 即桶容量，等价于信号量的权重——允许短时突发。

## 主问答
**Q（面试官原话）：** Go 里怎么给请求做限流？
**A：**
1. **四算法对比**：
   - 固定窗口：按时间片计数，实现简单但有窗口临界突刺（两窗口交界可双倍放行）。
   - 滑动窗口：细分时间片平滑临界，精度高、内存略增。
   - 漏桶：恒定速率出水，强制平滑、突发被削平，但无法应对合法突发。
   - 令牌桶：恒定速率放令牌、桶可积攒，能吸收短时突发——最常用。
2. **官方库**：`lim := rate.NewLimiter(rate.Limit(1), 3)` 表示每秒 1 个、桶容量 3（可突发 3）；`lim.Wait(ctx)` 在超限时阻塞，`ctx` 设超时则超时放行。
3. **自实现**：用 `time.Ticker` 按速率往带缓冲 `chan time.Time` 放令牌，请求侧从 channel 取令牌，取不到即受限。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 限流目的 | 基础 | 防下游过载 | P5 |
| L2 | 两算法 | 机制 | 令牌桶/漏桶 | P6 |
| L3 | 官方 API | 工程 | rate.Limit/burst/Wait | P6+ |
| L4 | burst 含义 | 演进 | 桶容量=允许突发 | P7 |
| L5 | 自实现 | 实战 | channel+ticker | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| golang.org/x/time/rate 长期稳定 | 无 | `rate.Limit` + `burst` + `Wait(ctx)` 长期成立 `[经验]` |

## 关键代码
```go
// 示意，未验证：官方令牌桶限流
import (
    "context"
    "time"
    "golang.org/x/time/rate"
)
lim := rate.NewLimiter(rate.Limit(1), 3) // 每秒 1 个，桶容量 3
for i := 0; i < 100; i++ {
    ctx, cancel := context.WithTimeout(context.Background(), time.Second)
    _ = lim.Wait(ctx) // 超限阻塞，超时放行
    cancel()
    go doRequest(i)
}
```

## 总结与追问预判
- 限流 = 控请求速率保护下游；令牌桶最常用，官方 `rate` 一行接入。
- 预判：分布式限流 → 见 108；微服务架构级限流 → 见 158。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词（如 另一排桶→令牌桶、硬排→令牌、扩大→channel/quota、牵l→请求、润景→程序、位置→Wait、tiken→Ticker），本卡统一为规范术语 `[经验]`。未做事实性更正。
