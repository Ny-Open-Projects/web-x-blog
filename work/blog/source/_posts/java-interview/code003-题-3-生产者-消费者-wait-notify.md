---
title: "题 3：生产者-消费者（wait/notify 版 + BlockingQueue 版）"
date: 2026-11-18
categories: [Java面试, 手写代码]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
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
