# 913 WaitGroup 用法与两个经典坑

> 分类：Go 并发/sync | 难度：L2 | 题型：用法题 | 频率：高 | 关键词：**Add/Done/Wait**/**必须传指针**/**noCopy**/**循环变量陷阱**
> 原文锚点：第 1~23、51~52 段「WaitGroup 用法；传值拷贝 panic；for 循环变量估值陷阱」

## 一句话总述
WaitGroup 用 **Add(delta) 加计数、Done() 减一(=Add(-1))、Wait() 阻塞到归零** 来等一组 goroutine；两坑必知：**必须传指针**（否则 noCopy 复制检测报 panic）、**for 循环里 go 需值拷贝循环变量**否则全打印同一值。

## 面试官视角
- 考察意图：是否真写过 WaitGroup，知不知道传值与循环变量两个高频 panic/bug。
- 分档：P5 知 Add/Done/Wait 语义；P6 知必须传指针、循环变量要拷贝；P7 知 noCopy 的运行时复制检测、能讲清变量估值时刻。
- 红旗答案：传值 WaitGroup（复制 panic）；在 for 里直接 `go func(){use i}()` 不拷贝 i。
- 惊艳点：点出「不传指针触发 noCopy 字段的复制检测，运行时直接报错」，以及「for 变量估值在循环结束后、需 `i:=i` 值拷贝」 [经验]。

## 主问答
**Q（面试官原话）：** WaitGroup 怎么用？有哪些坑？
**A：**
1. **三方法语义**：启动异步任务前 `Add(1)` 增计数；任务完成 `Done()`（即 `Add(-1)`）减一；主协程 `Wait()` **阻塞直到计数归零**才继续——用来等一组 goroutine 全部完成 [经验]。
2. **坑一：必须传指针**：WaitGroup 内部要改计数器，传值会触发结构体里的 **noCopy 复制检测**、运行时直接 panic（deadlock/复制报错）；函数参数与接收者都必须是 `*WaitGroup` [经验]。
3. **坑二：循环变量估值**：`for` 里 `go func(){ use i }()` 直接捕获循环变量，函数估值时刻可能在循环结束后、i 已是终值（如 10），导致全部打印同一值；需 `i := i` **值拷贝**再捕获 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 三方法干嘛？ | 语义 | Add 增/Done 减/Wait 等 | P5 |
| L2 | 为何传指针？ | 复制检测 | noCopy 检测拷贝即 panic | P6 |
| L3 | 循环变量坑？ | 闭包 | 估值在循环后、需值拷贝 | P6 |
| L4 | 不配对会怎样？ | 误用 | Add/Done 不配→死等/负计数 | P7 |
| L5 | 替代方案？ | 选型 | errgroup/chan 关闭信号 | P7+ |

## 版本与兼容性
- WaitGroup 属标准库 `sync`，跨版本稳定；Add/Done 配对与 race 检测见 1019（只引不重述 race detector）[边界]。

## 总结与追问预判
用法与坑讲完，内部怎么用「一个 uint64 + 信号量」实现计数与唤醒，是下一张重点。

## ⚠️ 原文纠错
1. 事实核校： [经验] 三方法语义、传指针否则 noCopy 复制检测 panic、for 循环变量估值陷阱需值拷贝——均正确。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语（WaitGroup、计数器、等待队列、goroutine、复制检测等）。

```go
var wg sync.WaitGroup
for i := 0; i < 10; i++ {
    wg.Add(1)
    i := i // 值拷贝，避免闭包捕获同一循环变量
    go func() {
        defer wg.Done()
        fmt.Println(i)
    }()
}
wg.Wait() // 必须传 *WaitGroup；传值会触发 noCopy 复制检测 panic
```
