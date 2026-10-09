# 1025 Singleflight 的 Forget：手动让「合并结果」失效

> 分类：Go 并发 | 难度：中 | 题型：用法 + 原理 | 频率：中 | 关键词：**Forget、合并项失效、map 删除、重新回源、Group**

> 原文锚点：第 60~61 段「Forget 提供覆盖方法、删除 map 的 key、后续同 key 重新执行 fn」

## 一句话总述
**`Forget(key)` = 把 Group 里该 key 的合并记录删掉，让下一波同 key 请求重新回源执行 fn**。一句话背法：**「Forget 删记录、不掐进行中、之后重新跑」**。它解决的是「合并结果被长期复用、需要主动失效」的问题，常与缓存主动失效搭配。

## 面试官视角
这是**易被忽略的细节题**，考官用它区分「用过 singleflight」和「真懂 singleflight」：
- P5 答「Forget 删除 map 项」；
- P6 要补**关键边界：它不取消正在进行中的请求，只影响「之后的」调用**；
- P7 会主动说出**误用风险**（频繁 Forget → 合并失效 → 回到缓存击穿），并讲清与「缓存 TTL / 主动失效」的配合。
- **红旗答案**：以为 Forget 会「取消正在执行的请求」——这是最常见的错答。

## 主问答
**Q（面试官原话）：** singleflight 的 Forget 是做什么的？什么时候用？

**先铺垫（由浅入深第 1 层）**：singleflight 的作用是**合并同一个 key 的并发请求**——同一时刻只让一个请求真正执行 fn（回源），其余请求等待并复用结果，用来防缓存击穿。这个「正在合并/已合并」的记录存在 `Group.m` 这个 map 里。

1. **行为（第 2 层·机制）**：`g.Forget(key)` 就是**从 `Group.m` 这个 map 里删除该 key 对应的 call 记录**（源码就三步：加锁 → `delete(g.m, key)` → 解锁）。
2. **直接效果（第 3 层）**：删掉之后，后续再来相同 key 的 `Do` 调用，在 map 里查不到记录，于是**重新创建一个 call、重新执行一次 fn**（重新回源），而不是复用上一次的结果。
3. **关键边界（第 4 层·最常考）**：**Forget 不会影响「正在进行中」的请求**。若此刻正有同 key 的请求在执行，Forget 不会中断、不会取消它，只影响**它之后**才发起的调用。
4. **适用场景（第 5 层）**：结果有时效、希望**周期性重新回源**（如缓存 TTL 很短），或缓存主动失效后**强制刷新**；典型写法是「回源成功 → 写缓存 → `Forget(key)`」，让之后的请求走新缓存而非一直复用旧合并结果。
5. **误用风险（第 6 层）**：无脑高频调用 Forget 会让**合并保护失效**——同 key 请求不再被合并，等于退回「每个请求都回源」，缓存击穿防护形同虚设。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | Forget 做什么？ | 删掉 Group map 里该 key 的合并记录 | — |
| L2 | 删了之后会怎样？ | 后续同 key 的 Do 查不到记录 → 重新执行 fn 回源 | 停 L2：说不清「重新回源」 |
| L3 | 会取消正在跑的请求吗？ | **不会**，只影响之后发起的调用 | 停 L3：答成「会取消」（最常见错答） |
| L4 | 典型怎么用？ | 回源成功→写缓存→Forget，让后续走新缓存；或配合短 TTL 周期回源 | 停 L4：说不清与缓存失效的配合 |
| L5 | 误用会怎样？ | 高频 Forget → 合并不生效 → 退回每请求回源，击穿防护失效 | 停 L5：答不出击穿风险 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| 所属包 | `golang.org/x/sync/singleflight`（**标准库外**，需 `go get golang.org/x/sync`） |
| 方法签名 | `func (g *Group) Forget(key string)` —— **无返回值**，不告知是否真删到了 |
| 并发安全 | 内部 `mu sync.Mutex` 保护，Forget 本身并发安全 |
| Go 版本 | 与 Go 版本无关（x/sync 独立演进）；本项目实测 Go 1.26.5 |
| 与 Do 关系 | `Do/DoChan` 负责「合并等待」，`Forget` 负责「主动解除合并」，二者配合 |

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
	// ① 不 Forget：两次 Do 同 key，fn 只执行 1 次（合并生效）
	var wg sync.WaitGroup
	for i := 0; i < 2; i++ {
		wg.Add(1)
		go func() { defer wg.Done(); g.Do("k", fetch) }()
	}
	wg.Wait()
	fmt.Println("合并后 fn 执行次数:", hits) // 1

	// ② 调 Forget：删掉 "k" 的合并记录
	g.Forget("k")

	// ③ 再 Do 同 key：map 里已无记录 -> 重新执行 fn（重新回源）
	g.Do("k", fetch)
	fmt.Println("Forget 后再 Do，fn 执行次数:", hits) // 2

	// ④ 边界验证：Forget 不会取消「进行中」的请求
	var wg2 sync.WaitGroup
	wg2.Add(1)
	go func() {
		defer wg2.Done()
		g.Do("slow", func() (interface{}, error) {
			time.Sleep(200 * time.Millisecond) // 慢请求
			return "slow-done", nil
		})
	}()
	time.Sleep(20 * time.Millisecond)
	g.Forget("slow") // 此时 slow 正在执行
	wg2.Wait()
	fmt.Println("进行中的请求仍正常完成，未被取消")
}
```

## 总结与追问预判
**背这三句就够**：① **Forget = 删 map 里的合并记录**；② **之后同 key 重新执行 fn（重新回源）**；③ **不取消进行中的请求，只影响之后**。
**预判追问**：
- 「Forget 和缓存失效怎么配合？」→ 回源成功写缓存后 Forget，让后续请求走新缓存，避免一直复用旧合并结果。
- 「为什么不能一直 Forget？」→ 合并保护失效，退回每请求回源，缓存击穿。
- 「Forget 有返回值吗？」→ 没有，无法得知是否真删到了某个 key（这也是它的设计取舍：极简）。
- 想深入「Do/DoChan 的合并与等待机制」，翻同组 **见 1025** 的相邻卡。

## ⚠️ 原文纠错
1. 事实核校： [经验] 源所述「Forget 删除 map 的 key、后续同 key 重新执行 fn」**均正确**，本卡保留；但源**未提最关键边界「不影响进行中请求」**，本卡已补为第 3 条并在追问链 L3 单列，避免面试时答错。
2. 补充核校： [经验] 源未讲误用风险，本卡补第 5 条（高频 Forget → 合并失效 → 缓存击穿），并补完整可运行示例与「无返回值」这一设计细节。
3. 崩坏词归一：源码将 Go、goroutine、singleflight 等音译为多组崩坏词，本卡统一为规范术语。
