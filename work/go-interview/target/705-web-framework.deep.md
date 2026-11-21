# 705 Web 框架选型三维拆解深挖

## 思路与架构
"你用过哪些 Web 框架"本质是**框架生态认知 + 选型权衡**：把框架按「功能定位 / API 风格 / 性能内核」三维拆开，再映射回「业务 / 团队 / 交付」三约束做选择。它把 705- 三张主卡收敛成一张可现场套用的决策表。

```text
Go Web 框架选型决策树
  业务需求 ──► 团队储备 ──► 交付时间 ──► 选谁
  高并发/轻量服务     有 Gin 经验      短    ✅ Gin（httprouter 高性能）
  极致吞吐/内存敏感   愿学 fasthttp     短    ✅ Fiber（零拷贝极致性能）
  全功能/快速交付     要 ORM+MVC        紧    ✅ Beego（开箱即用）
  现代 API/均衡       有 Node 背景      中    ✅ Echo（Express 风+高性能）
  仅原型/依赖度低     net/http 够       任意   ✅ 标准库直写
```

## 方案取舍
| 框架 | 定位 | 路由内核 | 适合 |
| --- | --- | --- | --- |
| Gin | 轻量 | httprouter(Radix 树) | 高并发通用服务 |
| Echo | 轻量 | 自建高性能路由 | 现代均衡 API |
| Beego | 全功能 | net/http | 全功能快速交付 |
| Fiber | 轻量高性能 | fasthttp(内存池+零拷贝) | 极致吞吐 |
| 标准库 | 极简 | net/http 默认 | 原型/低依赖 |

**取舍结论**：没有"最好"只有"最匹配"——Gin 是安全默认项（生态+性能+命中率），Fiber 在内存敏感场景更优，Beego 在要全功能时省事。选型三约束权重：业务 > 团队 > 时间。

**分层边界**：框架用法细节在 706/707/708（Gin）、702（net/http）；语言级选型在 201-；本卡只做横向对比与决策，不重述用法 [边界]。

## 答题技巧
1. **三维拆框架**：开口"轻量vs全功能 / API 风格 / 性能内核"，结构立现。
2. **点路由内核**：httprouter 的 Radix 树、fasthttp 的内存池零拷贝，是拉开差距的细节。
3. **落到选型三原则**：业务 > 团队 > 时间，再加"先上线再迭代"，显务实。
4. **Gin 当安全牌**：不会就推 Gin（最流行、命中率高、生态全）。
5. **避坑**：不说"Go 不用框架"（net/http 够≠不选型）；不把 Gin/Beego 当同类；不忽略 Fiber 底层是 fasthttp 非 net/http。

## 细节与核心 API

```go
// 标准库 net/http 已可构建生产服务；框架提供路由/中间件/绑定等便利
// gin 示例（路由分组 + 中间件 + JSON 绑定）
r := gin.Default()
r.Use(gin.Logger(), gin.Recovery()) // 全局中间件（panic 不崩）
api := r.Group("/api")
api.POST("/login", func(c *gin.Context) {
    var req struct{ User, Pwd string }
    if err := c.ShouldBindJSON(&req); err != nil { c.JSON(400, gin.H{"e": err.Error()}); return }
    c.JSON(200, gin.H{"ok": true})
})
r.Run(":8080")
// 选型：轻量用 net/http + chi；全功能用 gin/echo；注意框架的 Context 复用陷阱
```
