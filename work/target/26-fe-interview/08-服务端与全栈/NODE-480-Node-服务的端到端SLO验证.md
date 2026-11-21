---
title: [NODE-480] Node 服务的端到端 SLO 拨测（合成监控）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-480：端到端 SLO 拨测（合成监控）
**答**:
- 拨测定位：真实用户流量之外的第二只眼（低峰期无真实流量时段的唯一信号、早期故障发现——用户没来之前知道挂了）。
- 拨测设计：核心链路剧本（登录 → 浏览 → 下单（测试商品）→ 取消——完整闭环，不注入生产数据污染）、频率与分布（核心 1min/边缘 15min，多地域多运营商节点）、沙箱标记（测试账号 + 影子数据——与真实流量区分 NODE-373）。
- 拨测与 SLO：拨测结果参与可用性 SLI（与 RUM 加权——拨测是保底，RUM 是事实）、拨测失败≠事故（可能脚本问题）——失败确认协议（连续 3 次 + 多地域同时失败才告警）。
- 维护成本治理：拨测脚本与产品变更联动（页面改版 → 拨测脚本同步更新——拨测脚本腐烂是最大问题：选择器断言自动化修复辅助）、假失败率监控（拨测自身健康）。
- 产出：拨测成功率/延迟趋势、故障发现贡献（多少故障是拨测先发现的——证明价值）。
```javascript
// 多地拨测剧本
probe.register('core-order', {
  every: '1m', regions: ['cn-north', 'cn-east'],
  steps: [login(testUser), browse('goods/g1'), order({ sandbox: true }), cancel(orderId)],
  sandbox: true,
  alarm: { onFail: '3 consecutive + 2 regions' }                 // 防脚本问题误报
});
```
