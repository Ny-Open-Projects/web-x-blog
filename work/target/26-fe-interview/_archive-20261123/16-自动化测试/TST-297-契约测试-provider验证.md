---
title: [TST-297] 提供者如何验证满足所有消费者的契约（Pact broker 流程）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-297：提供者如何验证满足所有消费者的契约（Pact broker 流程）？
**答**：
- provider CI 拉 broker 上「该服务作为 provider」的所有 consumer 契约逐一验证。
- pact-message/given 状态处理器：把契约的 providerStates 映射到真实数据准备。
- 验证结果回写 broker，consumer 发布时 broker 依此判断「可部署吗」（can-i-deploy）。
- 多版本消费者并存：契约带 consumer 版本，provider 要兼容在役版本集合。

```javascript
# provider CI
pact-verifier --pact-url "https://broker/pacts/fe-cart-order-svc/latest" \
  --provider-base-url http://localhost:3000 \
  --provider-states-setup-url http://localhost:3000/_pactStates
r
```
