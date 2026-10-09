# 608 recover 就近捕获与多个 defer 的 panic 覆盖

> 分类：错误处理 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**就近捕获** / **defer LIFO** / **panic 覆盖**
> 原文锚点：第 61~98 段「defer 中的 panic 覆盖外层 panic…多个调用层 recover 就近捕获」

## 一句话总述
同一 goroutine 内，谁先遇到 panicking 谁先 recover，即"就近捕获"；若 defer 闭包自身又 panic，新 panic 覆盖旧的，最终 recover 只拿到最后一个 panic 值。

## 面试官视角
- **考察意图**：是否理解 recover 的最近优先与 defer 内二次 panic 的覆盖。
- **P5** 知就近捕获 / **P6** 能解释 defer 内 panic 覆盖外层 panic / **P7** 知多个 defer 按 LIFO 执行，最后注册的最先跑其 panic。
- **红旗**：以为外层 recover 能拿到"最先"的 panic；以为多个 panic 会全部被捕获。
- **惊艳点**：内层 defer 的 recover 抢先捕获后，外层 defer 的 recover 拿到的是 nil —— 验证：`go run`，go1.26.5，见关键代码。

## 主问答
**Q（面试官原话）：** 函数里好几层 defer 都有 recover，到底谁捕获？
**A：**
1. **结论**：panic 沿 defer 链向外传递，先被遇到的 recover 截获，外层再 recover 只能拿到 nil。
2. **机制**：defer 按 LIFO 执行；若某 defer 闭包内部又 panic，该新值成为当前 panic，覆盖外层原本的值。
3. **边界**：无论多少层 defer panic，recover 一次只返回一个值（最后设定的那个）。
**加分层：** 想确认捕获了什么，直接比较 recover 返回值即可，不要假设是"第一个"panic。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 谁先捕获 | 概念 | 最近的 recover | 换题 |
| L2 | LIFO 顺序 | 机制 | defer 后进先出 | 判 P5 |
| L3 | 覆盖怎么发生 | 边界 | 闭包内再 panic | 判 P6 |
| L4 | 返回几个值 | 权衡 | 只返最后一个 | 判 P6+ |
| L5 | 实战排错 | 实战 | 定位是哪层抛的 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.x 全版本稳定 | 无 | defer LIFO 与 recover 就近语义自 Go1 起未变 `[源码]` |

## 关键代码
```go
// 示意，未验证：内层 recover 先截获，外层拿到 nil
func f() (outer string) {
	defer func() {
		if r := recover(); r != nil { outer = "outer:" + fmt.Sprint(r) }
	}()
	defer func() {
		if r := recover(); r != nil { fmt.Println("inner:", r) } // 先截获
	}()
	panic("boom")
}
```

## 总结与追问预判
- recover 就近优先，defer 内再 panic 会覆盖；recover 一次只返一个值。
- 预判：正确使用姿势 → 见 608；跨协程 → 见 608。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 Go、互斥锁、nil 等专有名词被音译为同音词，已还原为正确术语），技术结论未做更正。
