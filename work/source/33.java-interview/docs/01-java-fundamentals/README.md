# 第 1 章 Java 语言基础与集合 —— 从零基础到阿里 P10

> 本章目标：零基础的人能读懂每一句话；P5-P6 的人能背下标准答案；P8 以上的人能被
> "追问链"逼到源码与设计权衡层面。P10 面试中，基础题不是重点，但答错基础题一票否决——
> P10 面试官会用 5 分钟基础题快速校准你的下限，再用 25 分钟架构题测量你的上限。

---

## 1.0 本章考察范围雷达（面试官视角）

| 维度 | P4-P5 要求 | P6-P7 要求 | P8-P10 要求 |
|------|-----------|-----------|------------|
| 语言核心 | 会用 final/String/equals | 讲清契约与陷阱 | 从语言设计角度评价优劣 |
| 集合 | 会用 ArrayList/HashMap | 讲清扩容、树化、并发容器源码 | 指出 JDK 设计缺陷并给出改进方案 |
| 泛型 | 会写泛型方法 | 类型擦除与 PECS | 与 Kotlin/C# 泛型对比、性能影响 |
| 编码素养 | 代码能跑 | 阿里规约、防御式编程 | 用代码风格判断团队工程文化 |

**面试官常用开场**："我看你简历写了熟悉 Java，那我们先聊聊基础。"——这不是客气，
接下来 3~5 道题每一道都有坑。

---

## 1.1 零基础起步：先把"地基"概念钉死

在背任何面试题之前，先把下面 8 张"概念卡"读三遍。后面所有题都建立在这上面。

### 卡片 1：JDK / JRE / JVM
- **JVM**：虚拟机，负责把字节码（.class）翻译成机器码执行。一次编译，到处运行。
- **JRE** = JVM + 核心类库（java.lang、java.util 等），只能运行程序。
- **JDK** = JRE + 开发工具（javac 编译器、jdb 调试器、jstack/jmap 排查工具），能开发程序。
- 记忆口诀：**JDK 开发用，JRE 运行用，JVM 是心脏**。

### 卡片 2：编译型 vs 解释型，Java 是什么？
Java 是**混合型**：javac 先把 .java 编译成 .class（字节码），JVM 再边解释边编译
（JIT 把热点代码编译成机器码）。所以 Java 既不是纯编译型（如 C），也不是纯解释型（如 Python）。

### 卡片 3：8 种基本类型与包装类型
| 类型 | 字节 | 范围/备注 | 包装类 |
|------|------|-----------|--------|
| byte | 1 | -128~127 | Byte |
| short | 2 | | Short |
| int | 4 | 约 ±21 亿 | Integer |
| long | 8 | | Long |
| float | 4 | 单精度 | Float |
| double | 8 | 双精度 | Double |
| char | 2 | Unicode | Character |
| boolean | — | JVM 规范未定大小，通常按 1 byte 或 int 处理 | Boolean |

为什么要包装类？**泛型不支持基本类型**（List<int> 非法），且包装类提供了
MAX_VALUE、parseInt 等工具与 null 语义（数据库字段可空）。

### 卡片 4：自动装箱与拆箱
- `Integer a = 127;` 自动装箱 = 编译器插入 `Integer.valueOf(127)`。
- `int b = a;` 自动拆箱 = `a.intValue()`。
- **必背坑点**：Integer 缓存 -128~127。`Integer a=127, b=127; a==b` 为 true；
  `Integer c=128, d=128; c==d` 为 false（128 超出缓存，new 了新对象）。
  阿里规约禁止用 == 比较包装类，必须用 equals。

### 卡片 5：== 与 equals 与 hashCode
- `==`：基本类型比值；引用类型比**地址**。
- `equals`：默认就是 ==（Object 源码 `return this == obj;`），重写后比内容。
- **契约**：重写 equals 必须重写 hashCode，否则 HashMap/HashSet 出错。
  契约内容：equals 相等 ⇒ hashCode 必须相等；hashCode 相等 ≠ equals 相等（哈希冲突）。
- 反例：只重写 equals 不重写 hashCode，两个"相等"的对象放进 HashSet 会出现两份。

### 卡片 6：String 为什么是不可变的？
String 内部是 `private final byte[] value`（JDK9 后从 char[] 改为 byte[] + coder 字段，
拉丁字符省一半内存）。不可变的好处必背 4 条：
1. **字符串常量池复用**：不可变才能安全共享，省内存。
2. **hashCode 可以缓存**：String 的 hash 字段懒计算后缓存，作 HashMap key 更快。
3. **线程安全**：天然不可变，多线程随便读。
4. **安全性**：类加载器、网络参数用 String 传，防止被中途篡改。

### 卡片 7：栈、堆、方法区（先记结论，第 3 章展开）
- 局部变量、方法调用 → **栈**（线程私有，栈溢出 StackOverflowError）。
- new 出来的对象 → **堆**（线程共享，GC 主战场，OOM）。
- 类信息、常量、静态变量 → **元空间/方法区**（JDK8 起字符串常量池已从方法区挪到堆）。

### 卡片 8：final / finally / finalize 三兄弟
- `final`：修饰类（不能继承）、方法（不能重写）、变量（基本类型值不能变，引用类型地址不能变）。
- `finally`：try-catch 后必执行（除非 System.exit() 或 JVM 崩溃）。**不要在 finally 里 return**，会吞掉异常。
- `finalize`：Object 的回收前回调，JDK9 已标记 @Deprecated，性能差且不可靠，用 try-with-resources 或 Cleaner 替代。

---

## 1.2 入门题（P4-P6 必答对，答错即出局）

### 题 1.2.1：String s = new String("abc") 创建了几个对象？

**【面试官意图】** 不在考数字，在考你是否知道常量池、编译期 vs 运行期。

**【参考回答（可背）】**
标准说法是 1 个或 2 个：
- 若 "abc" 字面量**不在**常量池中：先在常量池创建 "abc"（编译期就确定，类加载解析阶段放入），再在堆中 new 一个 String 对象，共 **2 个**。
- 若常量池中已有 "abc"（比如之前执行过字面量赋值）：只在堆中 new **1 个**。
- 补充：JDK7 起字符串常量池从永久代移到了堆中。

**【追问链】**
1. "abc" 是什么时候进常量池的？→ 编译期是 class 文件常量池里的符号引用，类加载解析阶段转为直接引用；intern 时才真正入池（JDK7 后入池的是堆中对象的引用而非拷贝）。
2. `s.intern() == s` 返回什么？→ JDK7+：new String("abc") 的对象在堆中，intern 发现常量池已有等值引用（或把堆引用复制进池），返回 true。（JDK6 会返回 false，因为 intern 是把字符串**拷贝**进永久代。）

**【P10 加分项】**
主动指出这是"面试考古题"，真实工程意义在于：**用字面量代替 new**（编译器优化+池化），
以及 JDK9 的 Compact Strings（byte[]+coder）让纯 ASCII 字符串内存减半——说明你关注 JDK 演进而非背题。

---

### 题 1.2.2：== 和 equals 的区别？为什么重写 equals 必须重写 hashCode？

**【参考回答（可背）】**
- == 比较基本类型的值或引用类型的地址；equals 默认行为是 ==，重写后比较业务内容。
- 契约：equals 相等的两个对象，hashCode 必须相等。原因：HashMap 先用 hashCode 定位桶，再用 equals 精确匹配。只重写 equals 不重写 hashCode，两个业务上相等的对象会落进不同桶，导致"get 不到、set 去重失效"。
- 反例必背：把对象当 HashMap 的 key，之后修改了参与 hashCode 计算的字段 → 该对象"丢失"，get 返回 null，且无法 remove。

**【追问链】**
1. hashCode 相等，equals 一定相等吗？→ 不一定，这是哈希冲突；equals 相等 hashCode 一定相等，这是硬契约。
2. 有没有重写过 hashCode？怎么写？→ 用 Objects.hash(field...)；或 IDE 生成；进阶说 31 的原因（见题 1.2.3）。

**【P10 加分项】**
提到 Lombok @EqualsAndHashCode 的坑（callSuper 默认 false，继承场景会漏比较父类字段）、
以及"可变对象不适合做 HashMap key"这一架构级结论。

---

### 题 1.2.3：为什么 HashMap 计算 hash 要用 31 作为乘子？

**【参考回答（可背）】**
1. 31 是奇素数，乘出来的散列分布更均匀，冲突更少。
2. 性能：`31 * i == (i << 5) - i`，JVM 可优化为移位和减法，一条指令级别。
3. 历史经验：这是经过大量字符串测试（Effective Java 引用的研究）得出的折中值；太小（如 2 的幂）低位信息丢失严重，太大容易溢出。

**【追问链】**
1. HashMap 是直接用 hashCode 吗？→ 不是，`(h = key.hashCode()) ^ (h >>> 16)`：高 16 位异或低 16 位，让高位也参与运算，因为定位桶用的是 `hash & (n-1)`，n 通常很小，只有低位参与。
2. 为什么桶定位用 & 而不是 %？→ & 只在 n 是 2 的幂时等价于 %，但快得多——这就是 HashMap 容量必须是 2 的幂的根本原因。

**【P10 加分项】**
指出 String.hashCode 在大面积数字字符串（如订单号）场景下分布并不好，
公司内部曾有"hashCode 撞桶导致 HashMap 退化成链表"的真实案例，解决方式是自定义 key 或改用更均匀的哈希。

---

### 题 1.2.4：ArrayList 和 LinkedList 的区别？谁更快？

**【参考回答（可背）】**
- ArrayList 底层是 Object[] 数组，支持随机访问 O(1)；LinkedList 底层双向链表，随机访问 O(n)。
- 插入删除：**并非 LinkedList 一定快**。尾部追加 ArrayList 均摊 O(1)；LinkedList 虽然插入动作 O(1)，但先要遍历定位 O(n)。中间插入两者都要移动/遍历元素。
- 内存：ArrayList 连续内存、CPU 缓存友好（局部性原理）；LinkedList 每个节点额外 2 个指针 + 对象头，内存放大严重且对缓存极不友好。

**【追问链】**
1. ArrayList 扩容机制？→ 默认初始容量 10（懒加载：new ArrayList() 时数组是空的，首次 add 才扩到 10），扩容 1.5 倍（oldCapacity + (oldCapacity >> 1)），用 Arrays.copyOf 复制。
2. 为什么是 1.5 倍？→ 平衡"扩容次数"与"内存浪费"；3 倍浪费内存，1.1 倍扩容太频繁。k 倍扩容的总复制代价近似与 n·k/(k-1) 成正比。
3. 可以边遍历边删除吗？→ 不能用 for 循环 + list.remove(i)，会漏元素且索引错位；要用 Iterator.remove() 或 JDK8 的 removeIf。并发场景用 CopyOnWriteArrayList。

**【P10 加分项】**
- 明确说"工程上几乎总是选 ArrayList"，LinkedList 在 Java 标准库中被认为是设计失误的 API（它还实现了 Deque，应该只暴露 Deque 接口）。
- 提到缓存行（64 字节）与内存局部性对性能的影响，说明你理解"为什么数组快"的硬件原理，而不只是背 API。

---

### 题 1.2.5：HashMap 的 put 流程？（JDK8）

**【参考回答（可背）】**（这是 Java 面试出现率第一的题，必须脱口而出）
1. 计算 key 的 hash：高 16 位异或低 16 位。
2. 若 table 未初始化（或容量 0），先 resize() 初始化。
3. `(n-1) & hash` 定位桶：
   - 桶为空 → 直接放入；
   - 桶首节点 key 相同（hash 相等且 == 或 equals）→ 覆盖；
   - 首节点是 TreeNode → 走红黑树插入；
   - 否则遍历链表：找到相同 key 就覆盖，到尾部就尾插新节点（JDK8 改为尾插）。**树化的精确触发**：bin 已有 8 个节点时，下一次插入（第 9 个）调用 treeifyBin——容量 ≥ 64 → 转红黑树；容量 < 64 → 只扩容不树化。（本机实测：64 容量表插 8 个同桶键仍是链表 Node，第 9 个才变 TreeNode，见 notes/verify）。
4. ++modCount（fail-fast 机制），++size 后若超过 threshold（容量×负载因子 0.75）→ resize 扩容为 2 倍。

**【追问链】**
1. 为什么负载因子是 0.75？→ 空间与时间的折中：太小频繁扩容浪费内存，太大冲突多查询变慢。泊松分布推导：负载 0.75 下 bin 长度达到 8 的概率约千万分之一（0.00000006），这正是选 8 做树化阈值的依据。
2. JDK7 和 JDK8 的区别？→ 头插改尾插（头插在并发扩容时会形成环形链表导致 CPU 100%，虽然 HashMap 本身就不该并发使用）；链表+红黑树（最坏从 O(n) 到 O(logn)）。
3. 为什么树化阈值是 8、退化阈值是 6？→ 阈值 8 的语义是“bin 已有 8 个节点时，下一次插入触发树化”（TREEIFY_THRESHOLD javadoc 原文：adding an element to a bin with at least this many nodes——本机实测 8 键仍是链表、第 9 个转 TreeNode）；8 来自泊松分布统计边界。退化用 6 留 2 的缓冲，防 8 附近插入删除导致树↔链表来回抖动。
4. 扩容时元素怎么迁移？→ JDK8 优化：扩容后元素要么留在原位置 i，要么去 i + oldCap，由 `hash & oldCap` 是否为 0 决定，无需重新计算 hash。

**【P10 加分项】**
- 主动讲 JDK8 红黑树实现细节：TreeNode 保留了 next 指针，树节点同时是链表节点，且树化/退化共享同一份节点对象，避免对象重建。
- 指出 HashMap 在极端 hash 攻击下的退化问题（Tomcat 曾因此改用随机 hash 种子），体现安全视角。
- 讲清 fail-fast（modCount）≠ 线程安全：ConcurrentModificationException 只是尽力而为的检测。

---

### 题 1.2.6：ConcurrentHashMap 如何保证线程安全？（JDK8）

**【参考回答（可背）】**
- JDK7 是分段锁（Segment 继承 ReentrantLock，默认 16 段，并发度=段数）。
- JDK8 抛弃分段锁，改为 **CAS + synchronized 锁单个桶头节点**：
  1. 桶为空 → CAS 放入头节点，失败自旋重试；
  2. 桶非空 → synchronized 锁住头节点后链表/树插入；
  3. 正在扩容的桶（ForwardingNode）→ 当前线程帮助迁移（多线程协助扩容）；
  4. size 用 baseCount + CounterCell[] 分段计数（思想同 LongAdder），避免所有线程争抢一个计数器。
- get 全程无锁：Node.val 和 next 用 volatile 保证可见性；table 用 volatile 读。

**【追问链】**
1. 为什么 JDK8 用 synchronized 而不是 ReentrantLock？→ 锁粒度已经细到单个桶，冲突概率低，synchronized 经锁升级优化后（偏向/轻量级）性能不吃亏，且省内存（无 AQS 队列节点）、JVM 可继续优化。
2. ConcurrentHashMap 的 key/value 能为 null 吗？→ 都不能。二义性问题：get 返回 null 无法区分"不存在"还是"值就是 null"（HashMap 可以，因为它容许并发出错再重查；并发容器必须一次确定）。这与 Hashtable 一致。
3. size() 准确吗？→ 返回的是统计瞬间的近似值（并发下无全局锁），强一致需求要用 synchronized 包裹或改用其他结构。
4. 多线程 put 会丢数据吗？→ 不会丢（CAS+锁），但"check-then-act"复合操作（先 get 判断再 put）依然需要 putIfAbsent/computeIfAbsent 这类原子方法。

**【P10 加分项】**
- 讲清多线程协助扩容的 transfer 细节：按桶区间（stride，最小 16）认领迁移任务，ForwardingNode 作为"此处已迁移"的路标。
- 指出 computeIfAbsent 的死循环坑（JDK8 中若回调里又操作同一个 key 的桶会卡住，JDK9 修复）——这是真实生产事故素材。

---

### 题 1.2.7：HashMap 是线程安全的吗？多线程下会发生什么？用什么替代？

**【参考回答（可背）】**
不安全。JDK7 并发扩容可能形成环形链表 → get 死循环 CPU 100%；JDK8 修复了成环，但仍会丢数据、size 不一致。替代方案：
1. 只读场景：Collections.unmodifiableMap 或 Map.copyOf（不可变）。
2. 并发写：ConcurrentHashMap。
3. 需要保持插入/访问顺序：Collections.synchronizedLinkedHashMap 或自己加锁。
4. 高频读低频写：读写锁 + 不可变快照（Copy-On-Write 思想）。

**【P10 加分项】**
区分"线程安全"与"复合操作原子性"：即使换成 ConcurrentHashMap，`if(!map.containsKey(k)) map.put(k,v)` 仍不是原子的，必须用 putIfAbsent——大量生产 bug 出在这里，说明你被真实场景毒打过。

---

## 1.3 进阶题（P7-P8 深挖）

### 题 1.3.1：泛型的类型擦除是怎么回事？会带来哪些限制？

**【参考回答（可背）】**
Java 泛型是**编译期**的，编译后字节码里泛型信息基本被擦除：`List<String>` 和 `List<Integer>` 运行时都是 `List`。类型检查在编译期完成，编译器在调用处自动插入 checkcast 强转。
限制（必背 4 条）：
1. 不能 `new T()`、`T[]`、`instanceof T`（运行时没有 T）。
2. 不能 `List<int>`（擦除后 Object 存不了基本类型）。
3. 静态方法/字段不能使用类的泛型参数（静态成员属于类，实例化前泛型已无关）。
4. 重载冲突：`void f(List<String>)` 和 `void f(List<Integer>)` 编译不过（擦除后签名相同）。

**【追问链】**
1. 完全擦除了吗？→ 不是，泛型签名保留在 class 文件的 Signature 属性里，所以反射通过 `getGenericSuperclass()` 能拿到字段/方法的泛型——Jackson/Gson 反序列化就靠这个。
2. 通配符 `? extends` 与 `? super`？→ PECS 原则（Producer Extends, Consumer Super）：只读用 extends（List<? extends Number> 只能取不能加），只写用 super（List<? super Integer> 只能加 Integer 及子类）。本质是协变/逆变的编译期安全设计。
3. 为什么要设计成擦除而不是像 C#/Kotlin 那样的真泛型？→ **向后兼容**：JDK5 要让泛型代码与 JDK1.4 的非泛型字节码二进制兼容，擦除是当时唯一现实解；代价是运行时性能（装箱/拆箱、强转）与表达能力。

**【P10 加分项】**
- 对比 Valhalla 项目（ specialized generics，未来可能支持 List<int>），展示对 JDK 演进路线的跟踪。
- 讲清"桥接方法"（bridge method）：泛型子类重写父类方法时编译器生成的合成方法，AOP/反射框架需要特殊处理。

---

### 题 1.3.2：ThreadLocal 的原理与内存泄漏？

**【参考回答（可背）】**（放本章因为它是"语言级"机制，第 2 章会再用它）
- 每个 Thread 内有一个 ThreadLocalMap，key 是 ThreadLocal 对象的**弱引用**，value 是强引用。
- set/get 时先拿当前线程的 map，以 ThreadLocal 自身为 key。
- 泄漏路径：ThreadLocal 外部引用消失后，key 被 GC 回收变成 null，但 value 仍被 Thread→map→entry 强引用链持有；线程池中线程不死，value 就一直无法释放。
- 正确姿势：**用完必须 remove()**，且放在 finally 中；框架层面（如 Spring 的 RequestContextFilter）用 try-finally 清理。

**【追问链】**
1. 为什么 key 用弱引用？→ 缓解而非根治泄漏：让"ThreadLocal 实例本身"可被回收；且 set/get/remove 时会顺带清理 key 为 null 的 stale entry（探测式清理 expungeStaleEntry）。
2. 为什么 value 不用弱引用？→ 若 value 也弱引用，外部没有引用时 value 会随时被回收，业务数据会无故丢失——宁可泄漏（可通过 remove 清理）也不能丢数据。
3. InheritableThreadLocal 和 TransmittableThreadLocal 区别？→ 前者仅在线程创建时复制给子线程，线程池复用线程时不生效；阿里开源的 TTL 通过装饰 Runnable/Callable，在提交任务时捕获、执行时回放、结束时恢复，解决线程池上下文传递（链路 traceId 传递的标准方案）。

**【P10 加分项】**
结合真实事故讲：一次压测中 ThreadLocal 泄漏导致老年代缓慢上涨最终 Full GC 频繁，通过 jmap histo 找到 ThreadLocalMap 中大量 null-key entry 定位。这体现了"把语言知识接到 JVM 排查能力"的 P10 闭环。

---

### 题 1.3.3：接口和抽象类怎么选？JDK8 后接口有了默认方法，两者还有区别吗？

**【参考回答（可背）】**
- 语法差异：抽象类单继承可有状态（字段、构造器），接口多实现无状态（JDK8 后可有 static/default 方法，字段仍只能是常量）。
- 语义差异（核心答案）：抽象类表达 **"是什么"**（is-a，模板复用，如 AbstractList），接口表达 **"能做什么"**（can-do，能力契约，如 Comparable、Serializable）。
- JDK8 默认方法的意义：让接口可以**演进**——Collection.stream() 就是通过 default 方法加到所有既有实现上的，不需要修改千万个实现类。

**【追问链】**
1. 两个接口的 default 方法冲突怎么办？→ 实现类必须重写冲突方法，可用 `InterfaceA.super.method()` 显式委托。
2. 模板方法模式在 JDK 源码哪里？→ AQS（acquire 定骨架，tryAcquire 留给子类）、AbstractList、ThreadLocalMap 的部分设计，AQS 是最典型的例子（第 2 章展开）。

**【P10 加分项】**
从"面向组合优于面向继承"的角度谈：默认方法解决了接口演进，但也引入菱形继承的复杂度，团队规范上应约束 default 方法仅用于"接口演进"而不作为多继承手段。

---

### 题 1.3.4：讲讲 Java 的异常体系？Checked 异常是好设计吗？

**【参考回答（可背）】**
- Throwable → Error（OOM/StackOverflowError 等不可恢复）与 Exception。
- Exception 分 Checked（编译器强制 catch/throws，如 IOException）与 Runtime（RuntimeException 及其子类，如 NPE、数组越界）。
- 使用原则：可恢复、调用方必须处理的用 Checked；编程错误用 Runtime。
- 最佳实践（可背清单）：不要捕获 Throwable/Error；不要吞异常（catch 空块）；保留异常链（throw new X("...", e)）；自定义异常继承 RuntimeException；日志与抛出二选一不要都做（避免重复打日志）。

**【追问链】**
1. Checked 异常是好的设计吗？→ 争议题。正方：强制调用方处理，契约清晰。反方（P10 应敢于表态）：实践证明 lambda/流式 API 中 Checked 异常极其碍事（Function 不允许抛），C#/Kotlin/Go 都放弃了它，大量工程中 Checked 异常被 `catch (Exception e) {}` 吞掉，反而制造事故。结论：**理念好、工程代价大**，新设计建议用 Runtime + 全局异常处理器。
2. try-with-resources 原理？→ 编译器生成字节码按逆序 close()，并做 suppressed exception 附加（主异常保留，close 抛的异常挂到 addSuppressed），比手写 finally 更正确。

**【P10 加分项】**
谈异常对性能的真实影响：JVM 无异常表命中时的抛出代价主要是**栈回溯填充**（-XX:-OmitStackTraceInFastThrow 可禁用 HotSpot 对高频异常的"无栈化"优化——排查生产 NPE 却看不到行号就是它干的）。

---

## 1.4 压轴题（P9-P10：源码、权衡、复盘）

### 题 1.4.1：如果要你设计一个"高并发下的本地缓存"，集合层面你会怎么做？LinkedHashMap 怎么改成 LRU？

**【面试官意图】** 这题从 JDK 集合直接跳到架构设计，考察"从源码到系统"的能力纵深，是 P9/P10 分水岭题。

**【参考回答（结构可背）】**
1. **LRU 基础实现**：继承 LinkedHashMap，重写 `removeEldestEntry()` 返回 size > capacity，构造时传 accessOrder=true（访问顺序排序）。原理：LinkedHashMap 在 HashMap 基础上用双向链表串起所有节点，get/put 都把节点移到尾部，淘汰头部。
2. **线程安全升级**：LinkedHashMap 非线程安全，简单方案 synchronized 包裹但高并发下锁竞争严重；升级为**分段锁**或 CAS 环形链表；工业级方案是 JDK 自带 Caffeine 的思路：
   - 用 **W-TinyLFU** 替代纯 LRU（LRU 对偶发批量扫描不友好，会把热点全冲掉）——频率统计用 Count-Min Sketch（近似计数，内存 O(桶数) 而非 O(key数)）；
   - 写缓冲（RingBuffer）异步刷主结构，读基本无锁（Buffer 后置合并）；
   - 热点 key 用异步 refresh（loadingCache），过期时间加随机抖动防雪崩。
3. **与分布式层配合**：本地缓存只放"读多写少 + 可容忍秒级不一致"的数据，配合消息广播失效（Redis Pub/Sub 或 MQ 通知所有节点失效本地 key）。
4. **监控兜底**：命中率、缓存大小、淘汰速率必须暴露到 Metrics，命中率突然下跌往往是大促预热失效的先兆。

**【追问链】**
1. 为什么不用 synchronized 的 LruCache / Guava Cache？→ 逐步对比：Hashtable 时代 LruCache 锁粒度太粗；Guava 用分段+LRU 但单桶操作仍有锁；Caffeine 是 JUC 作者 Doug Lea 参与后的新一代设计，读路径接近 ConcurrentHashMap（JMH 数据大约 10x Guava）。
2. 多级缓存的一致性怎么取舍？→ 承认"做不到强一致"，给方案矩阵：秒级容忍→TTL；准实时→广播失效；要求强一致→本地缓存退化为"只存可重建数据"，以 DB/分布式缓存为准。

**【P10 加分项】**
复盘视角："我们业务上曾把本地缓存从 Guava 迁到 Caffeine，动机是大促时一次全量跑批把 LRU 热点全冲掉，DB QPS 飙了 8 倍；迁移后用 TinyLFU 的 admission 策略挡住了扫描流量，缓存命中率从 82% 回到 97%。"——**有数字、有事故、有方案、有验证**，这就是 P10 的叙事范式。

---

### 题 1.4.2：HashMap 已经很成熟了，如果让你重新设计一个 Java 集合框架，你会改什么？

**【面试官意图】** 开放题，考察对 JDK 集合的整体评价与架构批判力，没有标准答案，考察思维框架。

**【参考回答（框架可背：肯定 → 批判 → 改进 → 兼容性）】**
1. **肯定**：接口分层（Collection/Map/List/Set）清晰；迭代器模式统一遍历；JDK8 Stream 把"做什么"与"怎么做"分离。
2. **批判**：
   - 可变集合为默认，不可变集合反而要绕（List.of JDK9 才有），导致防御式复制遍地都是；
   - 原始类型装箱税：Collection 只能存对象，int 装箱带来内存 4 倍放大与 GC 压力（Eclipse Collections/HPPC 的存在价值）；
   - equals/hashCode 契约靠程序员自觉，是 HashMap 一切误用的根源；
   - 部分历史 API 设计矛盾：Stack 继承 Vector、Properties 继承 Hashtable、LinkedList 兼任 Deque。
3. **改进方向**：以不可变集合为默认（函数式风格，结构共享代替深拷贝）；值类型泛型（Valhalla）；集合的字面量语法与模式匹配深度集成（JDK21 记录解构）。
4. **兼容性约束**：JDK 每一步都要保证二进制兼容，这正是"擦除泛型、List.of 延迟出现"的根本原因——架构演进的第一约束不是理想设计，而是存量生态。

**【P10 加分项】**
落到自己团队："我们在公司基础库做了同样的事——封一层 immutable-first 的集合工具，禁止跨服务边界传可变集合，线上因'调用方改了入参 List'导致的事故归零。"体现把语言判断转化为团队工程规范的能力。

---

## 1.5 本章高频追问链图谱（背诵版）

```
String 不可变 ──→ 常量池 ──→ intern 在 JDK7 的行为变化 ──→ Compact Strings
==/equals ──→ hashCode 契约 ──→ HashMap 定位原理 ──→ 31 乘子/扰动函数 ──→ 2 的幂
ArrayList ──→ 扩容 1.5 倍 ──→ fail-fast modCount ──→ 并发替代品选择
HashMap put ──→ 树化阈 8（第 9 插触发）/退化 6 ──→ 泊松分布/负载因子 0.75 ──→ JDK7 头插成环 ──→ CHM CAS+sync
泛型 ──→ 擦除 ──→ PECS ──→ 反射拿泛型 ──→ Valhalla
ThreadLocal ──→ 弱引用 key ──→ 泄漏与 remove ──→ TTL 上下文传递
```

## 1.6 一页速记卡（考前 30 分钟过一遍）

1. Integer 缓存 -128~127；包装类比较必须 equals。
2. String 不可变 4 大好处：池化、hash 缓存、线程安全、安全。
3. 重写 equals 必重写 hashCode；可变对象别做 key。
4. ArrayList 扩容 1.5 倍、懒初始化 10；LinkedList 工程上基本不用。
5. HashMap：hash=高16异或低16；容量 2 的幂；负载 0.75；树化阈 8（bin 8 个后第 9 插触发）容量 64；尾插。
6. CHM：CAS+synchronized 锁桶头；size 用 CounterCell；key/value 不许 null；get 无锁。
7. 泛型擦除 4 限制；PECS；Signature 属性可反射拿泛型。
8. ThreadLocal：key 弱 value 强；用完 remove；线程池传上下文用 TTL。
9. LinkedHashMap accessOrder=true + removeEldestEntry = LRU；工业级用 Caffeine（TinyLFU）。
10. 异常：Error 别捕、别吞、留链（cause）、别重复打日志；-OmitStackTraceInFastThrow 排查无栈 NPE。

## 1.7 参考资料与延伸阅读
- 《Effective Java》第 3 版 —— Item 10-17（equals/hashCode）、Item 31（PECS）
- 《Java 源码分析》系列：HashMap/ConcurrentHashMap 逐行注释（本仓库 notes 目录后续补充）
- JDK 源码：java.util.HashMap#putVal、ConcurrentHashMap#transfer、LinkedHashMap#afterNodeAccess
- 阿里《Java 开发手册》（嵩山版）—— 集合处理篇全部为强制条款，值得整篇背诵

---
*下一章：第 2 章 并发编程与 JUC —— 从 happens-before 到 AQS 源码，P10 面试的真正主战场。*
