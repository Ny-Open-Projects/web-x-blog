# 710 mergo 合并选项与取舍

> 分类：数据结构 | 难度：L3 | 题型：工程题 | 频率：低 | 关键词：**WithOverride** / **WithOverwriteWithEmptyValue** / **slice 深拷贝**
> 原文锚点：第 91~99 段

## 一句话总述
mergo 默认"零值才覆盖"；`WithOverride` 强制用 src 覆盖 dst 任意字段，`WithOverwriteWithEmptyValue` 仅覆盖零值，二者语义不同。

## 面试官视角
- 意图：是否读过配置项、能按场景选对覆盖策略。
- P5 会加 option / P6 说清两选项差异 / P7 知误用 WithOverride 会抹掉 dst 数据。
- 红旗：把 WithOverride 当默认用；以为选项能合并未导出字段。
- 惊艳点：WithOverwriteWithEmptyValue 才覆盖零值，WithOverride 连非零也覆盖 —— 验证 mergo Config 字段。

## 主问答
**Q（面试官原话）：** 默认合并不满足，你想强制覆盖怎么办？
**A：**
1. **结论**：`WithOverride` 让 src 无条件覆盖 dst 同名字段（含非零值）。
2. **机制**：`WithOverwriteWithEmptyValue` 仅在 dst 为零值时覆盖，是"更温柔"的覆盖。
3. **边界**：slice 有深拷贝等选项，未导出字段任何选项都改不了。
**加分层：** WithOverride 会清空 dst 原有数据，只适合"以 src 为准"的重建场景。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 有哪些选项 | 知否 | 说两覆盖项 | 换题 |
| L2 | 两选项区别 | 会用 | 零值 vs 无条件 | 判 P5 |
| L3 | 误用后果 | 边界 | 抹掉 dst 数据 | 判 P6 |
| L4 | slice 深拷贝项 | 进阶 | 选项+副作用 | 判 P6+ |
| L5 | 自研合并策略 | 实战 | 反射+自定义 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| mergo v0.3.x `[存疑]` | 未核实 | WithOverride/WithOverwriteWithEmptyValue 长期存在 |

## 关键代码
```go
// 示意，未验证：用 WithOverride 强制覆盖非零值
package main

import (
	"fmt"
	"log"

	"dario.cat/mergo"
)

type User struct{ Name, Hobby string }

func main() {
	u1 := User{Name: "t3", Hobby: "swim"}
	u2 := User{Name: "t4", Hobby: "ping"}
	if err := mergo.Merge(&u1, u2, mergo.WithOverride); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%+v\n", u1) // {t4 ping}
}
```

## 总结与追问预判
- 默认零值才覆盖；WithOverride 无条件覆盖；WithOverwriteWithEmptyValue 只覆盖零值。
- 预判：反射机制与替代库 → 见 710.md。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 mergo / 勾浪→Go 等拼写还原），技术结论未做更正。
