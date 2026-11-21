# 对话版 · 第 2 章 并发编程与 JUC（一面后半 + 二面，约 25 分钟）

**【面试官】** 聊并发。先说说线程池的核心参数和任务提交后的执行流程？

**【面试者】** 七参数：corePoolSize、maximumPoolSize、keepAliveTime+unit、workQueue、threadFactory、handler（+name）。流程口诀：先核心、再队列、后非核心、最后拒绝——工作线程数 < core 直接建线程执行；到 core 任务入队；队列满且线程数 < max 建非核心线程；都满执行拒绝策略。另外本机做过实证：core=2/max=4/queue=2，前 2 个占核心、第 3~4 个入队、第 5~6 个创建非核心线程、第 7 个被 AbortPolicy 拒绝——顺序是死记不出来的，跑一遍就有体感。

**【面试官】** 四种拒绝策略怎么选？

**【面试者】** AbortPolicy 抛异常（默认，快速失败）；CallerRunsPolicy 让提交线程自己跑——**天然反压**，适合能接受提交侧变慢的场景；Discard 丢新任务；DiscardOldest 丢最老。我的实践：核心链路用自定义"延迟 1 秒再 CallerRuns"，避免调用线程被立即拖死。

**【面试官】** 核心线程数怎么定？

**【面试者】** 反对背"CPU 核数+1"：公式 N ≈ C × U × (1 + W/C) 只是起点（IO 密集线程数远大于核数），**正确答案是压测**：调到 RT 达标且 CPU 未饱和的平衡点。更进一步用动态线程池——参数进配置中心，运行时 setCorePoolSize 热调整（美团方案），参数是治理出来的不是算出来的。

**【评注】** ✅ "反对背公式+动态化" 是标准 P7 表达。

**【面试官】** volatile 的语义？能保证 count++ 吗？

**【面试者】** 可见性 + 有序性，不保证原子性——count++ 是读改写三步，volatile 拦不住，要 AtomicLong 或锁。可见性底层是 lock 前缀指令 + MESI 缓存失效；有序性靠内存屏障。本机做过对照实验：volatile 标志位另一线程 2 秒内看到写入；**去掉 volatile 后等待线程自旋 9 分钟都没看见写**（CPU 跑满 325 秒）——可见性问题不是理论，是确定性 bug。

**【面试官】** synchronized 的锁升级过程？

**【面试者】** 无锁 → 偏向锁（记线程 ID，此后同线程免 CAS）→ 轻量级（CAS 自旋，栈上 Lock Record）→ 重量级（OS 互斥量，内核态切换）。版本时间线要背：**JDK15 禁用+废弃（JEP 374），JDK18 标志废弃，JDK21 彻底移除——本机实测 `-XX:+UseBiasedLocking` 直接报 Unrecognized VM option**。撤销偏向要全局安全点、批量重偏向 20/40 这些细节说明我读过不止表面。

**【面试官】** CAS 是什么？ABA 怎么解决？

**【面试者】** Compare-And-Swap，CPU 原子指令（lock cmpxchg）。三坑：ABA——值 A→B→A 过程 CAS 察觉不到，加版本号（AtomicStampedReference/DB 乐观锁 version）；自旋开销——竞争激烈空转烧 CPU，LongAdder 分段到 Cell[] 分散热点；单变量——多变量 CAS 要封装成对象用 AtomicReference。

**【面试官】** LongAdder 为什么比 AtomicLong 快？

**【面试者】** AtomicLong 所有线程 CAS 同一个 value，热点竞争；LongAdder 先 CAS base，失败就散到 Cell[] 数组（按线程 hash 探测），sum() 时汇总。读弱写强：sum 是近似快照。本机实证：8 线程×2500 AtomicLong CAS 精确 20000 无丢失——正确性没问题，LongAdder 买的是吞吐不是精度。

**【面试官】** ThreadLocal 在线程池里为什么会串数据？

**【面试者】** 线程复用，上一个请求 set 的值没清理，下一个请求读到旧值（用户 A 串到 B）。三层解法：业务 finally remove；框架拦截器统一清理；线程池层用 TTL 装饰任务（提交捕获、执行回放、结束恢复）。原理上 key 是弱引用，外部引用消失+GC 后 key 被回收（本机实证 WeakReference 场景），value 有泄漏风险所以必须 remove。

**【面试官】** AQS 讲讲？你读的哪个版本？

**【面试者】** 原理：volatile state + CLH 变体双向队列 + park/unpark + 模板方法（tryAcquire 留给子类）。JDK8 的 acquireQueued 细节：前驱是 head 才再试一次；shouldParkAfterFailedAcquire 把前驱 waitStatus 置 SIGNAL 后才 park；抢到锁 setHead 摘旧头。**版本问题主动交代**：JDK15+ AQS 重构过——JDK21 里 acquire 统一成私有方法，setHead/shouldParkAfterFailedAcquire 这些方法名没了，但 state+队列+SIGNAL 语义不变。我按 JDK8 讲原理、按 JDK21 讲现状——这是对照 src.zip 核实过的。

**【评注】** ⭐⭐ "主动交代版本 + 原理不变" 是源码题的最佳防御姿态，答出这句面试官不会再追。

**【面试官】** CompletableFuture 用过吗？注意什么？

**【面试者】** 三件套：自定义线程池（默认 commonPool 是 JVM 全局共享，一个慢任务拖垮所有并行流——全局故障域）；allOf 聚合并行调用；orTimeout 超时。异常沿链传播，用 exceptionally/handle 兜底。上下文丢失用 TTL 或 TaskDecorator。并行详情页四路调用（商品/价格/库存/营销）是我们的标准用法，RT 从 sum 变 max。

**【面试官】** JDK21 虚拟线程你怎么看？

**【面试者】** 有结论的：IO 密集聚合服务已上，吞吐 x2.5，代码还能回退成同步写法；核心交易没迁——**连接池才是真瓶颈，虚拟线程只会把阻塞更快怼到连接池上**。踩过 pinning 坑：synchronized 包住的慢调用钉住载体线程，JDK21 吞吐不升反降，升 JDK24 才解决（JEP 491）。判断标准一句话：下游配额是不是瓶颈。

**【面试官】** 最后一题：说说 Java 内存模型的 happens-before？

**【面试者】** 它是可见性承诺不是时间顺序：若 A hb B，A 的写对 B 可见。必背规则：程序顺序、监视器锁、volatile、线程 start/join、中断、传递性、final。价值在于 review 并发代码时问三个问题：谁写谁读？有 hb 吗？没有的话用什么建立？——把 JMM 当工具而不是名词。

**【评注·终局】** 定级 **P7**。亮点：本机实证贯穿全场（9 分钟挂起、线程池顺序、偏向锁标志位）、虚拟线程决策标准。这场没有暴露短板——并发域过。

---

## 对话要点速记（本章）

1. 追问顺序：线程池三连 → volatile 对照实验 → 锁升级时间线 → CAS 三坑 → ThreadLocal → AQS 版本 → CF → 虚拟线程 → JMM。
2. 四个超预期点：本机实证四连、动态线程池、AQS 版本主动交代、虚拟线程"下游配额"决策标准。
3. 姿态要领：每个源码题先答原理再主动交代版本边界。
