import java.util.ArrayList;
import java.util.List;

/**
 * Arthas practice target (ASCII-only output to avoid Windows console encoding issues).
 *
 * Usage:
 *   javac ArthasPractice.java
 *   java  ArthasPractice cpu       -> hot loop (practice: dashboard / thread -n 3)
 *   java  ArthasPractice leak      -> static map leak (practice: memory / heapdump / getstatic)
 *   java  ArthasPractice slow      -> random slow method (practice: trace / watch / tt)
 *   java  ArthasPractice deadlock  -> classic deadlock (practice: thread -b / thread --state BLOCKED)
 *
 * Each mode runs forever until you kill it - that is intentional so you can attach Arthas.
 *
 * Code-review exemption (see ../review/REVIEW-STANDARD.md): explicit `new Thread` is used
 * on purpose - this is an attach target, not business code. Production code must create
 * threads via ThreadPoolExecutor (Alibaba manual, concurrent section).
 */
public class ArthasPractice {

    // Leak mode target: inspect me with `getstatic ArthasPractice LEAK` later
    public static final List<byte[]> LEAK = new ArrayList<byte[]>();

    public static void main(String[] args) throws Exception {
        String mode = args.length > 0 ? args[0] : "help";
        System.out.println("ArthasPractice started, mode=" + mode + ", pid available via jps");
        System.out.println("Now attach: java -jar arthas-boot.jar   (choose this process)");
        if ("cpu".equals(mode)) {
            runCpu();
        } else if ("leak".equals(mode)) {
            runLeak();
        } else if ("slow".equals(mode)) {
            runSlow();
        } else if ("deadlock".equals(mode)) {
            runDeadlock();
        } else {
            System.out.println("Unknown mode. Use: cpu | leak | slow | deadlock");
        }
    }

    // ---------------- CPU mode ----------------
    // Practice goal: with `thread -n 3`, you should see a thread burning in
    // hotMethod(...) and the exact line number in the stack.
    private static void runCpu() {
        Thread hot = new Thread(new Runnable() {
            public void run() {
                long i = 0;
                while (true) {
                    // Hot loop: stack top will point to this line.
                    i = hotMethod(i);
                }
            }
        }, "cpu-burner");
        hot.start();

        Thread idle = new Thread(new Runnable() {
            public void run() {
                while (true) {
                    try { Thread.sleep(1000); } catch (InterruptedException e) { return; }
                }
            }
        }, "idle-thread");
        idle.start();
    }

    static long hotMethod(long i) {
        // A little math so JIT does not eliminate the whole loop
        long x = i;
        for (int j = 0; j < 100_000; j++) {
            x = x * 31 + j;
            x = x ^ (x >>> 7);
        }
        return x;
    }

    // ---------------- Leak mode ----------------
    // Practice goal:
    //   1. watch old-gen usage grow in `dashboard` / `jstat -gcutil <pid> 1000`
    //   2. confirm with Arthas: getstatic ArthasPractice LEAK
    //   3. dump: heapdump /tmp/leak.hprof --live   then analyze in MAT
    private static void runLeak() throws Exception {
        int seq = 0;
        while (true) {
            // ~1 MB per second of "never-referenced-again" data
            LEAK.add(new byte[1024 * 1024]);
            System.out.println("leaked MB total=" + LEAK.size());
            Thread.sleep(1000);
            seq++;
            if (seq == Integer.MAX_VALUE) break;
        }
    }

    // ---------------- Slow mode ----------------
    // Practice goal:
    //   trace com.example? No - use fully-qualified name of this class:
    //   trace ArthasPractice slowService '#cost > 300' -n 5
    //   watch ArthasPractice slowService '{params, returnObj, #cost}' -x 2 -n 5
    //   tt -t ArthasPractice slowService   then replay: tt -p -i <index>
    private static void runSlow() throws Exception {
        int n = 0;
        while (true) {
            String r = slowService("req-" + n);
            if (n % 10 == 0) System.out.println("slowService ok: " + r);
            Thread.sleep(200);
            n++;
        }
    }

    static String slowService(String req) {
        try {
            // 90% fast, 10% slow (500-800ms): the slow ones are the ones to catch
            if (Math.random() < 0.10) {
                Thread.sleep(500 + (long) (Math.random() * 300));
            } else {
                Thread.sleep(20);
            }
            return "done:" + req;
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return "interrupted";
        }
    }

    // ---------------- Deadlock mode ----------------
    // Practice goal:
    //   thread -b                       -> "Found one Java-level deadlock"
    //   thread --state BLOCKED          -> see both blocked threads and lock addresses
    // Then fix mentally: lock ordering (t1 and t2 must acquire A then B consistently).
    private static final Object LOCK_A = new Object();
    private static final Object LOCK_B = new Object();

    private static void runDeadlock() throws Exception {
        Thread t1 = new Thread(new Runnable() {
            public void run() {
                synchronized (LOCK_A) {
                    sleep(200);
                    synchronized (LOCK_B) {
                        System.out.println("t1 got both locks");
                    }
                }
            }
        }, "deadlock-t1");
        Thread t2 = new Thread(new Runnable() {
            public void run() {
                synchronized (LOCK_B) {
                    sleep(200);
                    synchronized (LOCK_A) {
                        System.out.println("t2 got both locks");
                    }
                }
            }
        }, "deadlock-t2");
        t1.start();
        t2.start();
    }

    static void sleep(long ms) {
        try { Thread.sleep(ms); } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    }
}
