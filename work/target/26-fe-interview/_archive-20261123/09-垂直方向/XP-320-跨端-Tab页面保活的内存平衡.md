---
title: [XP-320] 跨端 Tab/页面保活的内存平衡
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-320：跨端 Tab/页面保活的内存平衡

**答**：
- 保活：Tab 页切走保留状态（回切秒开）——代价内存常驻。
- 策略：核心 Tab 保活（3 个），非核心销毁（状态序列化恢复）；内存水位高时强制释放非活跃 Tab。
- 度量：保活页面内存 + 恢复耗时（< 100ms 体验无感）。

```javascript
// Tab 保活策略
function keepAlivePolicy(tabs, memRatio) {
  const core = tabs.filter(t => t.core);
  const others = tabs.filter(t => !t.core);
  return {
    keep: memRatio > 0.8 ? core.slice(0, 2) : core,   // 高水位减保活
    destroy: memRatio > 0.8 ? others : [],
    note: '销毁页面状态序列化到 store，恢复时反序列化',
  };
}
```
