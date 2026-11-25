---
title: [PER-1018] 手写一个渲染内存预算守卫：监控 detached 节点并告警
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1018：手写一个渲染内存预算守卫：监控 detached 节点并告警

**答**：
- 需求：实现 memoryGuard(opts)。每 5s 采样：performance.memory（若有）取 usedJSHeapSize 增速；用 MutationObserver 记录被移除但被闭包引用无法直接检测的节点——简化为：统计 document 节点总数趋势（连续 3 次增长 > 10% 判泄漏嫌疑）；超 JS 堆阈值（默认 500MB）触发回调。
- 边界：无 performance.memory 的浏览器只做节点趋势检测；回调同一事件 5 分钟内只触发一次；stop() 清理定时器。
- 评分点：双通道检测（堆+节点）；连续增长判定；告警去抖；stop

```javascript
function memoryGuard({ heapMaxMB = 500, onAlert } = {}) {
  let lastNodes = 0, growth = 0, lastAlert = 0;
  const timer = setInterval(() => {
    const now = document.querySelectorAll('*').length;
    if (lastNodes && now > lastNodes * 1.1) growth++; else growth = 0;
    lastNodes = now;
    const mem = performance.memory;
    const heapMB = mem ? mem.usedJSHeapSize / 1024 / 1024 : null;
    const leakSuspect = growth >= 3;
    if ((heapMB && heapMB > heapMaxMB) || leakSuspect) {
      const now = Date.now();
      if (now - lastAlert > 5 * 60_000) {        // 5 分钟去抖
        lastAlert = now;
        onAlert({ heapMB, nodes: now, leakSuspect,
          advice: leakSuspect ? 'DOM 持续增长，排查路由残留' : 'JS 堆超预算' });
      }
    }
  }, 5000);
  return { stop: () => clearInterval(timer) };
}
```
