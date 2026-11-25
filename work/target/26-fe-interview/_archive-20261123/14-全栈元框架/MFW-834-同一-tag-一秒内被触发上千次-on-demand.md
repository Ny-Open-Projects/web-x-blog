---
title: [MFW-834] 同一 tag 一秒内被触发上千次 on-demand revalidate 怎么合并去抖
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-834：同一 tag 一秒内被触发上千次 on-demand revalidate 怎么合并去抖

**答**：
- 结论：高频 revalidate 会击穿缓存、放大回源；按 tag 维度做时间窗口合并：窗口内同一 tag 的多次触发合并为一次，窗口结束时统一失效。
- 落地：维护 tag→pending 定时器，首次触发启动窗口，后续重置计时或忽略，到期执行一次 revalidateTag。
- 追问钩子：窗口大小怎么定？——按业务容忍的陈旧度，通常 100ms~1s；强时效场景不合并。

```javascript
const pending = new Map();
function debouncedRevalidate(tag, fn, windowMs = 300) {
  if (pending.has(tag)) clearTimeout(pending.get(tag));
  const timer = setTimeout(() => {
    pending.delete(tag);
    fn(tag);                                       // 窗口内多次 → 一次
  }, windowMs);
  pending.set(tag, timer);
}

// 模拟：商品更新风暴
let calls = 0;
for (let i = 0; i < 1000; i++) debouncedRevalidate('product-1', () => calls++);
setTimeout(() => console.log(calls), 400);         // 1 —— 合并为一次失效
```
