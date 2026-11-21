# 第 20 册 源码逐行精读 —— 四大必考源码的行级注释与背诵点

> 前面 19 册讲的是原理层；P8 以上的追问会直接落到源码行。
> 本册精读四段"出现率最高"的源码：HashMap.putVal、ConcurrentHashMap.transfer、
> AQS.acquireQueued、Spring refresh 十三步。代码为 JDK8 节选（省略无关行），注释是我的批注。
> 背法：先背批注（每段的★背诵点），再对着源码把批注"安放"回去。

---

## 20.1 HashMap.putVal（JDK8）

```java
final V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) {
    Node<K,V>[] tab; Node<K,V> p; int n, i;
    if ((tab = table) == null || (n = tab.length) == 0)
        n = (tab = resize()).length;              // ① 懒初始化：首次 put 才建表
    if ((p = tab[i = (n - 1) & hash]) == null)
        tab[i] = newNode(hash, key, value, null); // ② 桶空：直接放入（无锁，HashMap 本就不安全）
    else {
        Node<K,V> e; K k;
        if (p.hash == hash && ((k = p.key) == key || (key != null && key.equals(k))))
            e = p;                                // ③ 头节点命中：先比 hash 再 ==/equals
        else if (p instanceof TreeNode)
            e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value); // ④ 树化桶：走树插入
        else {
            for (int binCount = 0; ; ++binCount) {
                if ((e = p.next) == null) {
                    p.next = newNode(hash, key, value, null);   // ⑤ 尾插（JDK7 是头插）
                    if (binCount >= TREEIFY_THRESHOLD - 1)      // ⑥ binCount≥7 = bin 已有 8 个节点（新节点是第 9 个）→ 尝试树化
                        treeifyBin(tab, hash);                   //    注意：方法内部先查容量<64 则 resize
                    break;
                }
                if (e.hash == hash && ((k = e.key) == key || (key != null && key.equals(k))))
                    break;                        // ⑦ 中途命中相同 key：跳出走覆盖
                p = e;                            //    指针后移
            }
        }
        if (e != null) {                          // ⑧ 覆盖路径：返回旧值
            V oldValue = e.value;
            if (!onlyIfAbsent || oldValue == null)
                e.value = value;
            afterNodeAccess(e);                   //    LinkedHashMap 在此把节点移到尾部（LRU 钩子）
            return oldValue;
        }
    }
    ++modCount;                                   // ⑨ fail-fast 计数
    if (++size > threshold)
        resize();                                 // ⑩ size 超阈值：扩容 2 倍
    afterNodeInsertion(evict);                    //    LinkedHashMap 在此触发 removeEldestEntry
    return null;
}
```

**★背诵点（能脱口而出的 6 句）**：
1. 懒初始化：table 为 null 时首次 put 走 resize()；
2. 定位用 `(n-1) & hash`，前提容量是 2 的幂；
3. 匹配顺序：hash 相同 → `==` → equals（短路设计，equals 是兜底）；
4. 尾插在 `p.next == null` 分支，树化阈值判断在**插入后**，且 binCount 从 0 起、计的是“遍历过的非头节点数”——`binCount >= 7` 意味着 bin 已有 8 个节点、新节点是第 9 个；
5. treeifyBin 内部先判 `table.length < MIN_TREEIFY_CAPACITY(64)`，不足则先扩容不树化——这就是"树化 8 + 容量 64"的出处；**本机实测：64 容量表插 8 个同桶键仍是链表（Node），第 9 个才转 TreeNode**——与 TREEIFY_THRESHOLD 的 javadoc（adding an element to a bin with at least this many nodes）完全吻合；
6. 覆盖返回旧值、新增返回 null；LinkedHashMap 的 LRU 钩子全在 afterNodeAccess/afterNodeInsertion 两个回调里——**HashMap 专为子类预留的扩展点**。

**高频追问对照**：为什么是 `>= TREEIFY_THRESHOLD - 1` 而不是 `>= 8`？——binCount 计的是**除头节点外的遍历次数**：binCount=7 时 bin 恰有 8 个节点（头 + 7）。阈值语义是“bin 已有 8 个节点再插入就树化”（TREEIFY_THRESHOLD javadoc 原文），所以写 `-1`；若写 `>= 8` 会在 9 个节点后才触发，语义错误。

---

## 20.2 ConcurrentHashMap.transfer（扩容关键段）

```java
private final void transfer(Node<K,V>[] tab, Node<K,V>[] nextTab) {
    int n = tab.length, stride;
    if ((stride = (NCPU > 1) ? (n >>> 3) / NCPU : n) < MIN_TRANSFER_STRIDE)
        stride = MIN_TRANSFER_STRIDE;             // ① 每线程认领的最小区间 16 个桶
    if (nextTab == null) {
        // ② 第一个到达的线程创建 2 倍新表（用 CAS 保证只建一次）
        Node<K,V>[] nt = (Node<K,V>[])new Node<?,?>[n << 1];
        nextTable = nt;
        transferIndex = n;                        //    从旧表尾部往前迁移
    }
    ...
    for (int i = 0, bound = 0;;) {
        // ③ 认领区间：CAS 递减 transferIndex，拿到 [bound, i) 一段
        ...
        if (i >= n || i + n >= nextn) break;      // ④ 整表迁完：收尾换表
        if ((f = tabAt(tab, i)) == null)
            advance = casTabAt(tab, i, null, fwd);      // ⑤ 空桶放 ForwardingNode 路标
        else if (f.hash == MOVED)
            advance = true;                              // ⑥ 已是路标：跳过
        else {
            synchronized (f) {                     // ⑦ 锁桶头节点（锁粒度=单桶）
                if (tabAt(tab, i) == f) {          //    双检：防止并发中头节点变了
                    // ⑧ 拆链表/树，按 hash & oldCap 分两路：
                    //   低位链留在原桶 i，高位链放到 i + n
                    ...
                }
            }
        }
    }
}
```

**★背诵点（5 句）**：
1. stride 最小 16：线程按区间认领，CPU 多则区间小、并行度高——**多线程协助扩容的核心机制**；
2. 迁移方向从旧表**尾部往头**推进（transferIndex 递减），第一个线程建新表；
3. 每迁完一个桶放 **ForwardingNode**（hash=MOVED）作路标：get 遇到它会沿 nextTable 查新表；put 遇到它会**加入协助迁移**（helpTransfer）；
4. 迁移时锁桶头 + `tabAt(tab,i)==f` 双检——锁粒度细到单桶且防 ABA；
5. 拆分规则 `hash & oldCap` 决定去 i 还是 i+n——这就是 JDK8 扩容"不用重算 hash"的出处（呼应第 1 章追问链）。

**高频追问对照**：为什么 get 无锁也能保证正确？——空桶/迁移中桶靠 ForwardingNode 兜住，正常桶靠 Node.val 的 volatile 可见性；扩容期间的读要么读到旧表要么读到新表，都是一致视图。

---

## 20.3 AQS.acquire / acquireQueued

```java
public final void acquire(int arg) {
    if (!tryAcquire(arg) &&                        // ① 子类实现：非公平锁先 CAS 抢
        acquireQueued(addWaiter(Node.EXCLUSIVE), arg))  // ② 抢不到：入队尾再排队自旋
        selfInterrupt();
}

final boolean acquireQueued(final Node node, int arg) {
    boolean failed = true;
    try {
        boolean interrupted = false;
        for (;;) {
            final Node p = node.predecessor();
            if (p == head && tryAcquire(arg)) {    // ③ 只有前驱是 head 才再试一次
                setHead(node);                     // ④ 抢到：自己升为 head（原 head 摘除）
                p.next = null;                     //    断开引用 help GC
                failed = false;
                return interrupted;
            }
            if (shouldParkAfterFailedAcquire(p, node) &&  // ⑤ 先把前驱 waitStatus
                parkAndCheckInterrupt())                   //    置为 SIGNAL，再 park
                interrupted = true;                // ⑥ park 返回即检查中断标志
        }
    } finally {
        if (failed) cancelAcquire(node);           // ⑦ 异常路径：取消排队（摘链）
    }
}
```

**★背诵点（5 句）**：
1. 模板方法结构：acquire 定骨架，tryAcquire 留给子类（公平/非公平的差异只在 tryAcquire 里有没有 `hasQueuedPredecessors` 前置判断）；
2. **自旋+park 的混合**：前驱不是 head 就不白抢；`shouldParkAfterFailedAcquire` 把前驱置 SIGNAL 后**下次循环才真正 park**——留一次免挂起的机会；
3. 抢到锁的节点会 `setHead` 把自己变成新 head，旧 head 断链——队列头是"当前持有者或空位"的语义；
4. `parkAndCheckInterrupt` 返回"是否被中断"，acquire 用 selfInterrupt 补回中断状态（不能在 park 里直接抛，因为拿锁这件事优先级更高）；
5. finally 的 cancelAcquire 处理"tryAcquire 抛异常"的兜底摘链——双向链表的意义之一就是能摘自己（呼应第 2 章"为什么双向队列"）。

**高频追问对照**：release 后唤醒的是谁？——unparkSuccessor 从 head 往后找**第一个非取消节点**唤醒；为什么从后往前找？——addWaiter 入队时先设前驱再 CAS 尾指针，反向遍历能绕过尚未完全链接的新节点。

**⚠️ 版本核对（已对照 JDK 21.0.2 源码，2026-11-14）**：本节代码为 JDK8 节选——`putVal`、`transfer`（CHM 的 `runBit = fh & n` 拆分、`MIN_TRANSFER_STRIDE=16`、ForwardingNode）在 JDK 21 中逐行核实**完全一致**。但 **AQS 在 JDK 15+ 已重构**：JDK 21 中 `acquire` 变为 `if (!tryAcquire(arg)) acquire(null, arg, false, false, false, 0L);`（统一的私有 acquire 方法），`setHead/shouldParkAfterFailedAcquire/acquireQueued` 等旧方法名已消失。**原理不变**（state + CLH 变体队列 + park/unpark + SIGNAL 语义），变的是实现形态。面试时若被问"你读的哪个版本"，答："源码细节我按 JDK8 讲，JDK15+ AQS 重构过、方法名变了，但队列与唤醒语义不变"——这一句本身就是加分项。

---

## 20.4 Spring refresh() 十三步（必背顺序）

```java
public void refresh() throws BeansException, IllegalStateException {
    synchronized (this.startupShutdownMonitor) {
        prepareRefresh();                          // ① 环境准备：标志位、属性源初始化
        ConfigurableListableBeanFactory beanFactory = obtainFreshBeanFactory();  // ② 创建/刷新 BeanFactory（加载 BeanDefinition）
        prepareBeanFactory(beanFactory);           // ③ 给容器配置基础件：ClassLoader、SpEL 解析器、Aware 后处理器
        postProcessBeanFactory(beanFactory);       // ④ 子类扩展点（钩子）
        invokeBeanFactoryPostProcessors(beanFactory);  // ⑤ 执行 BFPP（★Configuration 解析、占位符都在这）
        registerBeanPostProcessors(beanFactory);   // ⑥ 注册 BPP（★AutowiredAnnotation/AutoProxyCreator 在此入册）
        initMessageSource();                       // ⑦ 国际化
        initApplicationEventMulticaster();         // ⑧ 事件广播器
        onRefresh();                               // ⑨ 子类钩子：Boot 在此启动 WebServer！
        registerListeners();                       // ⑩ 注册监听器
        finishBeanFactoryInitialization(beanFactory);  // ⑪ 实例化所有非懒加载单例（★Bean 生命周期全流程在这发生）
        finishRefresh();                           // ⑫ 发布 ContextRefreshedEvent、启动 Lifecycle
        // finally:
        resetCommonCaches();                       // ⑬ 清反射/注解缓存
    }
}
```

**★背诵点（6 句）**：
1. 第 ⑤ 步最关键：**BeanFactoryPostProcessor 先于一切 Bean 实例化执行**——@Configuration 类解析（ConfigurationClassPostProcessor）、${} 占位符填充都发生在这；这也解释了为什么 BFPP 不能注入业务 Bean（那时它们还没创建）；
2. 第 ⑥ 步注册 BPP：AOP 代理创建器（AbstractAutoProxyCreator）此刻入册，等 ⑪ 实例化 Bean 时逐个生效——**注册顺序决定增强顺序**；
3. 第 ⑨ 步 onRefresh：Spring Boot 的内嵌 Tomcat 就是在 WebServerApplicationContext 的 onRefresh 里启动的——"refresh 里嵌着整个 Boot"；
4. 第 ⑪ 步是 Bean 生命周期的舞台：实例化→注入→Aware→BPP→初始化全在这发生（呼应第 4 章题 4.2.1）；
5. 第 ⑫ 步发布 ContextRefreshedEvent：很多"启动后初始化"逻辑挂在这（注意父子容器会各发一次， dubbo 老版本的重复暴露坑就在这）；
6. 整个方法在 synchronized 里：refresh 与 close 互斥——优雅停机的互斥基础。

**高频追问对照**：@Configuration 类的 CGLIB 增强是谁做的？——ConfigurationClassPostProcessor（一个 BFPP）在 ⑤ 注册了增强后的 BeanFactoryPostProcessor，@Bean 方法互调保证单例语义全靠它生成的增强类。

---

## 20.5 精读方法论（比四段源码更重要的东西）

1. **三遍读法**：第一遍通读方法主干（只看 if/循环结构）；第二遍对每个 if 问"为什么作者要防这个"；第三遍找"为子类预留的钩子"（afterNode* / tryXxx / onRefresh）——**钩子是设计意图的显影液**；
2. **配平背诵**：先背"★背诵点"，再回头把每个背诵点安放到源码行——顺序反了就是死记硬背；
3. **对照 JDK7/8 差异**：putVal 的尾插、transfer 的多线程协助、CHM 的 CAS——每个差异都是一道面试题的出处；
4. **别贪多**：这四段覆盖了 HashMap/并发/AQS/Spring 四大必考区，读透这四段，其他源码（如 ThreadPoolExecutor.execute 三步）可以按同样的三遍法自行推导——**授人以渔的部分就在 20.5**。

## 速记卡

1. putVal 六结构：懒初始化→空桶→头命中→树→尾插+树化判→覆盖返回旧值→modCount/扩容。
2. 树化：binCount≥7 ⇒ bin 已有 8 个节点，第 9 个插入触发（实测 8 键仍链表）；容量<64 先扩容。
3. CHM transfer：stride≥16 认领区间、尾部往头迁、ForwardingNode 路标、锁桶头+双检、hash&oldCap 分两路。
4. AQS：前驱是 head 才再试、shouldPark 置 SIGNAL 后才 park、setHead 摘旧头、cancelAcquire 兜底。
5. release 从 head 向后找第一个非取消节点；入队先设前驱再 CAS 尾——所以反向遍历。
6. refresh 十三步，背 ⑤BFPP→⑥BPP→⑨onRefresh(Boot 启动 Tomcat)→⑪实例化单例 四个锚点。
7. @Configuration 的 CGLIB 增强来自 ConfigurationClassPostProcessor（BFPP）。
8. 源码三遍读法：主干 → 每个防御性 if 问为什么 → 找子类钩子。

---
*返回 [INDEX.md](../../INDEX.md)。源码精读完——至此全卷 20 册，从概念卡到源码行，一条完整的阶梯。*
