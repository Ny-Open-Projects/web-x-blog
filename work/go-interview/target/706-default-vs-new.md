# 706 gin.Default 与 gin.New 的区别

> 分类：网络与 IO | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**Logger 中间件** / **Recovery 中间件** / **panic 恢复**
> 原文锚点：第 19~69 段「gin.Default 包含 logo 和 recover 两个默认中间件…无 recover 则 panic 抛出」

## 一句话总述
gin.Default() 在初始化路由时自动挂载 Logger 与 Recovery 两个内置中间件；gin.New() 不挂任何中间件，需手动 Use 引入，否则 handler 内 panic 会直接崩掉服务。

## 面试官视角
- 考察意图：是否清楚默认路由自带 Recovery 这层保护
- P5 知"Default 含 Logger+Recovery" / P6 能讲 Recovery 捕获 panic 避免进程崩 / P7 能讲生产用 New+显式 Recovery
- 红旗：以为 gin.New 也自带 Recovery；不知道 panic 不捕获的后果
- 惊艳点：Recovery 中间件把 handler 的 panic 转成 500 响应并打栈，未挂载时 panic 直接终止 HTTP server `[源码]`

## 主问答
**Q：** Default 和 New 初始化路由差在哪？
**A：**
1. **Default 自带两个**：Logger（访问日志）+ Recovery（恢复 panic），自动 Use 进链 `[源码]`。
2. **New 零中间件**：纯空路由，要自己 `r.Use(gin.Logger(), gin.Recovery())` 引入 `[源码]`。
3. **不捕获即崩**：New 路由的 handler 里 panic 不会被兜住，客户端拿不到正常响应、server 抛栈 `[源码]`。
**加分层：** 生产常选 New + 显式挂载，控制中间件顺序与最小集；Default 多为快速起 demo。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 差啥 | 概念 | 默认两中间件 | 换题 |
| L2 | Recovery 作用 | 机制 | 兜 panic | 判 P5 |
| L3 | 不挂会怎样 | 边界 | server 崩 | 判 P6 |
| L4 | 生产怎么选 | 权衡 | New+显式 | 判 P6+ |
| L5 | 自定义 Recovery | 实战 | 统一错误体 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| gin v1.0+ 稳定 | 无 API 翻转 | 照"Default=Logger+Recovery，New=空"答 |

## 关键代码
```go
// 示意，未验证：Default 等价于 New + Use 两中间件
r1 := gin.Default()                 // 含 Logger + Recovery
r2 := gin.New()                     // 空
r2.Use(gin.Logger(), gin.Recovery()) // 手动补齐
// r2 的 handler 内 panic 若无 Recovery 会终止 server
```

## ⚠️ 原文纠错
未发现技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 g安→Gin、建安→Gin、耳boat→Abort、logo→Logger、recover→Recovery 等拼写还原），技术结论未做更正。

## 总结与追问预判
- Default=Logger+Recovery，New 需手动 Use；不挂 Recovery 则 panic 崩服务。
- 引入方式见 706-middleware-register.md（路由组 vs 单路由）。
