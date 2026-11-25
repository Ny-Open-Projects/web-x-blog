---
title: [WEB-076] TCP 慢启动是什么？为什么它直接拖慢首屏？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-076：TCP 慢启动是什么？为什么它直接拖慢首屏？
**答**：
- 建连初期拥塞窗口 cwnd 很小（初始 10 个 MSS，约 14KB），每个 RTT 翻倍，直到丢包或达到阈值——前几个 RTT 能传的数据极少。
- 首屏关键资源（HTML + CSS + JS）普遍超过初始窗口，意味着要经历多个 RTT 才能传完，慢启动是首屏延迟的隐藏大头。
- 因此有"首屏关键资源总量控制在 14KB 内"的经验法则（对齐初始 cwnd），HTML 内联关键 CSS、压缩体积都是这个逻辑。
- HTTP/2 复用单连接反而放大慢启动影响：所有资源共享一条刚慢启动完的连接；HTTP/3 的连接迁移与更快恢复是应对方向。

```bash
# 演示慢启动的数学：初始 cwnd=10 MSS，每个 RTT 翻倍，估算传完 500KB 需要几个 RTT
awk 'BEGIN {
  mss = 1460; cwnd = 10; total = 0; rtt = 0;
  target = 500 * 1024;
  while (total < target) {
    rtt++;
    total += cwnd * mss;
    printf "RTT %d 本轮可发 %d KB 累计 %d KB\n", rtt, cwnd * mss / 1024, total / 1024;
    cwnd = cwnd * 2;  # 慢启动阶段指数增长
  }
  printf "传完 500KB 需要 %d 个 RTT\n", rtt;
}'

# Linux 可调初始拥塞窗口（一般不动，理解概念即可）
ip route change $(ip route | grep default) initcwnd 10
```
