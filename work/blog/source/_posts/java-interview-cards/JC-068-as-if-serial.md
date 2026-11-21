---
title: "[JC-068] JMM·as-if-serial（重排）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## JMM · as-if-serial（重排）

- **事实**：单线程内程序表现为串行语义（as-if-serial）编译器与 CPU 可自由重排
- **原理**：重排只在不改变单线程结果的前提下进行，多线程下重排导致可见性问题，需要 happens-before 约束
- **常见误区**：
  1. 重排在单线程也会出错（错）
  2. CPU 不做任何重排（错）
  3. as-if-serial 是多线程语义（错）
- **工程用法**：判断重排问题时先看是否跨线程
- **版本锚点**：JLS 17.4
