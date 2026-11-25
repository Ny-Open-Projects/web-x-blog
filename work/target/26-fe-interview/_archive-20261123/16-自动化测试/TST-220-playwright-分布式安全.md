---
title: [TST-220] 分布式 E2E 的安全注意点（凭据/网络边界）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-220：分布式 E2E 的安全注意点（凭据/网络边界）？
**答**：
- 测试账号密码不进代码/CI 日志：secret manager 注入，storageState 文件加 .gitignore 且 artifact 限期。
- E2E 环境网络隔离：只能访问测试环境，禁止配置连生产（配置校验门禁）。
- 第三方 stub 替代真实外部调用，避免测试流量打到真实支付/短信。
- 测试数据用明显标记（E2E- 前缀 + 测试库），防误触真实用户数据。

```javascript
// 凭据注入而非硬编码
const user = { phone: process.env.E2E_BUYER_PHONE!, pwd: process.env.E2E_BUYER_PWD! };
// CI 校验：if (config.env === 'prod') throw new Error('E2E 禁止指向生产');
r
```
