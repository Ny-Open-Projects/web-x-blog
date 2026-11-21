---
title: [WEB-528] A/B 实验的前端接入与正确性
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 监控]
type: 面试题
---

## WEB-528：A/B 实验的前端接入与正确性

**答**：
- 接入三件套：分流（uid 哈希进实验组/对照组）、配置下发（实验参数版本化）、埋点归因（所有事件带实验标识与桶号）
- 正确性坑一：分流时机——必须在「用户身份确定后」分流，登录前后 uid 不同会导致同用户漂移桶
- 正确性坑二：SRM（样本比失衡）——实验/对照组流量比偏离配置值说明分流有 bug 或埋点丢数据，实验数据不可信
- 正确性坑三：闪烁（flash of wrong variant）——实验渲染晚于首屏会出现旧版闪现，既伤体验又污染数据；关键实验要SSR/首屏前分流
- 收尾：实验结束条件是「统计显著+观察周期完整」，不是「看起来好了就上」

```javascript
// 分流与归因一致性：埋点带桶号
const bucket = ab.assign('new-checkout', user.uid);
track({ event: 'pay_success', exp: 'new-checkout', bucket });
```
