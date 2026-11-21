# 对话版 · 第 3 章 JVM 与性能调优（一面收尾/二面，约 25 分钟）

**【面试官】** JVM 内存区域说一下？

**【面试者】** 线程私有三个：程序计数器（唯一不 OOM）、虚拟机栈（StackOverflowError）、本地方法栈；共享两个：堆（Eden:Survivor 8:1:1 + 老年代）、方法区——JDK8 起是元空间，用本地内存，参数从 MaxPermSize 变 MaxMetaspaceSize，永久代 OOM 历史问题终结。字符串常量池 JDK7 起就在堆里。对象分配路径：TLAB → Eden CAS → Survivor 复制 → 年龄 15（MaxTenuringThreshold 默认值，PrintFlagsFinal 验证过）或动态年龄判定 → 老年代；1MB 大对象可能直接进 Humongous。

**【面试官】** 对象怎么判断该回收？引用分几种？

**【面试者】** 可达性分析，GC Roots：栈帧局部变量、静态变量、常量、JNI 引用、活跃线程。引用四等级：强不回收、软内存不足才收（缓存）、弱下次必收（ThreadLocalMap key）、虚配合 ReferenceQueue（堆外清理）。本机验证过 ThreadLocal key 的弱引用语义：外部引用消失+GC 后 key 确实被回收。

**【面试官】** G1 和 CMS 对比？你们怎么选？

**【面试者】** G1：Region 化、停顿预测模型、SATB；CMS：标记-清除有碎片、增量更新、并发模式失败退 Serial Old。选择有反直觉点：**小堆（<6G）CMS 反而更优**——G1 的 RSet 维护成本可能吃掉堆的 10%~20%，写屏障也有吞吐代价。我们 8G+ 全部 G1，低延迟核心服务在 JDK21 用分代 ZGC。"没有免费的并发"——每个收集器的停顿优化都是拿吞吐和内存换的。

**【面试官】** 三色标记讲一下？漏标怎么解决？

**【面试者】** 白未扫、灰自身扫完引用未扫、黑全扫完。漏标两条件：黑引用了白 + 灰到白的引用被断。两种修复：CMS 增量更新（把黑变灰重扫）、G1 SATB（记旧引用按快照算）。ZGC 更彻底：着色指针+读屏障自愈，连复制都并发。

**【面试官】** 线上服务 CPU 突然 100%，你的排查步骤？

**【面试者】** 传统三板斧：top 找进程 → top -Hp pid 找线程 → printf 转 16 进制 → jstack 抓栈定位。现在用 Arthas 更快：dashboard 总览 → thread -n 3 直接给最忙线程堆栈。判断逻辑：栈顶是业务代码行→死循环/低效算法；大量 GC 线程忙→转 GC 风暴，jstat 看趋势。我在沙盘里完整跑过：cpu 模式下 thread -n 3 直接给出 hotMethod 的行号。

**【评注】** ✅ "判断逻辑"那段是关键——面试官考的是分流思维，不是命令背诵。

**【面试官】** 频繁 Full GC 呢？完整排查流程？

**【面试者】** 四步：① jstat -gcutil 看趋势分流（堆内/元空间/堆外）；② 保留现场 heapdump -dump:live；③ MAT 支配树找 Retained Heap 最大对象→GC Roots 引用链；④ 常见结论速查：大 byte[]/String→大查询，ThreadLocalMap null-key→ThreadLocal 泄漏，静态 Map→只进不出缓存。全程必开三件套：HeapDumpOnOutOfMemoryError、GC 日志、ExitOnOutOfMemoryError。

**【面试官】** GC 日志你能读懂吗？说一行。

**【面试者】** 读过真实的。JDK9+ 统一日志：`GC(n) Pause Young (Normal) (G1 Evacuation Pause) 2048M->456M(4096M) 12.3ms`——GC(12) 的序号是重点（版本特征），停顿类型看序列：young → initial-mark → concurrent → mixed 是 G1 健康周期；回收后水位不回落=泄漏方向；`to-space exhausted`=Humongous 晋升失败先查大对象。Times 行 user≈2~3×real 是多线程并行正常。

**【评注】** ✅ 能背出"GC(12) 序号"这种细节，面试官会认定你真看过日志。

**【面试官】** 类加载过程？双亲委派为什么存在？什么场景打破？

**【面试者】** 加载→验证→准备（静态变量赋零值）→解析→初始化（<clinit>）。双亲委派：安全（核心类不可替换）、唯一（同类一个加载器）、复用。打破三场景：SPI 用线程上下文加载器反向委派、Tomcat 每应用隔离、热部署。JLS 细节我实测过：**实现类初始化会连带初始化"含 default 方法的"接口，不含 default 的不会**。

**【面试官】** JIT 为什么能让 Java 接近 C++？举一个你亲手验证的现象。

**【面试者】** 分层编译（C1 快 C2 深）+ 方法内联（<35 字节）+ 逃逸分析。亲手验证的：循环里 `new byte[64]` 三千万次，`-Xmx64m` 下 **GC 日志为零、瞬间跑完**——未逃逸分配被标量替换全消除了；把数组写到静态字段（逃逸）后，GC 立即按预期出现。所以逃逸分析不是玄学，日志能自证。工程落点：新实例要预热（灰度爬坡），避免编译期抖动。

**【面试官】** 给新服务配 JVM 参数，你的思路？

**【面试者】** 从业务画像推导不背圣经：容器场景 -Xms=-Xmx（或 MaxRAMPercentage 65）、必开三件套（HeapDumpOnOutOfMemoryError/统一 GC 日志/ExitOnOutOfMemoryError——最后这个让 OOM 快速失败被 K8s 重启）、堆外合计留 15%。验证闭环：压测看 P999 停顿调参。公司级做法：统一 JVM 基线镜像，新服务零配置继承。

**【评注·终局】** 定级 **P7~P8**。亮点：GC 日志实读、逃逸分析自证、参数从业务推导。JVM 域过。

---

## 对话要点速记（本章）

1. 追问顺序：内存区域 → 分配路径 → 引用等级 → 收集器对比 → 排查三板斧 → GC 日志 → 类加载 → JIT → 参数设计。
2. 三个实证背书：偏向锁标志移除、逃逸分析零 GC、MaxTenuringThreshold=15（PrintFlagsFinal 验证）。
3. 关键姿态：所有结论都挂"本机验证过"，把背诵题变成实验报告。
