---
title: [MFW-244] 预览环境数据库分支的数据合规脱敏
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-244：预览分支的数据脱敏

**答**:
- 合规风险：生产快照分支（Neon 类）携带真实 PII 进预览环境——预览链接常外泄（QA/产品/客户演示）——泄露面等于生产
- 脱敏管线：分支创建后自动跑脱敏 job（字段级策略：姓名/手机/邮箱假名化、token 清空、金额扰动保分布）——脱敏策略是代码（可 review/测试）不是口头约定
- 分级通道：内部预览可用低脱敏（员工 NDA 面）/ 外部演示用强脱敏固定剧本数据——按受众分级
- 校验闭环：脱敏后自动扫描已知 PII 模式（手机号正则/邮箱密度）——漏脱敏 fail 门禁

```javascript
// 脱敏 job（分支创建触发）
const rules = {
  users: { email: fakeEmail, phone: fakePhone, name: fakeName },
  tokens: { value: () => null },
}
await runOnBranch(branch, rules)
await scanPii(branch, { patterns: [PHONE_RE, EMAIL_RE], fail: true })   // 门禁
```
