---
title: [OPS-188] 接口 mock 与联调环境怎么治理？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-188：接口 mock 与联调环境怎么治理？
**答**：
- 契约先行：接口定义（OpenAPI）入库，mock 服务从契约生成——联调双方对着同一份契约，前端不必等后端。
- mock 不只有成功场景：延迟注入、错误率注入、异常场景显式建模（配额超限、鉴权失败），前端错误处理被提前验证。
- 环境治理：联调默认走 mock 域名；真联调环境按窗口开启，后端服务注册进服务目录，防僵尸环境（呼应 OPS-156）。
- 契约校验自动化：CI 跑契约测试，后端破坏契约时前端用例自动红——破坏在合入前暴露。
- mock 数据与生产脱敏数据分离：禁止把生产用户数据拷进联调环境。

```javascript
// 联调环境治理：契约 mock 优先 + 异常场景建模 + 契约校验
import { createOpenapiMock } from './mock-server';

// 1. mock 从 OpenAPI 契约生成，联调双方对同一份契约
const app = createOpenapiMock('openapi/user.yaml', {
  delayMs: 30,          // 模拟真实延迟，暴露加载态问题
  errorRate: 0.02,      // 2% 失败注入，提前验证错误处理
});

// 2. 异常场景显式建模，不只有一个"成功"
app.when({ query: { uid: 'vip_user' } }).reply({ 200: { profile: { level: 6 } } });
app.scenario('quota_exceeded').reply({ 403: { code: 'QUOTA_EXCEEDED', msg: '次数不足' } });
app.scenario('auth_expired').reply({ 401: { code: 'AUTH_EXPIRED' } });

// 3. CI 契约校验：后端破坏契约时前端用例自动红，破坏在合入前暴露
await contractTest(app, 'openapi/user.yaml');

// 4. 环境治理规则：
//    - 联调默认走 mock-api.example.com，前端切换只改 .env.local 一行
//    - 真联调环境按窗口开启，服务注册进服务目录（防僵尸，OPS-156）
//    - mock 数据与生产数据隔离，禁止拷贝生产用户数据
```
