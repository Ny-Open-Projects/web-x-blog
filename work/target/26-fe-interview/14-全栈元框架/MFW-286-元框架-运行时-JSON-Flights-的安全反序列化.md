---
title: [MFW-286] RSC Payload 反序列化的安全面（原型污染与注入）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 笔试题
---

## MFW-286：RSC 反序列化安全面

**答**:
- 风险面：Flight 流中的客户端引用（client component props）由攻击者可构造的场景（中间人/开放代理/自托管误配置）——反序列化需防原型污染（__proto__/constructor 注入键）
- 框架层防线：React 生产版反序列化对危险键有防护——自建 RSC/自解析 flight 时必须复刻（键黑名单 + Object.create(null) 容器）
- 上游依赖即攻击面：React 版本滞后于安全公告（CVE-类反序列化问题）——升级纪律与漏洞订阅是流程不是临时抱佛脚
- 通用加固：所有来自客户端的可序列化输入过 zod（白名单字段——不做深合并/不透传到危险 API：eval/innerHTML/路径拼接）

```javascript
// 自解析防护要点
const safe = Object.create(null)                       // 无原型容器
for (const k of Object.keys(raw)) {
  if (k === '__proto__' || k === 'constructor' || k === 'prototype') continue   // 键黑名单
  safe[k] = raw[k]
}
// 白名单优先：zod parse 后才进业务（黑名单是最后防线不是唯一防线）
```
