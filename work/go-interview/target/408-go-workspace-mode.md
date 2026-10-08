# 408 Go 工作区模式：不用 replace、不用推远端，本地多模块怎么联调？

> 分类：Go 工程 / 模块管理 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**工作区模式**/**go.work**/**go work init**/**go work sync**/**GOWORK**/**多模块联调**/**私有包调试**
> 原文锚点：第 1~9、22~26 段「通过 replace 的方式导入，我们需要开发完成之后将 replace 去掉再提交到仓库…第二种方式也是一样，我们需要提交到仓库之后才能调试，不适合开发环境…这种方法就是 Go 1.18 版本之后的新特性 Go 工作区模式…这里的工作区模式可以支持本地多个 go module 的开发…在当前目录下面它就为我们生成了一个 go.work 的文件」
> [边界] 本文只讲 **go.work 工作区模式本身**：`replace` 指令与私有包导入见 `406-private-replace`，`GOPRIVATE`/`GONOPROXY`/`GONOSUMDB` 配置见 `407-goprivate`，GOPATH 与 module 的世代差异见 `405-gopath-vs-modules`，go.mod 四条指令见 `406-gomod-directives`，均不重述。

## 一句话总述
Go 工作区模式（**Go 1.18 起**）用**一个 `go.work` 文件**把本地**多个 module** 临时组成一个"超级模块"：在各自的父目录执行 `go work init ./pkg1 ./project`，生成的 `go.work` 里只有 **`go` 版本 + `use (...)` 目录列表**；此后构建时 Go 会**优先从本地目录解析这些模块**，于是**既不用 `replace`，也不用把私有包推到远端仓库**就能联调。开发完成后各模块**分别提交**，`go.work` 留在本地即可。

## 面试官视角
- 考察意图：这是**"你有没有真的做过多仓库联调"**的验证题。只会 `replace` 的人，通常没碰过微服务拆分后"改一个公共库要同时验证三个下游"的场景。
- 分档：P5 不知道工作区模式；P6 知道 `go work init` 这条命令；P7 能讲出**它解决的到底是哪两个痛点**（`replace` 要来回删、推远端才能调）、**与 GOPATH workspace 的本质差异**（单模块 vs 多模块）、**`GOWORK=off` 怎么临时关掉**，以及**`go.work` 该不该入库**。
- 红旗答案：「`go.work` 要提交到仓库，团队共用」——**错**。它是**本地联调的临时产物**，入库会干扰 CI 与其他人。
- 惊艳点：主动补「`go work` **只有 `init` / `sync` / `edit` 三个子命令**，`sync` 的语义是**把工作区的构建列表回写到各模块的 `go.mod`**——实测 `go help work` 原文可佐证」[实测]。

## 主问答
**Q（面试官原话）：** 本地要同时改一个私有库和依赖它的工程，怎么在不 replace、不推远端的情况下联调？

**A：**
1. **先看老办法的两个痛点**：一是用 `go.mod` 的 **`replace` 语句**把远程包换成本地路径，**开发完成后必须把 replace 去掉再提交**，内部包一多就很繁琐；二是把包**推到代码平台**再用 `go mod` 处理依赖，**必须先提交才能调试**，不适合开发环境 [经验]。
2. **工作区模式的定位**：**Go 1.18 之后**的新特性，正是为了**既不用 replace、也不用提交到远端仓库**就能在本地开发调试内部私有包 [经验]。
3. **与 GOPATH 时代的 workspace 不是一回事**：老 workspace 只服务于**单个** module；**工作区模式支持本地多个 go module 同时开发**——这是二者最关键的区别 [经验]。
4. **怎么用（一步）**：来到**第三方包与工程目录的共同父目录**，执行 **`go work init ./pkg1 ./project`**；有多个包就都列上（`pkg2`、`pkg3` 同理）[实测]。
5. **生成了什么**：当前目录下出现 **`go.work`**，内容是 **`go` 版本声明 + `use (...)` 目录列表**。实测生成结果为 `go 1.26.5` 加 `use ( ./pkg1 ./project )` [实测]。
6. **效果**：回到工程目录**直接构建即可通过**，不再抛异常，调用本地包的函数能正常输出——**完全不用关心这个包有没有传到远端平台** [实测]。
7. **多模块还有别的依赖时**：在 **`go.work` 所在目录**执行 **`go work sync`**，同步工作区下各工程的依赖；实测退出码 **0** [实测]。
8. **怎么临时关掉**：设 **`GOWORK=off`** 即可回到"没有工作区"的行为。实测此时构建会重新报 `no required module provides package ...`，证明工作区确实在生效 [实测]。
9. **收尾**：开发完成后，把**各个包与工程代码分别提交**到自己的代码平台即可，`go.work` **不必入库** [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | replace 联调有什么麻烦？ | 动机 | 开发完要删掉再提交 | P5 停 |
| L2 | 工作区模式从哪个版本开始？ | 版本 | **Go 1.18** | P6 停 |
| L3 | 它和 GOPATH workspace 的区别？ | 辨析 | 单模块 vs **多模块** | P6 停 |
| L4 | `go.work` 里有什么？ | 结构 | `go` 版本 + `use (...)` | P7 停 |
| L5 | 怎么临时禁用 / `go.work` 要不要入库？ | 工程 | `GOWORK=off`；**不入库** | P7+ 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.18 起 | 工作区模式引入 | 现行答案起点 |
| 实测 go1.26.5 | `go work init` 写入 `go 1.26.5` | `go` 指令跟随工具链版本 [实测] |
| 全版本（1.18+） | 子命令仅 **init / sync / edit** | 别臆造别的子命令 [实测] |
| `GOWORK=off` | 临时禁用工作区 | 实测恢复为"找不到模块" [实测] |
| `GOWORK=<path>` | 可指定任意 go.work | 多工作区切换用 |
| 全版本 | **`go.work` 官方建议不入库** | 入库会干扰 CI 与他人 [经验] |

## 关键代码
```go
// 目录结构（在 /tmp/ws 下联调两个模块）
//   /tmp/ws/pkg1/pkg1.go      模块 github.com/demo/pkg1
//   /tmp/ws/project/main.go   模块 github.com/demo/project

// ---------- pkg1/pkg1.go ----------
package pkg1

const Name = "PKG1"

// ---------- project/main.go ----------
package main

import (
	"fmt"

	"github.com/demo/pkg1" // 这个仓库在远端并不存在
)

func main() {
	fmt.Println("hello", pkg1.Name)
}
```

对应的三条命令（在 `/tmp/ws` 这一**共同父目录**执行）：

```bash
cd /tmp/ws && go work init ./pkg1 ./project   # 生成 go.work
cd /tmp/ws/project && go run .                # 直接构建运行
cd /tmp/ws && go work sync                    # 同步工作区构建列表回各 go.mod
```

> 验证（`[实测]` 输出，go1.26.5 / macOS）：① **无 `go.work` 时** `go mod tidy` 报 `go: finding module for package github.com/demo/pkg1` 并以 `git ls-remote ... exit status 128` 失败——远端根本没有这个仓库。② 执行 `go work init ./pkg1 ./project` 后，`go.work` 内容为：
> ```
> go 1.26.5
>
> use (
> 	./pkg1
> 	./project
> )
> ```
> ③ 再 `go run .` 输出 **`hello PKG1`**，构建通过。④ `go env GOWORK` 输出 **`/tmp/ws/go.work`**。⑤ `go work sync` 退出码 **0**。⑥ `GOWORK=off go run .` 立刻回到 `no required module provides package github.com/demo/pkg1; to add it: go get github.com/demo/pkg1`——**反证工作区确实在生效**。⑦ `go help work` 列出的子命令只有 **`edit` / `init` / `sync`** 三个。

## 总结与追问预判
- 一句话收尾：**"父目录一条 `go work init`，`use` 里挂上所有模块，本地联调不再求远端；`GOWORK=off` 随时退回，开发完各模块分别提交、`go.work` 不入库"**。
- 大概率被追的三问：① 和 `replace` 比好在哪（不用改 `go.mod`、不会误提交、多模块一次搞定）；② 团队里要不要共享 `go.work`（**不要**，各人本地路径不同，入库会互相干扰）；③ `go work sync` 干什么（把工作区解析出的构建列表**回写**到各模块的 `go.mod`，让单模块独立构建时也能复现）。
- 反向加分：主动指出**"工作区模式支持多模块"才是它与 GOPATH workspace 的分水岭**，而不是"都能本地开发"。

## ⚠️ 原文纠错
1. 源码称工作区模式「跟 GOPATH 时代的 workspace 不同」却未说清——后者**单模块**，前者支持**多模块** [经验]。
2. 源码只讲 `go work init`，未提 **`GOWORK=off`** 可临时关闭工作区 [实测]。
3. 源码未提 `go work` **只有 init / sync / edit 三个子命令**，容易臆造 [实测]。
4. 源码称 replace「开发完成后要去掉」——也可保留 `go.work` **不入库**、只提交各模块 [经验]。
5. 源码未提 **`go.work` 不应提交到仓库**，否则会干扰 CI 与他人 [经验]。
6. 源码未提 `go.work` 里的 **`go` 指令版本由工具链写入**（实测为 `go 1.26.5`）[实测]。
