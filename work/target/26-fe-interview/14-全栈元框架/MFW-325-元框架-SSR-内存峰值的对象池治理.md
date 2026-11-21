---
title: [MFW-325] SSR 渲染内存峰值治理（大列表/深树的流式策略）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-325：SSR 内存峰值

**答**:
- 峰值来源：renderToString 整树先建全量 vNode（万行列表 = 数百 MB 峰值）+ 序列化字符串双份——OOM 与 GC 抖动的根源
- 流式拆解：renderToPipeableStream 天然分块（Shell 先出、段按需求值）+ 段内列表分页（SSR 只渲染首屏 N 条，其余客户端增量——「SSR 不是全量打印器」）
- 对象复用：请求级大缓冲用池化（Buffer 池/复用序列化 scratch——GC 压力减半）；禁一次性 JSON.stringify 巨树（分段拼接）
- 度量与门禁：渲染期 RSS 采样（P95 峰值按路由）——超预算路由强制改造（分页/分段），进 CI 性能快照

```javascript
// 万行列表的 SSR 策略
<InfiniteList initial={firstPage20} />      // SSR 只渲染 20 条
// 客户端 useInfiniteQuery 拉后续——峰值从 500MB → 30MB
// 门禁：render RSS P95 per route < 256MB
```
