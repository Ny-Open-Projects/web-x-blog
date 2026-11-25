---
title: [TST-909] toBeVisible / 轮询等待类断言超时，报错怎样写才能区分「没出现」和「出现又被移除」？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-909：toBeVisible / 轮询等待类断言超时，报错怎样写才能区分「没出现」和「出现又被移除」？
**答**：
- 结论：等待类断言要记录「等待期间元素的状态轨迹」，超时报错附上最后 3 次观察到的状态变化，而不是只报 Timeout。
- 做法：轮询时记录每次观察的时间戳与可见性，超时时输出「一直不可见 / 曾可见后被移除 / 一直抖动」三类诊断。
- 注意：区分「元素不存在」与「存在但 hidden/display:none」——报错要点明 selector 命中数量。
- 追问钩子：大促秒杀按钮先禁用再启用，测试在启用瞬间点击仍报超时，轨迹信息如何帮你判断是等待策略问题还是前端 bug？

```javascript
async function waitVisible(page, selector, timeout = 5000) {
  const trace = [];
  const start = Date.now();
  while (Date.now() - start < timeout) {
    const loc = page.locator(selector);
    const count = await loc.count();
    const state = count === 0 ? 'absent' : (await loc.isVisible()) ? 'visible' : 'hidden';
    trace.push({ t: Date.now() - start, state, count });
    if (state === 'visible') return true;
    await page.waitForTimeout(100);
  }
  const last = trace.slice(-3).map(x => `${x.t}ms:${x.state}(${x.count})`).join(' ');
  throw new Error(`等待可见超时 | selector=${selector} | 轨迹=${last}`);
}
// 报错形如：轨迹=4700ms:hidden(1) 4800ms:visible(1) 4900ms:absent(0) → 曾可见后被移除
```
