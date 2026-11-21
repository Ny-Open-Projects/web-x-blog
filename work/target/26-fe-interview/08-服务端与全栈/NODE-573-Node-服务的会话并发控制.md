---
title: [NODE-573] Node 服务的会话并发控制（同账号多设备策略）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-573：会话并发控制
**答**:
- 策略谱系：允许多端（默认——多设备各自会话）、互踢（新登录踢旧——强安全场景）、限数（最多 N 端——超出踢最旧）、按端类型（Web+手机各一——类型配额）。策略产品配置化（按业务安全等级）。
- 实现：会话注册表（账号 → 会话集合（设备/时间/位置）——Redis hash）、登录时按策略执行（互踢：标记旧会话 revoked → 全端踢出广播 ARC-415）、会话列表（用户可见的登录设备管理——可手动踢出）。
- 一致性：踢出生效（被踢端下次请求 401 → 长连接同步断开 NODE-481）、并发登录竞争（两端同时登录互踢——最后写入胜，可接受）。
- 安全联动：异常并发检测（短时间多地区登录——风控验证 NODE-455）、敏感操作绑定当前会话（改密码后除当前端全踢——防他人保持）。
- 观测：并发会话数分布、互踢频率（互踢频繁 = 用户困扰或盗号——分类处理）。
```javascript
async function onLogin(user, device) {
  const sessions = await sessionRegistry.list(user.id);
  const policy = concurrencyPolicy(user.tier);                   // {maxPerType: web1+app2}
  const evict = sessions.filter(s => violates(policy, s, device));
  for (const s of evict) await revoke(s);                        // 策略踢出
  await sessionRegistry.add(user.id, device);
}
// revoke：token 黑名单 + 各端推送下线（长连接断开）
```
