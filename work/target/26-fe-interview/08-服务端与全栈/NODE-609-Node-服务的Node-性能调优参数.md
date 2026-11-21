---
title: [NODE-609] Node 服务的运行时调优参数（GC/内存/V8）如何配置？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-609：Node 运行时调优
**答**:
- 内存参数：--max-old-space-size（按容器 limit 留余量：limit 1Gi → 768MB——native/Buffer 余量 NODE-374）、--max-semi-space-size（新生代——高分配率服务调大减少 scavenge 频率）、GC 日志（--trace-gc --trace-gc-verbose——GC 停顿分析）。
- GC 调优思路：识别 GC 压力（GC 频率/停顿时长指标 NODE-372）、减少分配（对象复用/避免大临时对象——代码层优先于参数层）、增量标记（大堆服务——major GC 停顿分摊）。
- V8 其他：--optimize-for-size（内存受限——牺牲速度）慎用、--max-http-header-size（特殊场景）、--dns-result-order（IPv4 优先——连接延迟）。
- 事件循环：UV_THREADPOOL_SIZE（默认 4——fs/crypto/dns 密集服务调大，上限与 CPU 核对齐）、监控验证（调参前后事件循环延迟对比——数据驱动调优）。
- 方法论：参数是最后手段（先代码后参数——调优顺序：算法/缓存/参数）、参数变更进配置管理（启动参数版本化——变更留痕演练）、A/B 验证（参数效果用压测对比验证——不凭感觉）。
```bash
# 生产启动参数模板（容器 1Gi limit）
node --max-old-space-size=768 --max-semi-space-size=32 \
     --trace-gc=stderr --dns-result-order=ipv4first dist/server.js
# UV_THREADPOOL_SIZE=8 （fs/crypto 密集服务）
```
