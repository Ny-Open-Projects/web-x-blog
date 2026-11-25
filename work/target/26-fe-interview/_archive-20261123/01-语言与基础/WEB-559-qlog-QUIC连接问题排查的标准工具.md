---
title: [WEB-559] qlog：QUIC 连接问题排查的标准工具
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-559：qlog：QUIC 连接问题排查的标准工具

**答**：
- QUIC 全程加密，传统 TCP 抓包看不到握手细节，qlog 是 QUIC 规范定义的事件日志 JSON 格式，两端（客户端/服务端）都能导出，是 QUIC 时代的 tcpdump
- 服务端开启 qlog 后按 Connection ID 存文件，配合 qvis/quic-trace 可视化时间线，握手/丢包/流控事件一目了然
- 前端浏览器侧：Chrome `net-export` 导出网络日志（含 QUIC 事件），`chrome://net-export` + 在线 netlog viewer 分析
- 典型排查流程：拿失败连接的服务端 qlog → 看是否收到 Initial → 没收到是网络拦截；收到但无响应是服务端问题；握手中断看 TLS 事件
- 生产注意：qlog 开销不小（每连接一个文件），线上采样开启（如 1% 失败连接 + 灰度地区全量），不要全量常开

```bash
# 服务端: nginx quic 模块 / quic-go 按 CID 采样落盘 qlog
# 分析: 上传 qvis (https://qvis.quictools.info) 查看时间线
# chrome: chrome://net-export → stop → 导出 .json → netlog viewer
```
