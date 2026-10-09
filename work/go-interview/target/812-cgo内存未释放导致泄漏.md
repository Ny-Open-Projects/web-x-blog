# 812 cgo 内存未释放导致泄漏

> 分类：Go 互操作 | 难度：L3 | 题型：八股题 | 频率：低 | 关键词：**cgo**/**C.malloc**/**C.free**
> 原文锚点：第 93~97 段「使用 cgo 时没正确释放 C 分配的内存」

## 一句话总述
cgo 调用 C 侧 `malloc`/`C.CString` 分配的内存位于 **C 堆**，**Go 的 GC 管不到**；不显式 `C.free` 就会永久泄漏，且 Go 的 pprof 默认看不见 C 堆占用。

## 面试官视角
- 考察意图：是否知道 Go GC 的边界——只回收 Go 堆，不碰 C 堆。
- 分档：P5 知 cgo 要手动释放；P6 知 `C.CString`/`C.malloc` 配对 `C.free`；P7 知 C 泄漏在 Go pprof 不可见、需 C 侧工具。
- 红旗答案：以为"Go 程序里 malloc 也会被 GC 回收"。
- 惊艳点：点出 **C 堆内存逃逸出 Go GC 视野**——常规 pprof 看不出，得用 `runtime.SetFinalizer` 或 Valgrind/ASan 等 C 侧手段 `[经验]`。

## 主问答
**Q（面试官原话）：** 用 cgo 调 C 代码也会有内存泄漏？
**A：**
1. **结论**：C 侧 `malloc`/`C.CString` 申请的内存活在 C 堆，Go GC 不回收，必须手动 `C.free`。
2. **机制**：`C.CString("x")` 在 C 堆复制一份字符串；用完不 `C.free` 就泄漏。每次调用都泄漏一点，长期运行内存稳步上涨。
3. **边界**：cgo 调用本身有跨语言开销（栈切换、参数拷贝）；更隐蔽的是 **C 泄漏不计入 Go 的 heap profile**，单看 pprof 会误判"Go 侧没问题"。

**加分层：** 可用 `runtime.SetFinalizer` 在 Go 对象被回收前兜底调用 `C.free`，降低遗漏风险（非绝对保证）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | cgo 要手动释放？ | 基础 | C 堆 GC 不管 | P5 |
| L2 | 配对什么？ | 机制 | C.CString↔C.free | P6 |
| L3 | pprof 能看到？ | 盲区 | 看不到 C 堆 | P7 |
| L4 | 怎么查 C 泄漏？ | 工具 | Valgrind/ASan | P7 |
| L5 | 兜底方案？ | 进阶 | SetFinalizer | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.0+（cgo 启用时） | 无 | 答"C 堆内存 Go GC 不回收，C.CString/C.malloc 必须 C.free；且 pprof 默认不可见" |

## 关键代码
```go
import "C"
import "unsafe"

func useCString(s string) {
    cstr := C.CString(s)        // C 堆分配
    defer C.free(unsafe.Pointer(cstr)) // 必须手动释放
    C.some_c_func(cstr)
}

// 错误：只分配不释放 → C 堆永久泄漏
func leak(s string) {
    _ = C.CString(s) // 没有 C.free
}
```

## 总结与追问预判
cgo 泄漏特殊在"逃出 Go GC 视野"——C 堆内存须显式 `C.free`，且常规 pprof 看不见。追问接"pprof 内存诊断"与"goroutine 泄漏总览"。

## ⚠️ 原文纠错
1. 机翻崩坏词归一：`cinputc`→**cgo**；`gatestring`→**GetString**（C 函数名，对应 `C.CString` 思路）；`mallogy`→**malloc**；`c点free`→**C.free**。原文还把 **Go/Go 语言** 多处音译为崩坏词，本卡统一为 Go 语言。事实正确，仅术语崩坏，本卡已归一 `[经验]`。
2. 原文称"include 进来 c 程序、通过 gatestring 申请一块函数"——其意是"用 C 字符串函数申请内存"，已归一为 `C.CString`/`C.malloc` 标准写法。
