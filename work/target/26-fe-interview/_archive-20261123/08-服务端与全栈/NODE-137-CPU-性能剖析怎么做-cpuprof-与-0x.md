---
title: [NODE-137] CPU 性能剖析怎么做（--cpu-prof 与 0x 火焰图）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-137：CPU 性能剖析怎么做（--cpu-prof 与 0x 火焰图）？
**答**：
- 工具矩阵：`node --cpu-prof`（内置零依赖，产出 .cpuprofile 给 Chrome DevTools）、`0x`（一行命令交互式火焰图）、`clinic doctor`（先诊断症状再开方）。
- 火焰图阅读法：宽度 = CPU 占比，找**平顶宽块**就是热点；典型热点：大 JSON.parse、正则回溯、同步 crypto、深度递归。
- 生产在线采样：避免常驻 profiler 开销，用 SIGUSR2 之类信号按需采 5~10 秒。
- 与 NODE-083 复盘案例呼应：先有 lag 告警（NODE-105），再有火焰图定位，最后回归压测验证。

```bash
# 1. 内置 profiler：运行一段真实流量后自动生成 .cpuprofile
node --cpu-prof --cpu-prof-dir=./prof --cpu-prof-interval=1000 server.js
# Chrome DevTools → Performance → Load 打开查看火焰图

# 2. 0x：一行命令出交互式火焰图（按 Self time 排序找热点）
npx 0x -- node server.js

# 3. clinic doctor：先看症状（事件循环延迟 / GC / IO 哪种病）
clinic doctor -- node server.js
clinic flame -- node server.js

# 4. 生产在线采样：给运行中进程发信号按需采 5s（避免常驻开销）
kill -USR2 <pid>
# 阅读法：宽度 = CPU 占比；平顶宽块 = 热点；自顶向下找自己代码的帧
```
