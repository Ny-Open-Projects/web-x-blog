import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.RejectedExecutionException;
import java.util.concurrent.Semaphore;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.StampedLock;

/**
 * 全卷断言实证套件。运行方式（反射需要打开 JDK 内部模块）：
 *   java --add-opens java.base/java.util=ALL-UNNAMED \
 *        --add-opens java.base/java.lang=ALL-UNNAMED \
 *        JavaVerificationSuite
 * 每项输出 PASS / FAIL / INFO，结尾汇总。
 *
 * Code-review 豁免声明（见 notes/review/REVIEW-STANDARD.md §三）：
 * 本套件使用裸 Thread 创建而非线程池——并发观测（getState/BLOCKED/TIMED_WAITING 断言）
 * 需要直接持有线程引用，池化会破坏断言目标；生产业务代码仍必须遵循线程池规约。
 */
public class JavaVerificationSuite {

    static int pass = 0, fail = 0;
    static final List<String> FAILS = new ArrayList<>();
    static final List<String> INFOS = new ArrayList<>();

    static void check(boolean ok, String name, String detail) {
        if (ok) { pass++; System.out.println("PASS  " + name + (detail.isEmpty() ? "" : "  [" + detail + "]")); }
        else { fail++; FAILS.add(name); System.out.println("FAIL  " + name + "  [" + detail + "]"); }
    }

    static void info(String name, String detail) {
        INFOS.add(name); System.out.println("INFO  " + name + "  [" + detail + "]");
    }

    public static void main(String[] args) throws Exception {
        coreChecks();
        mapChecks();
        concurrencyChecks();
        virtualThreadChecks();
        subProcessChecks();
        System.out.println("\n======== SUMMARY ========");
        System.out.println("PASS=" + pass + "  FAIL=" + fail + "  INFO=" + INFOS.size());
        if (!FAILS.isEmpty()) System.out.println("FAILED: " + FAILS);
    }

    // ============ 核心语言 ============
    static void coreChecks() throws Exception {
        // 1. 包装类缓存 -128~127
        check(Integer.valueOf(127) == Integer.valueOf(127), "IntegerCache127", "valueOf(127) 同一对象");
        check(Integer.valueOf(128) != Integer.valueOf(128), "IntegerCache128", "valueOf(128) 新对象");
        check(Long.valueOf(127) == Long.valueOf(127), "LongCache127", "");
        check(Long.valueOf(128) != Long.valueOf(128), "LongCache128", "");

        // 2. String.hashCode 31 乘子: 97*31+98=3095, 3095*31+99=96354
        check("abc".hashCode() == 96354, "StringHashCode31", "\"abc\"→96354");

        // 3. Compact Strings: JDK9+ String.value 是 byte[]
        Field v = String.class.getDeclaredField("value");
        check(v.getType() == byte[].class, "CompactStrings", "JDK9+ String.value 为 byte[]");

        // 4. intern：JDK7+ 堆内首次串入池后返回自身引用（用未入池的新串）
        String fresh = new StringBuilder("polyx").append(2026).toString();
        check(fresh.intern() == fresh, "InternReturnsSelf", "JDK7+ intern 保留堆引用");
        // 经典 gotcha："java" 在 System 初始化时已入池
        String javaStr = new String("ja") + "va";
        info("InternJavaGotcha", "\"ja\"+\"va\" intern != 自身（java 已预入池）=" + (javaStr.intern() != javaStr));

        // 5. ArrayList 1.5 倍扩容（反射 elementData）
        ArrayList<Integer> al = new ArrayList<>();
        al.add(1);
        int cap1 = capacity(al);
        for (int i = 2; i <= 10; i++) al.add(i);
        int cap10 = capacity(al);
        al.add(11);
        int cap11 = capacity(al);
        for (int i = 12; i <= 15; i++) al.add(i);
        al.add(16);
        int cap16 = capacity(al);
        check(cap1 == 10 && cap10 == 10 && cap11 == 15 && cap16 == 22,
                "ArrayListGrowth", "首插10, 第11个→15(1.5x), 第16个→22");
    }

    static int capacity(ArrayList<?> list) throws Exception {
        Field f = ArrayList.class.getDeclaredField("elementData");
        f.setAccessible(true);
        return ((Object[]) f.get(list)).length;
    }

    // ============ Map 家族 ============
    static void mapChecks() throws Exception {
        // 6. HashMap 默认容量 16 / 扩容 2 倍
        HashMap<String, Integer> hm = new HashMap<>();
        hm.put("k0", 0);
        int len0 = tableLen(hm);
        for (int i = 1; i <= 12; i++) hm.put("k" + i, i);   // size 13 > threshold 12
        check(len0 == 16 && tableLen(hm) == 32, "HashMapInitCap16AndDouble",
                "首插后表长16；第13个插入触发翻倍→32");

        // 7. 树化：容量64 + 同桶8个 → TreeNode（JDK21 实证）
        HashMap<FixedHash, Integer> tree = new HashMap<>(64);
        for (int i = 0; i < 9; i++) tree.put(new FixedHash(), i);
        Object bin = tableBin(tree, 3);                     // FixedHash.hashCode=3 → bin 3
        check(bin != null && bin.getClass().getSimpleName().equals("TreeNode"), "HashMapTreeifyAt8Cap64",
                "9个同桶键后 bin 为 TreeNode");

        // 8. hash 扰动 = h ^ (h >>> 16)（直接调 HashMap.hash 私有静态方法）
        Method hashM = HashMap.class.getDeclaredMethod("hash", Object.class);
        hashM.setAccessible(true);
        int h = "abc".hashCode();
        check((int) hashM.invoke(null, "abc") == (h ^ (h >>> 16)), "HashMapHashSpread",
                "hash = h ^ (h>>>16)");

        // 9. CHM 拒绝 null key/value
        ConcurrentHashMap<String, Integer> chm = new ConcurrentHashMap<>();
        boolean npeKey = false, npeVal = false;
        try { chm.put(null, 1); } catch (NullPointerException e) { npeKey = true; }
        try { chm.put("k", null); } catch (NullPointerException e) { npeVal = true; }
        check(npeKey && npeVal, "CHMNullRejected", "key/value null 均抛 NPE");

        // 10. CHM 并发计数正确
        final ConcurrentHashMap<Integer, Integer> cc = new ConcurrentHashMap<>();
        ExecutorService es = Executors.newFixedThreadPool(8);
        for (int t = 0; t < 8; t++) {
            final int base = t * 1000;
            es.submit(() -> { for (int i = 0; i < 1000; i++) cc.put(base + i, i); });
        }
        es.shutdown();
        check(es.awaitTermination(10, TimeUnit.SECONDS) && cc.size() == 8000,
                "CHMConcurrentPuts", "8线程×1000 → size=8000");

        // 11. fail-fast
        HashMap<String, Integer> ff = new HashMap<>();
        ff.put("a", 1);
        boolean cme = false;
        try {
            Iterator<Map.Entry<String, Integer>> it = ff.entrySet().iterator();
            it.next();
            ff.put("b", 2);
            it.next();
        } catch (java.util.ConcurrentModificationException e) { cme = true; }
        check(cme, "HashMapFailFast", "迭代中 put → ConcurrentModificationException");

        // 12. ThreadLocal 弱引用：外部强引用消失 + GC → key 被回收
        ThreadLocal<Integer> tl = new ThreadLocal<>();
        tl.set(42);
        java.lang.ref.WeakReference<ThreadLocal<Integer>> wr = new java.lang.ref.WeakReference<>(tl);
        tl = null;                                          // 清掉唯一的强引用
        int tries = 0;
        boolean collected = false;
        while (tries++ < 30) {
            System.gc();
            try { Thread.sleep(100); } catch (InterruptedException e) { Thread.currentThread().interrupt(); break; }
            if (wr.get() == null) { collected = true; break; }
        }
        check(collected, "ThreadLocalWeakRefCollected",
                "ThreadLocalMap 的 key 是弱引用：外部引用消失后 GC 即回收");

        // 13. LinkedHashMap accessOrder = LRU 语义
        LinkedHashMap<String, Integer> lru = new LinkedHashMap<>(4, 0.75f, true);
        lru.put("a", 1); lru.put("b", 2); lru.put("c", 3);
        lru.get("a");                                       // a 变为最新
        String eldest = lru.keySet().iterator().next();
        check("b".equals(eldest), "LinkedHashMapLRU", "访问 a 后最老的是 b（将被淘汰）");
    }

    static class FixedHash {
        public int hashCode() { return 3; }
    }

    static int tableLen(HashMap<?, ?> m) throws Exception {
        Field f = HashMap.class.getDeclaredField("table");
        f.setAccessible(true);
        Object[] t = (Object[]) f.get(m);
        return t == null ? -1 : t.length;
    }

    static Object tableBin(HashMap<?, ?> m, int idx) throws Exception {
        Field f = HashMap.class.getDeclaredField("table");
        f.setAccessible(true);
        Object[] t = (Object[]) f.get(m);
        return t[idx];
    }

    // ============ 并发 ============
    static void concurrencyChecks() throws Exception {
        // 14. volatile 可见性：另一线程写 flag，等待线程退出
        class VolFlag { volatile boolean go = false; }
        VolFlag vf = new VolFlag();
        CountDownLatch started = new CountDownLatch(1);
        Thread waiter = new Thread(() -> {
            started.countDown();
            while (!vf.go) { /* spin */ }
        });
        waiter.start();
        started.await();
        Thread.sleep(100);
        vf.go = true;
        waiter.join(2000);
        boolean exited = !waiter.isAlive();
        check(exited, "VolatileVisibility", "volatile 写后 2s 内等待线程退出");

        // 15. 非 volatile 经典演示（观察项，不判分）
        class PlainFlag { boolean go = false; }
        PlainFlag pf = new PlainFlag();
        CountDownLatch nonVolatileStarted = new CountDownLatch(1);
        Thread w2 = new Thread(() -> {
            nonVolatileStarted.countDown();
            while (!pf.go) { }
        });
        w2.setDaemon(true);   // 守护线程：该循环预期永远看不到写，不能阻塞 JVM 退出
        w2.start();
        nonVolatileStarted.await();
        Thread.sleep(300);
        pf.go = true;
        w2.join(800);
        boolean exited2 = !w2.isAlive();
        info("NonVolatileLoopObserved", exited2 ? "本机 JIT 下也退出了（现象因 JIT/平台而异，经典演示通常挂起）"
                                               : "如预期挂起（无 happens-before，写不可见）");

        // 16. 线程池执行顺序：core2/max4/queue2 → 第7、8个任务创建非核心线程，第9个拒绝
        CountDownLatch blocker = new CountDownLatch(1);
        ThreadPoolProbe tpe = new ThreadPoolProbe(2, 4, 2, blocker);
        Runnable probeTask = () -> { try { blocker.await(); } catch (InterruptedException e) {} };
        tpe.execute(probeTask);   // 核心1
        Thread.sleep(120);
        tpe.execute(probeTask);   // 核心2
        Thread.sleep(100);
        tpe.execute(probeTask);   // 入队1
        Thread.sleep(80);
        tpe.execute(probeTask);   // 入队2
        Thread.sleep(80);
        tpe.execute(probeTask);   // 非核心3（队列满 → 创建线程）
        Thread.sleep(80);
        tpe.execute(probeTask);   // 非核心4
        Thread.sleep(150);
        int poolSize = tpe.getPoolSize();
        int queueSize = tpe.getQueue().size();
        boolean rejected = false;
        try { tpe.execute(probeTask); } catch (RejectedExecutionException e) { rejected = true; }
        check(poolSize == 4 && queueSize == 2 && rejected, "ThreadPoolOrder",
                "poolSize=" + poolSize + " queue=" + queueSize + " 第9个拒绝=" + rejected
                + "（先核心→队列→非核心→拒绝）");
        blocker.countDown();
        tpe.shutdownNow();

        // 17. submit 吞异常（存进 Future），execute 走 UEH
        ExecutorService ses = Executors.newSingleThreadExecutor();
        java.util.concurrent.Future<?> f = ses.submit(() -> { throw new IllegalStateException("boom"); });
        boolean execEx = false;
        try { f.get(); } catch (java.util.concurrent.ExecutionException e) { execEx = true; }
        check(execEx, "SubmitExceptionInFuture", "submit 的异常存进 Future，get 时以 ExecutionException 抛出");
        ses.shutdown();

        AtomicReference<Throwable> ueh = new AtomicReference<>();
        ExecutorService uehExec = Executors.newSingleThreadExecutor(r -> {
            Thread t = new Thread(r, "probe-ueh");
            t.setUncaughtExceptionHandler((tt, e) -> ueh.set(e));
            return t;
        });
        uehExec.execute(() -> { throw new IllegalStateException("boom2"); });
        Thread.sleep(400);
        uehExec.shutdownNow();
        check(ueh.get() != null, "ExecuteUncaughtHandler", "execute 的异常进入 UncaughtExceptionHandler");

        // 18. AtomicLong 并发自增
        java.util.concurrent.atomic.AtomicLong al = new java.util.concurrent.atomic.AtomicLong();
        ExecutorService es2 = Executors.newFixedThreadPool(8);
        for (int t = 0; t < 8; t++) es2.submit(() -> { for (int i = 0; i < 2500; i++) al.incrementAndGet(); });
        es2.shutdown();
        check(es2.awaitTermination(10, TimeUnit.SECONDS) && al.get() == 20000,
                "AtomicLongCAS", "8×2500 并发 CAS → 20000");

        // 19. Semaphore 配额
        Semaphore sp = new Semaphore(2);
        boolean a1 = sp.tryAcquire(), a2 = sp.tryAcquire(), a3 = sp.tryAcquire();
        sp.release();
        boolean a4 = sp.tryAcquire();
        check(a1 && a2 && !a3 && a4, "SemaphoreQuota", "2 许可：第3次失败，release 后成功");

        // 20. CountDownLatch
        CountDownLatch cd = new CountDownLatch(2);
        ExecutorService es3 = Executors.newFixedThreadPool(2);
        for (int i = 0; i < 2; i++) es3.submit(cd::countDown);
        boolean proceeded = cd.await(2, TimeUnit.SECONDS);
        es3.shutdown();
        check(proceeded, "CountDownLatch", "");

        // 21. CyclicBarrier 可重用
        CyclicBarrier cb = new CyclicBarrier(3, () -> {});
        AtomicInteger rounds = new AtomicInteger();
        for (int r = 0; r < 2; r++) {
            ExecutorService es4 = Executors.newFixedThreadPool(3);
            for (int i = 0; i < 3; i++) es4.submit(() -> { try { cb.await(); rounds.incrementAndGet(); } catch (Exception e) {} });
            es4.shutdown();
            es4.awaitTermination(5, TimeUnit.SECONDS);
        }
        check(rounds.get() == 6, "CyclicBarrierReusable", "3方×2轮 全部通过栅栏（可重用）");

        // 22. 线程状态：BLOCKED / TIMED_WAITING
        Object lock = new Object();
        Thread holder = new Thread(() -> { synchronized (lock) { sleepMs(600); } });
        holder.start();
        Thread.sleep(100);
        Thread seeker = new Thread(() -> { synchronized (lock) {} });
        seeker.start();
        Thread.sleep(150);
        Thread.State stHolder = holder.getState();
        Thread.State stSeeker = seeker.getState();
        seeker.join(1000); holder.join(1000);
        check(stHolder == Thread.State.TIMED_WAITING && stSeeker == Thread.State.BLOCKED,
                "ThreadStates", "holder=" + stHolder + " seeker=" + stSeeker);
    }

    static class ThreadPoolProbe extends java.util.concurrent.ThreadPoolExecutor {
        ThreadPoolProbe(int core, int max, int queue, CountDownLatch blocker) {
            super(core, max, 0, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(queue),
                    r -> new Thread(r, "probe"));
        }
    }

    static class ThreadFactoryProbe extends Thread {
        ThreadFactoryProbe(AtomicReference<Throwable> sink) {
            setName("probe-ueh");
            setUncaughtExceptionHandler((t, e) -> sink.set(e));
        }
    }

    static void sleepMs(long ms) {
        try { Thread.sleep(ms); } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    }

    // ============ 虚拟线程（JDK21 特性） ============
    static void virtualThreadChecks() throws Exception {
        AtomicInteger counter = new AtomicInteger();
        try (ExecutorService vexec = Executors.newVirtualThreadPerTaskExecutor()) {
            for (int i = 0; i < 10000; i++) {
                vexec.submit(() -> { counter.incrementAndGet(); return null; });
            }
        } // close() 等待全部完成
        check(counter.get() == 10000, "VirtualThread10k", "1 万虚拟线程全部执行完成");

        Thread v = Thread.ofVirtual().name("vt-demo").unstarted(() -> {});
        check(v.isVirtual(), "VirtualThreadFactory", "Thread.ofVirtual() 可用");
    }

    // ============ 子进程：GC 日志格式 / OOM / JVM 参数 ============
    static String runProcess(String[] cmd, long timeoutSec) throws Exception {
        ProcessBuilder pb = new ProcessBuilder(cmd);
        pb.redirectErrorStream(true);
        Process p = pb.start();
        StringBuilder out = new StringBuilder();
        Thread reader = new Thread(() -> {
            try (var is = p.getInputStream()) {
                byte[] buf = new byte[4096];
                int n;
                while ((n = is.read(buf)) != -1) out.append(new String(buf, 0, n));
            } catch (Exception ignored) {}
        });
        reader.start();
        boolean fin = p.waitFor(timeoutSec, TimeUnit.SECONDS);
        if (!fin) { p.destroyForcibly(); reader.join(3000); }
        return out.toString();
    }

    static void subProcessChecks() throws Exception {
        String java = ProcessHandle.current().info().command().orElse("java");
        String cp = System.getProperty("java.class.path");

        // 23. GC 日志格式：GC(序号) Pause Young（验证第3/15册对 JDK9+ 格式的描述）
        String out1 = runProcess(new String[]{java, "-Xlog:gc", "-Xmx64m", "-Xms64m",
                "-cp", cp, "GcProbe"}, 45);
        boolean seqFormat = out1.contains("Pause Young") && out1.matches("(?s).*GC\\(\\d+\\).*");
        check(seqFormat, "GcLogUnifiedFormat",
                "JDK9+ 日志含 GC(序号) Pause Young（与第3/15册描述一致）");

        // 24. 堆 OOM 类型与消息
        String out2 = runProcess(new String[]{java, "-Xmx16m", "-Xms16m",
                "-cp", cp, "OomProbe"}, 30);
        check(out2.contains("OutOfMemoryError") && out2.contains("Java heap space"),
                "HeapOOMMessage", "堆 OOM 报 Java heap space");

        // 25. 容器时代常用参数被识别（含反向对照：不存在的参数会报 Unrecognized）
        String out3 = runProcess(new String[]{java, "-XX:MaxRAMPercentage=65",
                "-XX:+ExitOnOutOfMemoryError", "-version"}, 20);
        boolean flagsOk = out3.contains("21.0.2") && !out3.contains("Unrecognized");

        String out4 = runProcess(new String[]{java, "-XX:NoSuchFlagProbe", "-version"}, 20);
        boolean controlWorks = out4.contains("Unrecognized VM option");
        check(flagsOk && controlWorks, "ContainerJvmFlags",
                "MaxRAMPercentage/ExitOnOutOfMemoryError 被识别；错误参数被拒（对照项）");

        // 26. StampedLock 乐观读
        StampedLock sl = new StampedLock();
        long ws = sl.writeLock();
        sl.unlockWrite(ws);
        long rs = sl.tryOptimisticRead();
        boolean valid = sl.validate(rs);
        check(valid, "StampedLockOptimisticRead", "乐观读 stamp 校验通过（无锁读）");

        // 27. ReentrantLock 可重入
        ReentrantLock rl = new ReentrantLock();
        rl.lock(); rl.lock();
        int hold = rl.getHoldCount();
        rl.unlock(); rl.unlock();
        check(hold == 2, "ReentrantLockReentrant", "同线程重入 holdCount=2");
    }
}

class GcProbe {
    static byte[] sink;   // 分配逃逸到静态字段，阻止 JIT 逃逸分析消除
    public static void main(String[] args) {
        for (long i = 0; i < 50_000_000L; i++) {
            byte[] b = new byte[16 + (int) (i & 63)];
            b[0] = (byte) i;
            if ((i & 0xFFFF) == 0) sink = b;   // 逃逸写
        }
        System.out.println("done, last=" + (sink == null ? -1 : sink.length));
    }
}

class OomProbe {
    public static void main(String[] args) {
        List<byte[]> keep = new ArrayList<>();
        while (true) keep.add(new byte[1024 * 1024]);   // -Xmx16m 下必然 Java heap space
    }
}
