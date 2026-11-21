# 第 3 章 JVM 与性能调优 —— 内存、GC、线上排查三板斧

> P10 面试里 JVM 题的作用是"分层"：P6 背内存区域，P7 讲 GC 流程，P8 对比收集器，
> P9/P10 必须能讲一个**完整的线上事故复盘**：现象 → 排查路径 → 根因 → 修复 → 防复发。
> 本章每个压轴题都给出可背诵的"事故叙事模板"。

---

## 3.0 本章考察范围雷达

| 维度 | P4-P5 | P6-P7 | P8-P10 |
|------|-------|-------|--------|
| 内存区域 | 背五区 | 理解对象分配全流程 | 结合逃逸分析/栈上分配谈优化 |
| 类加载 | 知道双亲委派 | 讲清加载全过程 | 打破委派的场景设计与热部署 |
| GC | GC 是什么 | 分代收集流程 | 收集器选型、G1 调参、ZGC 落地 |
| 排查 | 会看日志 | 会用 jstack/jmap | Arthas 在线诊断 + 完整事故复盘 |

---

## 3.1 零基础起步

### 卡片 1：JVM 运行时数据区（必背五区 + 两个线程私有）
**线程私有**：
1. **程序计数器**：当前执行字节码行号，唯一不会 OOM 的区域。
2. **虚拟机栈**：方法调用的栈帧（局部变量表、操作数栈、动态链接、返回地址）；递归太深 → StackOverflowError。
3. **本地方法栈**：native 方法用。

**线程共享**：
4. **堆**：对象实例，GC 主战场，分新生代（Eden + 2×Survivor）+ 老年代，默认比例 1:2；Eden:S0:S1 = 8:1:1。
5. **方法区（元空间 Metaspace，JDK8+）**：类元信息、运行时常量池；JDK8 起从永久代（堆内）改为**本地内存**，参数从 -XX:MaxPermSize 变为 -XX:MaxMetaspaceSize——永久代 OOM 的历史问题由此终结。

另注意：**字符串常量池 JDK7 起在堆中**；直接内存（NIO DirectByteBuffer）不属于五区但会 OOM。

### 卡片 2：一个对象的生死（必背流程）
1. new 指令 → 检查类是否加载；
2. **TLAB 分配**（Thread Local Allocation Buffer，Eden 里每个线程私有小块，指针碰撞，无锁极快，占 99% 对象）；
3. TLAB 不够 → Eden CAS 分配 → Eden 满 → **Minor GC/Young GC**；
4. 存活对象年龄+1（Survivor 之间复制），**年龄到 15（默认）晋升老年代**；
5. 特殊晋升：大对象直接进老年代（-XX:PretenureSizeThreshold）、动态年龄判定（同龄对象超 Survivor 一半）、Survivor 放不下直接进老年代。

### 卡片 3：怎么判断对象该死了？
- **可达性分析**：从 GC Roots（栈帧局部变量、静态变量、常量、JNI 引用、活跃线程等）出发，不可达 = 可回收。
- 引用四等级：强（不回收）→ 软 SoftReference（内存不足才回收，适合缓存）→ 弱 WeakReference（下次 GC 必回收，ThreadLocalMap 的 key、WeakHashMap）→ 虚 PhantomReference（配合 ReferenceQueue 跟踪回收，DirectByteBuffer 清理用）。

### 卡片 4：GC 算法三件套
1. **标记-清除**：碎片问题；
2. **标记-复制**：新生代用，浪费一半空间但无碎片、速度快；
3. **标记-整理**：老年代用，移动对象整理连续。
一切收集器都是这三样的组合与并发化改造。

---

## 3.2 入门题（P4-P6）

### 题 3.2.1：说说 Minor GC、Major GC、Full GC 的区别？什么情况触发 Full GC？

**【参考回答（可背）】**
- **Minor GC**：Eden 满触发，回收新生代，STW 短（存活对象少，复制算法快）。触发最频繁。
- **Major GC**：术语混乱，通常等价于老年代收集（CMS 的 concurrent collection）。
- **Full GC**：整堆+元空间，STW 最长，是性能事故的头号嫌疑。
触发条件必背 5 条：
1. 老年代空间不足（晋升对象超限）；
2. 元空间不足；
3. System.gc()（建议，可用 -XX:+DisableExplicitGC 禁掉——**堆外内存依赖 System.gc() 的话禁了会 Direct Memory OOM**，正确姿势是 -XX:+ExplicitGCInvokesConcurrent）；
4. CMS 晋升失败（promotion failed）或并发模式失败（concurrent mode failure）→ 退化 Serial Old；
5. G1 的 to-space exhausted / humongous 对象堆积失败退化 Full GC。

**【追问链】**
1. 为什么新生代用复制、老年代用整理？→ 新生代对象朝生夕死、存活率低，复制便宜；老年代存活率高，复制代价大，且需要无碎片支持大对象。
2. 为什么需要两个 Survivor？→ 一个 Survivor 放不下"本次存活 + 上次残留"时会直接晋升，破坏年龄分代设计；两块轮流用保证每次复制都有空区。

**【P10 加分项】**
指出"Full GC 频率"是最该监控的指标，且给出经验阈值：老年代增长速率稳定、Full GC 每天夜深发生一次可以接受；白天突发 Full GC 必查。顺带讲"元空间泄漏"：动态生成类（CGLIB 代理、Groovy 脚本、反射频繁生成）撑爆元空间——连接了第 4 章的 Spring 场景。

---

### 题 3.2.2：类加载过程和双亲委派？为什么需要双亲委派？

**【参考回答（可背）】**
加载过程五步（前四步合称"类加载"）：
1. **加载**：读字节码生成 Class 对象；
2. **验证**：格式/元数据/字节码/符号引用校验；
3. **准备**：静态变量分配并赋零值（`static int a = 1` 此时 a=0）；
4. **解析**：符号引用 → 直接引用（可延后）；
5. **初始化**：`<clinit>` 执行（静态变量真正赋值 + static 块）。触发时机：new、读静态字段（非 final 常量）、反射、子类初始化连带父类等——**实现类初始化不触发“无 default 方法的”接口初始化；但含 default 方法的接口会随实现类初始化**（JLS 12.4.1，本机实测：new Impl() 打印了含 default 的接口 I 的初始化，不含 default 的 I2 未初始化）。

双亲委派：AppClassLoader → PlatformClassLoader（ext）→ Bootstrap，先委派父加载器，父找不到才自己加载。
三大理由：
1. **安全**：自定义 java.lang.String 不会被加载，核心类不可替换；
2. **唯一性**：同一个类保证由同一个加载器加载（类的相等性 = Class 对象相等 = 同一加载器+同一字节码）；
3. **层级复用**：父加载的类子加载器不用重复加载。

**【追问链】**
1. 打破双亲委派的场景？→ ① SPI/JDBC：核心库要加载厂商实现，用线程上下文类加载器（TCCL）反向委派；② Tomcat：每个 webapp 独立加载器实现应用隔离、webapp 优先；③ 热部署/OSGi/Arthas redefine：模块化+版本隔离；④ JDK9 模块化后委派链变化（扩展加载器改为平台加载器）。
2. 怎么写一个自定义类加载器？→ 继承 ClassLoader，重写 findClass（不是 loadClass，保留委派逻辑）；打破委派才重写 loadClass。
3. 类会卸载吗？→ 该类所有实例已回收、加载器已回收、Class 对象无引用。Bootstrap 加载的类永远不卸载。

**【P10 加分项】**
讲一个真实案例：热更新框架（如 Arthas 的 redefine、公司内部热修复平台）里"同一个类两个版本共存"的实现——不同加载器加载同名类即为不同类，但要注意跨版本反射调用与 ClassCastException 风险。

---

### 题 3.2.3：内存泄漏和内存溢出的区别？Java 会内存泄漏吗？

**【参考回答（可背）】**
- **溢出（OOM）**：申请内存时没有足够空间，直接报错。
- **泄漏（Leak）**：对象不再使用但可达性分析仍然可达，GC 无法回收，逐渐耗尽。
- Java 会泄漏，高频场景必背 6 个：① 静态集合持有大对象（Map 只进不出）；② ThreadLocal 未 remove（线程池）；③ 未关闭的资源（连接、流、Channel）；④ 监听器/回调未注销；⑤ 内部类持有外部类引用（非静态内部类的隐式 this$0）；⑥ 缓存无淘汰策略。

**【追问链】**
1. 怎么排查？→ 见题 3.3.2 完整三板斧。
2. 软引用做缓存靠谱吗？→ 弊大于利：软引用回收时机不可控且触发 full GC 才清理，现代实践用带权重淘汰的 Caffeine。

**【P10 加分项】**
区分"堆内泄漏"与"堆外泄漏"：DirectByteBuffer 堆外内存不受 -Xmx 管控（受 MaxDirectMemorySize），Netty 场景的 PooledByteBufAllocator 泄漏要靠 Netty 自带 ResourceLeakDetector（采样级别：SIMPLE/ADVANCED/PARANOID）。

---

## 3.3 进阶题（P7-P8）

### 题 3.3.1：G1 收集器的原理？和 CMS 比好在哪？

**【参考回答（可背）】**
- **内存布局**：G1 把堆划成 2048 个左右等大的 **Region**（1~32MB），每个 Region 动态扮演 Eden/Survivor/Old/Humongous 角色——**不再物理分代**，逻辑分代。
- **目标**：可控停顿（-XX:MaxGCPauseMillis，默认 200ms）。依据**每个 Region 的回收价值**（垃圾比例+回收耗时预测）排序，每次 GC 优先回收价值最高的 Region——这就是 **Garbage First** 名字的由来。
- **三色标记**（并发标记基础）：白色未访问、灰色自身已访问但引用未扫、黑色完全扫过。并发标记的两个问题与解法（必背）：
  - **浮动垃圾**：并发时新产生的垃圾本轮收不掉 → 下轮再收，无害；
  - **漏标（对象消失）**需同时满足：黑引用了白 + 灰到白的引用被断开。解法二选一：
    - **增量更新**（CMS）：黑色新增引用时记录，remark 阶段重新扫描——CMS 有此缺陷；
    - **原始快照 SATB**（G1）：引用被断开时记录旧引用，按标记开始时的快照处理。
- **回收流程**：初始标记（STW，随 Young GC）→ 并发标记 → 最终标记（SATB 缓冲处理，STW 短）→ 筛选回收（Evacuation，把存活对象复制到空 Region，STW，多线程并行）。
- **Humongous 对象**：≥ Region 一半的对象，直接进连续 Humongous Region；大对象多会引发 to-space exhausted → Full GC（JDK10 后并行 Full，之前单线程 Serial Full，很慢）。
- **记住集 RSet + 卡表**：Region 级跨代引用记录，空间换时间（可能占堆 10%+ 内存）。

**与 CMS 对比（背 4 点）**：
1. CMS 标记-清除有碎片，G1 复制整理无碎片；
2. CMS 只管老年代且与 ParNew 搭配，G1 一体化管理全堆；
3. 停顿可控：G1 有停顿预测模型，CMS 不可控；
4. 内存开销：G1 RSet 较贵（10%~20% 堆），CMS 卡表便宜——**小堆（<6G）CMS 反而更优**，G1 适合 6G+。

**【追问链】**
1. CMS 的并发模式和晋升失败？→ 并发阶段用户线程还在分配，老年代预留空间（CMSInitiatingOccupancyFraction，默认老年代 68% 触发）不够 → concurrent mode failure → 退化 Serial Old 单线程 Full GC，停顿秒级。
2. 什么时候选 ZGC？→ 堆 16G+ 且停顿要求 <10ms 的场景（见题 3.3.2）。
3. G1 怎么调优？→ 大原则：**先满足吞吐与停顿目标，再动参数**。常用：MaxGCPauseMillis（太激进会让 G1 频繁 GC）、 InitiatingHeapOccupancyPercent（默认 45%，并发标记启动阈值）、 大对象排查（Humongous 阈值调整 G1HeapRegionSize）。

**【P10 加分项】**
- 说清"Region 内复制也是复制算法，为什么 G1 老年代用复制而不是整理？"——因为只回收部分 Region，复制集小、代价可控，把"整理"拆成了增量操作；
- 提 G1 的 remembered set 维护成本与写屏障（pre/post barrier）开销，能引到"没有免费的并发"这一工程哲学。

---

### 题 3.3.2：线上一个服务频繁 Full GC / OOM，你的完整排查流程？

**【参考回答（这是 P10 必考的"流程题"，背模板）】**
**第一步：保留现场**
- 堆转储：`jmap -dump:live,format=b,file=heap.hprof <pid>`（大堆用 -F 或 gcore；OOM 自动 dump：-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=...）；
- 若进程还活着先看趋势再 dump（dump 本身 STW）。

**第二步：定位是哪种内存**
- `jstat -gcutil <pid> 1000`：看各代占用与 GC 次数/耗时趋势；
- 老年代涨且 Full GC 回不来 → 堆内泄漏/堆内不足；
- 元空间涨 → 动态类生成问题（CGLIB/Groovy/反射）；
- 堆正常但 OOM: Direct buffer memory → 堆外泄漏（Netty/NIO）。

**第三步：分析 dump（工具+思路）**
- MAT / JProfiler / arthas heapdump 分析：Dominator Tree 找 Retained Heap 最大的对象 → Leak Suspects 报告 → GC Roots 引用链定位持有者。
- 高频结论速查：
  - `byte[]`/String 巨多 → 查 SQL 大结果集、接口一次拉全量数据；
  - `ThreadLocalMap` 有大量 null-key entry → ThreadLocal 泄漏；
  - 某业务缓存类占 60% → 缓存无淘汰；
  - `Finalizer` 队列堆积 → finalize 滥用；
  - 大量 `ConcurrentHashMap$Node` → 静态 Map 只进不出。

**第四步：修复 + 防复发**
- 代码层修根因（改懒加载/加淘汰/流式处理）；
- 参数层兜底：HeapDumpOnOutOfMemoryError 必开；
- 监控层：GC 频率/耗时、老年代水位进告警；
- 复盘文档：现象、时间线、根因、修复、同类风险排查清单。

**【追问链】**
1. Arthas 常用命令？→ dashboard（整体）、thread -n 3（最忙线程）、thread --state BLOCKED（死锁）、jad（在线看源码）、watch/trace（方法观测）、profiler start（async-profiler 火焰图）、redefine（热修复）。**强调 Arthas 解决的是"不能重启、不能连调试器"的生产现场问题**。
2. 频繁 Full GC 但 dump 里对象不多？→ 考虑：① 元空间/堆外问题不是堆；② 大对象晋升（Humongous）；③ System.gc() 被调用（RMI/堆外清理触发）；④ 内存对齐/堆参数过小。换角度查：GC 日志 + jstat 时间线。

**【P10 加分项】**
必须讲一个自己的一手事故（模板）：背景（什么业务、什么量级）→ 现象（监控曲线、告警）→ 误判（先怀疑了什么后来排除了——体现排查严谨性）→ 根因（如"运营批量导出一次查 500 万行，结果集在堆内构建 Excel"）→ 修复（MyBatis 流式查询 + 分页导出 + 限流）→ 防复发（大查询熔断规则、导出平台统一收口）。**有误判环节的复盘比"一次命中"更可信。**

---

### 题 3.3.3：ZGC 为什么能把停顿做到亚毫秒？

**【参考回答（可背）】**
核心四件套（背框架）：
1. **着色指针（Colored Pointers）**：64 位指针的几个 bit 用来存 GC 状态（Marked0/Marked1/Remapped/Finalizable），GC 元信息存在指针里而不是对象头里——ZGC 一切魔法的基础。
2. **读屏障（Load Barrier）**：应用线程读引用时检查指针颜色，若"坏色"则触发自愈：修正指针或转发到新地址——**对象移动过程中应用线程访问总是安全的**。
3. **并发整理**：因为读屏障能自愈，对象复制、指针更新都可以与应用并发进行，只有极短的根扫描/初始标记 STW。
4. **Region 自适应**：小/中/大 Region，动态调整。

版本演进：JDK11 实验（停顿 <10ms）→ JDK15 生产可用 → JDK21 **分代 ZGC**（Generational ZGC，吞吐大幅提升，日常停顿亚毫秒）→ 生产推荐 JDK21+ 的分代 ZGC。
代价：吞吐略降（读屏障开销 5%~10%）、内存占用略高；CPU 紧张时不如 G1 划算。

**【追问链】**
1. G1 停顿为什么做不到亚毫秒？→ Evacuation（复制）阶段 STW，停顿与存活对象量相关；ZGC 把复制也并发化了。
2. 什么时候不该上 ZGC？→ 堆小（<8G，G1 足够）、CPU 预算紧、JDK 版本受限；以及依赖 JVMTI/某些 APM agent 对着色指针兼容性的老版本探针。

**【P10 加分项】**
技术选型视角："我们把核心交易从 CMS 升 G1 再到 JDK21 分代 ZGC 的判断标准：不是停顿数字，而是**尾延迟对业务的实际影响**——支付回调 P999 每超时一次就是一笔资金对账工单。用业务语言评估 JVM 升级 ROI，才是 P10 的高度。"

---

## 3.4 压轴题（P9-P10）

### 题 3.4.1：为什么 JIT 能让 Java 跑得接近 C++？分层编译、方法内联、逃逸分析分别做什么？

**【参考回答（可背）】**
1. **分层编译**：C1（客户端编译，快但优化浅）与 C2（服务端编译，慢但优化深）配合：解释执行 → C1 快速编译 → C2 深度编译。热点探测基于**方法调用计数器 + 回边计数器**（OSR 栈上替换让循环内代码也能编译）。
2. **方法内联（最重要优化）**：把小方法体复制进调用点，消除调用开销，并且**让后续优化跨方法可见**（逃逸分析的前提）。启发式：方法字节码 <35 字节频繁调用会内联（MaxInlineSize/FreqInlineSize）。
3. **逃逸分析**：分析对象作用域：
   - 不逃逸 → **栈上分配**（实际实现为标量替换：拆成局部变量，根本不建对象）；
   - 线程不逃逸 → **锁消除**（StringBuffer 局部变量的 synchronized 去掉）。

> **本机实证（2026-11-14，验证套件 notes/verify）**：一个每轮 `new byte[64]` 循环 3000 万次的方法，在 `-Xmx64m` 下理应触发几十次 Young GC，实测 **GC 日志为零、循环瞬间完成**——循环内未逃逸的分配被 JIT 标量替换全部消除。把数组写入静态字段（逃逸）后，GC 立即按预期出现。"逃逸分析不是玄学"这件事，用日志就能自证。
4. 其他：循环展开、向量化（SIMD）、去虚化（类型剖析+内联热路径，单实现接口直接静态绑定——**为什么"接口调用慢"在 HotSpot 里常常不成立**）。
5. 代价与陷阱：**JIT 死区**——代码未编译时行为可能与编译后不同（如 Math 静态初始化顺序 bug）、去优化（deopt）抖动、预热流量（灰度机器冷启动 RT 高，需要预热方案）。

**【追问链】**
1. 为什么 Java 不像 C++ 一样 AOT 全静态编译？→ 动态特性（反射、动态代理、类加载）让编译期无法确定全部类型；GraalVM Native Image 用封闭世界假设 + 配置文件解决，代价是构建复杂与部分动态能力受限（见追问 2）。
2. GraalVM Native Image 什么时候用？→ Serverless/FaaS 冷启动敏感（毫秒级启动、常驻内存低）、边缘计算；代价：编译时间长、反射需注册、峰值吞吐可能低于 JIT。Spring Boot 3 AOT 支持已生产可用。

**【P10 加分项】**
讲预热实战：大促扩容的新实例灰度放量（自适应：从 1% 流量逐步爬坡）+ 接口预热调用 + JVM 预热参数（-XX:TieredStopAtLevel=1 快速启动再放开）——把 JIT 知识落到"扩容不抖动"的工程问题上。

---

### 题 3.4.2：给你一个新服务，JVM 参数你会怎么给？（而不是背默认参数）

**【参考回答（框架可背：从业务画像推导，不背玄学参数）】**
1. **业务画像**：QPS 多少？对象分配速率多大？RT 要求？有没有大对象（导出/报表）？容器还是物理机？内存多大？
2. **内存**：容器场景必给 -Xms=-Xmx（避免动态扩缩抖动），堆 = 容器内存的 50%~70%（留堆外+元空间+Netty+OS）；开 -XX:+AlwaysPreTouch 让物理内存提前提交，避免运行时缺页。
3. **收集器**：8G 以下 G1 默认；16G+ 低延迟要求分代 ZGC；老集群 CMS 不动（能升级 JDK 再谈）。
4. **必开三件套**：
   - -XX:+HeapDumpOnOutOfMemoryError + HeapDumpPath；
   - GC 日志统一格式（-Xlog:gc*:file=...:time,uptime,level,tags——JDK9+ 统一日志）；
   - -XX:+ExitOnOutOfMemoryError（OOM 后快速失败让 K8s 重启，避免"半死不活"状态——**这条体现运维视角，是加分关键**）。
5. **反模式声明**：不抄网上的"八大参数圣经"；不给 -XX:NewRatio 手工定死分代（让 G1 自适应）；不用 System.gc() 当清理手段。
6. **验证闭环**：压测观察 GC 日志 + Prometheus（jvm_gc_pause_seconds 分位数），以 P999 停顿和分配速率迭代参数——**参数是压出来的，不是背出来的**。

**【P10 加分项】**
补"JVM 治理"高度：全公司统一 JVM 基线镜像（JDK 版本、参数模板、诊断工具预装、APM agent 预配置），新服务零配置继承公司最佳实践；JDK 升级（8→17→21）的推进策略（字节码兼容性扫描、灰度、性能 A/B）——从"调参"上升到"平台化治理"。

---

## 3.5 本章高频追问链图谱

```
内存五区 ──→ TLAB/对象分配 ──→ 动态年龄/大对象晋升 ──→ Full GC 触发条件
可达性分析 ──→ 引用四等级 ──→ ThreadLocal 弱引用 ──→ 堆外内存 DirectByteBuffer
双亲委派 ──→ SPI/TCCL ──→ Tomcat 隔离 ──→ 热部署 ──→ Arthas redefine
三色标记 ──→ 漏标两条件 ──→ 增量更新(CMS)/SATB(G1) ──→ 读屏障自愈(ZGC)
G1 Region ──→ Humongous ──→ to-space exhausted ──→ 分代 ZGC(JDK21)
JIT ──→ 内联 ──→ 逃逸分析/标量替换 ──→ 预热 ──→ GraalVM AOT
```

## 3.6 一页速记卡

1. 五区：程序计数器不 OOM；栈溢出 SOE；元空间 JDK8 在本地内存。
2. 分配路径：TLAB → Eden CAS → Survivor 复制 → 年龄 15/动态年龄 → 老年代。
3. Full GC 触发 5 条：老年代满、元空间满、System.gc、CMS 失败、G1 失败。
4. 双亲委派三目的：安全、唯一、复用；打破场景：SPI/Tomcat/热部署。
5. 三色标记漏标两条件：黑引白 + 灰断白；CMS 增量更新，G1 SATB，ZGC 读屏障自愈。
6. G1：Region 化、停顿预测、Humongous 是大坑、小堆 CMS 反而优。
7. ZGC：着色指针+读屏障；JDK21 分代 ZGC 是生产推荐。
8. 排查三板斧：jstat 看趋势 → jmap dump → MAT 找支配树；Arthas 线上诊断。
9. OOM 三件套必开：HeapDumpOnOutOfMemoryError、GC 日志、ExitOnOutOfMemoryError。
10. JIT 三板斧：分层编译、内联、逃逸分析（标量替换/锁消除）；新实例要预热。

## 3.7 参考资料
- 《深入理解 Java 虚拟机》周志明 第 3 版 —— Java 面试 JVM 圣经，重点 2/3/4/7/8 章
- 《Java 性能权威指南》第 2 版 —— 收集器与调优的量化方法
- 周志明《深入理解 Java 虚拟机》配套案例 + 美团/阿里 JVM 技术博客
- 官方文档：JEP 377 (ZGC)、JEP 439 (Generational ZGC)、JEP 425 (虚拟线程)
- 工具：Arthas 官方文档、async-profiler、MAT

## 3.4a 增补题（v1.1 深度扩充）

### 题 3.4a.1：G1 的 Remembered Set 与写屏障的成本，为什么说"没有免费的并发"？

**【面试官意图】** 区分"背 G1 特性"与"理解 G1 代价"——P8 以上必考。
**【参考回答（可背）】** 问题背景：Region 化之后跨 Region 引用（老年代 Region 引用新生代，或任意方向）必须被记录，否则回收单个 Region 会漏活对象。机制：每个 Region 一张 RSet，通过**写屏障**维护——应用每次引用赋值都会触发 post-write barrier，找到目标 Region 的 card 标记。代价：① 写屏障是每次引用赋值都执行的指令，分配密集型应用吞吐损失 5%~10%；② RSet 内存可能占堆 10%~20%（引用密集场景）；③ 维护 RSet 的 Refinement 线程吃 CPU。**所以 G1 在小堆、分配密集、CPU 紧张时不占优**——"并发/增量回收的每一点停顿优化，都是用吞吐和内存换的"。
**【追问链】** ① 什么场景 RSet 特别大？（大量老年代对象互相引用且稀疏分布在多 Region）② 怎么缓解？（G1HeapRegionSize 调大减少跨 Region 数、或换 ZGC 用着色指针免 RSet）。
**【P10 加分项】** 哲学升华："三色标记解决'漏标'靠屏障，ZGC 解决 RSet 靠着色指针，分代 ZGC 换来吞吐——每一代 GC 的进步都是'把某个成本换到更便宜的地方'，调优者的工作就是找到你们业务的便宜成本项。"

### 题 3.4a.2：元空间泄漏（Metaspace OOM）的成因与专案排查？

**【参考回答（可背）】** 成因清单（背 5 条）：① CGLIB/Javassist 动态代理类不断生成（每次增强都新类，如反复 refresh 的 Spring Bean）；② Groovy/JSP 等脚本引擎编译类；③ 反射滥用（频繁 Method.invoke 走膨胀路径生成字节码，JDK8 需 -Dsun.reflect.inflationThreshold 调优）；④ 自定义类加载器持有引用不释放；⑤ 脚本热更新（热部署框架每次重载都新加载器+新类）。排查：jstat 看 MC 列持续涨 → Arthas `classloader -t` 看加载器数量异常 → dump 后 MAT 看 Classes/ClassLoader 视图定位谁在生成类。
**【追问链】** ① 怎么从代码层根治？（代理对象缓存：同一目标类只生成一次增强类；脚本编译结果缓存）② 元空间参数怎么设？（MaxMetaspaceSize 设上限 fail-fast，初始 MetaspaceSize 与峰值接近减少 retrigger）。
**【P10 加分项】** 举真实事故模板："灰度发布系统每次热更都新建类加载器，累积 2 万个加载器撑爆元空间，Full GC 每分钟 3 次——修复：热更改为'复用加载器+redefine 类'，并给元空间水位加告警。动态能力要有配额意识。"

### 题 3.4a.3：容器（K8s）环境下 JVM 参数怎么给？和物理机有什么不同？

**【参考回答（可背）】** 关键差异四点：① **内存感知**：JDK8u131+/JDK10+ 支持 cgroup 感知，容器内"看见"的是 Pod limit；但必须显式用 `-XX:MaxRAMPercentage=50~70`（留堆外/元空间/Netty 空间），别再用物理机时代的 -Xmx=机器内存思路；② **CPU 感知**：Runtime.availableProcessors 读 cgroup quota，直接影响 GC 线程数与 commonPool 大小——CPU limit 设太小 GC 并行度被砍；③ **OOM 行为**：Pod 超内存会被 cgroup OOMKill（无任何日志），必须区分"JVM OOM（有 dump）"与"容器 OOMKill（k8s 事件）"两种现象；④ **堆外合计**：Xmx + Metaspace + DirectMemory + 线程栈×线程数 + JIT 缓存 ≤ Pod limit 的 85%。
**【追问链】** ① OOMKilled 怎么排查？（kubectl describe 看 OOMKilled 事件 + 对比 RSS 曲线，常见根因是堆外泄漏或线程数爆炸）② ExitOnOutOfMemoryError 在容器里还必要吗？（必要且更重要——JVM 自杀让 K8s 拉起新 Pod，避免半死状态）。
**【P10 加分项】** 给"容器 JVM 参数模板"作为可背诵资产：`-XX:MaxRAMPercentage=65 -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/dumps -XX:+ExitOnOutOfMemoryError -XX:MaxMetaspaceSize=512m -XX:MaxDirectMemorySize=1g`，并强调"模板进公司基础镜像，新服务零配置继承"——呼应 3.4.2 的 JVM 治理。

### 题 3.4a.4：OOM 类型全景——9 种常见 OOM 及第一排查方向？

**【参考回答（可背）】**（背成一张速查表）① **java heap space**：堆不足/泄漏 → dump 支配树；② **GC overhead limit exceeded**：GC 占 98% 时间回收 <2% → 通常是慢泄漏的前兆；③ **Metaspace**：动态类 → classloader 分析（见上题）；④ **unable to create new native thread**：线程数超 OS 限制 → 查线程数与 ulimit，不是堆问题；⑤ **Direct buffer memory**：堆外 → Netty/NIO 引用泄漏，看 MaxDirectMemorySize；⑥ **Out of swap space / address space**：进程地址空间 → 检查 swap 与 mmap；⑦ **Requested array size exceeds VM limit**：单对象超大数组 → 业务代码边界；⑧ **压缩类空间（Compressed class space）**：Metaspace 子区 → 同 ③；⑨ **stack_overflow 不算 OOM 但常混问**：栈深 → 递归或栈帧过大。
**【追问链】** ④ 为什么新建线程也会 OOM？（每个线程预留栈内存（默认 1MB）是 OS 层分配，Xmx 管不着——这是"堆外合计"意识的关键例证）。
**【P10 加分项】** 排查方法论："看到 OOM 字符串先分流：堆类（有 dump 可分析）vs 资源类（native thread/direct memory，dump 没用要看线程数与 OS 层）——分流错误是排查最常见的时间浪费，这张表值得团队 oncall 手册必备。"

### 题 3.4b.1：实读一篇 G1 GC 日志——逐字段解读与五个观察点

**【面试官意图】** "你看得懂 GC 日志吗"是鉴别"背过调优"与"真调过优"的试金石。能逐字段解释一行日志的候选人，可信度立升一档。

**【参考回答（可背）】** 先说怎么开日志（必背）：
```
JDK8：  -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Xloggc:gc.log
JDK9+： -Xlog:gc*:file=gc.log:time,uptime,level,tags
```
然后给一行典型的 G1 Young GC（JDK8 格式）逐字段解读：
```
2026-11-14T03:12:45.102+0800: 1234.567: [GC pause (G1 Evacuation Pause) (young) (initial-mark) 2048M->456M(4096M) 123.456ms]
└─①墙钟时间            └─②进程启动后秒数  └─③停顿类型                  └─④标记周期起点    └─⑤回收前->回收后(总容量)   └─⑥本次停顿耗时
```
逐字段解释（背）：① 墙钟时间用于对齐业务监控；② uptime 是相对进程的——排查"启动后多久出的问题"；③ `(G1 Evacuation Pause)`=复制式回收，`(young)`=只收新生代；④ **`(initial-mark)` 是重点**：这次 Young GC 顺带启动了并发标记周期（G1 的初始标记搭 Young GC 便车），后面应看到 `concurrent-mark-start/.../end` 和 `(mixed)` 停顿——**young→initial-mark→concurrent→mixed 的序列是 G1 的正常完整周期**；⑤ 回收前 2048M→回收后 456M：**回收后水位是否回落是判断泄漏方向的第一指标**（每次回收都回不到低位=有东西活着）；⑥ 停顿耗时配合下面这行：
```
[Times: user=0.35 sys=0.02, real=0.12 secs]
```
**user≈real 的 2~3 倍是正常的**（多线程并行回收，user 是所有 GC 线程 CPU 时间之和）；user 远小于 real 说明 GC 线程没跑满（CPU 被抢/容器 limit 太小）。

**五个观察点（背成 checklist）**：
1. **停顿序列**：young → initial-mark → concurrent → mixed 循环 = 健康；只有 young 从不见 mixed = 并发标记没启动（IHOP 没到/调太高）；
2. **回收后水位**：full/mixed 后老年代仍高位不下 → 泄漏方向，转 dump；
3. **real 趋势**：Young GC 的 real 持续变长 → Eden 太大单次复制量增长，或晋升过快；
4. **to-space exhausted / (Evacuation Failure)**：晋升失败，几乎必是 Humongous 大对象——立刻查大对象来源；
5. **Full GC (Allocation Failure)**：退化兜底已发生，P0 级信号，先看频率再看出现在什么业务时段。

**【追问链】**
1. jstat 的 `jstat -gcutil 1000` 输出怎么读？——列含义：S0/S1/E/O/M/YGC/FGC/GCT；看 O 列趋势 + FGC 次数即可 10 秒判断"堆内泄漏 or 元空间 or 堆外"，是 dump 之前最快的分流手段（呼应第 12 册三板斧第一步）；
2. JDK9+ 统一日志的行变了哪些？——格式变 `[info][gc] GC(12) Pause Young (Normal) ... 12.345ms`，字段语义不变但多了 GC 序号，对账更方便；说得出"序号"这个细节=真的用过 9+；
3. Mixed GC 为什么叫 mixed？——同一轮 Evacuation 里既收新生代又收一部分"回收价值高"的老年代 Region，这正是 G1 名字的来源（价值优先）。

**【P10 加分项】** 给一个真实解读叙事："大促压测时我们从日志序列 `young(initial-mark) → concurrent-mark → young(to-space exhausted) → Full GC(3.4s)` 直接定位为 Humongous 晋升失败，全程没用 dump——**GC 日志的序列比单行数值更有信息量**，序列异常本身就会告诉你该查哪类问题。这也是我们 oncall 手册把'GC 日志解读'列在 dump 之前的原因。"

---
*下一章：第 4 章 Spring 与主流框架生态 —— IoC/AOP 源码、事务失效、自动装配，以及"Spring 解决了什么问题"的架构视角。*
