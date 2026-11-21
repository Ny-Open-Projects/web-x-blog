---
title: [HW-057] 手写 IntersectionObserver 曝光统计
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-057：手写 IntersectionObserver 曝光统计

**答**：
- 评分点：曝光定义要说清——元素进入视口且达到 `threshold`（如 0.5 表示可见面积过半）记一次曝光；`isIntersecting` 判定后立即 `unobserve`（**单次曝光去重**，同一元素不重复上报）；停留在视口的**时长**统计（要求 ≥ N ms 才算有效曝光）：进入时 setTimeout，离开/到期时结算——这是加分实现；`rootMargin` 扩大判定范围、批量 observe 复用同一个 observer 实例（性能）；上报要批量合并（queueMicrotask / 定时 flush）减少请求数。

```javascript
// ===== 5 分钟速写版 =====
function trackExposure(selector, report) {
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        report(en.target.dataset.trackId); // 上报埋点位
        io.unobserve(en.target);           // 单次曝光：去重
      }
    });
  }, { threshold: 0.5 });
  document.querySelectorAll(selector).forEach(el => io.observe(el));
  return io;
}

// ===== 标准完整版（含边界处理）=====
function trackExposurePro(selector, report, {
  threshold = 0.5, minDuration = 500, batchSize = 10, flushInterval = 3000
} = {}) {
  if (typeof report !== 'function') throw new TypeError('report must be a function');
  const reported = new WeakSet();       // 永久去重：页面刷新前只报一次
  const pending = [];                   // 待上报队列：批量合并
  const timers = new WeakMap();         // 停留时长计时
  let flushTimer = null;
  const flush = () => {
    flushTimer = null;
    if (pending.length === 0) return;
    const batch = pending.splice(0, pending.length);
    report(batch);                      // 一次请求上报一批
  };
  const queue = item => {
    pending.push(item);
    if (pending.length >= batchSize) flush();
    else if (!flushTimer) flushTimer = setTimeout(flush, flushInterval);
  };
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      const el = en.target;
      if (en.isIntersecting) {
        // 满足可见比例：起计时器，满 minDuration 才算有效曝光
        timers.set(el, setTimeout(() => {
          if (reported.has(el)) return;
          reported.add(el);
          queue({ id: el.dataset.trackId, duration: minDuration, ts: Date.now() });
          io.unobserve(el);           // 单次曝光后停止观察
          timers.delete(el);
        }, minDuration));
      } else {
        // 提前离开视口：未满时长不计曝光，清计时器
        if (timers.has(el)) { clearTimeout(timers.get(el)); timers.delete(el); }
      }
    });
  }, { threshold, rootMargin: '0px' });
  const observeAll = () => document.querySelectorAll(selector).forEach(el => {
    if (!reported.has(el)) io.observe(el);
  });
  observeAll();
  return {
    refresh: observeAll,                // 动态渲染的元素手动补观察
    disconnect() {
      io.disconnect();
      if (flushTimer) clearTimeout(flushTimer);
      flush();                          // 页面卸载前兜底上报
    }
  };
}
// 追问：为什么不用 scroll + getBoundingClientRect —— 每帧计算布局，主线程压力大；
// IO 由浏览器异步计算，不阻塞主线程。页面卸载兜底：visibilitychange / pagehide 里 flush。
```

---
