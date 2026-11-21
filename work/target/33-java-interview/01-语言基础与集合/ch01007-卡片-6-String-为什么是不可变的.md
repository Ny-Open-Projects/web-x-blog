---
title: "卡片 6：String 为什么是不可变的？"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 6：String 为什么是不可变的？
String 内部是 `private final byte[] value`（JDK9 后从 char[] 改为 byte[] + coder 字段，
拉丁字符省一半内存）。不可变的好处必背 4 条：
1. **字符串常量池复用**：不可变才能安全共享，省内存。
2. **hashCode 可以缓存**：String 的 hash 字段懒计算后缓存，作 HashMap key 更快。
3. **线程安全**：天然不可变，多线程随便读。
4. **安全性**：类加载器、网络参数用 String 传，防止被中途篡改。
