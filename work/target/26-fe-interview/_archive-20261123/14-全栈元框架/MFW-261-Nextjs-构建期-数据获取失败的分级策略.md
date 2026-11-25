---
title: [MFW-261] 构建期数据获取失败的分级策略（别让构建说谎）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-261：构建期数据获取失败的分级策略

**答**:
- 分级矩阵：关键数据失败（商品列表 SSG 源挂）→ 构建失败 fail-fast（坏产物不上线）；可降级数据（推荐位）→ 空占位 + 构建警告（页面仍发布）；低价值（统计角标）→ 静默默认值——每页声明数据级别而非全局一个开关
- 「构建成功的谎言」识别：警告被日志淹没、空数据页上线数天才被发现——警告必须聚合（构建摘要顶部）+ 非零退出码阈值（>N 个数据缺失即 fail）
- 重试与降级源：构建期 fetch 失败先重试/切镜像源，再降级——顺序：重试(2)→备源→占位→fail（按数据级别选择终点）
- 验证：CI 模拟数据源故障（mock 500）跑构建——断言分级行为符合声明（策略也要测试）

```javascript
// 数据级别声明
async function loadDataSafe(url, level /* 'critical'|'degradable'|'optional' */) {
  try { return await retryFetch(url, 2) }
  catch (e) {
    if (level === 'critical') throw e                        // fail-fast
    log.warn(`[degraded:${level}] ${url}: ${e.message}`)     // 聚合摘要
    return level === 'optional' ? DEFAULTS : PLACEHOLDER
  }
}
// 构建末尾：warnings.length > 5 → process.exit(1)
```
