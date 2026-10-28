---
disableNunjucks: true
title: "1025 Singleflight 用法：Group.Do 与同一 key 合并"
date: 2026-10-10 09:43:43
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：Go 并发 | 难度：中 | 题型：用法 | 频率：高 | 关键词：**Group.Do、key、并发合并、共享结果、回源**

> 原文锚点：第 12~35 段「demo 并发20请求、getArticleData、Group.Do、同 key 只一次打到 DB」

## 一句话总述
用法三步走：声明 `singleflight.Group`；在缓存未命中处调用 `g.Do(key, fn)`，fn 是真正的回源逻辑；同一 key 的并发调用会合并——只有一个 goroutine 执行 fn，其余直接拿返回值。一句话背法：**「Group.Do(key, fn)，同 key 并发只跑一次 fn，返回 (val, err, shared)」**。示例里 20 个并发请求用同一个 key，最终只有 1 个打到数据库，20 个都拿到数据。

## 面试官视角
考官常要求手写或描述用法。关键点：① Do 返回 `(val, err, shared)`；② key 必须一致才会合并（key 是合并的判据）；③ fn 的返回值被所有等待者共享。能点出「key 设计决定合并粒度」很关键。
- **P5**：写出 `g.Do(key, fn)` 基本用法。
- **P6**：说清返回三元组与 shared 含义。
- **P7**：指出 key 设计决定合并粒度，避免全局单 key 串行化。

## 主问答
**Q（面试官原话）：** 怎么使用 singleflight？Do 方法返回什么？

**先铺垫（由浅入深第 1 层）**：singleflight 通过 `Group` 管理「进行中的调用」，调用方只需声明一个 Group，然后在回源点用 `Do` 包住回源函数即可。

1. **声明 Group（第 2 层）**：`var g singleflight.Group`，无需初始化，**零值即可用**。
2. **调用 Do（第 3 层）**：`v, err, shared := g.Do(key, fn)`；fn 是回源函数（如查 DB），只在合并组中第一个请求时执行，其余等待复用。
3. **key 即合并判据（第 4 层）**：所有调用传相同 key 才会合并；key 不同则互不影响、各自执行。key 通常取「业务维度 + 资源标识」（如 `"article:"+id`）。
4. **返回值（第 5 层）**：`v` 是 fn 结果（被所有等待者共享），`shared` 表示该结果是否来自他人——`true` 表示本 goroutine 没执行 fn，是「搭车」拿到的结果。
5. **边界（第 6 层）**：`Do` 不取消进行中的 fn；若 fn panic，所有等待者都收到该 panic（无兜底），故 fn 内部应自行 recover。

## 追问链
| 档位 | 追问 | 答得到（背这句） | 答不出停在哪档 |
|------|------|------------------|----------------|
| L1 | 怎么用？ | `g.Do(key, fn)`，Group 零值可用 | — |
| L2 | 返回几值？ | `(val, err, shared)` 三个 | 停 L2：漏 shared |
| L3 | key 作用？ | key 是合并判据，相同才合并 | 停 L3：说不清合并判据 |
| L4 | shared 含义？ | `true`=搭车拿到别人的结果 | 停 L4：说不清是否搭车 |
| L5 | 20 并发结果？ | 都拿到同一份，DB 只被打一次 | 停 L5：说不清都拿到同一份 |

## 版本与兼容性
| 维度 | 说明 |
|------|------|
| 所属包 | `golang.org/x/sync/singleflight`（`go get golang.org/x/sync`） |
| Do 签名 | `func (g *Group) Do(key string, fn func() (interface{}, error)) (v interface{}, err error, shared bool)` |
| DoChan | `func (g *Group) DoChan(key string, fn func() (interface{}, error)) <-chan Result`——异步版，用 channel 收结果，便于配合 `select` 超时 |
| 零值 | `Group` 零值即可用，无需 `New` |
| 并发安全 | 内部 `sync.Mutex` 保护，可多 goroutine 并发 Do |
| Go 版本 | 与 Go 版本无关；本项目实测 Go 1.26.5 |
| 返回值 shared | 区分「自己执行的」与「搭车拿到的」，可用于埋点（搭车率） |

## 关键代码
```go
package main

import (
	"fmt"
	"sync"

	"golang.org/x/sync/singleflight"
)

var g singleflight.Group

// 模拟回源：每次真实执行都打印并计数
var dbHits int

func getArticleFromDB(id string) (interface{}, error) {
	dbHits++
	fmt.Printf(">>> 真正回源 article=%s (第 %d 次)\n", id, dbHits)
	return "article-content", nil
}

func getArticle(id string) (interface{}, error) {
	v, _, shared := g.Do("article:"+id, func() (interface{}, error) {
		return getArticleFromDB(id)
	})
	fmt.Printf("    拿到结果 shared=%v\n", shared)
	return v, nil
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 20; i++ { // 20 个并发请求同一个 article
		wg.Add(1)
		go func() {
			defer wg.Done()
			getArticle("1001")
		}()
	}
	wg.Wait()
	// 输出：只打印 1 次「真正回源」，但 20 次都拿到结果；dbHits == 1
	fmt.Println("DB 命中次数:", dbHits, "(20 并发同 key 只回源 1 次)")
}
```

## 总结与追问预判
**背这三句就够**：① **`g.Do(key, fn)` 合并同 key 并发**；② **返回 `(val, err, shared)`**；③ **shared=true 表示搭车、key 决定合并粒度**。
**预判追问**：
- 「底层如何保证只执行一次？」→ `map[key]*call` + WaitGroup（见 1025 源码）。
- 「合并结果能主动失效吗？」→ `Forget(key)`（见 1025 的 Forget）。
- 「和直接加锁有什么区别？」→ 加锁是串行执行 fn，singleflight 是「只第一个执行、其余等结果」，前者慢后者快（见 1025）。

## ⚠️ 原文纠错
1. 事实核校： [经验] Group 零值可用、Do(key,fn) 返回 (val,err,shared)、同 key 合并、shared 含义——均正确，本卡为准。
2. 崩坏词归一：源码将 Go/goroutine/singleflight 等音译为崩坏词；本卡统一为规范术语。
3. 补强：本卡第 6 层补「fn panic 会传播给所有等待者」这一实战边界，原卡未提。
