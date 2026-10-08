# 604 deferproc 与 deferreturn

> 分类：Go 运行时 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**deferproc** / **deferreturn** / **延迟调用栈** / **panic 捕获**
> 原文锚点：第 58~75 段「deferproc 封装 _defer 并头插入 goroutine defer 栈；deferreturn 函数返回时执行；执行时捕获 panic」

## 一句话总述
`defer` 语句编译为对 `runtime.deferproc` 的调用（封装 `_defer` 并头插当前 goroutine 的延迟栈），函数返回处插入 `runtime.deferreturn`（从栈顶取 `_defer` 执行）；defer 执行期间能捕获 panic，是 recover 的落点。

## 面试官视角
- 意图：考察候选人对 defer 编译产物的了解（红旗：以为 defer 是语言魔法、不知道编译成 runtime 调用）。
- P5 知道 defer 编译成 runtime 函数；P6 能说清 deferproc 与 deferreturn 各自职责；P7 能指出 defer 执行时捕获 panic 正是 recover 生效的机理。
- 红旗：以为 deferreturn 是"返回 defer"这种字面意思；不知道 defer 栈是 per-goroutine。
- 惊艳点：指出 defer 栈挂在 goroutine 上（不是线程/全局），所以不同 goroutine 的 defer 互不干扰。

## 主问答
**Q（面试官原话）：** defer 在运行时是怎么被调度执行的？
**A：**
1. **结论**：遇到 `defer` 编译为 `runtime.deferproc`（把待执行函数+参数封装成 `_defer` 头插当前 goroutine 延迟栈）；函数返回处编译器插入 `runtime.deferreturn`（循环从栈顶取 `_defer` 执行并弹栈）。
2. **机制**：`deferproc` 创建 `_defer` 并链到 goroutine 的 defer 链头；`deferreturn` 在 ret 指令前被调用，反复执行直到栈空；defer 函数执行期间若发生 panic，运行时会在此捕获并交还 `recover` `[源码]`。
3. **边界**：defer 栈是 **goroutine 级**的，每个 goroutine 独立拥有，函数返回即清空；所以跨 goroutine 不会共享 defer，子 goroutine 的 defer 不会在父 goroutine 返回时执行 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 编译成啥 | 基础 | deferproc/deferreturn | 判 P5 |
| L2 | 各自职责 | 机制 | 头插 / 取执行 | 判 P5+ |
| L3 | panic 关系 | 进阶 | 执行时捕获 panic | 判 P6 |
| L4 | 挂在哪 | 细节 | goroutine 级 | 判 P6+ |
| L5 | recover 机理 | 深度 | defer 捕获点 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.x | 无 | deferproc/deferreturn 是 defer 的核心运行时函数，长期成立；二者均为 runtime 内部调用，外部不可直接调用 `[源码]` |

## 关键代码
```go
// 示意，未验证：defer 的编译产物（概念映射）
func example() {
    defer fmt.Println("done") // 编译器插入: runtime.deferproc(...)
    _ = 1 + 1
    // 返回处编译器插入: runtime.deferreturn(...)  // 从 defer 栈顶取 "done" 执行
}
```

## 总结与追问预判
- defer 落点是 deferproc（注册）+ deferreturn（执行），panic 捕获在其间。
- 预判：_defer 结构 → 见 604-defer-struct；开放编码 → 见 604-defer-opencoded。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对 deferproc/deferreturn 的职责与"defer 栈挂在 goroutine"的描述；仅做了 ASR 解码将多组标识符崩坏词（如"defferPROC"→deferproc、"deruuntime点deferreturn"→runtime.deferreturn、"勾入进"→goroutine 等）统一还原为规范术语，技术结论未做更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
