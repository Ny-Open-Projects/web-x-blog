# 708 Gin 模板的 Debug 与 Release 模式

> 分类：网络与 IO | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**Debug 热加载** / **Release 只加载一次** / **子模板传参**
> 原文锚点：第 139~166 段

## 一句话总述
Gin Debug 每次渲染重解析模板（热更但 IO 重），Release（`gin.SetMode`）只解析一次。

## 面试官视角
- 意图：是否知道模板热加载的代价、会不会把 Debug 带进生产。
- P5 知两模式 / P6 说清加载次数差异与性能 / P7 知子模板传参用点号、生产必设 Release。
- 红旗：生产留 Debug；以为子模板自动继承父上下文。
- 惊艳点：Debug 用 `HTMLDebug` 重解析，Release 用 `HTMLProduction` 缓存 —— 验证 `gin/render/html.go`。

## 主问答
**Q（面试官原话）：** 为什么改了模板有时立刻生效、有时要重启？生产该怎么设？
**A：**
1. **结论**：Debug 每次渲染重解析模板，Release 只解析一次。
2. **机制**：Debug 用 `HTMLDebug` 每次重读，Release 用 `HTMLProduction` 复用已解析模板。
3. **边界**：子模板用父页变量时须 `{{template "x" .}}` 显式传上下文，否则取不到。
**加分层：** 生产必设 Release，否则高流量下模板 IO 拖垮服务。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 有哪两模式 | 知否 | Debug/Release | 换题 |
| L2 | 加载差异 | 会用 | 次次 vs 一次 | 判 P5 |
| L3 | 性能影响 | 边界 | IO 消耗 | 判 P6 |
| L4 | 子模板传参 | 实战坑 | template "x" . | 判 P6+ |
| L5 | 生产调优 | 工程 | SetMode+缓存 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| gin v1.x `[存疑]` | 未核实 | Debug/Release 模板加载行为长期稳定 |

## 关键代码
```go
// 示意，未验证：生产设为 Release
package main

import "github.com/gin-gonic/gin"

func main() {
	gin.SetMode(gin.ReleaseMode) // 模板只解析一次
	r := gin.Default()
	r.LoadHTMLGlob("./tpl/**")
	r.Run(":8888")
}
```

## 总结与追问预判
- 生产设 Release 避免每请求重解析；子模板传变量用 `{{template "x" .}}`。
- 预判：StaticFS 接口机制 → 见 708；整体静态方案 → 见 708.md。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 mergo / 勾浪→Go 等拼写还原），技术结论未做更正。
