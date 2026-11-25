---
title: [NODE-495] Node 服务的 BFF 层测试策略（编排逻辑如何测）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-495：BFF 层测试策略
**答**:
- BFF 测试重心：编排正确性（并行调用/依赖顺序/超时降级）+ 协议正确性（字段映射/profile 装配）+ 容错正确性（下游各种挂法的表现）——不是业务逻辑（业务在下游）。
- 测试分层：契约 stub 层（下游按契约 mock NODE-334——BFF 测试不依赖真实下游）、编排单测（聚合函数直接测：并行/降级/裁剪逻辑纯函数化——可测性的关键）、集成冒烟（真实下游 test 环境——端到端字段验证）。
- 容错矩阵测试：下游超时/500/慢响应/部分失败 × 接口（关键/非关键依赖）→ 断言降级行为（NODE-490 降级声明的每条都要有用例——声明与测试配对）。
- profile 一致性：多端装配断言（同数据各 profile 字段集正确 + 语义一致 NODE-494）。
- 稳定性测试：下游故障注入下的 BFF 表现（NODE-479 演练：熔断/降级/恢复全链路）。
```javascript
// 编排单测（纯函数化）
test('homePageAgg：非关键下游失败走兜底', async () => {
  const stub = stubDownstream({ marketing: timeout(3000), goods: ok(goodsData) });
  const r = await homePageAgg(stub);
  expect(r.goods).toEqual(goodsData);                            // 关键正常
  expect(r.marketing).toEqual(DEFAULT_BANNERS);                  // 非关键降级
  expect(r.marketing.degraded).toBe(true);
});
// 容错矩阵：{timeout, 500, slow} × {critical, edge} 全组合用例生成
```
