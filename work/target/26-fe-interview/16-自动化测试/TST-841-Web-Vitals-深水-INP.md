---
title: [TST-841] Web Vitals 深水：INP 为什么比 FID 难测？如何在 CI 里稳定采集 INP？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-841：Web Vitals 深水：INP 为什么比 FID 难测？如何在 CI 里稳定采集 INP？
**答**：
- 结论：FID 只量首次输入延迟，INP 量的是整个页面生命周期内最差的一次交互响应，受多次交互、长任务累积影响，所以更难稳定采集。
- 难点：INP 依赖真实用户交互路径，CI 里需用脚本模拟完整交互序列（点击/输入/滚动），并取 p75 而非单次值。
- 采集方案：用 web-vitals 库的 onINP + Playwright 跑真实交互脚本，多轮取分位数；实验室数据(Lighthouse TBT)只能作代理。
- 稳定性：固定设备型号/CPU 节流/网络条件，关闭无关后台任务，多次运行取中位数以对抗抖动。
- 追问钩子：实验室 INP 达标但线上 RUM 的 INP 超标，可能是什么原因？（提示：真实用户设备更差、交互路径更杂）

```javascript
// CI 中采集 INP：模拟真实交互 + 多轮取 p75
import { onINP } from 'web-vitals';
async function measureINP(page, interactions) {
  const samples = [];
  await page.evaluateOnNewDocument(() => {
    window.__inps = [];
    // 真实项目中用 onINP 收集并 push 到 __inps
  });
  for (let round = 0; round < 5; round++) {
    await page.reload();
    for (const act of interactions) await act(page); // 点击/输入/滚动
    samples.push(await page.evaluate(() => Math.max(0, ...window.__inps)));
  }
  samples.sort((a, b) => a - b);
  return { p75: samples[Math.floor(samples.length * 0.75)], samples };
}
onINP(m => console.log('RUM INP:', m.value));
```
