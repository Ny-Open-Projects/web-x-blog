---
title: [NODE-814] 笔试题——实现网关 WAF 规则引擎（特征拦截 + 分级处置）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-814：手写 WAF 规则

**需求与边界**：
- 需求：网关 WAF（SCN-联想-686/687）——① 特征规则（SQLi/XSS 特征/路径穿越——正则规则库）；② 分级处置（block/log/captcha——SCN-联想-686 三件套）；③ 规则热更（SCN-联想-686 快照）；④ 误报放行（灰度模式——先 log 观察，SCN-OPS-276 试用期）。
- 边界：① 正则性能（ReDoS 防御——正则超时/简化模式）；② 误报率统计（SCN-OPS-276 信任分级）；③ 新规则的 log 试用期（SCN-OPS-276 哨兵试用期同构）。

**答**：
```javascript
const WAF_RULES = [
  { id: 'sqli', re: /(\bunion\b.+\bselect\b)|(--\s)|('\s*or\s*'1')/i, action: 'block' },
  { id: 'xss', re: /<script|javascript:|on\w+\s*=/i, action: 'captcha' },
  { id: 'traversal', re: /(\.\.\/){2,}/, action: 'block' },
];
function waf(req) {
  const payload = `${req.url}|${JSON.stringify(req.body)}`;
  for (const rule of currentRules()) {                 // 热更快照（SCN-联想-686）
    const start = performance.now();
    const hit = withRegexTimeout(rule.re, payload, 10);   // ReDoS 防御（10ms 超时）
    if (hit === 'TIMEOUT') { report({ type: 'WAF_RE_TIMEOUT', rule: rule.id }); continue; }
    if (hit) {
      const action = ruleTrust(rule) === 'trial' ? 'log' : rule.action;   // 新规则试用期（SCN-OPS-276）
      if (action === 'block') throw new AppError('WAF-001', 'blocked', { http: 403 });
      if (action === 'captcha') return captchaChallenge(req);
      report({ type: 'WAF_LOG', rule: rule.id });      // 试用期只记录
    }
  }
}
```

**评分点**:
- 特征规则库 + 分级处置（block/captcha/log——SCN-联想-686）。
- ReDoS 防御（正则超时——性能保护）。
- 新规则试用期（log 观察——SCN-OPS-276 信任分级同构）。
- 热更快照（SCN-联想-686）。
