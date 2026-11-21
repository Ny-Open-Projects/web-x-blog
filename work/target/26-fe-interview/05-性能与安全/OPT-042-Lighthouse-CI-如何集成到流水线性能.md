---
title: [OPT-042] Lighthouse CI 如何集成到流水线？性能分数怎么正确解读？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-042：Lighthouse CI 如何集成到流水线？性能分数怎么正确解读？

**答**：
- 集成三步：PR 触发 `lhci autorun` → collect 阶段跑多次取稳定值 → assert 阶段按预算断言，失败阻断合并（卡口配置在 OPT-040，这里关注**分数解读**）。
- Lighthouse 性能分是加权综合分：FCP/TBT/LCP/CLS/SI/Speed Index 各有权重与对数曲线，**90+ 不是线性含义**——从 60 提到 80 和从 90 提到 95 难度差一个量级。
- 单项指标与总分要分开看：总分 95 但 TBT 超标，说明包体执行有问题；不要只盯总分绿灯。
- 实验室分数只用于回归对比（本分支 vs main），绝对值与真实用户无关，决策看 RUM。

```javascript
// 一一对应：用 Node API 跑 Lighthouse 并输出"总分 + 单项达标明细"的解读报告
import lighthouse from 'lighthouse';
import * as chromeLauncher from 'chrome-launcher';

async function audit(url) {
  const chrome = await chromeLauncher.launch({ chromeFlags: ['--headless'] });
  const { lhr } = await lighthouse(url, {
    port: chrome.port,
    formFactor: 'mobile',
    screenEmulation: { mobile: true, width: 412, height: 823, deviceScaleFactor: 1.75 },
  });
  await chrome.kill();

  const cats = lhr.categories.performance.score * 100;
  console.log(`性能总分: ${cats}（>90 绿 50-90 黄 <50 红，非线性刻度）`);
  // 单项解读：weight 越高对总分影响越大，TBT/LCP/CLS 是三大权重项
  const weights = { fcp: 10, si: 10, lcp: 25, tbt: 30, cls: 25 };
  for (const [id, w] of Object.entries(weights)) {
    const a = lhr.audits[id];
    console.log(
      `${id}: ${a.numericValue?.toFixed(0)}ms/分=${a.score} 权重=${w}% ` +
        (a.score < 0.9 ? ' <-- 优先治理，对总分拖累最大' : '达标')
    );
  }
}
audit('https://example.com');
```
