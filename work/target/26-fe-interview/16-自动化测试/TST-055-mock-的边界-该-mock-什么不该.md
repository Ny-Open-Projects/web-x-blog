---
title: [TST-055] 单测里该 mock 什么、不该 mock 什么？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-055：单测里该 mock 什么、不该 mock 什么？
**答**：
- 该 mock：进程外的东西——HTTP（axios/fetch）、浏览器存储、时间/随机、三方 SDK、文件系统、WebSocket。它们慢、不稳定、有真实副作用。
- 不该 mock：被测单元内部的东西——自己的工具函数、内部模块、store 计算逻辑。mock 它们等于把测试的「网」打穿，bug 会从洞里漏过去（测试全绿但功能坏）。
- 判断标准：「mock 掉它之后，这个测试还能不能发现真实集成会暴露的 bug」——mock 自己写的代码通常不能。
- 灰色地带：数据转换工具、格式化函数——如果你测的就是「用它的模块」，别 mock；工具本身有自己的测试文件。
- 追问钩子：mock 越多，测试越接近「复述实现」；MSW 这类「网络层 mock」之所以受推崇，就是因为 mock 边界推到了最外圈。

```javascript
// ❌ 反例：mock 自己的 utils —— 测试与实现强耦合
// vi.mock('./price-utils');   // calculateDiscount 被掏空，逻辑改动时测试仍绿

// ✅ 正例：只 mock 网络边界，内部逻辑真实执行
vi.mock('../api', () => ({ fetchPrice: vi.fn() }));   // 外部 HTTP，mock 合理
import { fetchPrice } from '../api';
import { getFinalPrice } from './price';              // 内部逻辑 + 自己的 utils 全真

it('用接口价减内部折扣计算最终价', async () => {
  vi.mocked(fetchPrice).mockResolvedValue(100);
  // getFinalPrice 内部调用真实的 calculateDiscount —— 逻辑 bug 会被这个测试抓住
  expect(await getFinalPrice({ vip: true })).toBe(90);
});
```
