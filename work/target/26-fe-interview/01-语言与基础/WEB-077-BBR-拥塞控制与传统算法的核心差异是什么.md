---
title: [WEB-077] BBR 拥塞控制与传统算法的核心差异是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-077：BBR 拥塞控制与传统算法的核心差异是什么？
**答**：
- 传统 CUBIC/reno 是"丢包驱动"：把丢包当拥塞信号，塞满缓冲区才减速，在长肥管道上会故意填满交换机队列，产生 bufferbloat 高延迟。
- BBR 是"模型驱动"：主动估算瓶颈带宽 BtlBw 与最小往返时延 RTprop，把发送速率控制在"带宽跑满但队列不堆积"的工作点。
- 效果：弱网高丢包环境下 BBR 吞吐显著高于 CUBIC；对视频、大文件下载、QUIC 场景收益明显。
- 部署视角：BBR 是内核参数，CDN 与网关侧开启，前端只需理解它为什么让弱网用户更快。

```bash
# Linux 开启 BBR
sysctl net.ipv4.tcp_congestion_control        # 查看当前算法
echo 'net.core.default_qdisc=fq' >> /etc/sysctl.conf
echo 'net.ipv4.tcp_congestion_control=bbr' >> /etc/sysctl.conf
sysctl -p
sysctl net.ipv4.tcp_available_congestion_control  # 确认 bbr 生效
```
