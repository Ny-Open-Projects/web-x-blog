---
title: "题 7：三个线程按序打印 ABC 循环 10 次（Semaphore 版）"
date: 2026-11-18
categories: [Java面试, 手写代码]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
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
