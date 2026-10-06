# 813 g 的 panic/defer 与阻塞原因字段

> 分类：并发模型 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**_defer** / **panic** / **waitreason** / **parkingOnChan**
> 原文锚点：第 28 段、59~67 段、124~132 段「defer 指向当前 g 的延迟调用…waitsince 表示被阻塞的近似时间」

## 一句话总述
g._defer 指向本 G 的 defer 链表头、g.panic 指向 panic 链表；waitsince/waitreason 记录阻塞时间与原因；parkingOnChan/activeStackChans 标记 channel 操作相关的栈安全点 `[源码]` runtime2.go。

## 面试官视角
- 考察意图：是否知道 defer/panic 在运行时是挂在 G 上的链表
- P5 知道 _defer 是 defer 链 / P6 讲清 waitreason 枚举与调度统计 / P7 讲 parkingOnChan 与栈收缩安全点
- 红旗：认为 defer 存在栈上（实为堆上链表挂 G）；答不出 waitsince 用途
- 惊艳点：defer 记录以链表挂在 G 上，函数返回逐节点执行，可跨栈增长 `[源码]` runtime/panic.go

## 主问答
**Q：** G 上那些"控制流/阻塞"字段分别干嘛？
**A：**
1. **_defer / panic**：_defer 指向 defer 链表头，panic 指向当前 panic 链表，随 G 生命周期 `[源码]`。
2. **waitsince / waitreason**：waitsince 记被阻塞近似时刻，waitreason 是等待原因枚举(IO/chan/睡眠等) `[源码]`。
3. **parkingOnChan / activeStackChans**：标记即将在 channel 操作休眠、或栈被通道引用，用于栈收缩安全点 `[源码]`。
**加分层：** waitreason 仅当状态为 `_Gwaiting` 时有效，供调试与调度统计。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | _defer 是什么 | 概念 | G 上的 defer 链 | 换题 |
| L2 | waitreason 用途 | 机制 | 阻塞原因统计/诊断 | 判 P5 |
| L3 | parkingOnChan 干嘛 | 边界 | 标 channel 休眠的安全点 | 判 P6 |
| L4 | 为何 activeStackChans | 权衡 | 防栈收缩时通道访问冲突 | 判 P6+ |
| L5 | 生产排查阻塞 G | 实战 | 看 waitreason 定位卡点 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| go1.20+ 稳定 | _defer 链表结构长期未变 `[存疑]` | 答"defer/panic 链表挂 G，waitreason 记原因"即可 |

## 关键代码
```go
// 示意，未验证：g 的控制流/阻塞字段（节选）
type g struct {
	_defer         *_defer    // 本 G 的 defer 链表头
	panic          *_panic    // 当前 panic 链表
	waitsince      int64      // 阻塞近似时刻
	waitreason     waitReason // 等待原因枚举
	parkingOnChan  bool       // 即将在 channel 操作休眠
	activeStackChans bool      // 栈被通道引用
}
```

## ⚠️ 原文纠错
未发现技术错误。核对范围：通读全文并重点核对代码 API 与版本相关行为；仅做了机翻解码（如 勾浪→Go、勾入进→goroutine 等拼写还原），技术结论未做更正。

## 总结与追问预判
- defer/panic 以链表挂在 G 上；waitsince/waitreason 支撑阻塞诊断；parkingOnChan 保栈收缩安全。
- 下一题接「M 的剩余字段与自旋」（见 815-m-spin-locks-blocked）。
