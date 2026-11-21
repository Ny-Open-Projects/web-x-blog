---
title: [TST-182] 灰度发布 / AB 实验下，自动化测试怎么做？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-182：灰度发布 / AB 实验下，自动化测试怎么做？
**答**：
- 核心难题：同一 URL 返回不同版本/不同实验组，E2E 的「页面长什么样」不再确定。解法是让测试**控制变量**：显式指定分流命中，而不是听天由命。
- 三种控制手段：① 请求头/cookie 强制命中（灰度网关认 `X-Gray-Tag: candidate` 或实验 cookie，route 统一注入）；② 测试账号白名单（实验配置里给 e2e- 前缀账号固定分组）；③ 本地/CI 环境关闭分流直达新版（feature flag 默认 on）。首选 ①，与环境解耦。
- 版本矩阵：门禁跑「旧版回归 + 新版回归」两组——新版必跑核心链路；旧版只需冒烟（确认没有连带破坏）。灰度期间每夜 E2E 同时覆盖两个版本直到放量结束。
- 实验本身的测试：实验 SDK 的分流确定性（同一 userId 每次命中同组）、实验配置下发后的 UI 生效（mock 实验接口返回不同配置断言 UI）、实验关闭回滚路径。
- RUM 联动：灰度监控指标（错误率/转化）与 E2E 结果一起作为放量门禁，E2E 只保证「功能没坏」，业务效果看数据。
- 追问钩子：怎么防「实验测试遗漏对照组」？——用例元数据标注适用版本（`@gray(candidate)`），CI 按当前灰度矩阵选择套件。

```javascript
// 统一注入灰度头：所有用例命中候选版本
test.beforeEach(async ({ request }) => {
  await extraHTTPHeaders({ 'X-Gray-Tag': 'candidate-v2' });  // playwright use.extraHTTPHeaders
});

test('V2 下单链路（灰度候选版）', async ({ page }) => {
  await page.goto('/checkout');
  await page.getByRole('button', { name: '提交订单' }).click();   // V2 新文案
  await expect(page.getByText('订单已创建')).toBeVisible();
});

// 实验 SDK 分流确定性测试
test('同一 userId 分流稳定', () => {
  const a = abClient.getGroup('exp-123', 'user-42');
  const b = abClient.getGroup('exp-123', 'user-42');
  expect(a).toBe(b);   // 分桶哈希确定性
});
```
