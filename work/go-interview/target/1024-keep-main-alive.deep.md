# 1024 主协程永不退出的常驻进程设计深挖

> 分类：Go 并发 / 常驻进程 | 难度：L3 | 题型：深挖 | 频率：中 | 关键词：**常驻进程** / **优雅退出** / **死锁陷阱** / **抢占版本** / **recover**
> 原文锚点：第 1~46 段「5 法卡 main；for死循环空转；channel/nil/空select 阻塞；signal.Notify 推荐；需 recover 防 panic」

## 思路与架构
"主协程不退出"本质是让 main goroutine 永远停在某个同步点上。五法分两类：① 空转/阻塞类（for{}、channel、nil、空 select）——靠 CPU 空转或 channel 永久阻塞；② 信号类（signal.Notify）——靠 OS 信号同步，额外能拿到退出原因。生产选信号类，因为它不浪费 CPU、可优雅关停、可观测退出来源。

## 方案取舍
```text
五法取舍矩阵：
──────────────────────────────────────────────────────────────
方式              原理             CPU 占用   能否拿退出原因   死锁风险
for{}             空转             高          否             无
无缓冲 channel    永久阻塞         低          否             有(无 goroutine)
nil channel       永久阻塞         低          否             有(无 goroutine)
select{}          永久阻塞         低          否             有(无 goroutine)
signal.Notify     OS 信号同步      低          是(推荐)       无(需运行 goroutine)

设计法则：
- 生产用 signal.Notify：低占用 + 可观测 + 可优雅关停
- 纯阻塞法必须已有持续 goroutine，否则 fatal: all goroutines asleep - deadlock
- for{} 仅演示用，空转浪费且需抢占调度兜底
- 常驻业务 goroutine 务必 defer recover，否则 panic 拖垮进程
```

## 答题技巧
```text
面试话术（先分类，再推荐，后避坑）：
1. 分类：空转类(for{}) vs 阻塞类(channel/nil/select{}) vs 信号类(signal.Notify)
2. 推荐：signal.Notify 最优选——低占用、可捕获退出原因、可接优雅关停
3. 避坑1：纯阻塞法须有运行中的 goroutine，否则死锁 fatal
4. 避坑2：for{} 空转占 CPU，且依赖 1.14+ 异步抢占才不饿死其他协程(非 1.4)
5. 收尾：业务 goroutine 配 recover，panic 不拖垮常驻进程
```

> 边界：空 select 死锁细节见 909-empty-select-block；信号捕获与优雅退出见 713-signal-capture、713-graceful-shutdown；nil channel 语义见 610-channel-make-and-nil；无缓冲阻塞见 609-channel-send-recv；抢占版本边界见 1024-for-loop-preempt。本卡只深挖"主协程不退出设计"不重述单机制卡。
