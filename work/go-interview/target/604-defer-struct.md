# 604 defer 底层结构体与 defer 栈

> 分类：Go 运行时 | 难度：L3 | 题型：原理题 | 频率：中 | 关键词：**_defer** / **link** / **LIFO** / **堆分配**
> 原文锚点：第 5~57 段「runtime2.go 中 _defer 结构体各字段含义；defer 用链表实现栈，link 头插，后声明先执行」

## 一句话总述
每个 `defer` 语句在运行时封装成一个 `_defer` 结构体，通过 `link` 字段串成**当前 goroutine 的延迟调用栈**（LIFO 链表）；新 defer 头插、函数返回时从栈顶取执行，所以"后声明先执行"。

## 面试官视角
- 意图：考察候选人是否懂 defer 的运行时实现，而非只会"后声明先执行"的结论。
- P5 知道 defer 是链表栈、LIFO；P6 能说清 `_defer` 关键字段（link/sp/pc/fn）；P7 能指出 `link` 头插机制与"后声明先执行"的因果。
- 红旗：以为 defer 用数组/优先队列；把 `heap` 字段理解成"优先级"。
- 惊艳点：指出 `_defer` 在无法开放编码时分配在堆上，`link` 是单向链表而非数组。

## 主问答
**Q（面试官原话）：** defer 的底层数据结构是什么？为什么后声明先执行？
**A：**
1. **结论**：`defer` 封装为 `_defer` 结构体，含 `link`（指向下一个）、`sp`（栈指针）、`pc`（程序计数器）、`fn`（待执行函数）等字段；多个 `_defer` 经 `link` 串成栈，新节点头插。
2. **机制**：执行 `defer` 时调用 `deferproc` 把新 `_defer` 插到链表**头部**；函数返回时 `deferreturn` 从**头部**（即最后插入的）开始取并执行，直到栈空，形成 LIFO `[源码]`。
3. **边界**：`heap` 字段表示这条 `_defer` 记录是否分配在**堆**上（无法开放编码时），并非"优先级/优先队列"；defer 始终是 LIFO 栈，没有按优先级排序的逻辑 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 什么结构 | 基础 | _defer 链表栈 | 判 P5 |
| L2 | 为啥 LIFO | 机制 | link 头插 | 判 P5+ |
| L3 | 关键字段 | 细节 | link/sp/pc/fn | 判 P6 |
| L4 | heap 含义 | 纠偏 | 堆分配非优先级 | 判 P6+ |
| L5 | 与栈帧 | 进阶 | sp 找栈帧变量 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 1.14 ~ 1.23 | `_defer` 字段随版本微调（现代版含 varp/framepc） | 核心字段 link/sp/pc/fn + LIFO 头插长期成立；open-coded defer 自 1.14 起 `[源码]` |

## 关键代码
```go
// 示意，未验证：_defer 结构体（教学简化版，现代 Go 还含 varp/framepc 等）
type _defer struct {
    link    *_defer // 指向下一个，串成 LIFO 栈
    sp      uintptr // defer 所在栈帧的栈指针
    pc      uintptr // 程序计数器，指向待调用的 defer 函数
    fn      func()  // 延迟执行的函数
    started bool    // 是否已开始执行
    heap    bool    // 是否分配在堆上（非优先级）
}
```

## 总结与追问预判
- defer = `_defer` 链表栈 + link 头插 + LIFO。
- 预判：deferproc/deferreturn → 见 604-deferproc-deferreturn；开放编码优化 → 见 604-defer-opencoded。

## ⚠️ 原文纠错
发现一处事实偏差并已更正：源码把 `heap` 字段说成"优先级/优先队列"，实际 `heap` 表示延迟记录是否分配在堆上，defer 是 LIFO 链表栈、无优先队列。其余仅做了 ASR 解码将多组标识符崩坏词（如"deffer"→defer、"勾入进"→goroutine、"runtimetwo点go"→runtime2.go、"opendefer"→openDefer 等）统一还原为规范术语，未做其他技术更正。源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
