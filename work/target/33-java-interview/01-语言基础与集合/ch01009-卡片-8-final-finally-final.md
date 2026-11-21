---
title: "卡片 8：final / finally / finalize 三兄弟"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 8：final / finally / finalize 三兄弟
- `final`：修饰类（不能继承）、方法（不能重写）、变量（基本类型值不能变，引用类型地址不能变）。
- `finally`：try-catch 后必执行（除非 System.exit() 或 JVM 崩溃）。**不要在 finally 里 return**，会吞掉异常。
- `finalize`：Object 的回收前回调，JDK9 已标记 @Deprecated，性能差且不可靠，用 try-with-resources 或 Cleaner 替代。

---
