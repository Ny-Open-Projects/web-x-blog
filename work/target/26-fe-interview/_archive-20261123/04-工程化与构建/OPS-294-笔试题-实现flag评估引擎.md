---
title: [OPS-294] 笔试题——实现 flag 评估引擎（规则求值 + 会话快照 + 决策日志）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## OPS-294：手写 flag 评估引擎

**需求与边界**：
- 需求：规则集按序求值（属性匹配/百分比/白名单/时间窗）；用户属性会话快照（SCN-OPS-235）；决策日志（命中哪条规则/为什么）；评估 O(flags×rules) 且无网络。
- 边界：① 规则类型白名单（未知类型跳过并告警）；② 百分比规则用稳定哈希；③ 时间窗规则边界含头含尾语义明确；④ 会话快照固化在引擎构造时。

**答**：
```javascript
const RULE_TYPES = ['attr', 'percent', 'whitelist', 'timeWindow'];
class FlagEngine {
  constructor(rulesSnapshot, userSnapshot, { hashFn = fnv1a } = {}) {
    this.rules = rulesSnapshot;                        // 规则快照
    this.user = Object.freeze({ ...userSnapshot });    // 用户属性会话快照（固化）
    this.hashFn = hashFn;
    this.log = [];
  }
  evaluate(flagKey) {
    for (const rule of this.rules[flagKey] ?? []) {
      if (!RULE_TYPES.includes(rule.type)) {
        report({ type: 'UNKNOWN_RULE_TYPE', flag: flagKey, rule }); continue;   // 跳过+告警
      }
      if (this[`match_${rule.type}`](rule)) {
        this.log.push({ flag: flagKey, matched: rule.id, value: rule.value });
        return rule.value;
      }
    }
    this.log.push({ flag: flagKey, matched: 'default' });
    return this.rules.defaults?.[flagKey] ?? false;
  }
  match_attr(rule) { return Object.entries(rule.attr).every(([k, v]) => this.user[k] === v); }
  match_percent(rule) { return this.hashFn(this.user.id + rule.salt) % 100 < rule.pct; }
  match_whitelist(rule) { return rule.users.includes(this.user.id); }
  match_timeWindow(rule) {
    const t = Date.now();
    return t >= rule.from && t <= rule.to;             // 含头含尾
  }
}
```

**评分点**:
- 双快照（规则 + 用户属性冻结）保证会话内分组稳定。
- 四类规则求值 + 未知类型跳过告警（容错不崩溃）。
- 百分比规则带 salt（分层正交复用）。
- 决策日志（命中规则可查询——SCN-OPS-235 调试能力）。
