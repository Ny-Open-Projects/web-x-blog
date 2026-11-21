---
title: "第 12 册 Arthas"
date: 2026-11-18
categories: [Java面试, 速记卡]
tags: [Java面试, 速记卡, 33]
type: 速记卡
disableNunjucks: true
---

## 第 12 册 Arthas

1. dashboard 总览；thread -n 3 栈顶定热点；thread -b 找死锁。
2. trace '#cost>200' -n 5 树形耗时；watch 看出入参；tt 存档回放偶现问题。
3. memory + heapdump --live + MAT 支配树；getstatic 免 dump 实锤静态泄漏。
4. profiler start/stop --format html 火焰图找平顶山。
5. sc -d / classloader -t 排依赖冲突；jad 核对运行代码版本。
6. retransform 热修复只止血，24h 内正式发版；用完必 stop。
