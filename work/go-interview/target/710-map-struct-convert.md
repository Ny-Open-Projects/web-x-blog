# 710 用 mergo 实现 struct 与 map 互转

> 分类：数据结构 | 难度：L1 | 题型：工程题 | 频率：中 | 关键词：**mergo.Map** / **未导出字段丢失**
> 原文锚点：第 13~27 段「小写字段丢失」

## 一句话总述
mergo 用反射按字段名在 struct 与 map 间互转；未导出字段跨包无法设值默认跳过，是行为不是 bug。

## 面试官视角
- 意图：用过转换库否、懂反射对未导出字段的 `CanSet` 限制。
- P5 会调用 / P6 解释小写丢失 / P7 知 mapstructure 替代。
- 红旗：说"mergo 有 bug"；以为传值能改（map 须传址）。
- 惊艳点：未导出字段 `CanSet()==false` 写不进 —— 验证 `reflect.Value.CanSet`。

## 主问答
**Q（面试官原话）：** 你怎么把结构体转成 map，又转回来？
**A：**
1. **结论**：`mergo.Map(dst, src)`，struct↔map 同一函数，看 dst/src 谁是 map。
2. **机制**：按名匹配；map 必须传地址 `&m`，否则写不进。
3. **边界**：未导出字段默认不处理（跨包反射无法 `Set`），map→struct 时小写字段保持零值。
**加分层：** 字段名须精确一致，不符不映射。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | mergo 干嘛 | 知否 | Map 互转 | 换题 |
| L2 | 怎么调用 | 会用 | Map(&m,p) | 判 P5 |
| L3 | 小写为何丢 | 边界 | CanSet | 判 P6 |
| L4 | 与 mapstructure 比 | 选型 | 反射 vs 生成 | 判 P6+ |
| L5 | 大结构性能 | 实战 | 反射开销 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| mergo v0.3.x `[存疑]` | 未核实 | 未导出字段不映射稳定，无翻转 |

## 关键代码
```go
// 示意，未验证：mergo struct<->map 互转（模块路径以实际为准）
package main

import (
	"fmt"
	"log"

	"dario.cat/mergo" // 或 github.com/imdario/mergo
)

type Person struct {
	name string // 未导出：转 map 会丢失
	Age  int
}

func main() {
	p := Person{Age: 18}
	m := map[string]interface{}{}
	if err := mergo.Map(&m, p); err != nil { // map 必须传地址
		log.Fatal(err)
	}
	fmt.Printf("%+v\n", m) // 仅 Age，无 name
}
```

## 总结与追问预判
- `mergo.Map` 按名匹配；map 传址；未导出字段默认不处理。
- 预判：字段丢失根因 → 见 710-struct-merge（合并同样跳过未导出字段）。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 mergo / 勾浪→Go 等拼写还原），技术结论未做更正。
