# 705 主流 Go Web 框架三维度横向对比

> 分类：Go Web 生态 | 难度：L3 | 题型：对比题 | 频率：中 | 关键词：**轻量vs全功能** / **API 风格** / **路由性能** / **httprouter** / **fasthttp**
> 原文锚点：第 12~43 段「从轻量级和全功能、API 实现风格、性能表现三个维度对比 Gin/Echo/Beego/Fiber/Martini」

## 一句话总述
横向对比 Go Web 框架抓住三个维度：**① 轻量(Gin/Echo) vs 全功能(Beego 带 MVC+ORM+session+cache+i18n)**；**② API 风格**(Fiber=Express、Gin≈Martini 依赖注入简洁、Beego≈Django)；**③ 性能**(Beego 用 net/http、Gin 用 httprouter Radix 树、Echo 用自建路由、Fiber 基于 fasthttp 内存池+零拷贝+指针传递达极致)。

## 面试官视角
- 考察意图：能否跳出"只会用"、从架构与性能内核做对比
- P5 能分轻量/全功能两类；P6 能讲 API 风格差异与各自定位；P7 能讲路由内核差异（httprouter Radix 树 vs fasthttp 内存池零拷贝）
- 红旗：把 Gin/Beego 当同类比；不知道 Fiber 底层是 fasthttp 而非 net/http
- 惊艳点：点出"Beego 用标准库 net/http、Gin 用 httprouter 弥补默认路由不足、Fiber 用 fasthttp 做到零拷贝极致性能" [源码]

## 主问答
**Q（面试官原话）：** Gin、Echo、Beego、Fiber 这些框架各有什么特点，怎么比？
**A：**
1. **维度一·功能定位**：Gin/Echo 是**轻量级**，只给路由+中间件+绑定+渲染，扩展靠插件；Beego 是**全功能**，自带 ORM、session、cache、i18n，支持完整 MVC，还有 `bee` 工具做创建/热编译/部署 [经验]。
2. **维度二·API 风格**：Fiber 是 **Express 风格**（Node 迁移者最顺手）；Gin 风格近似 **Martini**（依赖注入、代码简洁、纯 Go 味）；Beego 设计灵感来自 **Django**（Python 背景上手快）；Echo 性能向且 API 现代 [经验]。
3. **维度三·性能内核**：Beego 直接用 `net/http`；Gin 用 **httprouter**——基于 Radix 树、支持路径参数、查找快、内存占用低，弥补了 `net/http` 默认路由不支持参数解析的短板；Echo 用自建高性能路由；Fiber 基于 **fasthttp**，用内存池管理请求内存、零拷贝直读、指针传参，把内存优化做到极致 [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 轻量vs全功能 | 分类 | Gin/Echo vs Beego | P5 |
| L2 | API 风格 | 迁移 | Express/Martini/Django | P6 |
| L3 | Gin 路由好在哪 | 内核 | httprouter Radix 树 | P6+ |
| L4 | Fiber 为何快 | 内核 | fasthttp 内存池零拷贝 | P7 |
| L5 | net/http 不足 | 边界 | 无参数路由/同方法区分 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| go1.0+（net/http） | 无 | httprouter/fasthttp 均为稳定选型；Gin 默认路由实现长期为 httprouter 衍生 |

## 关键代码
```go
// Gin 用 httprouter 风格路由：支持路径参数（net/http 默认路由做不到）
r := gin.New()
r.GET("/user/:id", func(c *gin.Context) {
    id := c.Param("id") // 路径参数解析，弥补标准库默认路由不足
    c.String(200, "user %s", id)
})
// 对比：标准库需自行解析 URL，无法直接按 :id 注册 handler
```

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡统一为规范术语（外部框架→Web 框架、购→Beego、feber→Fiber、马里→Martini、HTTProot→httprouter、fastHTTP→fasthttp、ICS→Echo 路由实现等）；技术结论未做事实性更正 [经验]。

## 总结与追问预判
- 三维度对比是框架题的标准答法；路由内核差异（httprouter Radix 树 / fasthttp 内存池零拷贝）是加分点。
- Gin 用法细节见 706/707/708，net/http 基础见 702（只引不重述）；选型见 705-framework-selection-principles。
