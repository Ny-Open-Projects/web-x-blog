---
title: [ALG-468] 手写数位 DP 用于日志 ID 审计：合规编号检查
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-468：手写数位 DP 用于日志 ID 审计：合规编号检查

**答**：
- 题目：日志 ID 必须符合「8 位、首位非 0、不含字母混淆位（4/1 之类）」的合规规则，审计历史日志找出违规 ID。规则明确时直接逐条正则校验即可——数位 DP 用于「统计违规分布」（按违规类型分组计数）。
- 思路：违规类型枚举（长度错/首位 0/含非法位），扫描日志按类型分组计数。教学点：数位 DP 是「计数」，审计是「逐条判」——不要错用工具。
- 评分点：计数 vs 逐条判的分工；违规分型统计；正则/规则引擎的合理使用。

```javascript
function auditIds(ids, rule) {                             // rule: {len, banned, firstNonZero}
  const violations = { badLength: 0, badFirst: 0, bannedDigit: 0, clean: 0 };
  for (const id of ids) {
    if (id.length !== rule.len) { violations.badLength++; continue; }
    if (rule.firstNonZero && id[0] === '0') { violations.badFirst++; continue; }
    if ([...id].some(c => rule.banned.includes(c))) { violations.bannedDigit++; continue; }
    violations.clean++;
  }
  return violations;                                       // 分型统计
}
// 数位 DP 的正确场景：不需要逐条列出，只要「[a,b] 区间内合法/违规的总数」
// 审计逐条场景：规则校验器 + 分型计数，不需要数位 DP
```
