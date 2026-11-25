---
title: [TST-577] AI 辅助测试的伦理与边界
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-577：AI 辅助测试的伦理与边界

**答**：
- 结论：边界是「AI 不直接决定发布、不接触生产数据、不绕过评审」；伦理上注意数据隐私（不把敏感代码/数据传外部模型）、责任归属（错误由人担）、透明可审计。
- 做法：敏感信息脱敏后再送模型；优先用企业私有化模型；AI 产出留痕（Prompt/版本/生成物）便于追溯；明确「人机责任清单」。
- 追问钩子：用公有大模型测试涉密项目合规吗？——通常不合规；需私有化部署或数据脱敏 + 合规评估，且遵守公司数据出境与保密规定。

```javascript
// 送模型前的数据脱敏：避免敏感信息外泄
function sanitizeForModel(text) {
  return text
    .replace(/1[3-9]\d{9}/g, '<PHONE>')
    .replace(/[\w.-]+@[\w.-]+/g, '<EMAIL>')
    .replace(/\b\d{17}[\dX]\b/g, '<ID>')
    .replace(/sk-[A-Za-z0-9]{20,}/g, '<API_KEY>');
}
console.log(sanitizeForModel('联系 13800138000 或 a@b.com'));
console.log(sanitizeForModel('卡号 sk-abcdefghijklmnopqrstuv')); // <API_KEY>
```
