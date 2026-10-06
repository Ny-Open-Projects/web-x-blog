# 706 Gin 中间件的本质

> 分类：网络与 IO | 难度：L2 | 题型：概念题 | 频率：高 | 关键词：**HandlerFunc** / **gin.Context** / **next/abort 控制**
> 原文锚点：第 4~13 段「GIN 中间件的本质其实就是一个 function，入参是 gin.Context」

## 一句话总述
Gin 中间件本质就是一个函数：入参为 *gin.Context 的 HandlerFunc，可访问请求/响应与处理函数，并通过 c.Next() 放行、c.Abort() 中断后续处理链。

## 面试官视角
- 考察意图：是否理解"中间件=普通 handler 函数"这一本质
- P5 知"是函数、入参 Context" / P6 能讲可访问 context 并控制 next/abort / P7 能讲在简历里引导面试官
- 红旗：把中间件说成特殊类或框架魔法；不知道它和 handler 同类型
- 惊艳点：中间件与路由 handler 是同一类型 HandlerFunc，区别只在"是否在链中调用 c.Next" `[源码]`

## 主问答
**Q：** Gin 中间件到底是什么？
**A：**
1. **本质=函数**：签名就是 `func(*gin.Context)`，与业务 handler 同一类型 `[源码]`。
2. **可访问全上下文**：能读写请求参数、responseWriter、并控制是否继续 `[源码]`。
3. **控制继续**：调用 c.Next() 执行后续链；不调用则后续不执行 `[源码]`。
**加分层：** 因为同类型，中间件可像 handler 一样被注册进同一条处理函数链。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 签名 | 概念 | func(Context) | 换题 |
| L2 | 与 handler 关系 | 机制 | 同类型 | 判 P5 |
| L3 | 如何中断 | 边界 | Abort | 判 P6 |
| L4 | 为何能引导面试 | 权衡 | 简历写源码 | 判 P6+ |
| L5 | 自写中间件 | 实战 | 日志/鉴权 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| gin v1.0+ 稳定 | 无 API 翻转 | 照"HandlerFunc + Context + Next/Abort"答 |

## 关键代码
```go
// 示意，未验证：中间件就是一个 HandlerFunc
func Logger() gin.HandlerFunc {
    return func(c *gin.Context) {
        start := time.Now()
        c.Next() // 执行后续 handler
        log.Printf("%s %v", c.Request.URL.Path, time.Since(start))
    }
}
```

## ⚠️ 原文纠错
未发现技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 g安→Gin、建安→Gin、构入t→goroutine、耳boat→Abort、last→Next 等拼写还原），技术结论未做更正。

## 总结与追问预判
- 中间件=HandlerFunc，靠 c.Next/c.Abort 控制链。
- 深入见 706-middleware-chain.md（handlers 切片与 Next/Abort 实现）。
