---
title: [TST-013] describe / it 怎么组织才好维护？only / skip / todo 怎么用？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-013：describe / it 怎么组织才好维护？only / skip / todo 怎么用？
**答**：
- 结构原则：describe 描述「被测单元/场景」，it 描述「一条可断言的行为」，it 名字用完整句子（“未登录时跳转登录页”），不看代码也知道测什么。
- 嵌套：按场景分 describe（成功/失败/边界），不要一层套五层；重复的前置尽量上提到 beforeEach 而不是复制粘贴。
- only/skip：`it.only` 本地调试只跑某条；`describe.skip` 整块跳过；`it.todo` 记录待写用例（会出现在报告里当清单）。
- 风险：`.only` 提交进仓库会导致 CI 静默漏测——用 `vitest --allowOnly=false`（CI 默认拒绝 only）兜底。
- 追问钩子：测试名即文档，rename 被测函数时用 IDE 重构同步测试里的 describe 标题。

```javascript
describe('购物车 checkout', () => {
  describe('库存充足', () => {
    it('扣减库存并生成待支付订单', async () => { /* ... */ });
  });
  describe('库存不足', () => {
    it('抛出 OUT_OF_STOCK 且不创建订单', async () => { /* ... */ });
  });
  describe.skip('优惠券叠加（规则待定）', () => {
    it.todo('满减与折扣的叠加顺序');
  });
});
// CI 配置：vitest run --allowOnly=false，防止 only 漏测
```
