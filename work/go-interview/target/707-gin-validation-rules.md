# 707 常用校验规则与数字比较符

> 分类：Web框架 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**数字比较符** / **格式校验** / **contains-min-max**
> 原文锚点：第 11~34 段「GT代表的是大于等于…contains匹配指定子串…数组长度必须大于一」

## 一句话总述
validator/v10 内置大量规则：数字用 `gt/gte/lt/lte/eq/ne` 比较，字符串/字段有 `email/url/ip/min/max/contains`，数组/map 还能限定元素个数与元素长度。

## 面试官视角
- **考察意图**：是否真写过校验、知道常用操作符语义，而非只会 required。
- **P5**：会用 required/email/min/max。**P6**：说清数字比较符含义 + 数组 map 的长度规则。**P7**：知道 `contains` 是子串匹配、知道 `min/max` 对 string 是长度对 slice 是元素个数。
- **红旗答案**：把 `gte` 说成严格大于；以为 `min=2` 对切片是字符长度。
- **惊艳点**：数字比较符取英文首字母——gt=greaterThan、gte=greaterThanOrEqual、lt=lessThan、lte=lessThanOrEqual、eq=equal、ne=notEqual [源码]

## 主问答
**Q（面试官原话）：** 除了必填，还用过哪些校验规则？数字范围怎么写？
**A：**
1. **结论**：数字用 `gte=18` 之类比较符，非数字用格式/长度规则。
2. **机制**：`gt/gte/lt/lte/eq/ne` 作用于数值；`email/url/ip/ipv4/ipv6` 是格式校验；`min/max` 对字符串是长度、对切片是元素个数；`contains=abc` 是子串包含。
3. **边界**：`min/max` 语义随字段类型变化（string=长度，slice=元素数），别混用。
**加分层：** map 可用 `min,max` 校验 key 长度，逗号后再写 value 的 `min,max` 校验值长度。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | required 啥意思 | 知不知道 | 字段不能为零值 | 换题→不及格 |
| L2 | gte 和 gt 区别 | 背还是推 | 前者含等于 | 判 P5 |
| L3 | min 对切片什么意思 | 踩坑经验 | 元素个数而非长度 | 判 P6 |
| L4 | map 怎么校验值长度 | 边界掌握 | key 后逗号接 value 规则 | 判 P6+ |
| L5 | 怎么写自定义规则 | 实战 | RegisterValidation | 答得上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| validator/v10 全版本 | v8 标签名不完全一致 | 按 v10 操作符答 [经验] |

## 关键代码
```go
type Req struct {
    Age   int      `binding:"gte=18"`            // 数值比较
    Code  string   `binding:"contains=123abc"`   // 子串包含
    Tags  []string `binding:"gt=1,min=2,max=100"` // 元素>1个，每个长2~100
    M     map[string]string `binding:"min=2,max=100"` // key 长2~100
}
```
示意，未验证。

## 总结与追问预判
- 数字比较符=英文首字母缩写；min/max 语义随类型变；map 用逗号分隔 key/value 规则。
- 预判：接着问嵌套结构体如何跳过校验（见 707-gin-nested-struct）。

## ⚠️ 原文纠错
未发现技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 勾浪→Go 等拼写还原），技术结论未做更正.
