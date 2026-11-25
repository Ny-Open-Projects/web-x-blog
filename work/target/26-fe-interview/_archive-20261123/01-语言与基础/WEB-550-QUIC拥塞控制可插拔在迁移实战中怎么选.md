---
title: [WEB-550] QUIC 拥塞控制可插拔在迁移实战中怎么选
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-550：QUIC 拥塞控制可插拔在迁移实战中怎么选

**答**：
- QUIC 拥塞控制在用户态实现，换算法不用动内核——这是相比 TCP（要改内核参数/升级内核）的运维级优势
- 默认起步用 CUBIC（与内核 TCP 一致、行为可预期）；弱网/直播/RTC 业务切 BBR 类算法，抗丢包吞吐明显更好
- 可按业务路由选算法：同一网关上静态下载用 CUBIC、IM 心跳与视频流用 BBR，按 SNI/路径分流配置
- 自研空间：QUIC 用户态可拿到更精确的时间戳与每包 ACK 信息，可做按业务定制的拥塞策略（如短连接激进、长连接保守），但要有灰度验证机制
- 验证方法：同机房同线路压测对比 CUBIC/BBR 在 1%/5% 随机丢包下的吞吐曲线，弱网收益要有数据再全量

```text
网关路由示例:
  *.download.example.com  → CUBIC  (大文件, 公平性优先)
  *.live.example.com      → BBRv2  (弱网抗丢包)
  api.example.com         → CUBIC  (短连接, 稳定优先)
压测: netem 5% loss 下 BBR 吞吐通常比 CUBIC 高 2~5x
```
