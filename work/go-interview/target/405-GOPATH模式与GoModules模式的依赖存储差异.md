# 405 GOPATH 模式与 Go Modules 模式的依赖存储差异

> 分类：工程化与测试 | 难度：L2 | 题型：对比题 | 频率：中 | 关键词：**GOPATH/src** / **GOPATH/pkg/mod** / **单一版本** / **多版本并存**
> 原文锚点：第 128~136 段「GOPATH 下存 src 单版本带 git…Modules 下存 pkg/mod 多版本无 git」

## 一句话总述
GOPATH 模式把依赖放 $GOPATH/src，每包仅一份且带 .git；模块模式放 $GOPATH/pkg/mod，同一依赖多版本各占一目录且不含 .git，由 go.mod 决定用哪个。

## 面试官视角
- 考察意图：是否理解两种模式的存储模型差异，及其带来的"版本并存/可复现"能力。
- P5 知两个路径 / P6 能讲单版本 vs 多版本、带不带 .git / P7 知模块模式如何解决 GOPATH 的版本冲突。
- 红旗：以为模块模式也只存一份依赖；以为依赖还带 .git 历史。
- 惊艳点：pkg/mod 按 module@version 目录隔离，同一包多版本可并存，彻底解决 GOPATH 的"全局唯一版本"冲突 `[源码]`。

## 主问答
**Q（面试官原话）：** GOPATH 和 Go Modules 下依赖包存哪、有什么不一样？
**A：**
1. **结论**：GOPATH 存 $GOPATH/src（单版本、带完整仓库）；模块存 $GOPATH/pkg/mod（多版本、无 .git）。
2. **机制**：模块模式按 module@version 子目录隔离，go 工具链据 go.mod 精确选取，不互相覆盖 `[源码]`。
3. **边界**：GOPATH 模式无法并存不同版本依赖，遇到版本分歧只能全局升/降，这是它被淘汰的主因。
**加分层：** pkg/mod 是只读缓存，直接改里面的文件无效，需改源码应 replace 到本地或 fork。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 存哪 | 概念 | src vs pkg/mod | 换题 |
| L2 | 版本数差异 | 机制 | 单 vs 多 | 判 P5 |
| L3 | 带不带git | 边界 | GOPATH 带 | 判 P6 |
| L4 | 冲突解决 | 权衡 | 多版本并存 | 判 P6+ |
| L5 | 缓存清理 | 实战 | go clean -modcache | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| GOPATH 旧模式 / 模块模式 go1.11 起 `[源码]` | go1.16 GOPATH 默认模式退出 | 新项目只用模块模式；回答强调 pkg/mod 多版本隔离 |

## 关键代码
```go
// 示意，未验证：读取 GOPATH 与模块缓存路径
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("GOPATH:", os.Getenv("GOPATH"))
	fmt.Println("modcache:", os.Getenv("GOPATH")+"/pkg/mod")
}
```

## 总结与追问预判
- GOPATH/src 单版本带 git；pkg/mod 多版本无 git，靠 go.mod 选版本。
- 预判：go.mod 怎么描述这些版本 → 见 405；深挖 → 见 405.md。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：核对两种模式依赖存储路径与单版本/多版本、是否含 .git 的差异；仅做机翻解码（gopass→GOPATH、gopassPK机mode→GOPATH/pkg/mod、勾点mode→go.mod、SRC→src 等还原），技术结论未做更正。
