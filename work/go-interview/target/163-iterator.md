# 163 迭代器模式：统一遍历、隐藏内部结构

> 分类：设计模式/行为型 | 难度：L3 | 题型：八股题 | 频率：中 | 关键词：**iter.Seq** / **range** / **Go1.23**
> 原文锚点：第 26~32 段「迭代器提供按顺序访问集合元素的方法，无需暴露内部表示」

## 一句话总述
迭代器把"怎么遍历"从集合内部抽出来，给外部一致访问接口；Go 1.23 起标准库 `iter.Seq`/`iter.Seq2` 把自定义迭代做成一等公民，直接 `range`。

## 面试官视角
- 意图：是否知道 Go 1.23 的 `iter` 包与 push 式迭代器，而非只会手搓 `Next()`。
- P5 知用 `range` / P6 说清 `iter.Seq` push 模型与 yield 回调 / P7 知迭代器与并发、早停（break 不泄露 goroutine）。
- 红旗：手写 `Next() (v, ok)` 当现代 Go 首选；以为迭代器必须显式保存游标。
- 惊艳点：`iter.Seq` 是 push 式——`func(yield func(T) bool)`，break 时 yield 返回 false 让生产者停止，天然支持早停不泄漏 —— 验证：`go doc iter` + 早停示例，go1.23 `[源码]`。

## 主问答
**Q（面试官原话）：** Go 里怎么给自定义集合写遍历？
**A：**
1. **结论**：Go 1.23+ 定义返回 `iter.Seq[T]` 的方法（如 `All()`），调用方直接 `for v := range c.All()`。
2. **机制**：Seq 接收 yield 回调，集合逐项 push；yield 返回 false（break）时立即停止，无 goroutine 泄漏 `[源码]`。
3. **边界**：老版本（<1.23）无 iter 包，需手搓 `Next()/HasNext` 或暴露切片；迭代器本身不保证并发安全，遍历中改集合需外部同步。
**加分层：** `Seq2[K,V]` 对应键值对，map 的 `All`/`Keys`/`Values` 已内置，直接复用。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 迭代器干嘛 | 概念 | 统一遍历 | 换题 |
| L2 | 老 Go 写法 | 会用 | Next/HasNext | 判 P5 |
| L3 | Seq 模型 | 机制 | push+yield | 判 P6 |
| L4 | 早停泄漏 | 边界 | yield false | 判 P6+ |
| L5 | 并发安全 | 实战 | 遍历中改集合 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.23 引入 iter 包 | 1.23 新增 `iter.Seq`/`Seq2` | <1.23 手搓 Next；≥1.23 用标准 iter 直接 range `[源码]` |

## 关键代码
```go
// 示意，未验证：Go1.23 推送式迭代器
func (s *Set[T]) All() iter.Seq[T] {
	return func(yield func(T) bool) {
		for _, v := range s.items {
			if !yield(v) { return } // break 时停止，无泄漏
		}
	}
}
```

## 总结与追问预判
- 迭代器=隐藏内部结构一致遍历；Go 1.23 用 `iter.Seq` push 模型，早停安全。
- 预判：观察者联动 → 见 163-observer；深挖全行为型 → 见 163-design-patterns。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 利用→nil、勾浪→Go、首时→守时 等拼写还原），技术结论未做更正。
