# 608 panic/recover 的正确使用姿势

> 分类：错误处理 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**容忍度** / **error 与 exception** / **简化错误传播**
> 原文锚点：第 99~154 段「依应用对 panic 的忍受度决定…公共包返回 error…用 panic/recover 简化多步调用」

## 一句话总述
是否 recover 取决于程序对崩溃的容忍度：常驻服务应在入口兜底，初始化致命依赖应主动 panic；公共包优先返回 error；也可用 panic/recover 把多步调用的错误判断收敛到一处。

## 面试官视角
- **考察意图**：是否具备工程判断而非教条式"永远 recover"。
- **P5** 知服务入口 recover / **P6** 能区分 error 与 exception、知公共包不随意 panic / **P7** 有真实兜底与误用教训。
- **红旗**：说"所有函数都加 recover"；把业务逻辑错误用 panic 抛出。
- **惊艳点**：标准库 `encoding/json` 用 panic 标记 default 分支的潜在 bug，而非普通错误路径 —— 验证：`grep -n panic src/encoding/json/decode.go`，go1.26.5 `[源码]`。

## 主问答
**Q（面试官原话）：** 是不是该在每个函数加 recover 防崩？
**A：**
1. **结论**：不该。按崩溃容忍度决定：HTTP 服务入口 recover 保活，CLI 偶尔崩可接受。
2. **机制**：致命依赖（连不上 DB）应在启动时 panic 早退；业务错误用 error 返回，让调用方决策。
3. **边界**：公共包 panic 会拖垮未知调用方，应返回 error；panic 只用于不可恢复/潜在 bug 提示。
**加分层：** recover 简化多步调用是把"每步判错返回"改成"内部 panic、外层统一 recover"，代价是流程可读性下降，慎用。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 何时 recover | 概念 | 服务入口兜底 | 换题 |
| L2 | error vs panic | 机制 | 业务错用 error | 判 P5 |
| L3 | 公共包为何慎 | 边界 | panic 拖垮调用方 | 判 P6 |
| L4 | 简化多步取舍 | 权衡 | 可读性换简洁 | 判 P6+ |
| L5 | 真实误用教训 | 实战 | 过度 recover 藏 bug | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.x 全版本稳定 | 无 | 使用哲学与标准库用法长期一致 `[经验]` |

## 关键代码
```go
// 示意，未验证：多步调用错误收敛到外层 recover
func run() error {
	var err error
	defer func() {
		if r := recover(); r != nil { err = toError(r) } // 把 panic 转 error
	}()
	step1() // 内部出错时 panic(err)
	step2()
	return err
}
```

## 总结与追问预判
- 按容忍度决定 recover；公共包返回 error；panic 仅用于不可恢复/潜在 bug。
- 预判：跨协程兜底 → 见 608；机制细节 → 见 608。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 Go、互斥锁、nil 等专有名词被音译为同音词，已还原为正确术语），技术结论未做更正。
