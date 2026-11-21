# 第 24 册 笔试题库 —— 七卷全领域闭卷笔试（含答案与解析）

> 用法：**闭卷作答**，对照答案自评。评分：选择 2 分/题，判断 1 分/题，简答 5 分/题，编程 15 分/题；每卷满分 100。
> 覆盖：A Java 基础与集合 / B 并发与线程 / C JVM / D MySQL / E Redis / F **MongoDB**（新增领域）/ G 算法编程。
> **所有算法编程题的参考实现已在本机 JDK 21.0.2 实测，输出为真实运行结果**（代码见 notes/verify/ExamSolutions.java）。

---

## A 卷 Java 基础与集合

**A-1（选择）** `Integer a = 127, b = 127; Integer c = 128, d = 128;` 则 `a == b` 与 `c == d` 的结果？
A. true / true　B. true / false　C. false / false　D. true / 抛异常
**答案：B。** 包装类缓存 -128~127（`IntegerCache.high` 默认 127），128 超出缓存走 new。

**A-2（选择）** 下列哪项**不是** HashMap 树化的触发条件？
A. bin 中已有 8 个节点时发生下一次插入　B. 表长度 ≥ 64　C. 插入第 8 个节点　D. putAll/resize 后的再平衡
**答案：C。** 精确语义（JDK21 实测）：bin 已有 8 个节点时，**下一次插入（第 9 个）**才调用 treeifyBin；容量 <64 则改为扩容不树化。8 个节点时仍是链表。

**A-3（选择）** `new String("ja") + "va"` 后调用 `intern()`，与自身引用比较的结果？
A. 一定 true　B. 一定 false　C. 视字符串内容而定　D. 编译错误
**答案：C（本考点实测）**：内容为 "polyx2026" 这类**未入池**的新串 → true（JDK7+ 保留堆引用）；内容恰好是 **"java"** → false（它在 System 初始化时已被预入池）。经典的"背答案翻车题"。

**A-4（选择）** `new ArrayList<>()` 首次 add 后内部数组容量？此后加到第 11 个元素时容量？
A. 0→10→15　B. 10→15→22　C. 0→16→24　D. 10→20→30
**答案：A（实测）**。懒初始化；1.5 倍增长（10+10>>1=15；15+7=22）。

**A-5（选择）** 反射拿 `List<String>` 字段声明的泛型参数，靠的是什么？
A. 运行时泛型信息完整保留　B. class 文件的 Signature 属性　C. 注解处理器　D. 不可能拿到
**答案：B。** 擦除后泛型信息以 Signature 形式保留在 class 文件中，`getGenericType()` 可读——Jackson 反序列化的基础。

**A-6（判断）** "String 不可变，所以任何 String 做 HashMap key 后都绝对安全。"
**答案：错。** String 本身不可变且 hash 缓存安全，但若业务持有的是**可变对象**（如自定义 key）字段变化，hash 就失效。判断题考的是表述漏洞：不可变的是 String 对象本身，不是"所有 key"。

**A-7（判断）** "javac 会把 `"a" + b` 编译期直接合并成一个常量。"
**答案：错。** 仅**编译期常量**（两个字面量/常量）才会折叠；含变量的拼接 javac 改写为 StringBuilder（JDK8）或 invokedynamic StringConcatFactory（JDK9+，运行时按形态 specialize）。

**A-8（简答）** 重写 equals 必须满足哪五条性质？违反的后果各举一例。

**【思路】** 这题考的不是"背五条"，是**用反例证明你理解契约为什么存在**——每条违例都要能落到一个真实故障场景（最好的素材就是 HashMap/HashSet 出错）。

**【标准答案】**（先给五条，再给违例后果，一气呵成）
- **自反性**：x.equals(x) 为 true——违反则该对象在集合中"自己找不到自己"；
- **对称性**：x.equals(y) == y.equals(x)——违例：自定义类 equals 里用 instanceof 反向兼容 String，`myObj.equals("str")` 与 `"str".equals(myObj)` 结果不一致，放入 HashSet 后 contains 行为诡异；
- **传递性**：x=y 且 y=z → x=z——违例：继承场景父类 equals 用 instanceof 判断（Point 与 ColorPoint 互比），经典案例见《Effective Java》Item 10；
- **一致性**：多次调用结果相同（对象未修改）——违例：equals 依赖可变字段，对象入 HashMap 后修改字段 → get 返回 null（key"丢失"）；
- **非空性**：x.equals(null) 返回 false——违例：equals 里不判 null 直接强转 → NPE。

**【标准实现】**（背这个模板）
```java
@Override
public boolean equals(Object o) {
    if (this == o) return true;                    // 自反 + 性能短路
    if (!(o instanceof Point)) return false;       // 非空 + 类型（getClass 与 instanceof 的取舍要能讲）
    Point p = (Point) o;
    return x == p.x && y == p.y;
}
@Override
public int hashCode() { return 31 * x + y; }       // 与 equals 字段完全一致
```

**【常见错误】** ① 只重写 equals 不重写 hashCode（HashMap key 丢失）；② equals 里用 `==` 比较（除了枚举/包装类缓存场景全是错）；③ 在 equals 中使用可变字段；④ 用 Arrays.equals 比较对象数组而元素未重写 equals。

**A-9（编程）** 实现一个 `LinkedHashMap` 子类的 LRU，要求 accessOrder 语义正确。
**答案**：见第 13 册题 2（30 秒版）；核心：`super(16, 0.75f, true)` + 重写 `removeEldestEntry`。

---

## B 卷 并发与线程

**B-1（选择）** 线程池 core=2/max=4/queue=2（ArrayBlockingQueue），任务依次 T1~T9（T1 永久阻塞）。T5 提交时线程池状态？
A. poolSize=3 入队　B. poolSize=4 入队　C. poolSize=3 队列=2　D. 拒绝
**答案：A（实测推导）**：T1 占核心1，T2 占核心2，T3/T4 入队，T5 创建非核心线程3 → poolSize=3。
**实测注意**：非核心线程若执行空任务会瞬间完成并退出（keepAlive=0），测试该题必须让所有任务阻塞在同一闩上——否则队列被非核心线程消费，现象完全不同（本机踩过的实测坑）。

**B-2（选择）** volatile 不保证下列哪项？
A. 可见性　B. 禁止指令重排　C. 原子性　D. 禁止 CPU 缓存
**答案：C。** count++ 是读改写三步。

**B-3（选择）** 线程池 core=2/max=4，keepAliveTime=0ms。一个非核心线程执行完任务后？
A. 立即死亡　B. 等待 keepAlive 后死亡　C. 转为核心　D. 永远存活
**答案：A。** keepAlive=0 时非核心线程完成任务即退出——这解释了"为什么测试线程池顺序时必须让所有任务阻塞在闩上"（本机实测踩坑：空任务瞬间消费光队列，poolSize 掉回 2）。

**B-4（选择）** 线程的六种状态中，`Object.wait()` 与 `LockSupport.park()` 分别对应？
A. BLOCKED / WAITING　B. WAITING / WAITING　C. BLOCKED / TIMED_WAITING　D. WAITING / RUNNABLE
**答案：B。** BLOCKED 只针对 monitor 锁；JUC 的 Lock 用 park → WAITING（本机实测：holder=TIMED_WAITING、seeker=BLOCKED）。

**B-5（选择）** 虚拟线程（JDK21）下列说法错误的是？
A. 阻塞时不占 OS 线程　B. synchronized 块内阻塞可能 pinning（JDK24 修复）　C. 适合 CPU 密集任务　D. 栈存堆中按需伸缩
**答案：C。** CPU 密集收益为零甚至负（调度开销）。

**B-6（简答）** DCL 单例为什么必须 volatile？去掉会怎样？
**答案**：new 三步（分配→初始化→赋引用）中 2-3 可能重排，另一线程拿到"已赋值未初始化完成"的引用。volatile 禁止该重排并保证可见性。替代：Holder/枚举。

**B-7（简答）** notify 和 notifyAll 怎么选？用 if 判条件为什么错？
**答案**：notify 只唤醒一个，可能唤醒"同类等待者"造成死等，不确定时用 notifyAll；if 判条件在唤醒后不复查（虚假唤醒/条件被抢），必须 while 循环判条件。

**B-8（编程）** 两个线程交替打印 1~10（奇偶各一线程）。
**答案（实测输出：`1 2 3 4 5 6 7 8 9 10`）**：共享 lock + AtomicInteger num，条件命中打印并 notifyAll，否则 wait——完整实现见 notes/verify/ExamSolutions.java 的 examAlternate。

**B-9（编程）** 手写滑动窗口限流器 tryAcquire()，并分析窗口边界语义。
**答案与实测（含一个值得讲给面试官听的边界细节）**：Deque 存时间戳，tryAcquire 先弹出 `now - stamp >= window` 的过期项再判断容量。**实测陷阱**：window=300ms 内放行 3 个后，第 300ms 后再 acquire——只弹出最早的 t0，**两个 t50 请求仍在窗口内**，窗口内计数=3 而非 1（首次预期算错，代码实测纠正）。滑动窗口的"过期"是逐个时间戳判断，不是整窗一次性清空。

**B-10（编程）** 手写生产者消费者：有界队列、20 个元素全消费、优雅关闭、异常不静默。
**答案（实测 consumedSum=210、lastError=null）**：BlockingQueue put/poll(timeout)、CountDownLatch 停止信号、poll 带 timeout 的退出循环、异常捕获进 AtomicReference——完整实现见 ExamSolutions.examProducerConsumer。

---

## C 卷 JVM

**C-1（选择）** 哪个区域**不会**抛 OOM？
A. 堆　B. 元空间　C. 程序计数器　D. 直接内存
**答案：C**（唯一不 OOM 的区域）。

**C-2（选择）** 三色标记中"对象消失"必须同时满足？
A. 黑引用白 + 灰到白引用断开　B. 黑引用白 + 黑到黑断开　C. 灰引用白 + 白孤立　D. 只要黑引用白
**答案：A。** CMS 用增量更新（记录黑新增引用），G1 用 SATB（记录被断的灰引用），ZGC 读屏障自愈。

**C-3（选择）** `GC(12) Pause Young (Normal) (G1 Evacuation Pause) 2048M->456M(4096M) 12.3ms` 中 "GC(12)" 表示？
A. 第 12 次 Full GC　B. GC 编号（统一日志序号）　C. 12MB 回收　D. 12 个 Region
**答案：B（实测）**。JDK9+ 统一日志的序号特征——说得出这个细节 = 真用过 JDK9+。

**C-4（选择）** MaxTenuringThreshold 默认值？
A. 6　B. 8　C. 15　D. 21
**答案：C（PrintFlagsFinal 实测 =15）**。

**C-5（简答）** 类卸载的三个条件？
**答案**：所有实例回收、加载器回收、Class 对象无引用——Bootstrap 加载的类永不卸载。

**C-6（简答）** 为什么 G1 在小堆上反而可能不如 CMS？
**答案**：RSet 维护占堆 10%~20% + 写屏障吞吐代价；小堆收益小于成本。选型：小堆 CMS 或 Serial，6G+ 才考虑 G1。

**C-7（简答）** `-XX:+UseBiasedLocking` 在 JDK 21 上会怎样？
**答案（实测）**：`Unrecognized VM option`——偏向锁 15 禁用+废弃、18 标志废弃、21 **代码彻底移除**。讲锁升级主动报这条时间线是加分项。

**C-8（分析）** 循环内 `new byte[64]` 三千万次，`-Xmx64m` 下 GC 日志为 0，为什么？
**答案（本机实证）**：JIT 逃逸分析+标量替换——未逃逸分配全部消除。把数组写入静态字段（逃逸）后 GC 立即出现。配套教学点：GC 测试必须让对象逃逸。

---

## D 卷 MySQL

**D-1（选择）** MySQL 8.0 默认隔离级别与 RR 下防幻读的机制？
A. RC / MVCC　B. RR / MVCC+Next-Key Lock　C. RR / 仅 MVCC　D. SERIALIZABLE / 表锁
**答案：B。** 快照读靠 MVCC，当前读靠间隙锁+记录锁（左开右闭）；快照读后紧跟当前读的混用仍有幻读。

**D-2（选择）** 联合索引 (a,b,c)，下列走索引的是？
A. `b=1`　B. `a=1 and c=3`（只用到 a）　C. `a=1 and b>2 and c=3`（a,b 用到，c 不走索引排序）　D. `c=3`
**答案：B、C（多选考法：问"哪些能用"，B/C 都能用但 C 的 c 不参与索引过滤/排序）**——最左前缀 + 范围后失效的经典组合。

**D-3（选择）** 两阶段提交的正确顺序？
A. binlog → redo prepare → redo commit　B. redo prepare → binlog → redo commit　C. redo commit → binlog　D. binlog prepare → redo
**答案：B。** 崩溃恢复规则：redo 处于 prepare 且 binlog 完整 → 提交；不完整 → 回滚。

**D-4（选择）** RR 下下列哪个操作不会加间隙锁？
A. `select * from t where id>10 for update`　B. `update t set x=1 where id=10`（id 为主键等值命中）　C. `select ... where id between 10 and 20 for update`　D. `select * from t where name='x' for update`（name 无索引）
**答案：B。** 主键等值命中退化为记录锁；A/C 是范围当前读（Next-Key），D 无索引全表扫加全表间隙锁。

**D-5（简答）** 主从延迟 30 分钟，业务"写后立读"怎么处理？
**答案**：治理（并行复制 writeset）+ 读策略（写后 N 秒/本会话强制走主；关键校验强制主库）+ 监控三级告警；GTID 必开。

**D-6（简答）** 一条 SQL 突然从 10ms 变 3s，排查路径？
**答案**：slow log 确认 → explain（type/key/rows/Extra）→ 统计信息过期（analyze table）→ 锁等待（sys.innodb_lock_waits）→ 优化器选错索引（force index 验证）→ 参数/资源（buffer pool 命中率）。

**D-7（简答）** 数据被误删一行，恢复流程？
**答案**：停写缩小影响面 → 最近全量（XtraBackup）恢复到临时实例 → binlog 回放到误删前一秒 → 按表导回 → 对账。预防：权限分级、高危 SQL 审批、延迟从库、恢复演练（没演练过的备份=没有备份）。

**D-8（简答）** 分库分表的分片键怎么选？订单维度查询怎么办？
**答案**：最高频查询条件（user_id）+ 分布均匀 + 避免跨片事务；订单号用**基因法**内嵌 user 分片位；非分片键查询走异构索引（ES）或二次路由。

---

## E 卷 Redis

**E-1（选择）** RDB + AOF（everysec）的丢失窗口？
A. RDB 两次快照间　B. AOF 最多 1 秒　C. 两者同时开启取最小　D. 不丢
**答案：B（单看 AOF）；A 是 RDB 的窗口**——混合持久化兼顾两者。

**E-2（选择）** 缓存一致性"先更新 DB 再删缓存"中，删除失败怎么办？
A. 重试直到成功　B. 抛异常回滚 DB　C. binlog 订阅异步删 + 重试队列　D. 不处理
**答案：C**（订阅 binlog 与业务解耦，失败进重试队列；TTL 兜底最终一致）。

**E-3（选择）** 布隆过滤器"返回不存在"的含义？
A. 一定不存在　B. 可能存在　C. 大概率存在　D. 无法判断
**答案：A。** 无漏判（说不在必不在）+ 有误判（说在可能不在）→ 适合当 DB 前置拦截器，误杀靠 DB 兜底。

**E-4（选择）** mem_fragmentation_ratio = 0.8 说明？
A. 碎片严重　B. 正常　C. 数据被换到 swap（比碎片更紧急）　D. 内存泄漏
**答案：C。** used_memory > RSS = 数据落到磁盘，性能塌方。

**E-5（简答）** 分布式锁四要素 + 看门狗 + RedLock 的工程结论。
**答案**：SET NX PX + 唯一 value + Lua 原子释放 + 看门狗续期；RedLock 争议（GC 停顿/时钟跳变/fencing 缺失）→ 锁分级：效率锁用 Redisson，正确性锁 DB 原子条件更新兜底。

**E-6（简答）** 热 key 和大 key 治理分别怎么做？
**答案**：热 key——本地缓存兜底 + key 打散 + 预热（是预测出来的不是故障时发现的）；大 key——分桶/压缩/UNLINK 异步删/巡检门禁，且是 Cluster 迁移的前置工程。

**E-7（简答）** Cluster 扩容时业务为什么会收到 ASK？MOVED 和 ASK 区别？
**答案**：槽迁移中源节点对未迁移 key 返回 ASK（临时跳，不更新映射缓存）；迁移完成后返回 MOVED（永久，客户端更新槽映射）。

**E-8（简答）** 没有 MQ，用 Redis 做延迟队列？
**答案**：ZSet（score=执行时间）+ ZRANGEBYSCORE 轮询 + **Lua 封装"取+删"防多消费者竞争** + 任务表补偿崩溃丢失；边界：无 Ack/无背压/轮询耗 CPU——有 MQ 就别用 Redis。

---

## F 卷 MongoDB（新增领域速成 + 笔试）

> 30 秒背景：文档型数据库（BSON，单文档上限 16MB），默认存储引擎 WiredTiger（文档级并发 + MVCC + Snappy 压缩），副本集（oplog 复制、最多 50 成员/7 投票）、分片（mongos + config 副本集 + shard key）。

**F-1（选择）** ObjectId 的组成（现代驱动）？
A. 4B 时间戳 + 3B 机器 + 2B 进程 + 3B 计数　B. 4B 时间戳 + 5B 随机 + 3B 计数　C. 8B 时间戳 + 8B 随机　D. UUID
**答案：B**（2019 后驱动规范；旧版 A）。

**F-2（选择）** MongoDB 副本集最多几个投票成员？选举协议类似？
A. 12 / Paxos　B. 7 / 类 Raft　C. 50 / Raft　D. 7 / 2PC
**答案：B**（最多 50 成员、7 个可投票；选举为类 Raft 的多数派协议）。

**F-3（选择）** TTL 索引的作用与触发？
A. 按创建时间自动删文档，每 60 秒巡检　B. 按访问时间　C. 手动触发　D. 删除字段
**答案：A**（expireAfterSeconds 基于 Date 字段，后台任务约 60 秒一轮）。

**F-4（选择）** 联合索引设计的官方原则是？
A. ESR（Equality→Sort→Range）　B. RES　C. SRE　D. 随意
**答案：A**（等值列在前、排序列居中、范围列最后——MongoDB 官方索引设计指南）。

**F-5（简答）** MongoDB 和 MySQL 怎么选？
**答案**：MongoDB 适合——schema 多变（商品异构属性）、嵌套文档聚合读、海量写入水平扩展、原型快速迭代；MySQL 适合——强事务/多表关联/资金账务。**混合架构常见**：核心账务 MySQL + 行为/日志/内容 MongoDB。判断依据：关联复杂度、事务需求、schema 稳定性。

**F-6（简答）** 事务支持现状？
**答案**：4.0 起副本集多文档 ACID 事务、4.2 起分片集群事务；必须走 session，默认超时 60 秒；**能单文档原子解决就不开事务**（单文档天然原子——这是文档模型的核心优势）。

**F-7（简答）** 分片键选错的代价？
**答案**：分片键不可随意更改（4.4 可 refine 追加后缀字段、5.0 reshardCollection 在线改但代价大）；选错的后果：单调递增键全部写入最后一个分片（热点）、无法定向查询（全分片广播）。选片键原则：高基数、写分布均匀、查询必带。

**F-8（简答）** Write Concern w:"majority" 是什么？为什么生产推荐？
**答案**：写入需多数派节点确认才算成功——副本集主从切换时不丢已确认写；代价是延迟增加。配套 Read Concern majority 读已多数派确认的数据，避免回滚读取。

---

## G 卷 算法编程（6 题，含思路/分析/标准答案/常见错误，全部本机 JDK 21 实测）

> 作答要求：先写【思路】再落笔代码；代码命名规范、边界自查（空/1/满/并发）按 REVIEW-STANDARD 执行。

---

**G-1（编程，15 分）** 设计并实现 LRU 缓存：get/put 均要求 O(1)，容量溢出淘汰最久未访问的 key。

**【思路】** 从两个需求推导两个结构：① get/put 都要 O(1) 定位 → HashMap（key→节点）；② 淘汰要 O(1) 找"最旧"且访问要 O(1) 移动"最新" → 双向链表。两者共享同一个 Node 对象（链表节点内含 key，淘汰时才能反查 map 删除）。头尾**哨兵节点**消灭"空表/单节点"两类边界判断——这是写出无 bug 版本的关键决策。

**【分析】** 复杂度：get/put 均 O(1)，空间 O(capacity)。边界三问：① capacity=1 时每次 put 新 key 都淘汰旧 key；② put 已存在的 key 是"更新+提升为最新"，不是新建；③ 淘汰时**必须同时删链表节点和 map 条目**——漏删 map 就是"幽灵 key"（内存泄漏 + 后续 get 返回已被淘汰的数据）。备选方案否决：数组移动 O(n)；单链表摘除需前驱 O(n)——双向链表是唯一 O(1) 解。

**【标准答案】**（完整实现，实测通过——见 notes/verify/ExamSolutions.java#examLRU）
```java
static class LRUCache {
    private final int capacity;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(), tail = new Node();
    static class Node { int key, value; Node prev, next;
        Node() {} Node(int k, int v) { key = k; value = v; } }

    LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail; tail.prev = head;
    }
    public int get(int key) {
        Node n = map.get(key);
        if (n == null) return -1;
        unlink(n); addToHead(n);
        return n.value;
    }
    public void put(int key, int value) {
        Node n = map.get(key);
        if (n != null) { n.value = value; unlink(n); addToHead(n); return; }
        if (map.size() == capacity) {
            Node oldest = tail.prev;
            unlink(oldest); map.remove(oldest.key);
        }
        Node fresh = new Node(key, value);
        map.put(key, fresh); addToHead(fresh);
    }
    private void unlink(Node n) { n.prev.next = n.next; n.next.prev = n.prev; }
    private void addToHead(Node n) { n.next = head.next; n.prev = head;
        head.next.prev = n; head.next = n; }
}
```

**【实测输出】**（操作序列 put(1,1)/put(2,2)/get(1)/put(3,3)淘汰2/get(2)/put(4,4)淘汰1/get(1)/get(3)/get(4)）
```
get(1)=1, get(2)=-1, 顺序=[4,3], get(1)=-1, get(3)=3, get(4)=4
```
与 LeetCode 146 语义一致 ✓

**【常见错误】** ① 淘汰时只删链表忘删 map（幽灵 key + 内存泄漏）；② get 命中后忘 moveToHead（访问顺序失效，退化成 FIFO）；③ put 已存在 key 误走"新建+淘汰"分支（误淘汰一个无辜 key）；④ 不用哨兵导致空表/单节点判断漏边界。

---

**G-2（编程，15 分）** 数据流中求最大的 k 个数，要求 O(n log k)，空间 O(k)。

**【思路】** "维护当前最大的 k 个" → 每次只需要淘汰这 k 个里**最小的** → **小顶堆**（堆顶=门槛）：新元素 > 门槛才准入。对比备选：全量排序 O(n log n)（浪费——k 之外的元素白排）；大顶堆（全量入堆 O(n log n) + 需要全部内存）；快排 partition（O(n) 但适合静态数组，数据流/重复查询不友好）。所以小顶堆是"数据流 + TopK"场景的最优解。

**【分析】** 复杂度 O(n log k)、空间 O(k)——n 大 k 小时显著优于排序。边界：① k ≥ n → 全量入堆直接返回；② 重复元素正常处理（TopK 不去重，去重要另说）；③ 数据流场景堆天然支持增量。若面试官追问"亿级数据单机内存放不下" → 分片各求 TopK 再归并（map-reduce 思想，呼应第 9 章）。

**【标准答案】**（实测通过——ExamSolutions#examTopK）
```java
public List<Integer> topK(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);   // 小顶堆
    for (int n : nums) {
        if (minHeap.size() < k) minHeap.offer(n);
        else if (n > minHeap.peek()) { minHeap.poll(); minHeap.offer(n); }
    }
    List<Integer> result = new ArrayList<>(minHeap);
    Collections.sort(result, Collections.reverseOrder());      // 降序输出
    return result;
}
```

**【实测输出】** 输入 {5,2,8,1,9,3,7,6} k=3 → `[9, 8, 7]` ✓

**【常见错误】** ① 用大顶堆再截取前 k（全量入堆，复杂度退化 O(n log n)）；② 新元素与堆顶比较方向写反（应"大于门槛才准入"）；③ k > n 时未处理（堆逻辑其实自动兼容，但显式分支更清晰）。

---

**G-3（编程，15 分）** 两个线程交替打印 1~10（奇数线程 A、偶数线程 B），要求严格交替、不丢失。

**【思路】** "交替"= 一方打印后另一方才被允许 → 共享锁 + 共享计数器：条件命中（轮到自己）就打印并 notifyAll 唤醒对方；条件不命中就 wait 让出锁。这是"条件等待"模式的标准实现。

**【分析】** 三个必须：① **while 而非 if 判条件**——被 notifyAll 唤醒后条件可能已被对方改变（虚假唤醒/竞争），必须复查；② **notifyAll 而非 notify**——notify 随机唤醒，可能唤醒"同类等待者"造成永久死等；③ num++ 在锁内保证原子与可见性。备选方案：Semaphore 交替 acquire/release（无虚假唤醒问题，许可语义天然一一对应）、Lock+Condition（多条件队列更精细）——都能答出即加分。

**【标准答案】**（实测输出 `1 2 3 4 5 6 7 8 9 10`，严格交替——ExamSolutions#examAlternate）
```java
class AlternatePrinter {
    private final Object lock = new Object();
    private final AtomicInteger num = new AtomicInteger(1);
    public void print(boolean odd) {
        while (num.get() <= 10) {
            synchronized (lock) {
                if (num.get() <= 10 && ((num.get() % 2 == 1) == odd)) {
                    System.out.print(num.getAndIncrement() + " ");
                    lock.notifyAll();
                } else {
                    try { lock.wait(); } catch (InterruptedException e) {
                        Thread.currentThread().interrupt(); return;
                    }
                }
            }
        }
    }
}
```

**【常见错误】** ① 用 if 判条件（虚假唤醒后多打印/死循环）；② notify 只唤一个（两线程互相死等）；③ 打印与自增不原子导致越界到 11；④ 忘记中断恢复（catch 后直接 return 不补 interrupt 位）。

---

**G-4（编程，15 分）** 实现滑动窗口限流器 tryAcquire()：任意 300ms 窗口内最多放行 3 个请求。

**【思路】** "任意窗口内最多 N 个" → 必须记住窗口内每个请求的时间戳 → **Deque 存时间戳**：tryAcquire 先从队头弹出"已滑出窗口"的旧时间戳，再判断 size < N 则放行并记录。队头是最老的——过期从队头弹，天然契合 Deque。

**【分析】** 复杂度：均摊 O(1)（每个时间戳最多进出各一次），空间 O(窗口内请求数)。**边界语义（实测纠错点）**：过期判断是**逐时间戳**的，不是"整窗一次性清空"——本机实测：300ms 窗口放行 3 个（t0、t50、t50）后，第 310ms 再 acquire 只弹出 t0（310-0≥300），**两个 t50 仍在窗内**（310-50=260<300），窗口内计数=3 而非直觉的 1。并发：synchronized 临界区极短（弹出+判断+入队），单机够用；分布式扩展 → Redis Lua（ZADD+ZREMRANGEBYSCORE+ZCARD 原子三连，呼应第 6 章）。

**【标准答案】**（实测通过——ExamSolutions#examLimiter）
```java
static class SlidingWindowRateLimiter {
    private final int maxRequests;
    private final long windowMillis;
    private final Deque<Long> stamps = new ArrayDeque<>();
    SlidingWindowRateLimiter(int maxRequests, long windowMillis) {
        this.maxRequests = maxRequests; this.windowMillis = windowMillis;
    }
    public synchronized boolean tryAcquire() {
        long now = System.currentTimeMillis();
        while (!stamps.isEmpty() && now - stamps.peekFirst() >= windowMillis)
            stamps.pollFirst();               // 弹出所有已滑出窗口的旧时间戳
        if (stamps.size() < maxRequests) {
            stamps.addLast(now);
            return true;
        }
        return false;
    }
}
```

**【实测输出】**
```
t0: true → t50: true,true → 第4次: false（窗口内已 3 个）→ t310: true（t0 出窗）
窗口内剩余时间戳数 = 3（两个 t50 + 新 t310）
```

**【常见错误】** ① 以为"过 300ms 后窗口会清空"——实际只弹出真正过期的，t50 仍占坑（本题实测纠错点，讲出来=真写过）；② 用 size 与"距首个请求的时长"判断——窗口是滑动的不是固定的；③ 分布式场景直接套单机版——必须 Redis Lua 原子三连，否则竞态超卖配额。

---

**G-5（编程，15 分）** 旋转排序数组（无重复元素）找最小值，要求 O(log n)。例：{4,5,6,7,0,1,2} → 0。

**【思路】** 数组被"旋转"= 两段各自有序的拼接 → 部分有序可二分。关键洞察：**拿 mid 与 hi（右端点）比较**而不是与 lo 比较——`nums[mid] > nums[hi]` 说明断点（最小值）必在 mid 右侧（lo=mid+1）；否则最小值在左半段含 mid（hi=mid）。为什么不能和 lo 比：{3,4,5,1,2} 中 mid=5 > lo=3，但最小值在右半段——与 lo 比较无法区分"左侧有序"与"右侧有序"。

**【分析】** 复杂度 O(log n)。边界：① 未旋转（纯升序）→ hi=mid 一路收缩到 lo=0，正确返回 nums[0]；② 两元素 {2,1} → mid=0，nums[0]=2 > nums[1]=1 → lo=1 → 返回 1；③ **有重复元素** {2,2,2,0,1}：mid==hi 无法判断方向 → hi--（最坏退化 O(n)，这是无法避免的信息损失）。不变量（面试说出即加分）："最小值始终在 [lo, hi] 区间内"。

**【标准答案】**（实测四组输出全对——ExamSolutions#examBinarySearch）
```java
public int findMin(int[] nums) {
    int lo = 0, hi = nums.length - 1;
    while (lo < hi) {
        int mid = (lo + hi) >>> 1;             // 无符号右移防溢出
        if (nums[mid] > nums[hi]) lo = mid + 1; // 断点在右半段
        else hi = mid;                          // 最小值在 [lo, mid]
    }
    return nums[lo];
}
```

**【实测输出】** {4,5,6,7,0,1,2}→0；{3,4,5,1,2}→1；{11,13,15,17}→11（未旋转）；{2,1}→1 ✓

**【常见错误】** ① 与 lo 比较导致错误收缩（反例 {3,4,5,1,2}）；② 循环条件写 lo<=hi 造成死循环（hi=mid 时必须 lo<hi）；③ `(lo+hi)/2` 溢出（用 >>>1）；④ 忘记处理未旋转数组（其实 hi=mid 收缩天然兼容）。

---

**G-6（编程，15 分）** 生产者消费者：有界队列（容量 5），生产 20 个元素全部消费，支持优雅关闭，异常不静默丢失。

**【思路】** "有界 + 阻塞 + 线程安全" → **ArrayBlockingQueue 天然就是生产者消费者的标准解**（put 满阻塞、take 空阻塞、内部已封装条件队列）——手写 wait/notify 是面试考原理，工程上必须用 BlockingQueue。优雅关闭三件套：停止信号（CountDownLatch）+ 消费者 poll 带 timeout 的退出循环 + 异常收口（AtomicReference 收集，不静默）。

**【分析】** 复杂度 O(总元素数)。边界：① 队列满时 put 阻塞（背压）；② 消费者退出条件 `!stop && queue 非空` 的组合——只看 stop 会丢掉停止瞬间仍在队列里的数据，只看队列会永远等新数据；③ 消费异常必须收口（静默吞掉=数据消费状态不可知）。为什么不用 wait/notify 手写：BlockingQueue 内部已正确处理虚假唤醒/锁竞争，手写只用于面试演示原理（见第 13 册题 3）。

**【标准答案】**（实测 consumedSum=210=1+2+…+20，lastError=null——ExamSolutions#examProducerConsumer）
```java
BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(5);
AtomicInteger consumed = new AtomicInteger();
AtomicReference<Throwable> lastError = new AtomicReference<>();
CountDownLatch stop = new CountDownLatch(1);

Thread producer = new Thread(() -> {
    try {
        for (int i = 1; i <= 20; i++) queue.put(i);   // 满则阻塞（背压）
        stop.countDown();
    } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
}, "producer");

Thread consumer = new Thread(() -> {
    try {
        // 退出条件 = 收到停止信号 且 队列已排空——只看一个都会丢数据
        while (!stop.await(50, TimeUnit.MILLISECONDS) || !queue.isEmpty()) {
            Integer v = queue.poll(50, TimeUnit.MILLISECONDS);
            if (v != null) consumed.addAndGet(v);
        }
    } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    catch (Exception e) { lastError.set(e); }
}, "consumer");
```

**【常见错误】** ① 消费者退出只判 stop——停止瞬间队列剩余数据丢失（sum < 210）；② 消费异常吞掉不收口（消耗状态不可知）；③ 生产者 for 循环内 put 抛 InterruptedException 不恢复中断位。

---



## 笔试策略（简短）

1. **顺序**：先选择判断（拿满定级分）→ 编程题从最有把握的开始；
2. **手写代码**：先讲思路再落笔；变量命名规范（review 标准适用）；写完自查边界（空/1 个/并发）；
3. **不会的题**：写相关正确知识 + 标注不确定——笔试空题零分，部分正确有分；
4. **MongoDB 题冷知识**：ObjectId 结构、7 投票上限、ESR 原则——这三个点背下来，命中率极高。

## 速记卡

1. 笔试与面试不同：笔试看**确定性输出**，面试看**思维过程**——算法题务必实测边界。
2. Integer 缓存 127/128、intern 的 "java" 陷阱、树化第 9 插——笔试最爱考"背错细节"的人。
3. 线程池顺序题的关键是**非核心线程空任务即死**（keepAlive=0）——测试题必须让任务阻塞才有确定性。
4. 滑动窗口过期逐时间戳判断，不是整窗清空——本机实测纠正过一次预期错误。
5. MongoDB 三个高频冷知识：ObjectId=4+5+3、7 投票上限、ESR 索引原则。
6. 混合持久化/写关注 majority/分片键不可随意改——MongoDB 的"双 1"级必背。
7. 算法题 LRU/TopK/交替打印/限流器/旋转数组二分/生产者消费者——六大高频全在此卷有实测参考实现。

---
*返回 [INDEX.md](../../INDEX.md)。本册算法参考实现全部在本机 JDK 21.0.2 实测（notes/verify/ExamSolutions.java），输出为真实运行结果。*
