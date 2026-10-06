# 706 Gin 权限校验中间件实战

> 分类：网络与 IO | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**c.Next 放行** / **c.Abort 中断** / **AbortWithStatus 403**
> 原文锚点：第 111~125 段「os 中间件校验用户名密码…通过则 c.Next 并 return…不通过 c.Abort 响应 403」

## 一句话总述
权限校验中间件在 c.Next() 前检查请求参数（用户名/密码等），通过则放行并 return；不通过调用 c.Abort()（或 AbortWithStatus(403)）短路，直接返回错误状态码不再执行后续 handler。

## 面试官视角
- 考察意图：能否把一个中间件机制落到真实鉴权代码
- P5 能写"校验→Next/Abort"骨架 / P6 知 Abort 后需 return + 状态码含义 / P7 能讲鉴权失败的统一错误体
- 红旗：Abort 后不 return 导致后续仍跑；把 403 写成 401 混淆
- 惊艳点：Abort 只是跳过链，必须紧接着 return，否则本中间件函数体仍会继续执行 `[源码]`

## 主问答
**Q：** 怎么用中间件做权限校验？
**A：**
1. **校验通过放行**：参数合法时 `c.Next()` 执行后续 handler，随后 `return` `[源码]`。
2. **校验失败短路**：不合法时 `c.Abort()`（或 `c.AbortWithStatus(403)`）中断链，直接回 403 `[源码]`。
3. **务必 return**：Abort 不抛异常，调用后本函数会继续往下走，须 `return` 收尾 `[源码]`。
**加分层：** 403 表"已认证但无权限"、401 表"未认证"，实战按语义选状态码。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 怎么拦 | 概念 | Abort | 换题 |
| L2 | 通过咋办 | 机制 | Next | 判 P5 |
| L3 | 为何 return | 边界 | Abort 不抛 | 判 P6 |
| L4 | 403 vs 401 | 权衡 | 语义区分 | 判 P6+ |
| L5 | 统一错误体 | 实战 | 中间件封装 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| gin v1.0+ 稳定 | 无 API 翻转 | 照"校验→Next/Abort + return"答 |

## 关键代码
```go
// 示意，未验证：鉴权中间件骨架
func Auth() gin.HandlerFunc {
    return func(c *gin.Context) {
        if !check(c) {            // 校验用户名/密码等失败
            c.AbortWithStatus(403) // 短路并返回 403
            return               // 必须 return
        }
        c.Next() // 放行
    }
}
```

## ⚠️ 原文纠错
未发现技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 g安→Gin、建安→Gin、耳boat→Abort、last→Next、四零三→403 等拼写还原），技术结论未做更正。

## 总结与追问预判
- 鉴权 = 校验→Next 放行 / Abort+return 短路。
- 机制原理见 706-middleware-chain.md（Next/Abort 的 index 实现）。
