# 407 GONOPROXY 与 GONOSUMDB：和 GOPRIVATE 的关系

> 分类：Go 工程化 | 难度：L3 | 题型：对比题 | 频率：中 | 关键词：**GONOPROXY**/**GONOSUMDB**/**GOSUMDB**/**GOINSECURE**/**默认值**

> 原文锚点：第 68~81 段「GONOPROXY / GONOSUMDB 的作用与三者区别」

## 一句话总述
`GONOPROXY` 只让匹配模块**不走代理**，`GONOSUMDB` 只让匹配模块**不做校验和数据库校验**，两者都从 Go 1.13 起支持；而 `GOPRIVATE` 会同时作为这两者的默认值——配一条 `GOPRIVATE` 等价于把域名同时写进另外两个变量。

## 面试官视角
这题专治「只会抄配置」。考官要听的是**分工**：谁管代理、谁管校验、谁是一键合并。能主动补一句「GOINSECURE 只放开 HTTP 与证书、并不关闭校验」，说明你读过官方文档而不是博客。

## 主问答
**Q（面试官原话）：** GONOPROXY、GONOSUMDB 和 GOPRIVATE 到底有什么区别？

1. **GONOPROXY 管代理**：匹配到的模块不通过代理拉取，直接按模块地址走源码仓库。
2. **GONOSUMDB 管校验**：匹配到的模块不与校验和数据库比对，跳过哈希校验。
3. **两者都从 1.13 起支持**：语义上都是「对指定域名的包不走某套机制」，但各自只管一半。
4. **GOPRIVATE 是合并项**：一旦配置，它默认就把同一域名同时写进了代理免走与校验免除两项，因此实际工作直接用它更方便。
5. **只配 GONOPROXY 不够**：若不使用合并变量又希望免校验，必须**同时**配上校验免除变量，否则仍会去校验和数据库比对。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 三个变量分别管什么？ | 只能说出 GOPRIVATE |
| L2 | 都从哪个版本起支持？ | 说不出 1.13 |
| L3 | GOPRIVATE 为什么方便？ | 说不清是默认值 |
| L4 | 只配 GONOPROXY 会怎样？ | 说不清仍会校验 |
| L5 | GOINSECURE 能免校验吗？ | 误以为可以 |

## 版本与兼容性
| 变量 | 作用 | 1.13 起 |
|------|------|---------|
| GONOPROXY | 不走代理 | 是 |
| GONOSUMDB | 不校验哈希 | 是 |
| GOPRIVATE | 同时默认两者 | 是 |
| GOINSECURE | 仅放开 HTTP/证书 | 否（不关校验）|

## 关键代码
```go
// Go 侧视角：一次性核对三个变量，确认私有域名是否真的被全覆盖
package main

import (
	"fmt"
	"os/exec"
	"strings"
)

func main() {
	for _, k := range []string{"GOPRIVATE", "GONOPROXY", "GONOSUMDB"} {
		out, _ := exec.Command("go", "env", k).Output()
		fmt.Printf("%s = %s\n", k, strings.TrimSpace(string(out)))
	}
}
```

## 总结与追问预判
核心：**GONOPROXY 管代理、GONOSUMDB 管校验、GOPRIVATE 一键合并**。追问常拐向「GOINSECURE 是不是就够了」，备好「它只放开传输层限制，不关闭校验和数据库校验」这句官方文档原意。

## ⚠️ 原文纠错
1. 事实核校： [经验] 原文在列举环境变量时把校验免除变量一带而过，易让人以为是历史遗留——`go help environment` 至今仍将三者并列列出，并非废弃项。
2. 事实核校： [经验] 原文未提 `GOINSECURE`：它只放宽 HTTP 与证书校验，**不**关闭校验和数据库校验；要免校验仍须依赖另一组变量。
3. 崩坏词归一：源码将 GONOPROXY / GONOSUMDB / GOPRIVATE 等音译为多组崩坏词，本卡统一为规范术语。
