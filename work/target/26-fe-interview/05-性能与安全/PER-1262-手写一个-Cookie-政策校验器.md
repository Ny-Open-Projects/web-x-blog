---
title: [PER-1262] 手写一个 Cookie 政策校验器
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1262：手写一个 Cookie 政策校验器

**答**：
- 需求：实现 cookieAudit(cookies, policy)。cookies 为 [{ name, attrs: { Secure, HttpOnly, SameSite, Partitioned, Max-Age, Domain } }]；policy: { sessionNames, maxAgeDays, requirePartitioned }；检查：会话 cookie 必须 HttpOnly+Secure+SameSite；Max-Age 超限违规；跨站场景 requirePartitioned 时三方 cookie 必须带 Partitioned；输出 { violations: [{ name, rule }], pass }。
- 边界：attrs 缺失按未设置；Max-Age 单位秒；sessionNames 命中的按会话规则，其余按 maxAgeDays。
- 评分点：会话规则；Max-Age 换算；Partitioned 校验；汇总

```javascript
function cookieAudit(cookies, policy) {
  const violations = [];
  for (const c of cookies) {
    const a = c.attrs ?? {};
    const isSession = policy.sessionNames.includes(c.name);
    if (isSession) {
      if (!a.HttpOnly) violations.push({ name: c.name, rule: 'session 需 HttpOnly' });
      if (!a.Secure) violations.push({ name: c.name, rule: 'session 需 Secure' });
      if (!['Strict', 'Lax'].includes(a.SameSite))
        violations.push({ name: c.name, rule: 'session 需 SameSite=Strict/Lax' });
    } else if (a['Max-Age'] != null &&
      +a['Max-Age'] > policy.maxAgeDays * 86400)
      violations.push({ name: c.name, rule: `Max-Age 超 ${policy.maxAgeDays} 天` });
    if (policy.requirePartitioned && c.thirdParty && !a.Partitioned)
      violations.push({ name: c.name, rule: '三方 cookie 需 Partitioned (CHIPS)' });
  }
  return { violations, pass: !violations.length };
}
```
