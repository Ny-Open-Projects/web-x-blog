# 410 os.Args[0] 取可执行文件路径

> 分类：工程化与测试 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**os.Args** / **go run 临时文件** / **filepath.Abs**
> 原文锚点：第 56~86 段「os.Args 第零号元素在 go run 时是临时编译文件路径，go build 后是真实 exe 路径」

## 一句话总述
`os.Args[0]` 是程序启动路径：`go run` 时是临时编译出的 exe（路径无用），`go build` 后是真实 exe；配 `filepath.Abs`+`Dir` 取目录。

## 面试官视角
- 意图：是否分清 go run 与 go build 的路径差异，知道临时文件陷阱。
- P5 知 Args0 是程序路径 / P6 说清 go run 临时文件 / P7 知生产只用 build 产物。
- 红旗：以为 go run 时 Args0 就是源码目录；以为直接 Args0 就是绝对路径。
- 惊艳点：`go run` 先把 main 编到 `$TMP/go-build.../exe` 再执行，Args0 指向临时文件 `[经验]`。

## 主问答
**Q（面试官原话）：** os.Args[0] 拿到的是什么？能不能直接当根目录用？
**A：**
1. **结论**：Args0 是启动用的程序路径；`go run` 时是临时文件不能当根目录，`go build` 后才是真实 exe。
2. **机制**：`go run` 内部先 build 再跑临时 exe，Args0 指向那个临时路径；build 后运行 exe，Args0 即该 exe。
3. **边界**：拿到后需 `filepath.Abs` 转绝对、`filepath.Dir` 取目录；`LookPath` 仅在查 PATH 时用，别混淆 `[经验]`。
**加分层：** 生产只跑 build 产物，Args0 才可靠；开发期别用 go run 测路径逻辑。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 是什么 | 概念 | 程序路径 | 换题 |
| L2 | run差异 | 机制 | 临时文件 | 判 P5 |
| L3 | 取目录 | 边界 | Abs+Dir | 判 P6 |
| L4 | 生产 | 演进 | 只用build | 判 P6+ |
| L5 | LookPath | 实战 | PATH查找 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 | 无 | go run 的临时文件行为长期不变 `[经验]` |

## 关键代码
```go
// 示意，未验证：os.Args[0] 取 exe 所在目录
package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	abs, _ := filepath.Abs(os.Args[0]) // go build 后为真实 exe 绝对路径
	fmt.Println(filepath.Dir(abs))
}
```

## 总结与追问预判
- Args0 在 go run 是临时文件、build 后是真实 exe；需 Abs+Dir。
- 预判：更稳的取路径法 → 见 410-os-executable、410-runtime-caller。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 利用→nil 等拼写还原），技术结论未做更正。
