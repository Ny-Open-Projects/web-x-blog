# 对话版 · 第 1 章 Java 语言基础与集合（一面开局，约 20 分钟）

**【面试官】** 用过哪些集合？说说 ArrayList 和 LinkedList 的区别，什么场景选谁？

**【面试者】** ArrayList 底层是 Object[] 数组，支持随机访问 O(1)；LinkedList 是双向链表，随机访问 O(n)。结论是工程上几乎总是选 ArrayList：它内存连续、CPU 缓存友好；LinkedList 每节点两个指针内存放大严重，插入删除也必须先 O(n) 定位，优势场景几乎不存在。

**【面试官】** ArrayList 扩容机制说一下？

**【面试者】** 懒初始化：new ArrayList() 时数组是空的，首次 add 才扩到 10；超了按 1.5 倍增长（10→15→22），Arrays.copyOf 整体复制。1.5 倍是扩容次数与内存浪费的平衡。

**【评注】** ✅ 数字准确（已实证：第 11 个→15、第 16 个→22）。追加载体会问"为什么不是 2 倍"——答平衡即可。

**【面试官】** String 为什么设计成不可变？

**【面试者】** 四条：字符串常量池复用、hashCode 可缓存（hash 字段懒计算）、线程安全、安全性（类加载/网络参数不被篡改）。底层 JDK9+ 是 byte[] + coder（Compact Strings，纯 ASCII 省一半内存）。

**【面试官】** StringBuilder 和 StringBuffer 区别？循环里拼字符串要注意什么？

**【面试者】** StringBuffer 方法 synchronized 线程安全，StringBuilder 不安全但快——单线程一律 StringBuilder。拼接优化分两层：单行 `a+b` javac 会自动改写成 StringBuilder（JDK9+ 改为 invokedynamic + StringConcatFactory，按实际形态 specialize，比手写 Builder 还快）；但**循环内拼接即使有优化也每轮新建 Builder**，必须手动提到循环外。

**【评注】** ⭐ G1 补漏题。答出"JDK9 走 StringConcatFactory"直接超出面试官预期。

**【面试官】** == 和 equals 的区别？为什么重写 equals 必须重写 hashCode？

**【面试者】** == 比 基本类型的值 / 引用的地址；equals 默认也是 ==，重写后比业务内容。契约：equals 相等 → hashCode 必须相等，因为 HashMap 先 hash 定桶再 equals 精确匹配——只重写 equals 会 get 不到、set 去重失效。反面案例：可变对象做 key，修改字段后"丢失"。

**【面试官】** Integer 127 和 128 比较结果一样吗？

**【面试者】** 不一样。包装类缓存 -128~127：valueOf(127) 是同一对象，128 是新对象。规约是包装类比较一律 equals。（本机已实证 PASS。）

**【面试官】** 好，进阶一点。HashMap 的 put 流程完整说一遍？

**【面试者】** ① 计算 hash：`(h = key.hashCode()) ^ (h >>> 16)` 高低位异或；② table 为 null 先 resize 懒初始化；③ `(n-1) & hash` 定桶：桶空直接放；头节点命中（hash 相等且 ==/equals）覆盖；是 TreeNode 走树插入；否则遍历链表尾插，插入后若 bin 已有 8 个节点就调 treeifyBin——容量 <64 先扩容不树化，≥64 转红黑树；④ ++modCount，size 超阈值（容量×0.75）扩容 2 倍。

**【面试官】** 追问：树化的精确触发点？"链表长度 8"到底指什么？

**【面试者】** 这里有个容易答错的细节：**bin 已有 8 个节点时，下一次插入（第 9 个）才触发树化**——binCount 计的是遍历过的非头节点数，插到第 9 个时 binCount=7 ≥ TREEIFY_THRESHOLD-1。本机实测：64 容量表插 8 个同桶键仍是链表 Node，第 9 个才变 TreeNode（notes/verify 套件验证过）。TREEIFY_THRESHOLD 的 javadoc 写的语义就是"adding an element to a bin with at least this many nodes"。

**【评注】** ⭐⭐ 本场最高光时刻。绝大多数候选人答"8 个就树化"，能答出"第 9 个插入触发+给出实测证据"的凤毛麟角——直接从"背过源码"升级为"验证过源码"。

**【面试官】** 那为什么阈值选 8？退化为什么是 6？

**【面试者】** 泊松分布：负载 0.75 下 bin 长 8 的概率约千万分之一（0.00000006）——极端情况才值得树化的代价。退化 6 留 2 的缓冲，防 8 附近插入删除导致树↔链表来回抖动。

**【面试官】** JDK7 和 JDK8 的 HashMap 区别？

**【面试者】** 三条：头插改尾插（JDK7 并发扩容成环导致 CPU 100%，虽然 HashMap 本就不该并发）；链表+红黑树（最坏 O(n)→O(logn)）；扩容迁移优化——`hash & oldCap` 判断留在原位还是去 i+oldCap，不用重算 hash。

**【面试官】** ConcurrentHashMap 在 JDK8 怎么保证线程安全？key 能为 null 吗？

**【面试者】** CAS + synchronized 锁桶头：桶空 CAS 放头节点；非空 synchronized 锁头节点；遇到 ForwardingNode 协助扩容；size 用 baseCount + CounterCell 分段计数（LongAdder 思想）。get 全程无锁（Node.val volatile）。key/value 都不许 null——get 返回 null 有二义性，并发容器必须一次确定。

**【面试官】** 泛型的类型擦除是怎么回事？

**【面试者】** 编译期检查、运行时擦除：List<String> 和 List<Integer> 运行时都是 List。四个限制：不能 new T()/T[]/instanceof T；不支持基本类型；静态成员不能用类泛型参数；擦除后签名相同的重载编译不过。但 Signature 属性保留了泛型信息，反射 getGenericSuperclass 能拿到——Jackson 反序列化就靠这个。

**【面试官】** ThreadLocal 的原理和内存泄漏？

**【面试者】** 每个 Thread 有 ThreadLocalMap，key 是 ThreadLocal 的弱引用、value 强引用。泄漏路径：外部强引用消失后 key 被 GC 成 null，但 value 被线程强引用链持有，线程池线程不死就一直无法释放。修法：用完 finally 里 remove；本机实证过弱引用 key 在外部引用消失+GC 后确实被回收（WeakReference 验证）。跨线程池传上下文用阿里 TTL（提交捕获、回放、恢复）。

**【面试官】** 最后一个问题：Checked 异常是好设计吗？

**【面试者】** 敢于表态：理念好、工程代价大。lambda/Stream 里 Checked 异常极其碍事（Function 不允许抛），C#/Kotlin 都放弃了，大量代码 `catch(Exception e){}` 吞掉反而制造事故。我的实践：自定义异常继承 RuntimeException + 全局异常处理器 + 异常链保留。另外知道 HotSpot 会"无栈化"高频异常，排查时用 -XX:-OmitStackTraceInFastThrow 找回行号。

**【评注·终局】** 本场定级：**P6/P7 档通过**。亮点：树化精确触发点（实测证据）、CHM null 二义性、JDK9 拼接优化。风险点：无。可以进二面。

---

## 对话要点速记（本章）

1. 顺序：集合选型 → String → equals 契约 → HashMap 三连 → CHM → 泛型 → ThreadLocal → 异常表态。
2. 三个超预期点：树化第 9 插（实测）、StringConcatFactory、CHM null 二义性。
3. 面试官追问风格：每个"标准答案"后必有一个"边界追问"——背答案没用，理解才接得住。
