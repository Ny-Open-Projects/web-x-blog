---
title: [PER-532] SPA 路由切换性能怎么测？首开指标测不出切页卡的问题如何解决？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-532：SPA 路由切换性能怎么测？首开指标测不出切页卡的问题如何解决？

**答**：
- 首开指标（LCP/FCP）只在导航级触发，SPA 内部路由切换是 history pushState 不产生新的 performance entry，所以"切页卡"完全在传统指标盲区里。
- 测法三层：应用层埋点（路由 hook 里手动打 `performance.mark`，起点 routeChange、终点数据渲染完成 `measure` 出耗时）、交互指标复用（切页过程本质是交互，用 INP 思路统计切页最长任务）、切页探针（渲染完成后检查 frame gap）。
- 要定义"切换完成"口径：路由变了不算完，数据接口返回且列表渲染出来才算，口径不统一会各说各话。
- 优化目标参考：切页 p75 < 1s（含接口），切页过程 TBT < 200ms；每次切页要取消上一次未完成请求，否则慢接口会拖垮下一次切页。

```javascript

// 路由级计时：mark 起点 -> 数据渲染完成 mark 终点 -> measure
let markStart;
function onRouteChange(to) {
  performance.mark(`route:${to}:start`);
  markStart = performance.now();
}
function onDataRendered(to) {
  performance.mark(`route:${to}:end`);
  performance.measure(`route:${to}`, `route:${to}:start`, `route:${to}:end`);
  const [m] = performance.getEntriesByName(`route:${to}`).slice(-1);
  navigator.sendBeacon?.('/perf/route', JSON.stringify({
    to, ms: Math.round(m.duration), ts: markStart,      // p75 目标 < 1000ms
  }));
  performance.clearMeasures(`route:${to}`);
}
// 配合 CDP 节流在测试里断言：Fast 3G 下 /list -> /detail 切页 p75 不超预算
```
