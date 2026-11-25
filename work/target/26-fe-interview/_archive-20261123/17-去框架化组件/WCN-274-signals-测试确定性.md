---
title: [WCN-274] 信号应用的确定性测试策略（同步 flush/时间冻结）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-274：信号应用的确定性测试策略（同步 flush/时间冻结）。
**答**：
- 测试模式：同步调度器 + 显式 flushNow() —— 写完断言，无微任务等待。
- 异步派生测试：mock fetch + 受控 resolve（手动推进）。
- 时序断言：effect 执行顺序记录器（flush 内顺序数组断言）。
- 反模式：测试里 sleep 等待 flush——必须用库提供的 flush 钩子。

```javascript
configureScheduler({ schedule: f => f() });   // 同步
test('加购更新合计', () => {
  items.value = [{ price: 10 }];
  expect(total.value).toBe(10);               // 无需 await
  expect(effectLog).toEqual(['render-total']); // 顺序确定
});
r
```
