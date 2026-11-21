---
title: [NODE-176] 设计一个灰度发布服务端（规则引擎/染色）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-176：设计一个灰度发布服务端（规则引擎/染色）？
**答**：
- 规则引擎：规则有序（优先级即数组顺序），每条规则定义匹配条件（白名单 uid、按比例取模、城市/租户维度）与染色结果；规则存配置中心热更（NODE-150）。
- 染色传播：结果写入响应头 + 透传下游（`x-tint`），网关按 tint 路由到对应实例组（NODE-091/152）。
- 数据兼容：灰度实例的 schema 变更必须前向兼容或双写（NODE-197），保证随时可回退。
- 观测闭环：指标按 tint 维度出（NODE-135 标签扩展），灰度/稳定对比错误率与 P99，达标自动扩大比例。

```javascript
// 规则有序，先匹配先生效
const RULES = [
  { match: { uidIn: [1001, 1002, 1007] }, tint: 'gray-v2' }, // 白名单
  { match: { percent: 10 }, tint: 'gray-v2' },               // 按 uid 取模 10%
  { match: { cityIn: ['sh', 'hz'] }, tint: 'gray-v2' },      // 城市维度
];

function tint(ctx) {
  const uid = ctx.state.uid ?? 0;
  for (const rule of RULES) {
    const m = rule.match;
    if (m.uidIn && !m.uidIn.includes(uid)) continue;
    if (m.percent != null && uid % 100 >= m.percent) continue;
    if (m.cityIn && !m.cityIn.includes(ctx.query.city)) continue;
    return rule.tint;                            // 命中即染色
  }
  return 'stable';
}

app.use(async (ctx, next) => {                   // 染色中间件
  const t = tint(ctx);
  ctx.state.tint = t;
  ctx.set('x-tint', t);                          // 响应可见 + 下游透传
  await next();
});
```
