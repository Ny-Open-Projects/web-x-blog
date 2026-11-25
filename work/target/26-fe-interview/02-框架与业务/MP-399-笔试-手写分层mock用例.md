---
title: [MP-399] 笔试：手写分层 mock 的完整测试用例
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 测试]
type: 笔试题
---

## MP-399：笔试：手写分层 mock 用例

**答**：为「下单流程」编写分层测试：① 逻辑层单测（状态机：库存校验/价格计算——纯函数无 wx 依赖）；② 组件测试（simulate：下单按钮 disabled 逻辑/错误提示渲染——wx.request mock）；③ 集成测试（automator：真机完整链路——mock 支付返回）；④ 每层 mock 粒度说明（逻辑层无 mock/组件层 mock 网络/集成层 mock 支付 SDK）；⑤ 失败注入测试（库存不足/支付超时/回调丢失的用例设计）。写出实现。

```javascript
// L1: 逻辑层纯单测(无 mock)
import { calcPrice, validateStock } from '../../core/order';
it('价格计算: 满 200 减 30', () => {
  expect(calcPrice([{ price: 150 }, { price: 60 }])).toBe(180);
});
it('库存不足抛业务错误', () => {
  expect(() => validateStock([{ sku: 'a', stock: 0 }])).toThrow('OUT_OF_STOCK');
});

// L2: 组件测试(只 mock 网络)
import { createWxMock } from './wx-mock';
it('下单按钮: 库存校验失败禁用', async () => {
  const wx = createWxMock();
  wx.requestWhen('/api/stock').reply(200, { stock: 0 });
  const comp = simulate.render(simulate.load('/pages/order/index'));
  await simulate.sleep(50);
  expect(comp.querySelector('.submit').dom.disabled).toBe(true);
  expect(comp.dom.textContent).toContain('库存不足');
});

// L3: 集成(automator, mock 支付)
it('完整下单 → mock 支付回调', async () => {
  const mp = await automator.connect({ wsEndpoint });
  const page = await mp.reLaunch('/pages/order/index?sku=a');
  await mp.mockWxMethod('requestPayment', { errMsg: 'requestPayment:ok' });   // mock 支付(必须先于点击)
  await (await page.$('.submit')).tap();
  await page.waitFor(1000);
  expect((await page.$('.pay-success'))).toBeTruthy();
});
// 失败注入: mock 回调丢失(超时不回) → 断言「处理中」态 + 查单轮询触发
```

**评分点**：
- 三层分工清晰（逻辑无 mock/组件 mock 网络/集成 mock SDK）
- 失败注入设计（库存不足/支付超时/回调丢失）
- mock 粒度与被测职责对齐（不重复测基础设施）
- simulate/automator 的能力边界认知

## 变体与延伸（补充）

**变体与延伸**：

1. 为什么逻辑层要坚持零 mock？ → 纯函数不依赖平台，mock 只会掩盖真实分支；一旦为了测试必须 mock 计算过程，说明业务逻辑和 wx API 耦合了，应该先重构再测。
2. 集成层 mock 了支付 SDK，回调丢失怎么模拟？ → 让 mockWxMethod 返回永不 resolve 的 promise 或延迟到超时，断言"处理中"态与查单轮询被触发，而不是断言成功页出现。
3. simulate 与 automator 的边界怎么讲？ → simulate 跑在 Node 里、没有真实渲染层，适合逻辑与结构断言；automator 连真机或开发者工具，能覆盖双线程与原生能力，但慢且不稳，只放关键链路。
