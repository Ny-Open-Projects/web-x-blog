---
title: [PER-1007] 手写一个布局抖动检测器：Hook 读写序列定位抖动行
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1007：手写一个布局抖动检测器：Hook 读写序列定位抖动行

**答**：
- 需求：实现 installThrashDetector()。Hook Element.prototype 的读方法（getBoundingClientRect/offsetWidth/clientWidth 等）与写方法（style setter 简化为 setStyle）记录调用序列；窗口 > 50ms 内出现"读-写"交替 >= 3 轮判定抖动，回调 { start, reads, writes, duration }。返回卸载函数。
- 边界：同一元素连续多次读算一轮；嵌套调用按时间戳判定而非调用栈；重复抖动去抖（同窗口只报一次）。
- 评分点：Hook 设计；交替轮数判定；去抖；卸载清理

```javascript
function installThrashDetector(onThrash, { windowMs = 50, rounds = 3 } = {}) {
  const seq = []; let reported = 0;
  const READS = ['getBoundingClientRect', 'offsetWidth', 'clientWidth'];
  READS.forEach(m => {
    const orig = Element.prototype[m];
    Element.prototype[m] = function (...a) {
      seq.push({ t: performance.now(), kind: 'read', el: this });
      return orig.apply(this, a);
    };
  });
  const origSet = CSSStyleDeclaration.prototype.setProperty;
  CSSStyleDeclaration.prototype.setProperty = function (k, v, p) {
    seq.push({ t: performance.now(), kind: 'write' });
    return origSet.call(this, k, v, p);
  };
  const timer = setInterval(() => {
    const now = performance.now();
    const win = seq.filter(e => now - e.t <= windowMs);
    let alt = 0;
    for (let i = 1; i < win.length; i++)
      if (win[i].kind !== win[i - 1].kind) alt++;
    if (alt >= rounds && now - reported > windowMs) {
      reported = now;
      onThrash({ start: win[0].t, reads: win.filter(e => e.kind === 'read').length,
        writes: win.filter(e => e.kind === 'write').length, duration: windowMs });
    }
  }, windowMs);
  return () => clearInterval(timer);
}
```
