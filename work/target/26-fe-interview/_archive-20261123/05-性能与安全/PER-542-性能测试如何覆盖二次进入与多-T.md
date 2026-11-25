---
title: [PER-542] 性能测试如何覆盖二次进入与多 Tab 场景？这些场景有什么独特性能问题？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-542：性能测试如何覆盖二次进入与多 Tab 场景？这些场景有什么独特性能问题？

**答**：
- 二次进入的独特性：BFCache（前进后退缓存）命中时页面瞬间恢复，指标口径完全不同；SW 缓存命中的热加载；以及"回访但缓存过期"的半冷状态——三种状态要分别造场景。
- 多 Tab 的独特问题：共享的 localStorage/IndexedDB 争抢、BroadcastChannel 同步开销、每个 Tab 独立的 JS 堆内存叠加、Service Worker 成为跨 Tab 单点（SW 卡顿影响所有 Tab）。
- 测法：BFCache 用"导航走再返回"的脚本路径验证恢复时长与 `pagepersisted` 事件；多 Tab 用自动化开 5~10 个同站 Tab，观察总内存增长与 SW 崩溃率。
- 这些场景没有标准指标，要自定义口径（恢复时间、跨 Tab 同步延迟），进性能测试套件时标明"自定义指标"。

```javascript

// BFCache 恢复性能探针：记录从 pageshow 到首帧可交互的时长
let hideAt = 0;
addEventListener('pagehide', () => { hideAt = performance.now(); });
addEventListener('pageshow', (e) => {
  if (!e.persisted) return;                    // 非 BFCache 恢复不计
  const restoreStart = performance.now();
  requestAnimationFrame(() => requestAnimationFrame(() => {
    const restoreMs = performance.now() - restoreStart;
    navigator.sendBeacon('/perf/bfcache', JSON.stringify({
      persisted: true, awayMs: Math.round(restoreStart - hideAt),
      restoreMs: Math.round(restoreMs),        // 自定义口径：恢复可交互耗时
    }));
  }));
});
// 测试脚本：进入 -> 点外链 -> history.back() -> 断言 pageshow.persisted === true 且 restoreMs < 100
```
