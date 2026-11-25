---
title: [WCN-616] 元素库升级要做 AB 实验，前端分流与指标采集应如何与 WC 集成？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-616：元素库升级要做 AB 实验，前端分流与指标采集应如何与 WC 集成？

**答**：
- 结论：分流在「元素创建前」决定版本，指标在「事件协议里」采集；不要在渲染中读实验配置，避免闪烁。
- 做法：SDK 在页面初始化时算好 bucket→version，WC 渲染器读 data-exp-version；曝光/交互事件通过统一事件协议上报到实验平台。
- 追问钩子：如何保证同一用户跨页面分桶一致？用稳定哈希（ userId+实验 salt），而非随机数——考察实验基建认知。

```javascript
function bucket(userId, salt) {
  let h = 0;
  const s = `${userId}:${salt}`;
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0;
  return h % 100; // 稳定分桶
}
function pickVersion(userId, exp) {
  const b = bucket(userId, exp.salt);
  return b < exp.traffic ? exp.versionB : exp.versionA;
}
const exp = { salt: 'ds-button-2026', traffic: 20, versionA: '2.x', versionB: '3.x' };
const v = pickVersion('u_123', exp);
document.documentElement.dataset.expVersion = v;
// WC 渲染读取 document.documentElement.dataset.expVersion 决定策略
```
