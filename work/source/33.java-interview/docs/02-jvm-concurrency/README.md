# 第 2 章 并发编程与 JUC —— 从 happens-before 到 AQS 源码

> 本章是 Java 面试的"主战场"。P10 面试中并发题的打法是：先让你答对（volatile、线程池），
> 然后沿一条追问链一路问到你知识的边界，最后问"你们线上是怎么做的"——
> **只有源码理解 + 生产事故复盘两条腿都硬，才敢说精通并发。**

---

## 2.0 本章考察范围雷达

| 维度 | P4-P5 | P6-P7 | P8-P10 |
|------|-------|-------|--------|
| 内存模型 | 知道 volatile 可见性 | 讲清 happens-before 全套规则 | 用 JMM 解释真实并发 bug |
| 锁 | synchronized 用法 | 锁升级全过程 | 结合逃逸分析/锁消除谈性能 |
| AQS | 听说过 | 讲清 CLH 队列与独占模式 | 自己写过基于 AQS 的同步器 |
| 线程池 | 参数含义 | 执行流程+调优 | 动态线程池治理、事故复盘 |
| 异步编排 | Future 用法 | CompletableFuture | 全链路异步化架构与传递问题 |

---

## 2.1 零基础起步：并发到底在解决什么问题？

### 卡片 1：为什么会有并发问题？
一个变量 `count++` 实际是三步：**读内存 → 寄存器加 1 → 写回内存**。两个线程同时执行，
可能都读到旧值，各加 1，写回两次但只加了 1——这就是"竞态条件"（Race Condition）。
并发问题三兄弟：
1. **原子性**：操作被别人打断（count++ 被拆三步）。
2. **可见性**：A 线程改了变量，B 线程看不到（CPU 缓存/编译器优化）。
3. **有序性**：编译器和 CPU 会重排指令（double-checked locking 踩坑的根源）。

### 卡片 2：线程的三种创建方式（与一种推荐方式）
1. 继承 Thread；2. 实现 Runnable；3. 实现 Callable（有返回值、可抛异常）。
**推荐第 4 种：线程池**（复用、可控、可治理）。阿里规约：**禁止手动 new Thread**。

### 卡片 3：线程的 6 种状态（必背）
NEW → RUNNABLE →（synchronized 没抢到锁）BLOCKED →（抢到）RUNNABLE
→（wait/join/park）WAITING / TIMED_WAITING → 运行完 TERMINATED。
记忆：**BLOCKED 只针对 monitor 锁；JUC 的 Lock 用 park，进入的是 WAITING**。

### 卡片 4：sleep / wait / park / yield 区别
- sleep：Thread 静态方法，**不释放锁**，超时自动醒。
- wait：Object 方法，**必须在 synchronized 内**，释放锁，notify 唤醒。
- park/unpark：JUC 底层（LockSupport），以"许可"为单位，unpark 可先于 park 发放（不像 wait/notify 必须先等后通知），这就是 AQS 用它的原因。
- yield：提示调度器让出 CPU，不可靠，别用。

### 卡片 5：什么叫"可见性"问题的硬件根源
每个 CPU 核有自己的 L1/L2 缓存。线程 A 在核 0 改了变量，改的是核 0 的缓存；
线程 B 在核 1 读，读到核 1 缓存的旧值。硬件层靠 **MESI 缓存一致性协议** 同步，
但编译器/CPU 还会优化（写缓冲、重排），所以 Java 在语言层再加一堵墙——**JMM（Java 内存模型）**。

---

## 2.2 入门题（P4-P6 必答对）

### 题 2.2.1：volatile 是干什么的？能保证原子性吗？

**【参考回答（可背）】**
volatile 两个语义，一个不保证：
1. **可见性**：写 volatile 变量立即刷回主存，其他核心缓存行失效（MESI），读时强制从主存加载。
2. **禁止指令重排**：编译器在 volatile 读写前后插入**内存屏障**（写后 StoreStore+StoreLoad，读后 LoadLoad+LoadStore）。
3. **不保证原子性**：`volatile int count; count++` 依然错——读改写三步照样竞态。要原子用 AtomicInteger。

典型用途：**状态标志位**（如 `volatile boolean running` 控制优雅停机）、double-checked locking 的实例字段。

> **本机实证（2026-11-14，验证套件 notes/verify）**：同一台机器上，volatile 标志位的等待线程在写后 2 秒内退出（PASS）；而**去掉 volatile 的对照线程持续自旋 9 分钟仍未看见写入**（CPU 跑满、JVM 都无法退出，最后靠守护线程修复收场）。可见性问题不是理论——它是确定性发生的生产 bug。

**【追问链】**
1. 为什么 DCL 单例要 volatile？→ `new Singleton()` 三步：分配内存→初始化→引用赋值，2 和 3 可能重排；另一个线程拿到"已赋值但未初始化完成"的引用。volatile 禁止该重排。（更优雅方案：静态内部类 Holder 或枚举。）
2. volatile 底层怎么实现的？→ x86 上写 volatile 生成 `lock` 前缀指令（如 lock addl），lock 前缀会：锁缓存行、写回主存、使其他核心该缓存行失效。JMM 通过内存屏障抽象屏蔽各平台差异。
3. volatile 和 synchronized 怎么选？→ 一写多读用 volatile（如配置刷新）；复合操作必须锁或 CAS。

**【P10 加分项】**
讲 VarHandle（JDK9）替代 Unsafe 的意义：提供 acquire/release 模式（弱内存语义，比 volatile 更细粒度的性能选择），并指出 volatile 语义在 JSR-133 文档中的正式定义——能引到 JLS §17.4 说明你是读规范的人。

---

### 题 2.2.2：synchronized 的原理？锁升级过程？

**【参考回答（可背）】**
- 字节码层面：同步代码块用 **monitorenter/monitorexit**（可能多个 exit 配对异常出口），同步方法用 ACC_SYNCHRONIZED 标志。每个对象头（Mark Word）+ 关联的 Monitor（C++ ObjectMonitor，含 owner、EntryList、WaitSet）。
- **锁升级**（JDK8）：无锁 → 偏向锁（首次获取后记下线程 ID，之后该线程进入无需 CAS）→ 轻量级锁（第二个线程来竞争，栈上 Lock Record + CAS 自旋）→ 重量级锁（自旋失败次数多，膨胀为 OS 互斥量，线程挂起、涉及内核态切换）。
- JDK15 起默认废弃偏向锁（维护成本 > 收益，现代应用高并发场景多），JDK18 完全移除。

**【追问链】**
1. synchronized 和 ReentrantLock 区别？→ 功能：后者可中断、可超时（tryLock）、公平锁、多 Condition；实现：前者 JVM 内置+自动释放，后者 AQS；性能：JDK6 锁升级后基本持平，无特殊需求用 synchronized。
2. 什么是锁粗化/锁消除？→ JIT 优化：锁消除基于逃逸分析（对象不会逃逸出线程则去掉锁，如局部 StringBuffer append）；锁粗化把连续加锁合并（循环里每次 append 都解锁→扩大到循环外一次）。

**【P10 加分项】**
- 指出偏向锁的撤销代价：多线程交替但无竞争场景受益；一旦竞争，撤销偏向要等全局安全点，批量重偏向/批量撤销（BiasedLockingBulkRebiasThreshold=20/40）。

> **本机实证（JDK 21.0.2）**：`java -XX:+UseBiasedLocking -version` 直接报 `Unrecognized VM option`——偏向锁代码在 JDK 21 已**彻底移除**（JDK15 禁用+废弃 → JDK18 标志废弃 → 21 移除）。讲锁升级时主动报出这条版本时间线，是"跟踪 JDK 演进"的直接证据。
- 讲 wait/notify 与 ObjectMonitor 的 WaitSet 关系，说明对"重量级锁为什么慢"的理解停在用户态/内核态切换与线程挂起调度，而不是背名词。

---

### 题 2.2.3：线程池的核心参数和执行流程？

**【参考回答（可背）】**（出现率与 HashMap put 并列第一）
七大参数：corePoolSize、maximumPoolSize、keepAliveTime + unit、workQueue、threadFactory、handler。
执行流程（必背口诀：**先核心、再队列、后非核心、最后拒绝**）：
1. 提交任务，工作线程数 < core → 创建核心线程执行（即使有空闲线程）；
2. 达到 core → 任务入队；
3. 队列满且线程数 < max → 创建非核心线程；
4. 线程数达 max 且队列满 → 执行拒绝策略（AbortPolicy 抛异常-默认 / CallerRunsPolicy 调用者执行-天然反压 / Discard 丢新 / DiscardOldest 丢旧）。

四种常用线程池（Executors）与其问题（阿里规约禁止直接用 Executors）：
- newFixedThreadPool：无界 LinkedBlockingQueue → 堆积 OOM；
- newCachedThreadPool：max=Integer.MAX_VALUE → 线程爆炸 OOM；
- newSingleThreadExecutor：同样无界队列；
- newScheduledThreadPool：延迟/周期任务用。
正确姿势：手动 `new ThreadPoolExecutor(...)`，用有界队列 + 明确拒绝策略。

**【追问链】**
1. 队列选型？→ SynchronousQueue（不存任务，直接交接，Cached 用）、LinkedBlockingQueue（FIFO 可选有界）、ArrayBlockingQueue（有界、双锁分离）、DelayedWorkQueue（调度用）。
2. 线程数怎么定？→ 不是背"CPU核数+1"！IO 密集公式 N ≈ C × U × (1 + W/C)（目标 CPU 利用率×等待/计算比），但**正确答案是压测**：用不同参数压到 RT 达标且 CPU 未饱和的平衡点，并配合动态线程池运行时调整。
3. 核心线程会回收吗？→ 默认不回收；allowCoreThreadTimeOut(true) 可回收。
4. 提交方式 execute vs submit？→ submit 包装成 FutureTask，异常存进 Future 里，不打印——这是"线程池任务异常静默丢失"的经典 bug。

**【P10 加分项】**
讲美团动态线程池实践（必背案例）：参数写死是反模式，把 corePoolSize 等暴露到配置中心（Nacos/Apollo）监听变更，运行时调用 setCorePoolSize 动态调整；配合队列容量可调的 ResizableCapacityLinkedBlockingQueue。再补一个排查武器：ThreadPoolExecutor#getActiveCount/任务堆积指标接监控，"线程池必须可观测"。

---

### 题 2.2.4：ThreadLocal 在线程池里为什么会"串数据"？怎么系统性解决？

**【参考回答（可背）】**
线程池线程复用，上一个请求 set 的 ThreadLocal 值没清理，下一个请求读到旧值（比如用户 A 的身份信息串到用户 B）。
解决三层：
1. 业务层：finally 里 remove()（治标，靠自觉）；
2. 框架层：拦截器/Filter 统一 set 与 remove（Spring 的 RequestContextHolder 就是 Tomcat 每请求处理完后清理）;
3. 线程池层：装饰任务——阿里 TransmittableThreadLocal（TTL），提交时捕获快照、执行前回放、执行后恢复，同时解决"上下文跨线程池传递"。

**【P10 加分项】**
引申到"并发上下文传递"这个工程主题：traceId 跨 N 个线程池的传递、日志 MDC 与 ThreadLocal 的关系、虚拟线程（JDK21）下 ThreadLocal 的成本变化（百万虚拟线程每个都带 map 不划算，官方推荐 ScopedValue）——这一条链答完基本封顶。

---

## 2.3 进阶题（P7-P8 深挖）

### 题 2.3.1：讲讲 AQS 的实现原理？

**【参考回答（可背）】**
AQS（AbstractQueuedSynchronizer）= **一个 volatile int state + 一个 CLH 变体双向队列**。
1. **state**：语义由子类定义——ReentrantLock 表示重入次数（0→CAS 抢→非0判断是否自己重入），Semaphore 表示剩余许可，CountDownLatch 表示还差的计数。
2. **获取流程（独占）**：tryAcquire（子类实现）失败 → addWaiter 入队尾（CAS）→ acquireQueued 自旋：判断前驱是否 head，是则再试 tryAcquire；否则 park 挂起，等前驱 release 时 unpark 后继。
3. **释放**：tryRelease 成功后 unparkSuccessor 唤醒队列中第一个非取消节点。
4. **共享模式**：tryAcquireShared 返回剩余量，释放后**传播唤醒**（setHeadAndPropagate，保证 CountDownLatch 一次 release 唤醒一串）。
5. **条件队列**：ConditionObject 单向队列，await 把节点从同步队列移到条件队列并释放锁，signal 再移回来竞争。

模板方法思想：AQS 定骨架（排队、挂起、唤醒、传播），子类只实现"state 怎么变才算拿到锁"。这就是模板方法模式在 JDK 的最佳实践。

**【追问链】**
1. 公平锁和非公平锁差异？→ 非公平：上来直接 CAS 抢，不排队（吞吐高，可能饿死）；公平：先 hasQueuedPredecessors 判断有无排队的。
2. 为什么用双向队列？→ 取消节点需要找到前驱摘链；唤醒后继需要前驱状态传播。
3. 自旋 + park 结合的细节？→ 前驱不是 head 时会先短暂自旋（shouldParkAfterFailedAcquire 把前驱 waitStatus 置 SIGNAL 后才 park），避免刚入队就挂起的开销。

**【P10 加分项】**
现场手写过基于 AQS 的同步器（如 SimpleCountDownLatch 或读写状态打包：一个 int 高 16 位读锁低 16 位写锁——ReentrantReadWriteLock 的设计）；或指出 AQS JDK9 后的优化：LockSupport.park 骨架没变，但队列节点用 VarHandle 替代 Unsafe。

---

### 题 2.3.2：CAS 是什么？ABA 问题怎么解决？

**【参考回答（可背）】**
CAS（Compare-And-Swap）：CPU 原子指令（x86 的 lock cmpxchg），比较内存值与期望值，相等则更新，否则失败重试（自旋）。Java 里 Unsafe.compareAndSwapInt，JDK9 后 VarHandle.compareAndSet。
三大问题：
1. **ABA**：值从 A→B→A，CAS 以为没变。解决：版本号——AtomicStampedReference（stamp）/ 数据库乐观锁 version 字段。
2. **自旋开销**：竞争激烈时空转烧 CPU。解决：LongAdder 的分段思想（Cell[] 分散热点）。
3. **只能保证一个变量**：多变量要么锁，要么封装成对象用 AtomicReference。

**【追问链】**
1. LongAdder 为什么比 AtomicLong 快？→ AtomicLong 所有线程 CAS 同一个 value，热点竞争；LongAdder 先 base CAS，失败则散到 Cell[]（按线程 hash 探测），sum() 时汇总。**读弱写强**：sum 非原子快照。此思想同 CHM 的 CounterCell。
2. AtomicLong 还能用在哪？→ 单个计数器且要求每次读都精确时仍合适；监控指标这种最终一致读用 LongAdder。

**【P10 加分项】**
伪共享（False Sharing）：两个 hot 变量落在同一缓存行（64B），不同核心互相失效对方缓存。LongAdder 的 @Contended 注解让 Cell 独占缓存行（需 -XX:-RestrictContended）。提到生产中 @Contended 的使用与 JVM 参数配合，属于顶级加分。

---

### 题 2.3.3：CompletableFuture 怎么用？怎么处理异常？怎么并行调用多个服务？

**【参考回答（可背）】**
- 创建：supplyAsync（有返回）/ runAsync；默认用 ForkJoinPool.commonPool()——**生产必须传自定义线程池**（commonPool 是 JVM 全局共享，一个慢任务拖垮所有并行流和 CompletableFuture）。
- 编排：thenApply（转换）/ thenCompose（扁平化，避免 CF<CF<T>>）/ thenCombine（合并两个）/ allOf/anyOf（聚合）。
- 异步回调默认在哪个线程？→ 不指定 executor 时：前一步完成的线程执行（若已完成则当前线程）。
- 异常：exceptionally / handle（都处理）/ whenComplete（只看不动结果）；异常沿链传播，中断后续非异常回调。
- 典型场景（背模板）：详情页并行调 商品/价格/库存/营销 四个服务，allOf 聚合，超时用 orTimeout（JDK9）或 completeOnTimeout。

**【追问链】**
1. thenApply 和 thenApplyAsync 区别？→ Async 版本强制丢给 executor 新线程执行。
2. 上下文丢失问题？→ 异步化后 ThreadLocal（登录态/traceId）丢失：用 TTL 装饰 executor，或阿里开源的 transmittable-thread-local。
3. allOf 拿结果麻烦怎么办？→ 封装工具类收集 List<CompletableFuture> 再 join 转泛型列表（手写一段能力是加分项）。

**【P10 加分项】**
讲"全链路异步化"架构：Tomcat 请求线程（Servlet 异步/DeferredResult/WebFlux）→ 下游调用全异步 → 整个请求线程数从 200 降到个位数，吞吐提升数倍；代价是全链路 ThreadLocal 治理、堆栈可读性、调试难度。有此实践者直接对齐 P10。

---

### 题 2.3.4：读写锁与 StampedLock？

**【参考回答（可背）】**
- ReentrantReadWriteLock：state 高 16 位读、低 16 位写；读共享写独占；支持锁降级（写→读）不支持升级（死锁风险）；适合读多写少且读持有时间较长。
- 缺点：读线程多时写线程可能饥饿。
- StampedLock（JDK8）：**乐观读**——tryOptimisticRead 拿个 stamp（不加锁），读完 validate 校验期间有没有写；失败再升级悲观读锁。读性能显著高于 RWL；但不可重入、不支持 Condition，用错难排查。

**【P10 加分项】**
举真实用例：配置中心客户端本地缓存（读极多写极少）用 StampedLock 乐观读，压测 QPS 提升 30%+；同时讲"什么时候不用"——读持有时间长时乐观读反复 validate 失败反而更差。

---

## 2.4 压轴题（P9-P10）

### 题 2.4.1：设计一个支持动态调整、可观测、优雅关闭的线程池治理方案（结合你线上出过的事故）

**【参考回答（框架可背）】**
1. **背景/事故**：大促前压测发现某核心服务线程池 max=200/queue=1000，上游抖动时任务堆积 30 分钟无告警；或线程池参数靠猜，改参数要发版。
2. **方案**：
   - 动态化：core/max/queueCapacity 暴露配置中心，监听热更（setCorePoolSize 会按差值创建/回收线程；自定义 ResizableCapacity 队列改 capacity 字段）；
   - 可观测：activeCount、queueSize、rejectedCount、 oldestTaskAge 接 Prometheus + 告警阈值（队列水位 80%）；
   - 反压：CallerRunsPolicy 或自定义"延迟 1s 再 CallerRuns"，避免调用线程被拖死；
   - 优雅关闭：shutdown()（已提交任务跑完）+ awaitTermination + 超时后 shutdownNow()（中断，任务需响应 interrupt）；kill 信号钩子 Runtime.addShutdownHook 或 K8s preStop；
   - 隔离：按业务拆线程池（核心交易/普通任务/IO 密集分池），防止一个慢下游把公共池耗尽（舱壁模式）。
3. **效果量化**：参数变更分钟级生效；任务堆积告警从"事后发现"到"分钟级发现"；大促期间动态扩容线程 0 发布。

**【追问链】**
1. setCorePoolSize 增大后线程立刻创建吗？→ 会 prestart 至新 core（若任务足够）；减小不杀已存在线程，靠 keepAlive 回收。
2. 怎么给任务设置超时？→ Future.get(timeout) 或 JDK9+ CompletableFuture.orTimeout；注意任务内部也要能响应中断，否则超时只是"不等了"而非"停了"。

**【P10 加分项】**
上升到"资源隔离与容量治理"层面：线程池只是表象，本质是**对 CPU、连接池、下游 RT 的联合容量规划**——给出一个估算模板（单实例 QPS = 线程数 / 平均RT；下游 P99 突增时的自动降级联动 Sentinel），并提虚拟线程对这一整套治理的冲击与重新评估（JDK21：阻塞不再昂贵，线程池"防阻塞"的使命部分消失，但资源隔离依然需要）。

---

### 题 2.4.2：什么是 Java 内存模型？为什么需要它？happens-before 说出几条？

**【参考回答（可背）】**
1. **为什么需要**：不同 CPU/编译器重排行为不同，Java 要"一次编写到处运行"就必须定义统一的多线程可见性规则——JMM 是**语言级的抽象**，屏蔽硬件差异，而非描述硬件。
2. **定义**：主内存 + 工作内存抽象；所有共享变量存主存，线程操作在自己的工作内存副本上进行，何时同步回来由 JMM 规定。
3. **happens-before 规则（必背 8 条中至少 6 条）**：
   - 程序顺序规则（单线程内按代码顺序——注意是"结果等价"意义上的顺序）；
   - 监视器锁规则（解锁 hb 后续加锁）；
   - volatile 规则（写 hb 后续读）；
   - 线程启动规则（start 前 hb run 内）；
   - 线程终止规则（run 内 hb join 返回）；
   - 中断规则（interrupt 调用 hb 被中断线程检测到中断）；
   - 传递性；
   - final 规则（构造函数内写 final 字段 hb 其他线程读到该引用后的 final 字段——构造器不泄漏 this 的前提下）。
4. **本质**：happens-before 不是"时间先后"，而是**可见性承诺**：若 A hb B，则 A 的写对 B 可见；没有 hb 关系的重排都是允许的。

**【追问链】**
1. as-if-serial 和 happens-before 的关系？→ 单线程用 as-if-serial（结果不变即可重排），多线程用 happens-before 划定不可重排的边界——JMM 对编译器/处理器的约束是"最小必要限制"。
2. final 的内存语义？→ 写：构造器内对 final 字段的写与把对象引用发布出去之间有 hb；读：首次读对象引用与读其 final 字段之间有 hb。因此"不泄漏 this"时 final 对象多线程可见无需同步。
3. 怎么向面试官证明你真懂？→ 现场分析一个并发 bug：双重检查单例、可见性死循环（无 volatile 的 running 标志 JIT 把 while 读提升到循环外）、懒汉单例半初始化——任选其一按"哪个 hb 关系缺失→哪种重排发生→后果"三段式讲。

**【P10 加分项】**
指出 JMM 的工程落点：写并发组件时先画 happens-before 图再写代码；code review 中问三个问题——这个变量谁写谁读？他们之间有 hb 吗？没有的话用什么建立（volatile/锁/Unsafe）？这是把"背规则"升级为"用规则"。

---

## 2.4a 增补题（v1.1 深度扩充）

### 题 2.4a.1：JDK21 虚拟线程是什么？它颠覆了哪些旧经验？

**【面试官意图】** 检验技术雷达是否紧跟 JDK 演进——2025 年后的 Java 面试新分水岭。
**【参考回答（可背）】** 虚拟线程是 JVM 管理的轻量线程（JEP 444，JDK21 转正）：挂在少量载体线程（carrier）上，**阻塞时不占 OS 线程**，栈存堆中按需伸缩，百万级创建成本极低。颠覆的旧经验：① "线程池防阻塞"的使命基本消失——直接 `Thread.ofVirtual().start()` 或 executor per task；② 线程数不再需要精算（第 2 章题 2.2.3 的公式失效）；③ 同步阻塞代码重新变成好代码（不再强制异步化）。**不变的**：CPU 密集任务、资源隔离、限流背压、ThreadLocal 治理（百万虚拟线程携带 ThreadLocal 反而成为内存问题，官方推荐 ScopedValue）。
**【追问链】** ① 什么是 Pinning？（synchronized 块内阻塞、native 调用会"钉住"载体线程，暂时退化为平台线程行为——JDK24 优化了 synchronized pinning，需关注版本）② 怎么替代线程池做隔离？（虚拟线程不限量但**下游限流照旧**：Semaphore/信号量限流是正确姿势，而不是限线程数）③ 什么时候不该用？（CPU 密集、共享池复用昂贵资源如连接池——连接池容量才是真瓶颈）。
**【P10 加分项】** 给决策框架："我们把 IO 密集的聚合服务迁到虚拟线程后，吞吐 x2.5 且代码回退成同步写法；但连接池是新的容量单位——**资源模型从'线程数'迁移到'连接数/下游配额'**。这是虚拟线程时代最需要重建的心智。"

### 题 2.4a.2：ForkJoinPool 的工作窃取是什么？commonPool 有哪些坑？

**【参考回答（可背）】** ForkJoinPool：每个 worker 有自己的双端队列，自己从头部取任务，空闲 worker 从其他队列**尾部窃取**——减少竞争、提高缓存命中。commonPool 是 JVM 全局共享池（parallelStream、CompletableFuture 默认都在里面），大小=CPU 核-1。三大坑：① **全局共享**：一个阻塞任务拖垮所有并行流（所以 CF 生产必须自定义线程池）；② 阻塞任务让窃取失效（worker 被钉住）；③ ManagedBlocker 可告知阻塞让池补偿扩容，但很少人正确使用。
**【追问链】** ① parallelStream 的线程是哪来的？（commonPool，且并行流+外部阻塞=灾难组合）② 怎么给并行流指定池？（把流操作提交到自定义 FJP 中执行——技巧但更推荐直接不用 parallelStream 改显式线程池）。
**【P10 加分项】** "commonPool 的正确用法是'纯 CPU 计算的分治'；一旦任务里有 IO，它就是全局故障域。我们规定 parallelStream 只用于纯内存转换计算，IO 聚合一律 CompletableFuture+专用池。"

### 题 2.4a.3：JUC 容器的迭代器是弱一致性的，这有什么实际影响？

**【参考回答（可背）】** ConcurrentHashMap/CopyOnWriteArrayList 的 iterator 不抛 ConcurrentModificationException，遍历的是**创建时刻或快照**（COW）或"尽力最新"（CHM）视图：① 可能读到刚写入的数据、也可能读不到；② size() 是近似值；③ 这意味着"遍历时增删"不会异常但**统计可能不一致**——做报表聚合要意识到这点。强一致需求用 synchronized 包裹或换语义。
**【追问链】** ① COW 的写成本？（每次写复制全量数组，读极多写极少才合适，如监听器列表）② CHM 弱一致为什么够用？（读多写少的监控/遍历场景，最终一致即可；资金强一致场景不该在内存里做）。
**【P10 加分项】** "弱一致不是缺陷是设计——它换来的是无锁读。P10 该问的不是'怎么让它强一致'，而是'这个场景需要多强的一致性'。"呼应第 8 章 CAP。

### 题 2.4a.4：Semaphore、CountDownLatch、CyclicBarrier 怎么选？Phaser 是什么？

**【参考回答（可背）】** 一句话区分：**Semaphore 管许可**（限流/资源配额，可复用）；**CountDownLatch 一次性倒计数**（等 N 件事完成，不可重置）；**CyclicBarrier 可重用栅栏**（N 个线程互相等到齐再一起走，适合分批同步）。Phaser 是它们的统一体：多阶段栅栏，支持动态注册/注销参与者，替代"多批次的 CyclicBarrier"。
**【追问链】** ① Semaphore 公平模式？（支持 fairness 参数，默认非公平——限流场景一般无需公平）② CountDownLatch 的 await 带超时为什么必须用？（防止参与者异常导致永久等待）。
**【P10 加分项】** 组合实战："全链路压测预热：Semaphore(并发数) 控压测并发 + CountDownLatch(1) 统一发令 + AtomicLong 统计——三个最基础工具拼出压测框架，面试讲这个组合比背 API 高级。"

### 题 2.4a.5：死锁、活锁、饥饿怎么系统性预防？

**【参考回答（可背）】** 死锁：互斥+持有等待+不可剥夺+循环等待四条件，破其一——工程上靠**固定加锁顺序**与 tryLock 超时（防"持有等待"）。活锁：线程不断重试互相让步谁也走不了——对策：退避（随机 backoff）+ 让一个线程"坚持"。饥饿：低优先级/非公平锁下某线程永远抢不到——对策：公平锁（吞吐代价）或配额制（令牌桶按调用方分配）。检测手段：jstack/thread -b 找死锁；饥饿靠指标发现（某请求 P99 无界增长但无错误）。
**【追问链】** ① 锁顺序怎么全局约定？（按资源 ID 字典序，或在锁管理器统一 acquire 多把锁）② 分布式版死锁怎么防？（跨服务调用链形成"分布式锁环"——按调用链统一顺序或用 tryLock+超时+补偿，呼应第 8 章 SAGA）。
**【P10 加分项】** 体系化视角："并发 bug 的成本是指数增长的，所以预防要前置到代码规范：我们 CI 里有静态检查'多锁获取未排序''锁内调外部 IO'两条规则，把三类问题挡在上线前——并发问题治理靠门禁不靠 review 自觉。"

## 2.5 本章高频追问链图谱


```
volatile ──→ MESI/内存屏障 ──→ DCL ──→ 静态内部类/枚举单例
synchronized ──→ 锁升级 ──→ 偏向锁废弃(JDK15+) ──→ 锁消除/粗化(逃逸分析) ──→ 第3章 JIT
线程池 ──→ 拒绝策略 ──→ 动态化(美团方案) ──→ 舱壁隔离 ──→ 虚拟线程冲击
CAS ──→ ABA(版本号) ──→ LongAdder 分段 ──→ 伪共享 @Contended ──→ 缓存行
AQS ──→ CLH 双向队列 ──→ 公平/非公平 ──→ RWL 读写分离 ──→ StampedLock 乐观读
CF ──→ 自定义线程池 ──→ 上下文传递(TTL) ──→ 全链路异步化 ──→ WebFlux/虚拟线程
```

## 2.6 一页速记卡

1. volatile = 可见性 + 有序性，≠ 原子性；标志位/DCL 用它。
2. 锁升级：无锁→偏向→轻量→重量；JDK15 废弃偏向锁。
3. 线程池口诀：先核心、再队列、后非核心、最后拒绝；禁 Executors、必有界队列。
4. 线程数靠压测，公式只是起点：N = C×U×(1+W/C)。
5. AQS = volatile state + CLH 双向队列 + park/unpark + 模板方法。
6. CAS 三坑：ABA（加版本）、自旋烧 CPU（LongAdder 分段）、单变量（封装对象）。
7. LongAdder 读弱写强；sum() 是近似快照。
8. CF 生产三件套：自定义线程池、allOf 聚合、orTimeout 超时；异常用 handle/exceptionally。
9. ThreadLocal：key 弱 value 强、用完 remove、线程池传值用 TTL。
10. happens-before 是可见性承诺，不是时间顺序；8 条规则能默写 6 条。

## 2.7 参考资料
- 《Java 并发编程实战》（JCiP）—— 必读，"第 16 章 JMM"是面试源
- 《深入理解 Java 虚拟机》第 3 版 —— 第 12/13 章
- Doug Lea 论文：AQS（juc 作者综述）、jsr-133-faq
- 美团技术博客：《Java 线程池实现原理及其在美团业务中的实践》
- JDK 源码：AbstractQueuedSynchronizer、ThreadPoolExecutor#execute、LongAdder

---
*下一章：第 3 章 JVM 与性能调优 —— 内存区域、GC 算法、G1/ZGC、线上 OOM 排查实战。*
