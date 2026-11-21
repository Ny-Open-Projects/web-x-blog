---
title: "[JV-014] GC·GC Roots（判定）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## GC · GC Roots（判定）

- **事实**：GC Roots 包括虚拟机栈局部变量表、静态变量、常量引用、JNI 引用与活跃线程等
- **原理**：从这些根出发沿引用链遍历，不可达即死亡，理解泄漏必须能定位根
- **常见误区**：
  1. GC Roots 只有静态变量（错）
  2. 栈上变量不是 GC Roots（错）
  3. 本地变量表引用的对象会被误回收（错）
- **工程用法**：内存泄漏排查先找根到泄漏对象的路径
- **版本锚点**：JVM 规范
