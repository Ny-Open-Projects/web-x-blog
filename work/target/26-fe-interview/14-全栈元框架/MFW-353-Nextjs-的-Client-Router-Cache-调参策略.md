---
title: [MFW-353] Client Router Cache 调参（staleTime 的路由级策略）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→353：Router Cache 调参

**答**:
- 默认语义与痛点：静态段 5min/动态段 30s（旧版）→ 15 全 request-share 0s（导航回退也重验——一致性↑流畅↓）——策略要按路由画像重立
- 调参表方法：按「变更频率 × 回访概率」二维分档：高频变更低回访（搜索结果）0s；低变更高回访（设置页）5min 自定义 staleness 语义；中间态用 revalidate 精准戳
- 实验 API（staleTimes 配置）与升级迁移：调参集中在一次配置审计（逐路由标注期望档位——对照 build 标记与 RSC payload 的 revalidate 值）
- 验证断言：E2E 双导航时延对比（二次导航 < 100ms 为流畅档生效）+ 数据龄断言（关键页回到列表立即重验）

```javascript
experimental: { staleTimes: { dynamic: 30, static: 300 } }   // 起点而非终点
// 调参表：route → { tier: 'hot'|'fresh'|'stable', expectNavMs, expectAge }
// 断言：二次导航 P50 <100ms（流畅档）；关键页回列表必重验（新鲜档）
```
