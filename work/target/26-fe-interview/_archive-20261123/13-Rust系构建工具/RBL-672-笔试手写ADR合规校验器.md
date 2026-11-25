---
title: [RBL-672] 笔试：手写 RFC/ADR 流程合规校验器（状态机 + 时间窗 + 迁移期）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-672：笔试：手写 RFC/ADR 流程合规校验器（状态机 + 时间窗 + 迁移期）

**需求**：实现 `validateADR(adr, { now })`。adr: `{ id, title, status, openedAt, decidedAt?, deprecateVersion?, removeVersion?, codemod? }`。状态机：draft → discussion → accepted/rejected → implemented。规则：1) discussion 状态的 ADR：openedAt 距 now < 14 天 → violation 'discussion-window'（静默期强制）；2) accepted 必须有 decidedAt 且 decidedAt ≥ openedAt + 14 天，否则 'early-decision'；3) breaking（status 含 'breaking'）的 accepted 必须有 deprecateVersion/removeVersion/codemod 三件套，缺一 → 'missing-migration'；4) implemented 要求 removeVersion 存在（实施即旧 API 移除计划明确）；5) rejected 允许无其他字段。返回 `{ violations: Array<{ rule, detail }> }`，合规返回空数组。非法 status 抛错。

```javascript
const VALID = ['draft', 'discussion', 'accepted', 'rejected', 'implemented', 'accepted-breaking'];
const DAY = 86400000;

function validateADR(adr, { now = new Date() } = {}) {
  if (!VALID.includes(adr.status)) throw new Error(`非法状态: ${adr.status}`);
  const v = [];
  const opened = new Date(adr.openedAt).getTime();

  if (adr.status === 'discussion' && now.getTime() - opened < 14 * DAY)
    v.push({ rule: 'discussion-window', detail: `已讨论 ${Math.floor((now - opened) / DAY)} 天，需 ≥14 天` });

  if (adr.status === 'accepted' || adr.status === 'accepted-breaking') {
    if (!adr.decidedAt) v.push({ rule: 'missing-decision', detail: 'accepted 缺 decidedAt' });
    else if (new Date(adr.decidedAt) - opened < 14 * DAY)
      v.push({ rule: 'early-decision', detail: '决策早于静默期结束' });
    if (adr.status === 'accepted-breaking') {
      for (const k of ['deprecateVersion', 'removeVersion', 'codemod'])
        if (!adr[k]) v.push({ rule: 'missing-migration', detail: `breaking 缺 ${k}` });
    }
  }
  if (adr.status === 'implemented' && !adr.removeVersion)
    v.push({ rule: 'missing-removal-plan', detail: 'implemented 需明确移除版本' });
  return { violations: v };
}

// 自测
const base = { id: 'ADR-1', title: 't', openedAt: '2026-11-01' };

// 1) 静默期未满
let r = validateADR({ ...base, status: 'discussion' }, { now: new Date('2026-11-08') });
console.log(r.violations[0].rule === 'discussion-window');

// 2) 过早决策
r = validateADR({ ...base, status: 'accepted', decidedAt: '2026-11-05' }, { now: new Date('2026-11-20') });
console.log(r.violations[0].rule === 'early-decision');

// 3) 合规 accepted
r = validateADR({ ...base, status: 'accepted', decidedAt: '2026-11-20' }, { now: new Date('2026-11-25') });
console.log(r.violations.length === 0);

// 4) breaking 缺迁移三件套
r = validateADR({ ...base, status: 'accepted-breaking', decidedAt: '2026-11-20' });
console.log(r.violations.filter(x => x.rule === 'missing-migration').length === 3);

// 5) breaking 合规 + implemented
r = validateADR({ ...base, status: 'accepted-breaking', decidedAt: '2026-11-20',
  deprecateVersion: '1.8', removeVersion: '2.0', codemod: 'npx x' });
console.log(r.violations.length === 0);
r = validateADR({ ...base, status: 'implemented', deprecateVersion: '1.8', codemod: 'npx x' });
console.log(r.violations[0].rule === 'missing-removal-plan');

let e; try { validateADR({ ...base, status: 'weird' }); } catch (x) { e = x; }
console.log(/非法状态/.test(e.message));
```

**评分点**：
- 状态机校验完整：discussion 静默期、accepted 时序、breaking 三件套、implemented 移除计划
- 时区安全的日期比较（统一 getTime）；静默期不足天数可读化
- rejected 语义宽松（无其他字段要求）；非法 status 抛错
- 能说清「流程合规化的价值：决策可追溯 + 迁移纪律」属于加分
