---
title: [WEB-141] VPN 和系统代理对前端调试有哪些坑？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-141：VPN 和系统代理对前端调试有哪些坑？
**答**：
- VPN 工作在网络层接管路由，所有流量走隧道；系统代理工作在应用层，只有"认代理设置的应用"才受影响。
- 坑 1：Node 与多数 CLI 不读系统代理，需显式设置 HTTP_PROXY/HTTPS_PROXY 环境变量。
- 坑 2：WebSocket 默认跟随 HTTP 代理（CONNECT 隧道），某些代理对长连接有超时或分帧限制，表现成 WS 频繁断开。
- 坑 3：VPN 改变出口 IP，CDN 调度、风控、灰度结果都会变，测试结论可能失真。
- 坑 4：证书信任域不一致——系统钥匙串信任了抓包证书，但 Node 用自带 CA 列表，仍会报校验失败。

```bash
# 让 Node/CLI 也走代理：显式设置环境变量
export HTTPS_PROXY=http://127.0.0.1:8888 HTTP_PROXY=http://127.0.0.1:8888
export NODE_TLS_REJECT_UNAUTHORIZED=0   # 临时信任抓包证书，仅限调试环境
# 验证 WebSocket 是否被代理影响：直接探测握手
curl -x http://127.0.0.1:8888 -i -N \
  -H 'Connection: Upgrade' -H 'Upgrade: websocket' \
  https://ws.example.com/socket 2>&1 | head -5
# 查看当前系统代理与 VPN 接管情况
scutil --proxy | head -8
```
