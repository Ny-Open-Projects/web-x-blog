---
title: [NODE-094] 如何设计一个 Feature Flag（功能开关）服务？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-094：如何设计一个 Feature Flag（功能开关）服务？
**答**：
- 能力：开关存储与分组、**求值规则**（百分比放量、用户属性定向、白名单）、SDK 客户端（本地缓存 + 轮询/长连接同步，本地求值零网络延迟）、审计与一键回滚。
- 服务端求值核心：`isEnabled(key, context)` = 开关状态 → 白名单 → 用户属性规则 → 百分比哈希（稳定分桶，NODE-091 同理）→ 默认值。
- BFF 实践：求值结果进日志与埋点（谁看到了什么版本），方便 A/B 分析；宕机兜底用 SDK 最后快照 + 默认关。

```javascript
// Flag 求值引擎（服务端实现）
const flags = {
  'new-checkout': {
    enabled: true,
    rules: [
      { type: 'whitelist', uids: [1, 42] },
      { type: 'attribute', attr: 'country', op: 'in', values: ['CN', 'SG'] },
      { type: 'percentage', ratio: 20 },                  // 20% 放量
    ],
    defaultOn: false,                                     // 兜底
  },
};

function hash(key, uid) {                                  // 稳定哈希：同一 uid 结果恒定
  let h = 0;
  const s = `${key}:${uid}`;
  for (let i = 0; i < s.length; i++) { h = (h * 31 + s.charCodeAt(i)) | 0; }
  return Math.abs(h) % 100;
}

function isEnabled(key, ctx) {
  const flag = flags[key];
  if (!flag || !flag.enabled) return flag?.defaultOn ?? false;
  for (const rule of flag.rules) {
    if (rule.type === 'whitelist' && rule.uids.includes(ctx.uid)) return true;
    if (rule.type === 'attribute' && rule.values.includes(ctx.attrs?.[rule.attr])) return true;
    if (rule.type === 'percentage' && hash(key, ctx.uid) < rule.ratio) return true;
  }
  return flag.defaultOn;
}

// BFF 中使用 + 曝光埋点（A/B 分析依据）
app.get('/checkout', async (ctx) => {
  const ctxFlag = { uid: ctx.state.user.uid, attrs: { country: ctx.get('x-country') } };
  const useNew = isEnabled('new-checkout', ctxFlag);
  metrics.increment('flag_exposure', { flag: 'new-checkout', variant: useNew ? 'on' : 'off' });
  ctx.body = useNew ? await renderNewCheckout(ctx) : await renderLegacyCheckout(ctx);
});
```
