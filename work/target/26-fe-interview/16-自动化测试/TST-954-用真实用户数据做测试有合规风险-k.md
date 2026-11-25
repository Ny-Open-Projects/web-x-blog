---
title: [TST-954] 用真实用户数据做测试有合规风险，k-匿名 / l-多样性怎么在数据工厂落地？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-954：用真实用户数据做测试有合规风险，k-匿名 / l-多样性怎么在数据工厂落地？
**答**：
- 结论：k-匿名保证任意准标识符组合至少对应 k 条记录（防重识别），l-多样性保证每个等价类敏感属性至少 l 种取值（防属性推断）。
- 落地：数据工厂生成测试数据时，对age/城市/性别等准标识符做泛化（如 25→20-30）使满足 k=5，对敏感字段做扰动满足 l=3。
- 验证：生成后跑 k/l 校验器，不达标不出库。
- 追问钩子：k=5 的数据集里某个等价类全是「VIP 用户」，虽然 k 达标但泄露了等级信息，l-多样性怎么补？

```javascript
function checkKAnonymity(records, quasiKeys, k = 5) {
  const groups = new Map();
  for (const r of records) {
    const key = quasiKeys.map(k => r[k]).join('|');
    groups.set(key, (groups.get(key) || 0) + 1);
  }
  const violations = [...groups.entries()].filter(([, n]) => n < k);
  return { pass: violations.length === 0, violations };
}
function checkLDiversity(records, quasiKeys, sensitiveKey, l = 3) {
  const groups = new Map();
  for (const r of records) {
    const key = quasiKeys.map(k => r[k]).join('|');
    if (!groups.has(key)) groups.set(key, new Set());
    groups.get(key).add(r[sensitiveKey]);
  }
  return [...groups.entries()].filter(([, vals]) => vals.size < l).map(([k]) => k);
}
const data = [
  { age: '20-30', city: '北京', level: 'VIP' },
  { age: '20-30', city: '北京', level: '普通' },
  { age: '20-30', city: '北京', level: '新客' },
];
console.log(checkLDiversity(data, ['age', 'city'], 'level', 3).length); // 0
```
