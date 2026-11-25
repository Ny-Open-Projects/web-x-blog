---
title: [TST-641] 前端交互响应性能（INP）怎么做自动化回归？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-641：前端交互响应性能（INP）怎么做自动化回归？

**答**：
- 结论：INP 靠真实用户交互采样，不能只用实验室工具——用 PerformanceObserver 采集 long-animation-frame 与 event timing。
- 回归策略：固定交互脚本（点击/输入/滚动）跑 N 次，取 P75 与阈值比较；记录元素与阶段便于定位。
- CI 中用受控设备档位（4x CPU 降速）消除机器差异。
- 追问钩子：INP 在 CI 波动很大，你怎么区分「真回归」和「机器抖动」？

```javascript
function observeINP(cb) {
  let worst = 0;
  try {
    const po = new PerformanceObserver(list => {
      for (const e of list.getEntries()) {
        if (e.duration > worst) worst = e.duration;
      }
    });
    po.observe({ type: 'event', buffered: true });
  } catch (_) { /* 浏览器不支持 */ }
  return () => cb({ inpP75: worst, pass: worst < 200 });
}
// 测试脚本：模拟点击后读取 INP
setTimeout(observeINP(r => console.log(r)), 1000);
```
