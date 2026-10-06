# 1025 Singleflight 源码：合并如何只执行一次

> 分类：Go 并发 | 难度：中高 | 题型：源码 | 频率：中高 | 关键词：**Group、call、WaitGroup、map 合并、Do 逻辑**

> 原文锚点：第 36~60 段「Group 结构体(mu+map)、call(wg+val+chan)、Do 判断 key、首个执行其余 wait」

## 一句话总述
核心结构：Group 持有一把锁和一个 map[key]*call；call 内含 WaitGroup、结果值 val 与 channel。Do 进来先加锁查 map：key 不存在→建 call、放入 map、解锁后执行 fn，结束用 WaitGroup.Done 唤醒等待者；key 已存在→不执行 fn，直接 WaitGroup.Wait 等结果，返回同一 val。

## 面试官视角
源码题是加分项。考官期待你讲清「加锁保护 map」「第一个请求写 map 并跑 fn，其余阻塞在 WaitGroup」「fn 结果存进 call.val，等待者共享」。能补一句「Forget 可删除 map 项让同 key 重新执行」更完整。

## 主问答
**Q（面试官原话）：** singleflight 底层是怎么合并请求的？

1. **数据结构**：Group 含 `mu sync.Mutex` 与 `m map[string]*call`；call 含 `wg sync.WaitGroup`、结果 `val/err` 与 `ch chan struct{}`（用于中断/通知）。
2. **首请求路径**：加锁查 map，key 不存在则 new 一个 call 并 `m[key]=c`、解锁；执行 fn，完成后 `c.wg.Done()` 唤醒其他等待者，并把结果写入 `c.val`。
3. **后续请求路径**：map 中已存在该 key，说明有请求在执行，直接 `c.wg.Wait()` 阻塞；fn 结束后拿到 `c.val` 返回，自身不执行 fn。
4. **安全性**：锁保护 map 读写；WaitGroup 保证首请求结束前其余都在等，从而实现「只执行一次、结果共享」。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 核心结构？ | 说不清 Group(mu+map) |
| L2 | 首请求做什么？ | 说不清建 call 跑 fn |
| L3 | 后续请求？ | 说不清 WaitGroup 等 |
| L4 | 结果在哪？ | 说不清 call.val |
| L5 | 怎么重置？ | 说不清 Forget |

## 版本与兼容性
| 结构 | 作用 |
|------|------|
| Group.mu + map | 保护请求合并表 |
| call.wg | 等待首请求完成 |

## 关键代码
```go
// 伪代码逻辑
if c, ok := g.m[key]; ok { c.wg.Wait(); return c.val, c.err, true }
c := new(call); g.m[key] = c
c.val, c.err = fn()
c.wg.Done()
```

## 总结与追问预判
核心：**map[key]*call 去重 + WaitGroup 等待，首请求跑 fn 写 val，其余共享**。追问常接「Forget 怎么用」（见 1025-forget）或「与 CyclicBarrier 区别」（见 1025-cyclicbarrier）。

## ⚠️ 原文纠错
1. 事实核校： [经验] Group(mu+map)、call(wg+val+chan)、Do 查 key/首执行/余等待、结果共享——均正确，本卡为准。
2. 崩坏词归一：源码将 Go/goroutine/WaitGroup/singleflight 等音译为崩坏词；本卡统一为规范术语。
