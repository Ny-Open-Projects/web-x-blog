---
title: [SOFT-777] 手写 docRouter：按决策影响面路由文书类型（RFC/ADR/Memo）、公示期设定、反对意见回应追踪？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-777：手写 docRouter：按决策影响面路由文书类型（RFC/ADR/Memo）、公示期设定、反对意见回应追踪

**需求与边界**：
- 实现 docRouter(decision)。
- 边界要求：① 影响面字段 { teamsAffected, reversibility, costLevel }；② 路由规则：跨团队+不可逆→RFC（公示 7 天）/单团队不可逆或跨团队可逆→ADR/团队内可逆→Memo；③ RFC 生成公示期截止与反对意见追踪结构（每条反对必须回应：接受/拒绝+理由）；④ 未回应反对超 48h 告警。

**答**：
```javascript
function docRouter(d) {
  for (const k of ['teamsAffected', 'reversibility', 'costLevel'])
    if (d[k] === undefined) throw new Error(`缺字段：${k}`);
  const cross = d.teamsAffected > 1, irreversible = d.reversibility === 'hard';
  const kind = cross && irreversible ? 'RFC'
    : (irreversible || cross) ? 'ADR' : 'Memo';
  const out = { kind };
  if (kind === 'RFC') {
    out.publicUntil = new Date(Date.now() + 7 * 864e5).toISOString().slice(0, 10);
    out.objections = [];
    out.trackObjection = (o) => out.objections.push(
      { ...o, responded: false, respondedAt: null });
    out.respond = (idx, response, accepted) => {
      const o = out.objections[idx];
      o.response = response; o.accepted = accepted;
      o.responded = true; o.respondedAt = Date.now();
    };
    out.watchdog = () => out.objections.filter(o =>
      !o.responded && Date.now() - o.at > 48 * 3600e3)
      .map(o => `反对「${o.text.slice(0, 20)}」超48h未回应——告警`);
  }
  return out;
}
```

**评分点**:
- 三字段路由规则（跨团队×不可逆→RFC 最重文书）。
- RFC 反对意见强制回应 + 48h watchdog（反对必被回应的制度化）。

