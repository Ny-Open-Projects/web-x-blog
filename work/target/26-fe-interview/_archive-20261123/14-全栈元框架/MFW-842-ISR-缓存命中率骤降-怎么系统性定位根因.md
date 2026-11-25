---
title: [MFW-842] ISR 缓存命中率骤降，怎么系统性定位根因
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-842：ISR 缓存命中率骤降，怎么系统性定位根因

**答**：
- 结论：命中率骤降只有四类原因——键基数爆炸、TTL 过短、失效风暴、预热失败；先按路由分桶看 hit/miss，再分别查键基数、失效频率、预热状态。
- 落地：监控按路由+tag 分桶的命中率，键基数增长率、revalidate 调用频率、预热任务成功率作为三个关键信号。
- 追问钩子：命中率是不是越高越好？——100% 命中意味着永不更新、业务陈旧；命中率要与新鲜度平衡。

```javascript
function diagnose(metrics) {
  if (metrics.keyCardinalityGrowth > 0.5) return '键基数爆炸：检查是否把用户/utm 参数入键';
  if (metrics.revalidateRate > 10) return '失效风暴：排查 tag 高频触发，加去抖';
  if (metrics.ttlSeconds < 10) return 'TTL 过短：缓存频繁过期';
  if (metrics.warmupFailureRate > 0.1) return '预热失败：冷启动导致 miss';
  return '常规波动，继续观察';
}
console.log(diagnose({ keyCardinalityGrowth: 0.8 }));
// 键基数爆炸：检查是否把用户/utm 参数入键
// 三信号：key 基数增长 / revalidate 频率 / ttl / 预热成功率
```
