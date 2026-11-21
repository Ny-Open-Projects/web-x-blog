---
title: "题 1：双重检查锁定单例（DCL）—— 必考第一题"
date: 2026-11-18
categories: [Java面试, 手写代码]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

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
