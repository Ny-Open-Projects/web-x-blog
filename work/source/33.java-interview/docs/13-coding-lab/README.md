# 第 13 册 手写代码题全解 —— 面试现场白板可写的 10 道经典题

> P10 面试的代码环节不是算法竞赛，考察三点：**边界严谨、并发正确、边写边讲**。
> 本册每题给出：可背完整代码 + 边写边讲的话术 + 面试官埋的坑。
> 建议全部亲手敲一遍（装 JDK 后本机即可验证），白板手写时只保留核心结构。

---

## 题 1：双重检查锁定单例（DCL）—— 必考第一题

```java
public class Singleton {
    private static volatile Singleton instance;   // volatile 不可省！

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {                   // 第一次检查：避免每次加锁
            synchronized (Singleton.class) {
                if (instance == null) {           // 第二次检查：防止重复创建
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

**边写边讲**：① 第一次检查避免已初始化后的锁开销；② 双重检查防止两个线程同时通过第一次检查后重复创建；③ volatile 防止 `new` 的三步（分配→初始化→赋引用）发生 2-3 重排，导致其他线程拿到半初始化对象。

**面试官埋的坑**：
- "去掉第二次检查行不行？" → 不行，两个线程都能过第一次检查，B 在 A 释放锁后会再 new 一次。
- "为什么要 volatile，锁不是已经互斥了吗？" → 锁保证创建互斥，但**读**不受锁保护（第一次检查无锁），volatile 补的是读的可见性与有序性。
- 加分递进：写出更好的替代——静态内部类 Holder（利用类加载的天然线程安全+懒加载）与枚举（防反射+防反序列化破坏）：

```java
// Holder 版：推荐默认写法
public class Singleton {
    private Singleton() {}
    private static class Holder { static final Singleton I = new Singleton(); }
    public static Singleton getInstance() { return Holder.I; }
}
```

---

## 题 2：手写 LRU 缓存（LinkedHashMap 版 + 纯手写双向链表版）

**30 秒版（先给这个，体现 API 熟练）**：

```java
class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;
    LRUCache(int capacity) {
        super(16, 0.75f, true);          // true = accessOrder 按访问顺序
        this.capacity = capacity;
    }
    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;        // 超容量淘汰"最老"节点
    }
}
```

**追问必到手写版（双向链表 + HashMap，O(1)）**：

```java
class LRUCache {
    private final int capacity;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node();   // 哨兵头（存最新）
    private final Node tail = new Node();   // 哨兵尾（存最旧）

    static class Node { int key, value; Node prev, next; Node() {} 
                        Node(int k, int v) { key = k; value = v; } }

    LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail; tail.prev = head;
    }

    public int get(int key) {
        Node n = map.get(key);
        if (n == null) return -1;
        moveToHead(n);                    // 访问即提升为最新
        return n.value;
    }

    public void put(int key, int value) {
        Node n = map.get(key);
        if (n != null) { n.value = value; moveToHead(n); return; }
        if (map.size() == capacity) {     // 淘汰尾部
            Node oldest = tail.prev;
            unlink(oldest); map.remove(oldest.key);
        }
        Node fresh = new Node(key, value);
        map.put(key, fresh); addToHead(fresh);
    }

    private void unlink(Node n) { n.prev.next = n.next; n.next.prev = n.prev; }
    private void addToHead(Node n) { n.next = head.next; n.prev = head;
        head.next.prev = n; head.next = n; }
    private void moveToHead(Node n) { unlink(n); addToHead(n); }
}
```

**坑点**：① 用哨兵节点避免判空边界（面试官会问"为什么要哨兵"——消灭头尾特判）；② 淘汰时要同时摘链表和删 map（漏一个就内存泄漏）；③ 追问"并发版怎么做" → 加锁 or 讲 Caffeine 的无锁思路（呼应第 1 章题 1.4.1）。

---

## 题 3：生产者-消费者（wait/notify 版 + BlockingQueue 版）

```java
class BoundedBuffer {
    private final Object[] items = new Object[10];
    private int putIdx, takeIdx, count;

    public synchronized void put(Object x) throws InterruptedException {
        while (count == items.length) wait();     // while 不是 if！
        items[putIdx] = x;
        putIdx = (putIdx + 1) % items.length;
        count++;
        notifyAll();                              // notifyAll 不是 notify
    }

    public synchronized Object take() throws InterruptedException {
        while (count == 0) wait();
        Object x = items[takeIdx];
        takeIdx = (takeIdx + 1) % items.length;
        count--;
        notifyAll();
        return x;
    }
}
```

**两个必考坑（被问到就是送分）**：
1. **为什么用 while 不用 if**？→ 被 notifyAll 唤醒后条件可能又被别人抢走（虚假唤醒/竞争），必须重新检查条件；
2. **为什么 notifyAll 不是 notify**？→ notify 只随机唤醒一个，若唤醒的是"同类等待者"（生产者唤醒生产者）可能死等。两行是这个题的满分分水岭。
3. 工程版一句话：`BlockingQueue`（ArrayBlockingQueue 两把锁分离读写）已解决一切，手写只为理解原理。

---

## 题 4：两个线程交替打印 1~100（A 线程奇数，B 线程偶数）

```java
class AlternatePrinter {
    private final Object lock = new Object();
    private int num = 1;

    public void print(boolean odd) {
        while (num <= 100) {
            synchronized (lock) {
                if ((num % 2 == 1) == odd && num <= 100) {
                    System.out.println(Thread.currentThread().getName() + ": " + num++);
                    lock.notifyAll();
                } else {
                    try { lock.wait(); } catch (InterruptedException e) {
                        Thread.currentThread().interrupt(); return;
                    }
                }
            }
        }
    }
    // 启动：new Thread(() -> p.print(true), "A");  new Thread(() -> p.print(false), "B");
}
```

**讲清语义**：条件不满足就 wait 让锁，轮到谁谁打印并唤醒；`num++` 在锁内保证原子与可见。追问升级版："不用 synchronized 用两个锁轮流 acquire/release 也可以；或者用 Semaphore(0/1) 交替 acquire——你会选哪种？为什么 Semaphore 没有虚假唤醒问题？"（答：许可语义天然一一对应）。

---

## 题 5：手写一个简化线程池（考原理理解）

```java
class SimpleThreadPool {
    private final BlockingQueue<Runnable> tasks;
    private final List<Thread> workers = new ArrayList<>();

    SimpleThreadPool(int coreSize, int queueSize) {
        this.tasks = new LinkedBlockingQueue<>(queueSize);
        for (int i = 0; i < coreSize; i++) {
            Thread w = new Thread(this::runWorker, "worker-" + i);
            w.start();
            workers.add(w);
        }
    }

    private void runWorker() {
        while (!Thread.currentThread().isInterrupted()) {
            try {
                Runnable task = tasks.take();     // 阻塞取任务
                task.run();                        // 注意是 run 不是 start
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); break;   // 优雅关闭出口
            } catch (Throwable t) {
                // 任务异常不能杀死工作线程！生产环境用 log.error("worker task failed", t)，演示用 stderr：
                t.printStackTrace(System.err);
            }
        }
    }

    public void execute(Runnable task) {
        if (!tasks.offer(task)) {
            throw new RejectedExecutionException("queue full");  // 拒绝策略
        }
    }

    public void shutdown() { for (Thread w : workers) w.interrupt(); }
}
```

**必讲三点**：① worker 循环 `take()` 阻塞等任务——线程复用的本质；② **任务异常必须 try-catch 隔离**，否则 worker 死亡线程池缩容（对照 JDK：FutureTask 把异常存进 future）；③ 拒绝策略在队列满时触发——与 ThreadPoolExecutor 流程对照（第 2 章题 2.2.3）。

---

## 题 6：数组中的第 K 大元素（TopK，快排 partition / 小顶堆）

**堆版（背这个，10 行）**：

```java
public int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);   // 小顶堆
    for (int n : nums) {
        if (minHeap.size() < k) minHeap.offer(n);
        else if (n > minHeap.peek()) { minHeap.poll(); minHeap.offer(n); }
    }
    return minHeap.peek();
}
// 时间 O(n log k)，空间 O(k) —— 适合 n 大 k 小（TopK 热点词场景）
```

**快排 partition 版（追问时口述思路即可）**：随机选 pivot，partition 后若 pivot 位置正好是 n-k 就命中；偏左递归右、偏右递归左。平均 O(n)（每轮只走一半），最坏 O(n²)（随机化避免）。**追问"数据流实时 TopK"** → 堆 + 固定内存；"海量分片数据 TopK" → 各分片本地 TopK 再归并（map-reduce 思想）。

---

## 题 7：三个线程按序打印 ABC 循环 10 次（Semaphore 版）

```java
class AbcPrinter {
    private final Semaphore sa = new Semaphore(1);
    private final Semaphore sb = new Semaphore(0);
    private final Semaphore sc = new Semaphore(0);

    void printA() throws InterruptedException {
        for (int i = 0; i < 10; i++) { sa.acquire(); System.out.print("A"); sb.release(); }
    }
    void printB() throws InterruptedException {
        for (int i = 0; i < 10; i++) { sb.acquire(); System.out.print("B"); sc.release(); }
    }
    void printC() throws InterruptedException {
        for (int i = 0; i < 10; i++) { sc.acquire(); System.out.print("C"); sa.release(); }
    }
}
```

**讲清本质**：信号量构成单向依赖环，许可的释放就是"下家令牌"；比 wait/notify 版无虚假唤醒问题且语义直白。追问"如果要支持 N 个线程轮转" → 泛化成 `Semaphore[] + (i+1)%N release`。

---

## 题 8：手写两个线程死锁 + 怎么排查（写死锁是考排查）

```java
Object lockA = new Object(), lockB = new Object();

// 线程1：先 A 后 B        线程2：先 B 后 A
new Thread(() -> {
    synchronized (lockA) { sleep(100); synchronized (lockB) { } }   // 打破"固定顺序"
}, "T1").start();
new Thread(() -> {
    synchronized (lockB) { sleep(100); synchronized (lockA) { } }
}, "T2").start();
```

**排查话术（比写代码更重要）**：
1. `jstack <pid>` 或 Arthas `thread -b` → 输出 "Found one Java-level deadlock" 并打印互相等待的两个线程；
2. 修复四法：**固定加锁顺序**（按对象 hash/ID 排序）、tryLock 带超时（拿不到就释放重来）、缩小锁粒度、改用无锁结构；
3. 预防：Arthas `thread --state BLOCKED` 告警接入监控；code review 用锁顺序检查清单。

---

## 题 9：手写简单的 Bloom Filter（缓存穿透前置件）

```java
class SimpleBloomFilter {
    private final BitSet bits;
    private final int[] seeds = {7, 11, 13, 31, 37};   // 多哈希降低误判
    private final int size;

    SimpleBloomFilter(int expectedInsertions) {
        this.size = expectedInsertions * 4 / 3;        // 经验：约 25% 冗余
        this.bits = new BitSet(size);
    }

    void add(String value) {
        for (int seed : seeds) bits.set(hash(value, seed));
    }

    boolean mightContain(String value) {
        for (int seed : seeds)
            if (!bits.get(hash(value, seed))) return false;  // 有一位为 0 必不存在
        return true;                                          // 全 1 = 可能存在（有误判）
    }

    private int hash(String value, int seed) {
        int h = 0;
        for (char c : value.toCharArray()) h = h * seed + c;
        return (h & 0x7fffffff) % size;   // 抹掉符号位再取模——Math.abs(h % size) 在 h 为负时虽安全，但 abs 对 MIN_VALUE 会溢出，review 高频标记项
    }
}
```

**必讲**：① 无漏判（说不存在就一定不存在）→ 适合当"拦截器"放在 DB 前；② 有误判 → 拦截后仍要 DB 兜底一次（防止误杀）；③ 不支持删除 → 计数布隆/布谷鸟过滤器；④ 容量估算公式 `n = -m·ln(1-p... )` 讲不清就说"误判率与位数组大小和插入量相关，工程上用 Guava 的 BloomFilter，按预期插入量和误判率创建"。

---

## 题 10：生产者场景综合题——"手写一个限流器"（P8-P10 常见）

**滑动窗口版（背结构）**：

```java
class SlidingWindowRateLimiter {
    private final int maxRequests;            // 窗口内允许的最大请求数
    private final long windowMillis;
    private final Deque<Long> timestamps = new ArrayDeque<>();

    SlidingWindowRateLimiter(int maxRequests, long windowMillis) {
        this.maxRequests = maxRequests;
        this.windowMillis = windowMillis;
    }

    public synchronized boolean tryAcquire() {
        long now = System.currentTimeMillis();
        while (!timestamps.isEmpty() && now - timestamps.peekFirst() >= windowMillis)
            timestamps.pollFirst();           // 清理窗口外旧记录
        if (timestamps.size() < maxRequests) {
            timestamps.addLast(now);
            return true;
        }
        return false;
    }
}
```

**讲清与升级**：① synchronized 单机版够用（临界区极短）；② 时间戳队列内存 O(窗口内请求数)，高并发改用环形计数格（Sentinel LeapArray：把 1 分钟切 60 格，每格原子计数，取窗口和）；③ 分布式版 → Redis Lua（`ZADD + ZREMRANGEBYSCORE + ZCARD` 原子三连）；④ 讲取舍：滑动窗口 vs 令牌桶（允许突发）vs 漏桶（恒速），按下游承受能力选（呼应第 8 章题 8.3.1）。

---

## 白板代码通用心法（比任何一题都重要）

1. **先说思路再动笔**：30 秒讲清"数据结构 + 关键不变量"，方向错了面试官会拉住你；
2. **边界先行**：空参/单元素/并发条件，主动说"我假设……"，不等人问；
3. **写不完就降维**：时间不够时写核心方法骨架 + 口述其余，比涂改强；
4. **自我 review**：写完必说"我检查一下边界"——展示 review 习惯本身就是评分项；
5. **并发题三问自查**：谁可见（volatile/锁）？谁原子（CAS/锁）？谁等待（wait/while）？

## 速记卡

1. DCL 三件套：两次检查 + volatile + 私有构造；更优：Holder / 枚举。
2. LRU：LinkedHashMap accessOrder=true；手写版 = HashMap + 双向链表 + 哨兵。
3. 生产消费者：while 判条件、notifyAll、环形数组下标。
4. 交替打印：一个锁 + 条件翻转 或 信号量链。
5. 简易线程池：take 阻塞复用、异常隔离、队列满拒绝、interrupt 关闭。
6. TopK：小顶堆 O(n log k)；静态数据快排 partition 平均 O(n)。
7. 死锁排查：jstack / thread -b；修复靠固定顺序与 tryLock。
8. 布隆：无漏判有误判、不可删；DB 兜底一次。
9. 限流器：单机滑动窗口/LeapArray；分布式 Redis Lua 三连。
10. 白板五字诀：思、界、降、审、并。

---
*返回 [INDEX.md](../../INDEX.md) 选择下一册。*
