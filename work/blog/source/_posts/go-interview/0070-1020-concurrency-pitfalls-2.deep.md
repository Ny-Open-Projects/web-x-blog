---
disableNunjucks: true
title: "1020-concurrency-pitfalls-2.deep"
date: 2026-10-10 08:21:23
categories: [Go面试题集]
tags: [Go面试题集]
---

## 思路与架构
"并发编程误区（二）"本质是把三类**写并发代码时最容易闻不到的陷阱**收敛成一套"嗅觉"：① sync 类型值复制（锁状态不共享）② WaitGroup.Add 时机（Wait 竞态）③ 加解锁配对与调用链重入（漏解锁/fatal）。它和误区(一)的闭包陷阱（1017）互补，共同构成"并发代码自查清单"。

```text
并发三大误区(二) 识别矩阵
  现象                  根因                  识别信号              修复
  计数读出 0            sync 类型值复制       结构体值传/值接收者    传指针/*Mutex 接收者
  结果 < 预期/panic     WaitGroup.Add 在 goroutine 内   Wait 抢在 Add 前    Add 外提
  进程 fatal error       调用链重入同一锁      main→A→B 各加一次    defer 兜底+去重入
  提前 return 后卡死     加解锁不配对         中间分支漏 Unlock      defer mu.Unlock()
```

## 方案取舍
| 误区 | 对应既有卡 | 本卡新增视角 |
| --- | --- | --- |
| sync 值复制 | 913(noCopy)/508(值指针) | 含 Mutex 字段被值传→锁失效计数归零 |
| Add 时机 | 913(Add/Done/Wait) | Add 放 goroutine 内→Wait 竞态 |
| 重入死锁 | 925(不可重入/fatal) | 重入常藏调用链而非显式自锁 |
| 加解锁配对 | 925(重复 Unlock panic) | defer 兜 early-return |

**取舍结论**：这些误区单独看都在 913/925 有机制铺垫，本卡价值在"把分散的机制聚成现场可套的嗅觉"——写并发代码前先扫一遍"值复制/Add 时机/锁配对"。

**分层边界**：闭包/循环变量误区(一)在 1017；race detector 在 1018/1019；本卡只收 sync 值复制+WaitGroup 时机+锁配对三块 [边界]。

## 答题技巧
1. **先报框架**：开口"并发误区主要三类——值复制、WaitGroup 时机、锁配对"，立显体系。
2. **每个给最小反例**：counter 读 0 / Add 在内 <预期 / 调用链重入 fatal，比背名词更有说服力。
3. **关联误区(一)**：顺带提"闭包循环变量(1017)也是并发高频坑"，显知识网。
4. **修复一句话**：值复制→传指针；Add→外提；锁→defer 兜底+去重入。
5. **避坑**：不把"锁复制"当"浅拷贝无所谓"；不说"Add 先 go 后也行"；不忽略调用链里的重复加锁。

## 细节与核心 API

**① sync 类型值复制：含 Mutex 字段被值传 → 锁失效、计数读出 0**：

```go
type Counter struct{ mu sync.Mutex; n int }
func (c Counter) Inc() { c.mu.Lock(); c.n++; c.mu.Unlock() } // 值接收者：复制出独立锁，互不共享
func (c *Counter) Inc() { c.mu.Lock(); defer c.mu.Unlock(); c.n++ } // 修复：指针接收者
```

**② WaitGroup.Add 时机：Add 放 goroutine 内 → Wait 抢在 Add 前 → 计数 0 或 panic**：

```go
var wg sync.WaitGroup
for i := 0; i < N; i++ {
    wg.Add(1) // 正确：go 之前 Add（错误写法：写在 goroutine 内）
    go func() { defer wg.Done(); work() }()
}
wg.Wait()
```

**③ 调用链重入同一锁 → `fatal error: all goroutines are deadlocked`**（重入常藏调用链而非显式自锁）：

```go
func A(mu *sync.Mutex) { mu.Lock(); defer mu.Unlock(); B(mu) } // A 已持锁
func B(mu *sync.Mutex) { /* 不能再 Lock 同一把锁，否则死锁 */ }
// 修复：defer 兜底 + 去重入，或调用链上只持一次锁、内部函数不重复加
```

**④ 加解锁不配对：中间分支漏 Unlock → 提前 return 后卡死**：

```go
mu.Lock()
if err != nil { return } // 错误：漏 Unlock
defer mu.Unlock()        // 正确：defer 兜底 early-return
```

> 边界：闭包/循环变量误区(一)见 1017；race detector 见 1018/1019；sync noCopy 见 913；不可重入见 925。
