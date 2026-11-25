---
title: [NODE-463] Node 服务集成测试的数据管理（种子/隔离/清理）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-463：集成测试数据管理
**答**:
- 数据三来源：种子数据（版本化 seed 脚本：基础字典/测试账号/边缘 case 数据——与迁移同跑，保证 schema 演进后 seed 仍有效）、工厂模式（用例内按需构造：factory 生成器带默认值可覆盖）、生产脱敏子集（边缘 case 丰富但脱敏合规 NODE-396）。
- 隔离策略：每用例事务回滚（快但复杂关联有限制）、每用例独立 schema（PG schema per test——完全隔离并行安全）、用例内清理（标记删除 + afterEach 清表）——按需选择，并行优先选独立 schema。
- 清理纪律：测试数据可识别（统一前缀/专用测试库，禁止混入共享环境）、CI 每次全新库（容器化 DB testcontainers，NODE-333）防累积污染。
- 确定性：时间固定（clock 注入）、ID 固定序列（防快照测试抖动）、外部响应固定（契约 mock NODE-334）。
- 数据特征还原：性能测试的数据量级要贴近真实（索引效果在空库上测不出来——种子生成百万行用例）。
```javascript
// 工厂 + 隔离
const userFactory = defineFactory('user', { name: 'test-user', role: 'member' });
test('下单流程', async ({ pgSchema }) => {                        // 独立 schema 隔离
  const u = await userFactory.create({ role: 'vip' });           // 覆盖默认值
  const o = await orderFactory.create({ userId: u.id, amount: 10000 });
  await expect(createPay(o)).resolves.toMatchObject({ status: 'paying' });
});                                                              // 结束 schema 即弃
```
