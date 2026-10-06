# 805 runtime.main 流程：从 init 到用户 main 再到退出

> 分类：运行时 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**runtime.main** / **init 顺序** / **启动 GC**
> 原文锚点：第 93~95 段「runtime.main 执行 runtime init、启动 GC、用户包 init、用户 main…退出前清理」

## 一句话总述
`runtime.main` 是 Go 世界的真正"main"：先做 runtime 自身初始化、开启 GC，再按依赖顺序跑全部包的 `init()`，最后才调用用户 `main`；`main` 返回或异常后运行时统一清理资源再退出。

## 面试官视角
- 意图：是否掌握"在用户 main 之前还发生了一大堆事"以及 init 顺序。
- P5 知 init 先于 main / P6 能说 runtime.main 四步 + GC 开启点 / P7 知 init 依赖顺序与退出清理细节。
- 红旗：以为 main 是进程第一个函数；以为 init 顺序可随意。
- 惊艳点：所有包 init 在 main 前跑完，GC 在 runtime.main 才 enable —— 验证 `go doc` init 语义 `[源码]`。

## 主问答
**Q（面试官原话）：** 用户 `main` 函数之前，Go 还做了什么？退出时又做了什么？
**A：**
1. **结论**：`runtime.main` 先完成 runtime 初始化、启动 GC，再执行全部包的 `init()`，最后才进用户 `main`。
2. **机制**：`init` 按包依赖顺序自动执行；GC 在 `runtime.main` 内通过 `gcenable` 正式开启（之前 schedinit 只设参数）。
3. **边界**：用户 `main` 返回或程序异常时，运行时清理资源（关闭 goroutine、释放内存）后退出；与 C 的 `main` 不同，Go 在用户 main 前后都有运行时接管。
**加分层：** 和 C 比，Go 的 main 被 runtime 包裹，前后都有运行时职责，这也是 Go 程序"启动稍慢"的根因之一。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | main 前干啥 | 概念 | init | 换题 |
| L2 | 四步顺序 | 机制 | init→main | 判 P5 |
| L3 | GC 何时启 | 边界 | runtime.main | 判 P6 |
| L4 | init 顺序 | 权衡 | 依赖序 | 判 P6+ |
| L5 | 退出清理 | 实战 | 关 g/释放 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 `[源码]` | 无 | init 先于 main、GC 在 runtime.main 启，长期成立 |

## 关键代码
```go
// 示意，未验证：runtime.main 主干顺序（概念，非完整源码）
// runtime_main() {
//   runtimeinit(); gcenable()        // 开 GC
//   // 执行所有包 init()
//   main_main()                      // 用户 main
//   // 退出清理：关闭 goroutine、释放内存
// }
```

## 总结与追问预判
- runtime.main：runtime 初始化→开 GC→全包 init→用户 main→清理退出；与 C main 不同在于被运行时包裹。
- 预判：入口汇编 → 见 805-rt0-entry-asm；schedinit → 见 805-schedinit。

## ⚠️ 原文纠错
原文第 124 段称"main 函数是程序的入口点，它是程序第一个被执行的函数"不准确：严格地说，在用户 `main` 之前 `runtime.main` 及所有包的 `init()` 都已先执行，`main` 是"用户代码入口"而非进程第一个被执行的函数。其余流程（runtime 初始化、启动 GC、用户包 init、退出前清理资源）表述正确。机翻解码：勾浪→Go、魅影→main、勾入t→goroutine。
