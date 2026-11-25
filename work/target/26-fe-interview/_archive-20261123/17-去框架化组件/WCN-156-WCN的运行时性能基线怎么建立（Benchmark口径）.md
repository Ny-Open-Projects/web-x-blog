---
title: [WCN-156] WCN 的运行时性能基线怎么建立？Benchmark 口径与框架组件怎么公平对比？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-156：WCN 的运行时性能基线怎么建立？Benchmark 口径怎么定？

**答**：
- 场景基线四件套：① 首次 define + mount（1/100/1000 实例）；② 属性高频更新（60fps 写 attribute/property，测帧率与 long task）；③ 列表插入/删除（keyed 场景）；④ 内存（1000 实例创建销毁循环，heap 增长）。
- 公平性口径：同一页面同一批数据、同一交互序列脚本化驱动（Playwright/Puppeteer 控制输入）；对比对象 = 同功能的框架组件版本；运行 10 次取中位数 + 报告标准差。
- 指标：Long Tasks 数、INP 模拟值、总脚本时间、forced reflow 计数、heap 增长；浏览器固定版本与 profile。
- 常见结论：WCN 细粒度更新（Signals 绑定）在大列表高频更新优于 VDOM 重渲染；但 WC 首次 define 有解析开销（千实例级更明显），用静态模板缓存缓解。
- 持续化：benchmark 进 CI 每日跑，看板出趋势，回归 >10% 告警。

```javascript
// Playwright 驱动的基准口径示例
test('1000 实例属性高频更新', async ({ page }) => {
  await page.goto('/bench?count=1000');
  const measure = await page.evaluate(async () => {
    const els = [...document.querySelectorAll('x-row')];
    performance.mark('start');
    for (let i = 0; i < 60; i++) {          // 60 帧模拟 1 秒
      els.forEach((el, j) => { el.value = i * 1000 + j; });
      await new Promise((r) => requestAnimationFrame(r));
    }
    performance.mark('end');
    const m = performance.measure('update', 'start', 'end');
    return { ms: m.duration, longTasks: performance.getEntriesByType('longtask').length };
  });
  expect(measure.longTasks).toBeLessThan(3);   // 基线阈值
});
```
