---
title: "[RD-047] 分布式锁·SET NX EX（基础）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 分布式锁 · SET NX EX（基础）

- **事实**：分布式锁标准写法：SET key uniqueValue NX EX seconds 一条命令加锁
- **原理**：NX 保证互斥、EX 防死锁、value 存唯一标识（UUID）供安全释放，释放用 Lua 校验 value 后 DEL（防止删别人的锁）
- **常见误区**：
  1. SETNX 加锁后 EXPIRE 分两步（错）
  2. 释放锁直接 DEL 即可（错）
  3. 锁的 value 随便存（错）
- **工程用法**：手写分布式锁的标准答案
- **版本锚点**：实战共识
