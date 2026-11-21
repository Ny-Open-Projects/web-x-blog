---
title: [WEB-177] 哪些 chrome:// 内部页与 flags 对前端实用？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-177：哪些 chrome:// 内部页与 flags 对前端实用？
**答**：
- chrome://net-export 记录网络日志（DNS/连接复用/QUIC 细节），配合 netlog viewer 离线分析，比抓包更贴近浏览器真实行为。
- chrome://tracing 深挖浏览器内部；chrome://process-internals 看站点隔离的进程分配。
- chrome://net-internals 系列：DNS 缓存查看与清除、Sockets、HSTS 状态查询。
- 常用 flags 与启动参数：--disable-http-cache、force-effective-connection-type 模拟弱网、PartitionedCookies 验证 CHIPS。
- 提醒：内部页与 flags 是诊断用途，结论要与用户真实环境交叉验证。

```bash
# 记录网络日志：开始录制，复现问题，停止并保存 json
open -a "Google Chrome" "chrome://net-export"
# 把 json 导入 netlog viewer（官方在线工具）分析 DNS 与连接复用
# 用无头模式验证某个 feature 的行为差异
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --user-data-dir=/tmp/chrome-prof \
  --enable-features=PartitionedCookies --dump-dom https://app.example.com > /dev/null
# 查看站点隔离把哪些源分配到独立进程
open -a "Google Chrome" "chrome://process-internals"
```

## 二十九、协议细节陷阱
