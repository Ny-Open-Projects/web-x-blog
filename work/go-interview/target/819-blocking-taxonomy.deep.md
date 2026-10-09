# 819 阻塞分类学与「G 睡谁不睡」深挖

> 覆盖源 8-19 的机制延伸：阻塞的分类学（G 阻塞 vs M 阻塞）、syscall 全生命周期与 sysmon 接管、netpoller 为什么让网络 IO 不算「真阻塞」、waitreason 的线上用法。主卡已给四类阻塞，本附录做分类与机制深挖。

## 思路与架构

```text
阻塞的分类学: 睡的是 G 还是 M?
├─ G 阻塞 (M 醒着, 换 G 继续跑)
│   ├─ channel 收发阻塞 -> gopark, G 挂等待队列
│   ├─ 锁/WaitGroup/Cond/select -> 同上
│   ├─ time.Sleep -> G 挂定时器堆
│   └─ 网络 IO -> netpoller 托管, G 挂起 M 不睡
├─ M 阻塞 (G+M 一起陷进去, P 必须被移交)
│   ├─ 文件 IO / cgo / 重 syscall
│   ├─ 流程: 进 syscall 前 tryRetake P 交其他 M
│   │   -> 返回后找不回 P 则 G 进全局队列
│   └─ 兜底: sysmon 周期扫描, 超 10ms+ 强制 retake
└─ 全局性暂停 (所有人一起停)
    └─ STW (GC 两短停) / 1.8 前更重
```

## 方案取舍
- **「G 阻塞 vs M 阻塞」是本题主的隐藏主线**：channel/锁/Sleep 阻塞的是 **G**（用户态挂起，M 转身跑别的 G，零 CPU 浪费）；文件 syscall 阻塞的是 **M**（线程陷进内核，Go 想管也管不了内核）——所以调度器的重点动作是**把 P 从这个 M 手里抢救出来**。答「哪些情况阻塞」只列清单不分类，等于没答到调度层 [经验]。
- **netpoller 让网络 IO 退出 M 阻塞行列**：同样是「等数据」，磁盘 IO 要进内核等（M 阻塞），网络 IO 被 netpoller（epoll/kqueue）托管——G 挂到网络轮询器、M 立即回来跑别的 G，数据就绪后 G 重新入队。**「为什么 Go 写高并发网络服务不用协程池」的答案就在这**：阻塞语义被运行时吃掉了。这也解释了文件 IO 密集型服务与网络 IO 密集型服务的调参差异（见 `1833-io-model-matrix.deep.md`）[经验]。
- **syscall 的 sysmon 兜底与超时阈值**：M 进 syscall 前已尽力移交 P；但若一直没交出去，**sysmon** 以 ≥20µs 周期扫描，发现某 P 的 M 在 syscall 超过约 10ms 且队列有待跑 G，强制 retake P。这条「10ms 线」解释了两个现象：① 大量慢 syscall 会把 P 抢得七零八落、syscall 返回后 G 大量进全局队列；② cgo 调用（同属 M 阻塞）密集的服务要显式调 GOMAXPROCS 评估 P 配额 [经验]。
- **waitreason 的线上用法**：`g.waitreason` 把「睡在哪」变成可枚举字段——`GODEBUG=schedtrace` 看宏观、`runtime/pprof` 的 block profile 看热点（channel/锁的等待时长分布）、`go tool trace` 看时间线。排查「服务 QPS 掉了 CPU 却闲」类问题，先问 waitreason：大量 G 睡在 `chan receive` = 上游断了；睡在 `sync.Mutex` = 锁竞争热点——**从枚举直接定位到代码位置** [经验]。

## 答题技巧
- 报四类阻塞后主动升维：「真正要分的是 G 阻塞还是 M 阻塞——前者换 G，后者换 P」——分类学一句定调 [经验]。
- 用「同样是等」做对比：网络等（netpoller 托管）不睡 M、磁盘等（syscall）睡 M——差异即 Go 高并发网络服务的根基 [经验]。
- 被问「syscall 久了会怎样」→ sysmon 10ms 线强制 retake P + G 进全局队列——机制到参数层 [经验]。
- 被问「线上怎么发现阻塞」→ waitreason 枚举 + block profile + trace 三件套，报具体工具名 [经验]。
- 主动边界到 `819-gmp-blocking-cases`（四类主线）、`1006-gmp-resource-tuning.deep`（调度资源调参）、`809-hybrid-barrier-stack-norescan`（1.8 混合写屏障）、`1833-sync-vs-async-io`（同步异步判据）、`116-sched-diagnose-playbook.deep`（schedtrace 诊断），构成「调度器」专题 [边界]。
