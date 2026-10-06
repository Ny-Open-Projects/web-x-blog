# 708 Gin 加载 HTML 模板

> 分类：网络与 IO | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**LoadHTMLFiles** / **LoadHTMLGlob** / **/** 
> 原文锚点：第 26~33 段

## 一句话总述
`LoadHTMLFiles` 收显式文件路径（内部 filepath.Walk 递归按 `.html` 后缀收集），`LoadHTMLGlob` 收目录通配，嵌套目录每层要写 `/**`。

## 面试官视角
- 意图：是否分清两种加载 API、知不知道嵌套目录的通配写法。
- P5 会调两方法 / P6 说清显式路径 vs 目录通配 / P7 知模板重名用 define 取唯一名。
- 红旗：嵌套目录只写 `/*`；以为 LoadHTMLFiles 自动递归不用给全路径。
- 惊艳点：`LoadHTMLGlob("tpl/**/*")` 的 `/**` 每层目录一个 —— 验证 gin 用 `filepath.Glob` 展开。

## 主问答
**Q（面试官原话）：** Gin 怎么把一堆 HTML 模板加载进来？
**A：**
1. **结论**：`r.LoadHTMLFiles(paths...)` 传具体文件列表；`r.LoadHTMLGlob(pattern)` 传目录通配，更省心。
2. **机制**：Files 内部 `filepath.Walk` 递归、用 `strings.HasSuffix(.html)` 过滤后收集；Glob 按模式匹配。
3. **边界**：模板在子目录时，Glob 必须按层级写 `/**`（两级写 `/**/**`），否则扫不到。
**加分层：** 多目录有同名 HTML 时，用 `{{define "唯一名"}}` 避免模板名冲突。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 有哪两方法 | 知否 | Files/Glob | 换题 |
| L2 | 区别是什么 | 会用 | 显式 vs 通配 | 判 P5 |
| L3 | 嵌套目录怎么写 | 边界 | 每层 /** | 判 P6 |
| L4 | 重名怎么办 | 实战 | define 唯一名 | 判 P6+ |
| L5 | 热更新怎么做 | 工程 | debug 模式 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| gin v1.x `[存疑]` | 未核实 | LoadHTMLFiles/Glob 长期存在，写法稳定 |

## 关键代码
```go
// 示意，未验证：两种加载方式
package main

import "github.com/gin-gonic/gin"

func main() {
	r := gin.Default()
	r.LoadHTMLFiles("./tpl/index.html", "./tpl/base/header.html")
	r.LoadHTMLGlob("./tpl/**/**") // 两级子目录
	r.Run(":8888")
}
```

## 总结与追问预判
- Files 要显式路径，Glob 用 `/**` 管嵌套；重名靠 define 唯一名。
- 预判：模板语法与变量传递 → 见 708-template-syntax；调试/发布 → 见 708-debug-release-mode。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 mergo / 勾浪→Go 等拼写还原），技术结论未做更正。
