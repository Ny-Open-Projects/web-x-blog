---
title: [NODE-455] Node 服务的账号安全体系（撞库/盗号/异常登录）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-455：账号安全体系
**答**:
- 撞库防护：密码哈希（argon2/bcrypt 慢哈希 NODE-363）、登录限速（按账号/IP/设备多维限频）、密码泄露情报（已知泄露密码库比对——用户设置弱密码时拒绝）。
- 异常登录检测：登录特征评分（新设备/异地/非常用时间/代理 IP）→ 分级响应（低风险放行、中风险二次验证、高风险拒绝+通知）；设备指纹与会话绑定（NODE-415/ARC-415）。
- 盗号治理：会话异常行为检测（登录后行为突变：改绑手机+大额操作连续发生 → 冻结复核）、敏感操作二次认证（改密码/改手机号/支付，ARC-454 OTP）、异常会话踢出。
- 账号恢复安全：找回流程是最薄弱环——多因素验证（旧手机号失效场景的备用验证）、恢复后全端踢出 + 安全提醒、恢复流程审计。
- 观测与应急：撞库攻击波形告警（登录失败率激增）、批量盗号应急 SOP（批量冻结/回滚变更的预案 NODE-429）。
```javascript
// 登录分级响应
async function login({ account, password, device, ip }) {
  const user = await verifyPassword(account, password);          // 慢哈希校验
  const risk = await riskScore({ user, device, ip, history });   // 特征评分
  if (risk.level === 'high') { notify(user, '登录被拒绝'); throw new Blocked(); }
  if (risk.level === 'mid') return requireOtp(user);             // 二次验证
  await trackDevice(user, device);                               // 设备登记
  return issueSession(user, device);
}
```
