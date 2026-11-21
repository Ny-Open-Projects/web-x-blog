---
title: "G1. StringBuilder vs StringBuffer？字符串拼接编译器优化？（一面必问）"
date: 2026-11-18
categories: [Java面试, 追问地图]
tags: [Java面试, 补漏卡, 33]
type: 补漏卡
disableNunjucks: true
---

### G1. StringBuilder vs StringBuffer？字符串拼接编译器优化？（一面必问）

**【参考回答（可背）】** 三层：① StringBuffer 线程安全（方法 synchronized）、StringBuilder 不安全但快——单线程拼字符串一律 StringBuilder；② 编译器优化：`"a" + b` 常量折叠（编译期常量直接合并）+ 非 aconst 拼接在 javac 层自动改写为 StringBuilder（JDK8 及以前），**JDK 9+ 改为 invokedynamic + StringConcatFactory**（运行时按实际拼接形态选策略，比手写 StringBuilder 更快）；③ 循环内拼字符串即使编译器优化也每轮新建 Builder——循环拼接必须手动提到循环外。
**【追问链】** String.concat / + / StringBuilder 三者字节码差异？→ concat 每次 new；+ 在 JDK9+ 走 StringConcatFactory.makeConcatWithConstants。为什么 JDK9 改？→ 预估长度+按形态 specialize，基准测试比预 StringBuilder 快。
**【P10 加分项】** "我们规范：编译器已优化单行拼接，禁止手写 StringBuilder 反而降低可读性；循环拼接才强制 Builder。规范要跟着 JDK 版本演进，别把 8 年前的老规矩当真理。"
