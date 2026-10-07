# 107 用 channel 串行化：把 map 操作打包成请求交给单个 goroutine

> 分类：Go 并发 | 难度：L4 | 题型：实现题 | 频率：中 | 关键词：**channel 串行化、request、response、op、单 goroutine、阻塞、封装**

> 原文锚点：第 52~69 段「另一种避免 map 并发问题的方法是使用 channel 进行同步。我们可以创建一个专门用于处理 map 操作的 goroutine，所有对 map 的操作都在这个 goroutine 里面完成，这个 channel 实现的本质其实是一个串行化的操作…request 就是对 map 的一些操作，具体的操作进行了封装，这个操作有 operation 字段，还有 map 的键以及 map 的值，以及操作后的一个返回值…由于通道的读取是单线程的，所以如果使用 range 操作一个很大的 map，就会导致其他的操作被阻塞」

## 一句话总述
用 channel 实现并发安全 map 的思路是**串行化**：**起一个专门的 goroutine**，**所有对 map 的操作都在这个 goroutine 里完成**；外部把操作**封装成 request**（含 **operation 字段、key、value、以及操作后的返回值**）投递进 **request channel**，`run` 方法用 for 循环不断取出并按 **op** 分派；**get 通过 response channel 把结果回传**。它的代价是**通道读取是单线程的**，**遍历一个很大的 map 时会阻塞其他操作**。

## 面试官视角
- 考察意图：能否说出"用通信共享内存"在 map 场景下的**具体形态**，以及它**为什么通常不是最优解**。
- 分档：P5 知道可以用 channel；P6 能说"单 goroutine 串行处理"；P7 能讲清 **request/response 双 channel 结构**、**op 分派**，并指出**单线程读取导致大 map 遍历阻塞其他操作**这一致命缺点。
- 红旗答案：只说"用 channel 就并发安全了"却讲不出 request 结构；或不承认它有串行瓶颈。
- 惊艳点：**这个方案本质上是用 channel 把并发请求"排队"**，安全性来自"**只有一个 goroutine 碰 map**"，而不是 channel 本身有什么魔法 `[源码]`。

## 主问答
**Q（面试官原话）：** 怎么用 channel 让 map 并发安全？有什么问题？

1. **结论**：**创建一个专门处理 map 操作的 goroutine**，**所有对 map 的操作都在这个 goroutine 中完成**；**这个 channel 实现的本质其实是一个串行化的操作** `[源码]`。
2. **运行结构**：**只启动一个 goroutine**，**通过 for 循环不停地取 request** `[源码]`。
3. **request 的封装**：**request 就是对 map 的一些操作，具体操作做了封装**——**有 `operation` 字段，还有 map 的键、map 的值，以及操作后的一个返回值** `[源码]`。
4. **容器定义**：定义一个 map，**键和值都为 `any` 类型**，外加一个 **request channel**；**初始化时对 map 和 channel 都要做 make 初始化**，然后执行 `run` 方法 `[源码]`。
5. **run 方法**：**`run` 遍历对 map 的这些操作，根据不同的操作从 request channel 读出来，通过不同的 op 值进行不同的操作**；**本质上 request 就是把 map 的操作打包到 channel 里，然后借助 channel 并发安全的特性将它串行化到 for 循环里进行操作** `[源码]`。
6. **get 的回传**：**先组装一个 request，把它写进 request channel**；由于已启动 goroutine 不断读取，**读到值就执行对应操作**；**get 操作会通过 response channel 把 map 的值返回出去**；**set 方法同理**，**delete 与 range 方法也类似，都是组装请求丢进 channel** `[源码]`。
7. **用法**：**初始化对象（对 map、channel 做初始化）→ 通过 goroutine 调用 `run` 方法 → 通过 goroutine 向 map 存储键值对 → 通过 range 迭代** `[源码]`。
8. **缺点**：**由于通道的读取是单线程的**，**如果使用 range 操作一个很大的 map，就会导致其他的操作被阻塞** `[源码]`。

**加分层：** 一句话概括选型——**锁是"多个线程抢同一把锁"，channel 方案是"把线程数降到 1"**。后者天然无竞争，但把并发度也一并降到了 1，所以只适合**操作极轻量、且不需要遍历**的场景。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 这个方案为什么安全？ | 答出串行化 |
| L2 | request 里有什么？ | 答不出 op/key/value |
| L3 | get 的结果怎么回传？ | 答不出 response channel |
| L4 | run 做什么？ | 答不出循环取 + 按 op 分派 |
| L5 | 缺点是什么？ | 答不出大 map 遍历阻塞 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本 | channel 语义稳定 | 与版本无关 |
| Go 1.9+ | 有 `sync.Map` | 通常优先用它 |
| Go 全版本 | 单 goroutine 串行 | 并发度恒为 1 |
| 所有版本 | 遍历阻塞 | 大 map 不适用 |

## 关键代码
```go
package main

// request：把一次 map 操作打包 —— 操作类型 + 键 + 值 + 回填通道
type request struct {
	op       string // "get" / "set" / "delete" / "range"
	key      any
	value    any
	response chan any
}

type ChanMap struct {
	m       map[any]any
	request chan request
}

func NewChanMap() *ChanMap {
	return &ChanMap{m: make(map[any]any), request: make(chan request)}
}

// run：唯一的 map 操作者，把并发请求串行化
func (c *ChanMap) run() {
	for req := range c.request {
		switch req.op {
		case "get":
			req.response <- c.m[req.key]
		case "set":
			c.m[req.key] = req.value
		case "delete":
			delete(c.m, req.key)
		}
	}
}

func (c *ChanMap) Get(k any) any { // 组装请求 + 通过 response 回传结果
	resp := make(chan any)
	c.request <- request{op: "get", key: k, response: resp}
	return <-resp
}

func (c *ChanMap) Set(k, v any) {
	c.request <- request{op: "set", key: k, value: v}
}

func main() {
	cm := NewChanMap()
	go cm.run() // 只起一个 goroutine 处理所有操作
	cm.Set("a", 1)
	v := cm.Get("a")
	_ = v
	// 注意：遍历大 map 时，单线程读取会让其他操作全部阻塞
}
```

## 总结与追问预判
**必追问的是"和加锁比哪个好"**——**加锁通常更好**：锁只在临界区串行，而这个方案把**整个操作（含遍历）都串行了**，并发度恒为 1；加锁还能利用读写锁让读并发。channel 方案的价值更多是**教学与思路展示**——体现"**不要通过共享内存来通信**"。追问常接"那什么时候真的该用"——**操作本身很轻、且天然需要排队**的场景，例如事件总线、状态机串写入，或需要把 map 操作与其他 IO 操作统一串行化时。

## ⚠️ 原文纠错
1. 事实核校：专起一个 goroutine 处理全部 map 操作、本质是串行化、单 goroutine 循环取 request、request 封装 operation 与键值及返回值、map 与 channel 均需 make 初始化、run 按 op 分派、get 经 response channel 回传、set/delete/range 均为组装请求投递、通道读取单线程导致遍历大 map 阻塞其他操作——均与 channel 串行化实现一致 `[经验]`。
2. 补充：**该方案把并发度固定为 1**，遍历大 map 时阻塞尤为严重；生产上更常见的是**锁 + 分片**或直接用 `sync.Map`，channel 串行化主要用于**思路演示与事件总线类场景** `[经验]`。
3. 崩坏词归一：源码将 channel、goroutine、request、response、键值对、串行化等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
