# 1021 安全退出读取循环的两种方式

> 分类：并发模型 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**for-range** / **ok 判断** / **退出**
> 原文锚点：第 26~37 段「关闭后 for-range 自动退出；for-select 用第二返回值 false 退出」

## 一句话总述
读 channel 的循环有两套退出机制：for-range 在 channel 关闭且读完缓冲后自动退出；for-select 用 `v, ok := <-ch` 的 `ok==false` 显式 return 退出。

## 面试官视角
- 意图：会不会正确终结 consumer 循环，避免永久阻塞。
- P5 知两种写法 / P6 说清 for-range 退出条件与 ok 语义 / P7 知不关 channel 会死锁、会选场景。
- 红旗：在 for-select 里漏判 ok 导致死循环；为了退出手动 close 数据 channel。
- 惊艳点：for-range 退出前提是 channel 关闭且缓冲耗尽，否则主协程阻塞检测死锁 `[源码]`。

## 主问答
**Q（面试官原话）：** 怎么让读 channel 的循环正常退出来？
**A：**
1. **结论**：单 channel 用 `for v := range ch`；要混合退出信号用 `for { v, ok := <-ch; if !ok { return } }`。
2. **机制**：for-range 底层收到关闭态且缓冲空即退出；ok 为 false 表示 channel 已关闭且无数据。
3. **边界**：两者都依赖**发送方 close**；若永不 close，range 会一直阻塞直至 runtime 报死锁。
**加分层：** select 多路时别只靠 default，default 会忙轮询；用 done/stop channel 更稳。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 怎么退出 | 概念 | range/ok | 换题 |
| L2 | ok 含义 | 机制 | 关闭且无值 | 判 P5 |
| L3 | 不关后果 | 边界 | 死锁 | 判 P6 |
| L4 | select 写法 | 权衡 | done channel | 判 P6+ |
| L5 | default 陷阱 | 实战 | 忙轮询 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Go 全版本稳定 | 无 | for-range 与 ok 语义长期不变 `[源码]` 语言规范 |

## 关键代码
```go
// 示意，未验证：for-select 用 ok 退出
for {
    v, ok := <-ch
    if !ok {
        return // channel 已关闭且无数据
    }
    fmt.Println(v)
}
```

## 总结与追问预判
- 单路读用 for-range；多路/需混合信号用 `v, ok` 判断退出；退出靠发送方 close。
- 预判：谁来负责 close → 见 1021-close-fanout。

## ⚠️ 原文纠错
未发现事实性技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 利用→nil、勾浪→Go、fullselect→for select、fourrange→for range 等拼写还原），技术结论未做更正。
