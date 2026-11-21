---
title: [PER-231] FCP 不等于业务首屏，自定义"业务首屏可交互指标"应该怎么定义？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-231：FCP 不等于业务首屏，自定义"业务首屏可交互指标"应该怎么定义？

**答**：
- FCP 的局限：任何文本/图形渲染都算"内容"，骨架屏也会算 FCP——用户看到的可能还是加载态；它也不含可交互性（白屏画完但 JS 没执行完，点不了按钮）。
- 业务首屏定义三要素：① 时机——关键业务内容真实渲染完成（如商品图 + 标题 + 价格 DOM 完成首次 paint）；② 可交互——绑定核心操作的 handler 已注册且主线程空闲（可响应首次点击）；③ 稳定——之后 1s 内不再被替换/遮挡（排除骨架屏→真内容二次渲染）。
- 实现路径：业务代码在首屏组件 useEffect/挂载后打 `performance.mark('bizReady')`，配合 Longtask 观察到主线程空闲后取 mark 时间；或直接用 LCP（元素限定首屏区域）+ 首次 handler 可用时间的组合。
- 验收口径：按 p75 看数、按页面路由分组、与竞品同口径对比；指标定义要写进团队文档避免每次争论。

```javascript
// 业务首屏可交互：mark（内容就绪）+ 主线程空闲（可交互）的取大者
function bizReady() {
  performance.mark('biz-content');
}
async function firstInteractive() {
  await waitForIdle(500);                              // 等待主线程连续 500ms 无长任务
  const mark = performance.getEntriesByName('biz-content')[0];
  const idleTime = performance.now() - 500;
  return Math.max(mark?.startTime ?? 0, idleTime);     // 两者取大 = 真正可用时刻
}
function waitForIdle(quietMs, timeout = 8000) {        // 长任务安静期检测
  return new Promise((resolve) => {
    let last = performance.now(), timer;
    const done = () => { clearTimeout(outer); observer.disconnect(); resolve(); };
    const outer = setTimeout(() => { observer.disconnect(); resolve(); }, timeout);
    const observer = new PerformanceObserver((l) => { last = performance.now(); });
    observer.observe({ type: 'longtask', buffered: false });
    (function check() { if (performance.now() - last >= quietMs) return done();
      timer = setTimeout(check, 100); })();
  });
}
```
