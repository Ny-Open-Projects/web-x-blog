---
title: [TST-755] AI 辅助测试的安全与隐私边界：数据出境如何在架构层拦截
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-755：AI 辅助测试的安全与隐私边界：数据出境如何在架构层拦截

**答**：
- 结论：送模数据要有「架构级网关」——所有出站请求经过统一代理，做 PII 识别、脱敏、白名单与审计，杜绝测试用例私自外发数据。
- 网关按数据分级策略拦截：敏感字段自动脱敏，高风险走审批，违规直接拒绝并告警。
- 审计留痕：谁、何时、送了什么（脱敏后）、调了哪个模型，可追溯。
- 追问钩子：开发把敏感数据编码后绕过网关，如何发现？

```javascript
// 送模网关：PII 拦截 + 脱敏
const PII = [/\d{11}/g, /[\w.+-]+@[\w-]+\.[\w.]+/g];
function sanitizeForModel(text) {
  let out = text, blocked = false;
  for (const re of PII) {
    if (re.test(out)) { blocked = true; out = out.replace(re, '[REDACTED]'); }
  }
  return { out, blocked };
}
console.log(sanitizeForModel('用户 13800138000 邮箱 a@b.com'));
// out:'用户 [REDACTED] 邮箱 [REDACTED]', blocked:true
```
