---
title: "[JC-069] JMM·final（安全发布）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## JMM · final（安全发布）

- **事实**：final 字段在构造器内赋值后无需同步即可被其他线程安全读取
- **原理**：JMM 对 final 有特殊保证：构造器内写 final 与随后把引用发布给其他线程之间有 happens-before，this 不逸出是前提
- **常见误区**：
  1. final 字段也需要 volatile 才可见（错）
  2. 任何情况下读 final 字段都能立即看到（错）
  3. String 的不可变与 final 无关（错）
- **工程用法**：不可变对象（值对象、配置）用 final 构建
- **版本锚点**：JLS 17.5
