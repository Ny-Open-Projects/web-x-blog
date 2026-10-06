# 710 mergo 自定义转换器

> 分类：数据结构 | 难度：L4 | 题型：工程题 | 频率：低 | 关键词：**mergo.Transformer** / **反射 Transform** / **time.Time 特殊处理**
> 原文锚点：第 128~166 段「WithTransformer 接口」

## 一句话总述
`mergo.WithTransformer` 让你实现 `mergo.Transformer` 接口，在反射赋值前后自定义逻辑（如 time 格式、枚举、加解密），突破默认按名赋值。

## 面试官视角
- 意图：能否用反射做字段级定制、理解 mergo 扩展点。
- P5 知有 transformer / P6 说清接口签名 / P7 写得出时间归一实现。
- 红旗：以为转换器能改未导出字段；把 transformer 当全局函数滥用。
- 惊艳点：`Transform(t, dest, src reflect.Value) error` 内可自行 `Set` —— 验证 mergo Transformer 接口。

## 主问答
**Q（面试官原话）：** 默认合并搞不定 time.Time 这类特殊类型，你怎么处理？
**A：**
1. **结论**：实现 `mergo.Transformer`（`Transform(reflect.Type, dest, src reflect.Value) error`），用 `WithTransformer` 注册。
2. **机制**：Transform 内按 `reflect.Type` 判目标类型，读 src 值、改写后 `dest.Set`。
3. **边界**：dest 须为指针方可 `Set`；未导出字段仍无法设值，转换器救不了。
**加分层：** 同一转换器可顺带做"+1 天"等业务变换，但复杂度上升须谨慎测试。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | transformer 干嘛 | 知否 | 自定义规则 | 换题 |
| L2 | 接口签名 | 会用 | Transform 三参 | 判 P5 |
| L3 | 为何要指针 | 边界 | Set 需可寻址 | 判 P6 |
| L4 | 时间格式冲突 | 实战坑 | UTC/CST 不符 | 判 P6+ |
| L5 | 性能与测试 | 工程 | 反射成本+用例 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| mergo v0.3.x `[存疑]` | 未核实 | WithTransformer/Transformer 接口长期存在 |

## 关键代码
```go
// 示意，未验证：自定义转换器把 src 的 time 覆盖进 dst
package main

import (
	"fmt"
	"log"
	"reflect"
	"time"

	"dario.cat/mergo"
)

type T struct{ At time.Time }

type timeT struct{}

func (timeT) Transform(t reflect.Type, dest, src reflect.Value) error {
	if t != reflect.TypeOf(time.Time{}) {
		return nil
	}
	if dest.CanSet() {
		dest.Set(src)
	}
	return nil
}

func main() {
	a := T{At: time.Now()}
	b := T{At: time.Date(2020, 1, 1, 0, 0, 0, 0, time.UTC)}
	_ = mergo.Merge(&a, b, mergo.WithTransformer(timeT{}))
	fmt.Println(a.At)
}
```

## 总结与追问预判
- WithTransformer + Transformer 接口，反射级字段定制，未导出字段仍不可改。
- 预判：反射机制与 mapstructure 对比 → 见 710-mergo.deep.md。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 mergo / 勾浪→Go 等拼写还原），技术结论未做更正。
