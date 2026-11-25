---
title: [TST-960] 笔试：手写「PII 漏检扫描器」——扫描测试数据与日志，找出疑似未脱敏的敏感字段
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-960：笔试：手写「PII 漏检扫描器」——扫描测试数据与日志，找出疑似未脱敏的敏感字段
**答**：
- 需求：实现 scanPII(records, rules)，records 为 { field, values }[]，rules 为 [{ type, re, fieldHints }]。
- 规则：标记「值命中正则」或「字段名命中关键词」的字段为漏检候选，给出 confidence（两者都中 1.0，仅一项 0.6）；confidence>=0.6 输出。
- 边界：已标记 masked/desensitized 的字段跳过；值为空数组跳过；返回按 confidence 降序。

```javascript
function scanPII(records, rules) {
  const hits = [];
  for (const rec of records) {
    if (/mask|desens|脱敏/i.test(rec.field)) continue; // 已脱敏跳过
    if (!rec.values?.length) continue;
    let best = null;
    for (const rule of rules) {
      const valueHit = rec.values.some(v => rule.re.test(String(v)));
      const fieldHit = rule.fieldHints.some(h => rec.field.toLowerCase().includes(h));
      const confidence = valueHit && fieldHit ? 1.0 : (valueHit || fieldHit ? 0.6 : 0);
      if (confidence >= 0.6 && (!best || confidence > best.confidence))
        best = { field: rec.field, type: rule.type, confidence };
    }
    if (best) hits.push(best);
  }
  return hits.sort((a, b) => b.confidence - a.confidence);
}
const rules = [{ type: 'phone', re: /^1[3-9]\d{9}$/, fieldHints: ['phone', 'mobile'] }];
console.log(scanPII([
  { field: 'phone', values: ['13800000000'] },
  { field: 'phoneMasked', values: ['13800000000'] },
  { field: 'nickname', values: ['张三'] },
], rules)); // [{ field:'phone', type:'phone', confidence:1 }]
```
**评分点**：
- 值命中与字段名命中分别加权，两者都中置信度 1.0、单中 0.6。
- 已标记 masked/desensitized 的字段正确跳过。
- 空数组跳过，返回按 confidence 降序。
- 只输出 confidence>=0.6 的候选，降低噪声。
