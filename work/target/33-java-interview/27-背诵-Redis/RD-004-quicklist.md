---
title: "[RD-004] List·quicklist（编码）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## List · quicklist（编码）

- **事实**：List 底层是 quicklist（双向链表串起的紧凑节点），7.0 起节点从 ziplist 换成 listpack
- **原理**：兼顾链表的插入效率与紧凑结构的内存效率，7.0 用 listpack 消除 ziplist 的级联更新问题
- **常见误区**：
  1. List 是纯双向链表（错）
  2. quicklist 节点是跳表（错）
  3. 7.0 没有变化（错）
- **工程用法**：消息队列/最新列表场景
- **版本锚点**：Redis 7.0
