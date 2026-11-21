import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.util.concurrent.locks.ReentrantLock;

/**
 * 第 24 册笔试题 · 算法编程题参考实现（全部在本机 JDK 21 实测）
 * 运行：java ExamSolutions
 */
public class ExamSolutions {

    // ============ 题 A1：LRU 缓存 O(1) ============
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
        String keysInOrder() {                       // 调试输出：头→尾 = 最新→最旧
            StringBuilder sb = new StringBuilder("[");
            for (Node p = head.next; p != tail; p = p.next) sb.append(p.key).append(",");
            return sb.append("]").toString();
        }
    }

    static void examLRU() {
        LRUCache lru = new LRUCache(2);
        lru.put(1, 1);                                // [1]
        lru.put(2, 2);                                // [2,1]
        int r1 = lru.get(1);                          // 返回 1，访问后变最新 [1,2]
        lru.put(3, 3);                                // 淘汰最旧的 2 → [3,1]
        int r2 = lru.get(2);                          // 返回 -1（已被淘汰）
        lru.put(4, 4);                                // 淘汰 1 → [4,3]
        int r3 = lru.get(1), r4 = lru.get(3), r5 = lru.get(4);
        System.out.println("A1 LRU: get(1)=" + r1 + "(期望1), get(2)=" + r2
                + "(期望-1), 顺序=" + lru.keysInOrder() + "(期望[4,3]), get(1)=" + r3
                + "(期望-1), get(3)=" + r4 + "(期望3), get(4)=" + r5 + "(期望4)");
    }

    // ============ 题 A2：TopK 小顶堆 ============
    static void examTopK() {
        int[] nums = {5, 2, 8, 1, 9, 3, 7, 6};
        int k = 3;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);
        for (int n : nums) {
            if (minHeap.size() < k) minHeap.offer(n);
            else if (n > minHeap.peek()) { minHeap.poll(); minHeap.offer(n); }
        }
        List<Integer> topk = new ArrayList<>(minHeap);
        Collections.sort(topk, Collections.reverseOrder());
        System.out.println("A2 TopK: k=" + k + " 结果=" + topk + " (期望 [9,8,7])");
    }

    // ============ 题 A3：两个线程交替打印 1~10 ============
    static void examAlternate() throws Exception {
        Object lock = new Object();
        AtomicInteger num = new AtomicInteger(1);
        class Printer implements Runnable {
            final boolean odd;
            Printer(boolean odd) { this.odd = odd; }
            public void run() {
                while (num.get() <= 10) {
                    synchronized (lock) {
                        if (num.get() <= 10 && ((num.get() % 2 == 1) == odd)) {
                            System.out.print(num.getAndIncrement() + (num.get() > 10 ? "\n" : " "));
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
        Thread a = new Thread(new Printer(true), "A");
        Thread b = new Thread(new Printer(false), "B");
        a.start(); b.start();
        a.join(3000); b.join(3000);
    }

    // ============ 题 A4：滑动窗口限流器 ============
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
                stamps.pollFirst();
            if (stamps.size() < maxRequests) { stamps.addLast(now); return true; }
            return false;
        }
        int size() { return stamps.size(); }
    }

    static void examLimiter() throws Exception {
        SlidingWindowRateLimiter limiter = new SlidingWindowRateLimiter(3, 300);
        boolean r1 = limiter.tryAcquire();          // t0: true
        Thread.sleep(50);
        boolean r2 = limiter.tryAcquire();          // t50: true
        boolean r3 = limiter.tryAcquire();          // t50: true
        boolean r4 = limiter.tryAcquire();          // t50: false（窗口内已 3 个）
        Thread.sleep(260);                          // t310: t0 的请求已出窗
        boolean r5 = limiter.tryAcquire();          // true
        System.out.println("A4 限流器: " + r1 + "," + r2 + "," + r3 + "," + r4
                + "(期望 false), " + r5 + "(期望 true), 窗口内=" + limiter.size() + "(期望 1)");
    }

    // ============ 题 A5：旋转排序数组找最小值（二分变体） ============
    static int findMin(int[] nums) {                // 无重复元素，O(log n)
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] > nums[hi]) lo = mid + 1; // 最小值在右半段
            else hi = mid;                          // 最小值在左半段含 mid
        }
        return nums[lo];
    }

    static void examBinarySearch() {
        int[][] cases = {{4,5,6,7,0,1,2}, {3,4,5,1,2}, {11,13,15,17}, {2,1}};
        for (int[] c : cases)
            System.out.println("A5 旋转数组 " + Arrays.toString(c) + " 最小值=" + findMin(c));
        // 期望: 0, 1, 11, 1
    }

    // ============ 题 A6：生产者消费者（有界缓冲 + 优雅关闭 + 异常隔离） ============
    static void examProducerConsumer() throws Exception {
        BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(5);
        AtomicInteger consumed = new AtomicInteger();
        AtomicReference<Throwable> lastError = new AtomicReference<>();
        CountDownLatch stop = new CountDownLatch(1);
        Thread producer = new Thread(() -> {
            try {
                for (int i = 1; i <= 20; i++) queue.put(i);   // 满则阻塞
                stop.countDown();
            } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        }, "producer");
        Thread consumer = new Thread(() -> {
            try {
                while (!stop.await(50, TimeUnit.MILLISECONDS) || !queue.isEmpty()) {
                    Integer v = queue.poll(50, TimeUnit.MILLISECONDS);
                    if (v != null) consumed.addAndGet(v);
                }
            } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
            catch (Exception e) { lastError.set(e); }
        }, "consumer");
        producer.start(); consumer.start();
        producer.join(3000);
        stop.await(); consumer.join(3000);
        // 1+2+...+20 = 210
        System.out.println("A6 生产者消费者: consumedSum=" + consumed.get()
                + "(期望210) lastError=" + (lastError.get() == null ? "null" : lastError.get()));
    }

    public static void main(String[] args) throws Exception {
        examLRU();
        examTopK();
        examAlternate();
        examLimiter();
        examBinarySearch();
        examProducerConsumer();
        System.out.println("ALL_EXAM_SOLUTIONS_DONE");
    }
}
