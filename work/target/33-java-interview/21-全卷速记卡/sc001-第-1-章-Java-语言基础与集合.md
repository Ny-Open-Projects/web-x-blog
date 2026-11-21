---
title: "第 1 章 Java 语言基础与集合"
date: 2026-11-18
categories: [Java面试, 速记卡]
tags: [Java面试, 速记卡, 33]
type: 速记卡
disableNunjucks: true
---

# 全卷速记卡合订本 —— 考前最后一小时，只看这一个文件

> 汇总自 19 册的各章速记卡，内容与原文一致（略有压缩）。打印或手机上看都行。
> 配合 [INDEX.md](INDEX.md) 使用：哪条卡想不起展开，回对应章节重读追问链。

---


## 第 1 章 Java 语言基础与集合

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
