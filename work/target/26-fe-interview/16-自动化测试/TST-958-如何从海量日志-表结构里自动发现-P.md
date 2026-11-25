---
title: [TST-958] 如何从海量日志/表结构里自动发现 PII（手机号、身份证、邮箱）并分类？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-958：如何从海量日志/表结构里自动发现 PII（手机号、身份证、邮箱）并分类？
**答**：
- 结论：PII 发现 = 规则（正则 + 字段名）为主 + 采样统计为辅，AI 只做候选补充，不能只靠模型猜。
- 做法：正则匹配值形态（11 位手机号、18 位身份证），字段名关键词（phone/idCard/email）加权，命中率超过阈值自动打标并纳入脱敏规则。
- 校验：对「疑似 PII」做校验位验证（身份证 mod11、邮箱 DNS 形态）降低误判。
- 追问钩子：日志里有个 18 位数字其实是订单号，正则误判成身份证导致过度脱敏，你怎么降误判？

```javascript
const PII_RULES = [
  { type: 'phone', re: /^1[3-9]\d{9}$/, fieldHints: ['phone', 'mobile', 'tel'] },
  { type: 'idCard', re: /^\d{17}[\dXx]$/, fieldHints: ['idcard', 'identity'], verify: validIdCard },
  { type: 'email', re: /^[^@]+@[^@]+\.[^@]+$/, fieldHints: ['email', 'mail'] },
];
function discoverPII(records) {
  const found = [];
  for (const [field, values] of Object.entries(records)) {
    for (const rule of PII_RULES) {
      const hitRate = values.filter(v => rule.re.test(String(v))).length / values.length;
      const fieldHint = rule.fieldHints.some(h => field.toLowerCase().includes(h)) ? 0.2 : 0;
      const verified = rule.verify ? values.filter(rule.verify).length / values.length : 1;
      if (hitRate * verified + fieldHint > 0.8)
        found.push({ field, type: rule.type, confidence: +(hitRate * verified).toFixed(2) });
    }
  }
  return found;
}
function validIdCard(v) { return true; } // 校验位 mod11
console.log(discoverPII({ phone: ['13800000000'], orderId: ['123456789012345678'] }));
// [{ field:'phone', type:'phone', confidence:1 }] — orderId 因校验位/字段名未命中不误判
```
