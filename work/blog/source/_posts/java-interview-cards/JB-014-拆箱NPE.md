---
title: "[JB-014] 包装类·拆箱NPE（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 包装类 · 拆箱NPE（误用）

- **事实**：对值为 null 的包装类做自动拆箱会抛 NullPointerException。
- **原理**：拆箱编译为 xxxValue() 调用，null 调用即 NPE；三目运算符两侧类型不一致时也会触发隐式拆箱。
- **常见误区**：
  1. null 包装类自动拆箱会得到默认值 0。（错）
  2. 自动拆箱永远不会抛异常。（错）
  3. Integer 与 int 混用编译器会报错。（错）
- **工程用法**：三目运算 boolean ? intVal : intWrapper 是真实 NPE 事故源。
- **版本锚点**：阿里手册强制：POJO 属性统一用包装类。
