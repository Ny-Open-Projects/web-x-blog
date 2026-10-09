# 116 深挖：从 schedtrace 数字到性能结论——调度诊断 Playbook

> 分类：Go/性能 | 难度：L4 | 题型：排查题 | 频率：中 | 关键词：**调度诊断**/**idleprocs**/**线程膨胀**/**队列积压**/**sysmon**/**工作窃取**
> 原文锚点：第 26~36 段「假设我们系统里有十六个处理器，处于 idle 状态的逻辑处理器很多，就说明逻辑处理器没有充分利用…也可以看到全局队列和本地队列当中 goroutine 的堆积情况…采集本身也会消耗性能，线上代码不应该开启」
> [边界] 本文只讲**拿到数字后怎么下结论**：字段含义见 116，GMP 三元组基础见 813，窃取机制见 818，均不重述。

## 思路与架构

把调度诊断拆成**四步闭环**：取数 → 定位 → 归因 → 验证。每一步都有明确判据，避免"看着数字瞎猜"。

```text
Step 1 取数（本地 / 压测环境）
  GODEBUG=schedtrace=300 ./app 2> sched.log
  ↑ 必须 2>，因为 schedtrace 走标准错误

Step 2 定位：先做三道"是非题"
  Q1 idleprocs 是否长期 ≈ gomaxprocs？   → 并行度没吃满
  Q2 runqueue 或 [ ] 是否持续 > 0？      → 有积压
  Q3 threads 是否远超 gomaxprocs 且增长？→ 线程膨胀

Step 3 归因：每个 YES 对应一条因果链
  Q1 YES → 阻塞型任务（IO/锁/channel）或 GOMAXPROCS 设过大
  Q2 YES → 生产 G 速度 > 消费速度，或存在串行瓶颈
  Q3 YES → 系统调用/cgo 阻塞、netpoll 未生效、锁死等

Step 4 验证：改一个变量再采一次，看指标是否按预期移动
  不验证的调优 = 玄学
```

**核心判据表**（这是本卡最值钱的部分）：

```text
指标                     异常表现                     指向的根因
────────────────────────────────────────────────────────────
idleprocs 高             长期 = gomaxprocs             任务被阻塞 / 并发度不足
idleprocs 低 + 队列空    idleprocs=0 但 runqueue=0     健康满载
runqueue 持续 > 0        全局队列不清零                生产过快或全局队列成瓶颈
[ n1 n2 ] 极不均         例如 [ 40 0 ]                 窃取失效 / 绑核 / 单队列热点
threads 单调上涨         远超 P 且不回落               系统调用阻塞 / cgo / 未复用
spinningthreads 长期 > 0 一直有自旋 M                  频繁唤醒，调度抖动
schedticks 差异拉大      [ 5 900 ]                     某 P 空转或某 P 独占热点
```

## 方案取舍

```text
方案一：GODEBUG=schedtrace      （文本快照，秒级）
  + 零依赖、改一个环境变量就能开、可长期落到日志里
  - 只有聚合计数，看不到"哪个 goroutine 慢"；有持续开销
  适用：本地复现、压测环境、粗筛"是不是调度问题"

方案二：runtime/trace + go tool trace（图形，微秒级）
  + 能看到每个 G 的状态迁移、网络等待/同步阻塞/系统调用的时间分解
  - 采集开销更大、文件膨胀快、只能抓一小段
  适用：已定位到调度问题，需要精确到某个 G

方案三：pprof（CPU / mutex / block）
  + 直接给出热点函数与阻塞点，最贴近"改哪行代码"
  - 不是调度视角，看不出 P/M 层面的失衡
  适用：找代码热点与锁竞争

方案四：GODEBUG 之外 —— 直接看 runtime.NumGoroutine / NumCPU
  + 最轻，可长期埋进监控
  - 信息量最少
  适用：线上常驻指标
```

**线上选型的三条纪律**：

```text
1. 线上常驻只留"轻量指标"（NumGoroutine、GC 次数、自定义 gauge）
2. 出问题再按需抓 trace / pprof，抓完立即关闭
3. schedtrace 属于"诊断开关"不是"监控开关"——
   它让 sysmon 无法深睡（源码注释明确），常开 = 白烧 CPU
```

## 答题技巧

```text
1. 先给总纲再展开
   「我一般四步：取数、定位、归因、验证。」
   有方法论的人，面试官会直接少问一半。

2. 背下三条判据，别背字段
   - idleprocs 高  = 没吃满
   - 队列持续非零  = 有积压
   - threads 涨    = 阻塞 / cgo
   字段可以查，判据必须张口就来。

3. 必答的"线上能不能开"要有代价感
   「不能常开。它会阻止 sysmon 深睡，是持续性开销；
     线上改成常驻 NumGoroutine 指标 + 出问题抓 trace。」

4. 主动给一个完整排查故事（最有说服力）
   「某次压测 QPS 上不去，schedtrace 显示 idleprocs 长期 14/16、
     runqueue=0、threads 稳定 —— 说明不是调度问题，是并发度不够；
     把 worker 数从 8 提到 32 后 idleprocs 降到 2，QPS 翻倍。
     反过来如果 threads 一路涨，就该去查系统调用和 cgo。」

5. 收尾一句拔高
   「调度指标是**现象层**，它告诉你'失衡'，
     但'为什么失衡'要回到代码：锁、channel、系统调用、GOMAXPROCS。」
```

**面试高频反问与应答**：

```text
Q：idleprocs 高一定是坏事吗？
A：不一定。任务是 IO 密集型时 P 本来就会大量空闲，
   此时要看的是 threads 与吞吐，而不是把 GOMAXPROCS 调小。

Q：GOMAXPROCS 要不要设成核数？
A：默认就是核数，一般不动。容器里若拿到的不是真实 CPU 配额，
   需要显式设置或用自动化库对齐 cgroup 限额。

Q：schedtrace 和 gctrace 能一起开吗？
A：能，`GODEBUG=schedtrace=500,gctrace=1`，用逗号分隔多个开关。
```
