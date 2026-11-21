---
title: "[JV-051] 排查·top+Hp（CPU）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 排查 · top+Hp（CPU）

- **事实**：CPU 100% 排查流程：top 找进程、top -Hp 找线程、printf '%x' 转十六进制、jstack 按线程号定位
- **原理**：把 nid=0x十六进制 与线程栈对上，常见根因：死循环、正则回溯、GC 线程疯狂运转、JIT 编译
- **常见误区**：
  1. 该流程只在 Windows 有效（错）
  2. jstack 里线程号是十进制直接匹配（错）
  3. CPU 高一定是业务代码问题（错）
- **工程用法**：生产 CPU 故障标准动作
- **版本锚点**：实战共识
