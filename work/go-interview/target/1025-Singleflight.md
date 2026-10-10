# 1025 Singleflight：请求合并与防缓存击穿

> 分类：Go 并发 | 难度：中 | 题型：原理+场景 | 频率：高 | 关键词：**singleflight、请求合并、缓存击穿、并发原语、Group**

> 原文锚点：第 1~11 段「singleflight 使用场景、缓存穿透、合并并发请求只穿透一次」

## 一句话总述
singleflight 是 Go 官方扩展并发原语，把「同一时刻、同一 key 的多个并发请求」合并成「只让一个真正执行」，其余请求直接复用其结果。典型场景：本地缓存未命中时海量并发请求同时打到数据库（缓存击穿/穿透），用它能让 DB 只被访问一次。一句话背法：**「singleflight = 同 key 并发合并成一次回源，专治缓存击穿」**。

## 面试官视角
singleflight 是 Go 并发高频题。考官看你能不能讲清「它解决什么（缓存击穿）」「怎么用（Group.Do + 同一 key）」「底层靠什么（map 合并 + WaitGroup 等待）」。能对比「它不等同于限流/批处理，只合并相同 key 的并发」说明理解到位。
- **P5**：说出定义与防缓存击穿场景。
- **P6**：讲清 `Group.Do(key, fn)` 用法与「同 key 才合并」。
- **P7**：点出底层 `map[key]*call` + WaitGroup，并区分「与限流/批处理不同」。

## 主问答
**Q（面试官原话）：** singleflight 是什么？解决什么问题？

**先铺垫（由浅入深第 1 层）**：缓存失效瞬间，大量并发请求同时打到回源函数（DB/下游），这就是缓存击穿/穿透；如果每请求都回源，DB 直接被打垮。singleflight 的思路是「同一时刻同一 key 只让一个人去回源，其他人搭车」。

1. **定位（第 2 层·机制）**：官方扩展库 `golang.org/x/sync/singleflight` 提供的请求合并原语，属于并发控制，**不是限流也不是批处理**。
2. **解决的问题（第 3 层）**：缓存未命中时大量并发同时回源造成穿透/雪崩；singleflight 让同 key 并发只回源一次。
3. **核心语义（第 4 层）**：对「同一 key」的一组并发调用，只有一个 goroutine 真正执行 fn，其余阻塞等待并拿到同一份返回值。
4. **边界（第 5 层·最常考）**：只合并「同时刻」的并发；若第一个请求已结束、第二个稍后才来，则各自执行（除非显式 `Forget` 重置，见同组 Forget 卡）。
5. **误用风险（第 6 层）**：key 设计过粗（如全站用同一 key）会把所有请求串行化到一个 fn，反而成瓶颈；key 设计决定合并粒度。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 解决什么？ | 同 key 并发只回源一次，专治缓存击穿 | — |
| L2 | 怎么用？ | `g.Do(key, fn)`，同 key 才合并 | 停 L2：说不清 Group.Do |
| L3 | 只合并同 key？ | 与限流不同，只合并相同 key 的并发 | 停 L3：与限流混淆 |
| L4 | 时序边界？ | 仅合并同时刻并发，错峰各自执行 | 停 L4：说不清仅并发合并 |
| L5 | 底层靠什么？ | `map[key]*call` + WaitGroup 等待 | 停 L5：说不清 map+wg |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| 所属包 | `golang.org/x/sync/singleflight`（标准库外，需 `go get golang.org/x/sync`） |
| 核心 API | `Do(key, fn) (v, err, shared)` / `DoChan(key, fn) <- chan Result` / `Forget(key)` |
| 合并粒度 | 同一 key 的并发（key 是合并判据） |
| 返回值 shared | `true` 表示本 goroutine 没执行 fn，是「搭车」拿到的结果 |
| 并发安全 | 内部 `mu sync.Mutex` 保护 `callGroup` map |
| Go 版本 | 与 Go 版本无关（x/sync 独立演进）；本项目实测 Go 1.26.5 |
| 生产建议 | 配合本地缓存使用；key 需带业务维度避免合并过粗 |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"
	"time"

	"golang.org/x/sync/singleflight"
)

var g singleflight.Group

// 模拟回源：每次调用计数，用来观察 fn 到底被执行了几次
var hits int

func fetch() (interface{}, error) {
	hits++
	return fmt.Sprintf("result-%d", hits), nil
}

func main() {
	// ① 20 个并发请求用同一个 key，fn 只执行 1 次（合并生效）
	var wg sync.WaitGroup
	for i := 0; i < 20; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			v, _, shared := g.Do("article-list", fetch)
			_ = v
			_ = shared
		}()
	}
	wg.Wait()
	fmt.Println("20 并发同 key，fn 执行次数:", hits) // 1

	// ② 不同 key 互不合并，各自执行
	g.Do("other-key", fetch)
	fmt.Println("换 key 后再 Do，fn 执行次数:", hits) // 2

	// ③ 第一个已结束、稍后来同 key：各自执行（除非 Forget 重置）
	g.Do("article-list", fetch)
	fmt.Println("错峰同 key，fn 执行次数:", hits) // 3（说明仅合并同时刻并发）

	_ = time.Second
}
```

## 总结与追问预判
**背这三句就够**：① **singleflight 把同 key 并发合并为一次回源**；② **专治缓存击穿/穿透**；③ **只合并同时刻并发，与限流/批处理不同**。
**预判追问**：
- 「具体怎么用？返回值是什么？」→ `g.Do(key, fn)` 返回 `(val, err, shared)`，shared 标是否搭车（见 1025 用法）。
- 「源码怎么保证只执行一次？」→ `map[key]*call` 记录进行中的调用 + WaitGroup 让其余等待（见 1025 源码）。
- 「合并结果能主动失效吗？」→ 用 `Forget(key)`（见 1025 的 Forget）。

## ⚠️ 原文纠错
1. 事实核校： [经验] singleflight 用于请求合并/防缓存击穿、同 key 并发只回源一次、与限流/批处理不同——均正确，本卡为准。
2. 崩坏词归一：源码将 Go/goroutine/singleflight/CyclicBarrier 等音译为多组崩坏词；本卡统一为规范术语。
3. 补强：本卡在第 5、6 层补「仅合并同时刻并发」「key 过粗反成瓶颈」两处边界，避免面试时把 singleflight 等同于全局串行。
