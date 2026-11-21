---
title: [TST-207] 如何控制 Playwright 用例的执行顺序与依赖关系？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-207：如何控制 Playwright 用例的执行顺序与依赖关系？
**答**：
- 文件内按声明顺序执行，worker 内串行；fullyParallel 时顺序不保证——依赖顺序的用例要显式串行。
- 依赖流程用 test.describe.serial 声明（如先登录后下单），失败即跳过后续。
- 跨文件顺序靠文件名字典序或分组到单文件——更推荐拆解依赖而非排序 hack。
- 全局前置（登录/种子数据）放 globalSetup / project.dependencies。

```javascript
test.describe.serial('下单主流程', () => {
  let orderId: string;
  test('加购', async ({ page }) => { /* ... */ });
  test('结算', async ({ page }) => { /* 依赖加购结果 */ });
  test('支付', async ({ page }) => { /* 依赖结算 */ });
});
r
```
