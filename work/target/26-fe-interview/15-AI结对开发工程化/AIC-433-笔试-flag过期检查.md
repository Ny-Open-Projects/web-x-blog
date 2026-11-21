---
title: [AIC-433] 笔试：实现 feature flag 过期检查与清理建议。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-433：笔试：实现 feature flag 过期检查与清理建议。
**题目**：flag `[{name, expiresAt, owner, defaultOn}]`。过期 flag：defaultOn=true → 建议「删除分支只留默认行为」；false → 建议「恢复默认再删」。实现 `auditFlags(flags, now)` 输出 `{expired, urgent}`（7 天内到期为 urgent）。

```javascript
const DAY = 86_400_000;
function auditFlags(flags, now) {
  const expired = [], urgent = [];
  for (const f of flags) {
    if (now >= f.expiresAt) expired.push({ ...f,
      action: f.defaultOn ? '删除 flag 分支，保留默认行为' : '回滚默认值后删除' });
    else if (f.expiresAt - now <= 7 * DAY) urgent.push({ name: f.name, owner: f.owner });
  }
  return { expired, urgent };
}
console.log(auditFlags([
  { name: 'new-cart', expiresAt: 0, owner: 'li', defaultOn: true },
  { name: 'dark-mode', expiresAt: 3 * 86_400_000, owner: 'wang', defaultOn: false },
], 1 * 86_400_000)); // expired [new-cart]；urgent [dark-mode]

```

**评分点**：
- 过期判定（now > expiresAt）与临期判定（7 天窗口）分开。
- 清理建议按 defaultOn 分支给出——可执行而非一句「清理」。
- 输出带 owner 便于通知。
- 边界（恰好到期）算 expired。
