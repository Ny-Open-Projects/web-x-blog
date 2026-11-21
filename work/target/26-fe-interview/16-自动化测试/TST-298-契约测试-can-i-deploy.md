---
title: [TST-298] 「can-i-deploy」机制如何防止破坏性发布？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-298：「can-i-deploy」机制如何防止破坏性发布？
**答**：
- 发布前查 broker：该 provider 版本是否已验证通过所有「在环境中的 consumer」契约。
- 通过 → 允许部署；失败 → 阻断并指出哪个 consumer 哪条契约破裂。
- consumer 侧同理：发布新版 consumer 前确认其对 provider 的期望已被验证。
- 矩阵可视化：环境 × consumer × provider 版本兼容矩阵，一眼看清风险。

```javascript
pact-broker can-i-deploy --pacticipant order-svc --version 1.4.2 --to-environment prod
# ✅ verified against fe-cart 5.2.0, fe-admin 1.1.0 → deploy allowed
r
```
