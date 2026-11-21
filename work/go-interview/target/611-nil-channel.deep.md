# 611 nil channel 收发关闭语义深挖

## 思路与架构
```text
答题架构：nil channel 行为拆成"收发/关闭"两个动作，每个动作给后果：
- 收发：阻塞；同 goroutine → deadlock，异 goroutine → 仅阻塞等主退
- 关闭：panic(close of nil)
再横向拉 closed channel 做四维度对比(收发/关闭/零值/select)，定位其与 nil 的差异
底层：nil 无 hchan → 收发点无就绪方 → 阻塞；close 对 nil 判空直接 panic
```

## 方案取舍
```text
面试取舍：被问"nil channel 会怎样"先给两个动作后果(收发阻塞/关闭panic)，比罗列更利落。
被问"nil vs closed"直接上四维度对比表，显体系。
避免混淆：反复强调"closed 不是 nil"——这是最高频误点。
```

## 答题技巧
```text
技巧1：一句话封口——"nil 收发阻塞(同goroutine死锁)、关nil panic；closed 收零值、发panic、重复关panic"。
技巧2：用 select 永不选中(nil) vs 可触发(closed)这一对反例，强化区分。
技巧3：举 close 当广播的例子(引 612)，把死知识连到实战。
技巧4：收尾点"一般死锁场景另见 610"(引 610-channel-deadlock-scenarios)，不抢他人地盘。
```

> 边界：channel 基础/select 见 610；closed 行为见 612*`；关闭 panic见 `1019-*`/`1021-*`；本深卡只讲"如何答好 nil/closed 对比题"。

## 细节与核心 API

```go
var nilCh chan int // nil channel
// 在 select 中，向 nil channel 发送或接收会“永远阻塞”且其 case 永远不会被选中
// 利用此特性动态启用/禁用某个分支：
select {
case v := <-nilCh:        // 永不触发
    _ = v
case v := <-realCh:
    use(v)
case <-time.After(time.Second):
    timeout()
}
// 经典用法：多路扇入时，某个输入关闭后将其置为 nil，使 select 跳过该分支
// 注意：向 nil channel 发送在普通语句中会永久阻塞（不是 panic）
```
