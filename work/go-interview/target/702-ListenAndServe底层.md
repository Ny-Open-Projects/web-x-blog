# 702 ListenAndServe 底层：每连接一 goroutine

> 分类：Go 网络 / net/http | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**Serve**/**go c.serve**/**每连接 goroutine**/**handler==nil→DefaultServeMux**/**并发模型**

> 原文锚点：第 49~68 段「ListenAndServe 源码 / Serve 每连接 goroutine / handler nil 兜底」

## 一句话总述
`http.ListenAndServe` 底层是 `Server.Serve(ln)`：它**为每个到来的连接启动一个 goroutine（`go c.serve()`）**并发处理，连接间互不阻塞。若传入的 handler 为 `nil`，`Serve` 会把它设为包级 **DefaultServeMux**——这正是「`ListenAndServe(addr, nil)` 也能跑」的原因。ServeMux 负责把请求按路由分发到对应回调。

## 面试官视角
这题考 net/http 的并发模型，是「启动三步」之下的内核。能说出「每连接一个 goroutine、handler==nil 兜底 DefaultServeMux」，并点出「连接级并发、请求在回调内自行处理」的，明显超出只背 API。

## 主问答
**Q（面试官原话）：** ListenAndServe 底层发生了什么？

1. **Serve 循环 accept**：`ListenAndServe` 先 `net.Listen` 拿到 listener，再调 `srv.Serve(ln)` 进入 accept 循环。
2. **每连接一 goroutine**：`Serve` 每 accept 一个连接就 `go c.serve()`，连接处理并发、互不阻塞；单个连接内的请求默认串行（除非 handler 内再起 goroutine）。
3. **handler==nil 兜底**：`Serve` 判断若 `Handler == nil`，则设为 `http.DefaultServeMux`——所以 `ListenAndServe(addr, nil)` 等价于用全局默认 mux。
4. **分发到回调**：`c.serve()` 读请求后交给 mux（`ServeHTTP`），mux 按注册路由匹配并调用对应 `HandleFunc` 回调。
5. **并发含义**：连接级隔离使单连接阻塞不影响他连接；但**全局状态/共享资源仍需自己加锁**（mux 本身并发安全，业务共享变量不是）。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | Serve 干嘛？ | 说不清 accept 循环 |
| L2 | 每连接怎么处理？ | 说不清 go c.serve |
| L3 | 传 nil 为何能跑？ | 说不清 DefaultServeMux 兜底 |
| L4 | 请求并发吗？ | 说不清连接级并发/单连接串行 |
| L5 | 共享状态安全？ | 说不清业务自加锁 |

## 版本与兼容性
| 行为 | 实现 | 注意 |
|------|------|------|
| 接受连接 | Serve accept 循环 | 阻塞 |
| 处理连接 | go c.serve() | 每连接一 goroutine |
| handler 兜底 | nil→DefaultServeMux | 全局 mux |
| 路由分发 | mux.ServeHTTP | 注册匹配 |

## 关键代码
```go
// 等价关系：ListenAndServe(addr, nil) 内部 handler 被设为 DefaultServeMux
srv := &http.Server{Addr: ":8888", Handler: nil} // nil
_ = srv.ListenAndServe() // Serve 内：if srv.Handler == nil { srv.Handler = http.DefaultServeMux }
// 每个新连接：go c.serve() 并发处理，回调内写响应
```

## 总结与追问预判
核心：**Serve 每连接 go c.serve() 并发；handler==nil 兜底 DefaultServeMux**。追问拐向「路由怎么匹配」——备好「ServeMux 精确匹配优先、前缀/子树匹配」（见 702.md`）；Handler 链/中间件见 163.md` / `706-middleware-register.md`。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文「ListenAndServe 调 Serve、Serve 为每个连接起 goroutine、handler 为 nil 时设为 DefaultServeMux」——与 net/http 源码一致；本卡补入「单连接内请求默认串行、全局共享状态需自加锁」的并发澄清（原文未展开）。
2. 崩坏词归一：源码将 HTTP / serve / 携程 / 连接 / handler 等音译为多组崩坏词，本卡统一为规范术语。
