---
disableNunjucks: true
title: "913 WaitGroup 实现原理 深挖"
date: 2026-10-10 09:02:18
categories: [Go面试题集]
tags: [Go面试题集]
---

> 覆盖源 9-13 全文：从「用法与坑」到「源码三字段」到「Add/Wait 原子位域操作」的完整实现。主卡已拆成用法、字段布局、原子原理三张，本附录做横向串联与取舍。

## 思路与架构

```mermaid
graph TD
A[WaitGroup] --> B[用法:Add/Done/Wait]
B --> B1[必须传指针:noCopy 防复制]
B --> B2[for 循环变量需值拷贝]
A --> C[字段:noCopy/state/sema]
C --> C1[state 高32 counter]
C --> C2[state 低32 waiter]
C --> C3[sema 信号量]
A --> D[原理:原子+CAS]
D --> D1[Add:delta<<32 加 counter]
D --> D2[Done=Add(-1)]
D --> D3[Wait:增 waiter+CAS 阻塞]
D --> D4[counter=0 唤醒所有]
```

## 方案取舍
- **单 uint64 位域 vs 两字段**：位域用一次原子 CAS 同时管 counter+waiter，比两个独立原子变量+两把锁更省、更一致。
- **CAS 自旋 vs 加锁**：CAS 无锁临界区、竞争低时更快；极端高竞争下仍靠 sema 把等待者挂起，不空转。
- **noCopy 字段**：零成本（编译期 vet + 运行时检测）拦住最常见误用（传值），比运行时救火更稳。

## 答题技巧
- 被问「WaitGroup 原理」先抛三字段再讲位域与 CAS，避免只在用法层打转 [经验]。
- 主动连线 1019（并发陷阱/race）与 errgroup/chan 选型，显出并发编排全局观 [边界]。

## 细节与核心 API

```go
// 内部：counter（剩余任务）、sema（信号量）、waiter（等待数）
var wg sync.WaitGroup
for i := 0; i < 3; i++ {
    wg.Add(1)              // 必须在 go 之前 Add，否则竞态
    go func() {
        defer wg.Done()    // Done == Add(-1)
        work()
    }()
}
wg.Wait()                // 阻塞直到 counter==0
// 陷阱：在 goroutine 内 Add 会与 Wait 竞态；Done 多调用会 panic（counter 负）
// 复用 WaitGroup 前必须等 Wait 返回（不可在 Done 仍在进行时再次 Add）
// 实现等价于：原子操作 counter + 原子信号量休眠/唤醒
```
