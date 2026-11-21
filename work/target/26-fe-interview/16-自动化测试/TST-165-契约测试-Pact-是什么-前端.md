---
title: [TST-165] 契约测试（Contract Testing）是什么？前端怎么用它替代部分 E2E？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-165：契约测试（Contract Testing）是什么？前端怎么用它替代部分 E2E？
**答**：
- 定义：消费者驱动契约（CDC）——前端（消费者）把自己对接口的期望（请求 schema + 响应 schema + 语义）生成为「契约文件」，后端（提供者）在自己的 CI 里拿契约重放验证。「前端期望的数据」和「后端给的数据」在两边各自 CI 里被持续对齐。
- 解决的问题：mock 说成功、真后端改了字段、前端上线才崩——契约测试把这类「跨团队集成回归」从 E2E（慢、环境复杂）下放到两边的 CI（快、独立跑）。
- 流程：前端 CI 跑「契约验证」（MSW handler 按契约生成响应，确保前端代码消费契约数据没问题）→ 发布 pact 到 broker → 后端 CI 拉 pact 做 provider verification → 失败阻断后端合并（「你改的字段前端在用」）。
- 前端实操：轻量版不需要 Pact broker——接口层用 OpenAPI/zod schema 校验响应（MSW handler 里 `schema.parse(response)`），契约即代码；重量级用 Pact.js（PactV4 支持非 HTTP 队列）。
- 追问钩子：契约测试和集成测试的区别？——契约只验证「边界上的数据形状与语义」，不验证业务流程正确性，两者互补。

```javascript
// zod 契约：前端定义 + MSW 校验 + 后端 CI 重放三处共用
import { z } from 'zod';
export const GoodsListResp = z.object({
  list: z.array(z.object({ id: z.number(), name: z.string(), price: z.number() })),
  total: z.number(),
});

// MSW handler：mock 时就按契约出数据（防 mock 漂移）
http.get('/api/goods', () => {
  const mock = { list: [{ id: 1, name: 'x', price: 9.9 }], total: 1 };
  GoodsListResp.parse(mock);                 // 违反契约直接抛，测试失败
  return HttpResponse.json(mock);
});

// 业务代码消费处同样校验（运行时自愈 + 契约落地）
const resp = GoodsListResp.safeParse(await api.get('/api/goods'));
if (!resp.success) report.schemaViolation(resp.error);  // 上报监控
```
