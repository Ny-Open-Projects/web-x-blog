---
title: [HW-159] 手写 RUM 采集的降级链——新 API 不可用时的逐级 fallback（LoAF→longtask→估算）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-159：手写 RUM 采集的降级链——新 API 不可用时的逐级 fallback（LoAF→longtask→估算）
**答**：RUM 采集在旧浏览器的降级链：每个指标声明"主 API → 备用 API → 估算/跳过"三级——INP：Event Timing → 无则记 0 并标 degraded；LoAF：long-animation-frame → longtask（有任务时长无脚本归因）→ 无则跳过；CLS：layout-shift 全支持；采样标记 degraded 字段（看板按 degraded 分桶——降级数据单独看不做 SLO 判定）。

```javascript
const capability = {
  loaf: PerformanceObserver.supportedEntryTypes?.includes('long-animation-frame'),
  event: PerformanceObserver.supportedEntryTypes?.includes('event'),
  memory: !!performance.memory,
};
function trackWithFallback() {
  if (capability.loaf) {
    observeLoAF();                                        // 全量归因
  } else if ('PerformanceObserver' in window && capability.event) {
    observeLongtask();                                    // 降级：只有时长无归因
    markDegraded('loaf', 'longtask-fallback');
  } else {
    markDegraded('loaf', 'unavailable');                  // 跳过 + 标记
  }
}
function markDegraded(metric, mode) {
  report({ type: 'capability', metric, mode, ua: navShort() });   // 能力上报：看板按降级分桶
}
// 看板纪律：degraded 样本进"参考桶"不进 SLO 分母（口径不一致的数据混算 = 假达标率）
// 能力上报的价值：按浏览器版本看 degraded 占比 → 决定何时可以下线降级路径
```

**评分点**：
- 三级 fallback（主 API → 备用 → 跳过+标记）逐级语义清晰。
- degraded 字段标记与"降级样本不进 SLO 分母"的口径纪律——本题核心。
- capability 上报（按版本看降级占比，决定降级路径退役时机）。
- PerformanceObserver.supportedEntryTypes 的特性检测方式。
