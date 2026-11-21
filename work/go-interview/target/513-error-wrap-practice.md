# 513 优雅错误处理三纪律（wrap/return nil/仅最外层日志）

> 分类：Go 错误处理 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**errors.Wrap**/**上下文**/**返回nil**/**调用链**/**日志**

> 原文锚点：第 48~53 段「如果函数返回的错误不打算处理，需要用 errors.Wrap/errors.Wrapf 保存堆栈（如文件不存在包路径）…一旦确定处理方案，错误就不再是错误，返回 nil（如降级成功）…一般最外层才用日志保存错误，调用链中通过返回 error 传递」（优雅实践：wrap 保存堆栈/确定处理返回 nil/最外层记日志）

## 一句话总述
优雅错误处理的三条纪律：**① 不打算处理就 `wrap` 保存上下文与堆栈**（如把文件路径包进错误）；**② 一旦确定处理方案（如降级成功），错误就「消失」，返回 nil**；**③ 错误在调用链中只靠 `return` 传递，日志只在最外层记一次**。

## 面试官视角
这题是 error 处理的「收口纪律」，考边界判断。考点：① wrap 的时机与目的（加上下文/堆栈，非吞错）；② 「确定处理就返回 nil」的反直觉点（降级≠错误）；③ 「日志只放最外层」的单一职责。能讲清「错误消失 vs 错误传递」的边界，是架构级信号。

## 主问答
**Q（面试官原话）：** 实际项目里错误处理有什么经验纪律？

**A：**
1. **不处理就 wrap，加上下文**：中间层若不能消错，用 `errors.Wrap(err, "read config")` 或 `fmt.Errorf("read config %s: %w", path, err)` 把**路径/操作/ID** 包进错误链，保留底层错且叠加位置信息——上层一次拿到完整链路，无需每层拼字符串。
2. **确定处理就返回 nil**：一旦你用降级/默认值/重试等手段「消化」了错误，它就不再是错误，**应返回 nil** 而非原 err。例如读缓存失败→走 DB 成功，调用方不应再看到那个缓存错误。反之若没真消化（只是记了日志），必须继续 return，不能「记而不返」。
3. **日志只在最外层**：调用链中间层**只 return 不记日志**（避免重复/责任模糊），由最外层（main/HTTP handler/goroutine 顶层）统一记日志+决定告警。这样「错误被处理一次、记录一次」。
4. **wrap 不等于吞错**：wrap 是「附加信息继续上抛」，与「吞掉 return nil」相反；判断标准是「我是否真的解决了这个错误」。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 不处理咋办？ | wrap 纪律 | Wrap/WithMessage 加上下文上抛 | 说「记日志」算 L1 未过 |
| L2 | 降级成功返啥？ | 错误消失 | 真消化→返回 nil | 答「返原 err」算 L2 未过 |
| L3 | 日志放哪层？ | 单一职责 | 最外层记，中层只 return | 每层记算 L3 未过 |
| L4 | wrap 是吞错吗？ | 概念边界 | wrap=附加信息上抛≠nil | 混淆算 L4 未过 |
| L5 | %w 还是 pkg/errors？ | 版本演进 | Go1.13+ 用 %w 标准库 | 只会老库算 L5 未过 |

## 版本与兼容性
- 包装：`github.com/pkg/errors` 的 `Wrap/Wrapf`（历史），**Go 1.13+ 推荐 `fmt.Errorf("...: %w", err)`**——标准库、可被 `errors.Is/As` 穿透。
- `Wrap` 会附调用栈（pkg/errors 特色）；`%w` 本身不附栈，需要栈时可用 `runtime` 或在最外层 `debug.PrintStack()` 辅助。
- 与「错误日志规范」（`123-error-log.md`）配合：中层 wrap 传递、最外层用结构化日志（含 traceID）落盘。

## 关键代码

```go
// 片段：错误包装实战（load/cache 等外部辅助见工程）

import (
	"errors"
	"fmt"
)

// 不处理：wrap 上抛，带文件路径上下文（Go1.13+ 标准库写法）
func readConfig(path string) error {
	cfg, err := load(path)
	if err != nil {
		return fmt.Errorf("load config %s: %w", path, err) // 叠加位置，保留底层
	}
	_ = cfg
	return nil
}

// 确定处理（降级）：错误被消化，返回 nil
func getWithFallback(key string) (string, error) {
	v, err := cache.Get(key)
	if err != nil {
		v, err = db.Get(key) // 降级到 DB
		if err != nil {
			return "", err // 降级也失败，才上抛
		}
		// 降级成功：错误已消化，不返回原 err
	}
	return v, nil
}

// 最外层：统一记日志一次
func main() {
	if err := readConfig("/etc/app.yaml"); err != nil {
		if errors.Is(err, errNotFound) {
			fmt.Println("config missing, use default:", err)
			return
		}
		fmt.Println("fatal:", err) // 只此一处记日志
	}
}
```

## 总结与追问预判
收口：**不处理→wrap 上抛（带上下文）；真消化→返回 nil；日志只最外层**。预判追问：① error 本质与断言（见 513.md`）；② 反模式对照（见 513.md`）。回答时把「降级成功返回 nil」这个反直觉点讲透，最显工程成熟度——多数人卡在「错误必须一路返回」，不懂「被消化即消失」。

## ⚠️ 原文纠错
源视频转写将 error 包装、堆栈、降级、最外层等术语音译为若干崩坏词，本卡已统一还原为规范术语（error / errors.Wrap / fmt.Errorf / 堆栈 / 降级 / 最外层 等）。交付卡禁止保留任何原词崩坏写法。

> **[经验]** 「**确定处理就返回 nil**」是很多人想不通的点：他们以为「出了错就一定要把 err 传上去」。正确判据是——**我有没有真的解决了这个错误？** 降级/默认值/重试成功 = 解决了 = 返回 nil；只是记了日志没解决 = 必须继续 return。这条分清「错误传递」与「错误处理」的边界，是 senior 标志。
