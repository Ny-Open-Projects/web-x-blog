---
title: [AGT-799] 手写 detectMissed：已知信息重复检测、字段聚合、盲区优化路由？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-799：手写 detectMissed：已知信息重复检测、字段聚合、盲区优化路由

**需求与边界**：
- 实现 detectMissed(msg, profile)：检测用户重复陈述已知信息。
- 边界要求：① 匹配画像字段值的陈述性语句（用户说"我用的 React"且画像已有 stack=React）记 missed；② 疑问句不算（用户在确认不算重复）；③ 按字段聚合统计率；④ 路由：蒸馏质量低→修蒸馏，检索权重低→调权重；⑤ 连续 missed 触发即时注入修复（当次会话补注入）。

**答**：
```javascript
function detectMissed(msg, profile) {
  if (/\?|？|吗$/.test(msg.text.trim())) return []; // 疑问句跳过
  return profile.facts.filter(f =>
    f.kind === 'fact' && statedIn(msg.text, f.value)
    && !session.injectedThisTurn(f.key))            // 本轮未注入
    .map(f => f.key);
}
function route(field, stats) {
  const distill = distillQuality(field);
  if (distill < 0.8) return { fix: 'distill', field };
  if (stats.rate(field) > 0.2)
    return { fix: 'weight', field,
      bump: Math.min(0.2, stats.rate(field)) };     // 检索权重上调
  return null;
}
function immediateFix(keys, profile) {
  // 当次会话补注入，避免用户再说一遍
  session.inject(keys.map(k => profile.facts.find(f => f.key === k)));
}
```

**评分点**:
- 疑问句排除（确认不算重复）；本轮已注入不算 miss。
- 双路由（蒸馏质量/检索权重）+ 权重增量按率封顶。
- 即时修复（当次会话补注入）闭环用户体验。

