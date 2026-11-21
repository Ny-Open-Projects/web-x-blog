---
title: [TST-214] 分布式下被测服务与依赖（数据库/第三方 stub）如何编排？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-214：分布式下被测服务与依赖（数据库/第三方 stub）如何编排？
**答**：
- docker-compose 每套环境独立 network + 命名空间，shard 连自己的实例——避免共享环境串扰。
- webServer 配置由 Playwright 拉起被测服务（本地/单机），多机则用 staging 共享环境 + 数据隔离。
- 第三方依赖用 stub 容器（如 mock 支付网关），隔离外部不稳定因素。
- 健康检查就绪门（wait-on）后才开跑，避免「服务未起」的假失败。

```javascript
export default defineConfig({
  webServer: {
    command: 'npm run start:staging-proxy',
    port: 3000, reuseExistingServer: !process.env.CI,
    timeout: 60_000,     // 就绪门前置
  },
});
r
```
