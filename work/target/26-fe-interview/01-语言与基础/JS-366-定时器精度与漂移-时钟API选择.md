---
title: [JS-366] 定时器精度与漂移：时钟 API 选择
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-366：定时器精度与漂移：时钟 API 选择

**答**：
- setTimeout/setInterval 的真相：最小 4ms 聚合、嵌套 >5 层降到 ≥4ms、后台 tab 1s 节流、被冻结暂停——它们是「至少等这么久」，不是精确闹钟
- setInterval 漂移：回调执行耗时累积导致周期漂移（每次实际 >N ms）——精确周期用「自调度 setTimeout + 绝对时间对齐」；对齐到整秒的场景（倒计时）用 nextTick = nextSecondBoundary - now
- 时钟 API 分级：performance.now()（单调、高精度、不回拨——测量间隔唯一正解）、Date.now()（墙上时钟，会漂移/回拨——只用于展示与跨系统对齐）、performance.timeOrigin（与 Date 对齐的锚点）
- 跨端时间对齐：服务器时间校准（请求头 Date 或专门接口 + RTT 修正）——倒计时类业务必须服务端基准，本地时钟只做插值
- 后台恢复：visibilitychange resume 时按绝对时间重校准（H5/JS 通用模式），不清零进度

```javascript
// 精确秒级倒计时(不漂移)
function countdown(endAt, onTick) {
  const tick = () => {
    const left = Math.max(0, endAt - performance.now());
    onTick(Math.ceil(left / 1000));
    if (left > 0) {
      const nextBoundary = Math.ceil(left / 1000) * 1000;     // 对齐下一个整秒
      setTimeout(tick, Math.min(nextBoundary - (left % 1000), 1000));
    }
  };
  tick();
}
const endAt = performance.now() + serverRemaining * 1000;     // 服务端基准换算
```
