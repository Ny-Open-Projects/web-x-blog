> 原文锚点：第 6~26 段「我们需要理解 go 中 error 的本质…是一个包含 error 方法 interface…自定义错误类型实现 error 方法…给每种错误定义 code 值…借鉴标准库 FS 包的 PathError（记录 Op/Path/Err）…用类型断言判断是否 *PathError…避免依赖错误信息字符串断言」（error 接口本质/自定义 error+code/PathError 借鉴/errors.Is 类型断言）

## 一句话总述
Go 的 `error` 只是一个 **`Error() string` 接口**，没有异常机制；优雅处理的第一步是**用自定义类型（带 code/message）而非字符串**表达错误，并用 `errors.Is` / `errors.As`（Go 1.13+）做类型断言，而非依赖易变的错误文本去判断「到底是哪种错」。

## 面试官视角
这题考对 error 模型的理解深度。考点：① error 是接口不是值；② 为什么用 code/类型而非字符串判断；③ `errors.Is`/`errors.As` 与「== 比较」「字符串 contain」的区别。能讲出「同类型错误文本可能不同，不能靠文本断言」是高阶信号。

## 主问答
**Q（面试官原话）：** Go 的 error 是什么？怎么优雅地判断错误类型？

**A：**
1. **error 是接口，不是异常**：`type error interface { Error() string }`，任何实现 `Error()` 的类型都是 error。Go 把错误作为**普通返回值**显式传递，调用者先判 `err != nil` 再处理——这种「自主处理」模式是 Go 特色，但易写出大量判错逻辑。
2. **用 code/类型而非字符串**：给每种错误定义 `Code`（如 `CodeServiceUnavailable=1`），自定义类型携 `code+message`；判断时比对 code，而不是比对 `err.Error()` 文本——因为**同一类型错误的文本措辞可能不同**（如中英文/不同上下文），文本断言脆弱。
3. **借鉴标准库 `fs.PathError`**：`os.Open` 返回的错误是 `*fs.PathError{Op, Path, Err}`，把「操作+路径+底层错」一起带上，排查时直接知道「是哪个文件、什么操作失败」，而非满屏 `file not found` 不知所属。
4. **用 `errors.Is`/`errors.As` 做断言（Go 1.13+）**：`errors.Is(err, fs.ErrNotExist)` 判断「是否某类错」（穿透 wrap 链），`errors.As(err, &pe)` 抽取具体类型取 `pe.Path`——比手写 `if e, ok := err.(*fs.PathError)` 更稳，且能跨包装层。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | error 是啥？ | 接口认知 | Error() string 接口，非异常 | 说「是值」算 L1 未过 |
| L2 | 为啥不用字符串判？ | 健壮性 | 同类型文本可能不同 | 答「contains」算 L2 未过 |
| L3 | 标准库咋带上下文？ | PathError | Op/Path/Err 三字段 | 不知算 L3 未过 |
| L4 | Is 和 == 区别？ | wrap 穿透 | Is 穿透包装链，== 不穿 | 说一样算 L4 未过 |
| L5 | As 干啥？ | 抽具体类型 | As 抽取 *PathError 取 Path | 不知算 L5 未过 |

## 版本与兼容性
- `errors.Is` / `errors.As` / `fmt.Errorf("%w")` 均为 **Go 1.13（2019）** 引入；此前靠 `github.com/pkg/errors` 的 `Wrap`/`Cause` + 手写类型断言。
- `==` 比较只适用于**未包装**的哨兵错误（`errors.New`/`ErrNotExist`）；一旦 `fmt.Errorf("%w")` 包装，`==` 失效，必须 `errors.Is`。
- 注意与「`err != nil` 陷阱」（见 509.md`）区分：那张讲「返回 nil 却非 nil 指针」的坑，本卡讲「如何分类断言错误」。

## 总结与追问预判
收口：**error 是接口；用 code/类型分类，用 `errors.Is/As` 断言，绝不靠文本**。预判追问：① 哪些写法不优雅（见 513.md`）；② 怎么 wrap 保存上下文（见 513.md`）。回答时把「同类型错误文本可能不同，文本断言脆弱」抛出，最显经验。

## ⚠️ 原文纠错
源视频转写将 error 接口模型、PathError、类型断言、标准库等术语音译为若干崩坏词，本卡已统一还原为规范术语（error 接口 / *fs.PathError / errors.Is / errors.As / fmt.Errorf 等）。交付卡禁止保留任何原词崩坏写法。

> **[经验]** 面试金句：**「错误文本是给人看的，不是给代码判的。」** 判断错误类型永远用 `errors.Is`/`errors.As` + 自定义类型/哨兵值，不用 `strings.Contains(err.Error(), "...")`。后者在日志国际化、措辞微调时必炸，是新手与老手的分界线。

```go
package main

import (
	"errors"
	"fmt"
	"io/fs"
	"os"
)

// 自定义错误：带 code + message，用 code 分类而非文本
type MyError struct {
	Code    int
	Message string
}

func (e *MyError) Error() string { return e.Message }

const CodeServiceUnavailable = 1

func read(path string) error {
	f, err := os.Open(path) // 返回 *fs.PathError{Op,Path,Err}
	if err != nil {
		// ✅ 用 errors.Is 判断「是否文件不存在」（穿透 wrap 链）
		if errors.Is(err, fs.ErrNotExist) {
			return &MyError{Code: CodeServiceUnavailable, Message: "config missing: " + path}
		}
		// ✅ 用 errors.As 抽取具体类型，取结构化字段
		var pe *fs.PathError
		if errors.As(err, &pe) {
			fmt.Printf("操作=%s 路径=%s 底层=%v\n", pe.Op, pe.Path, pe.Err)
		}
		return err
	}
	defer f.Close()
	return nil
}
```
