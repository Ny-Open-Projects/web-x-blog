---
title: "卡片 2：编译型 vs 解释型，Java 是什么？"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 2：编译型 vs 解释型，Java 是什么？
Java 是**混合型**：javac 先把 .java 编译成 .class（字节码），JVM 再边解释边编译
（JIT 把热点代码编译成机器码）。所以 Java 既不是纯编译型（如 C），也不是纯解释型（如 Python）。
