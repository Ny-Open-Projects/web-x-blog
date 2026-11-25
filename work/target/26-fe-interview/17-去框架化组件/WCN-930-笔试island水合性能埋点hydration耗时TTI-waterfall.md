---
title: [WCN-930] 手写 island 水合性能埋点：记录每岛 hydration 耗时与 TTI 贡献输出 waterfall
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-930：手写 island 水合性能埋点：记录每岛 hydration 耗时与 TTI 贡献输出 waterfall

**题目**：实现 `createHydrationProfiler()`，返回 `{ begin(id), end(id), getWaterfall(), summary() }`。要求：① begin(id) 记录开始时间戳（注入的 now 函数，默认 Date.now）；② end(id) 记录结束并计算 duration，未 begin 的 id 直接忽略；③ getWaterfall() 返回按开始时间排序的 `[{ id, start, end, duration }]`；④ summary() 返回 `{ total, max, maxId, avg, count }`（total 为各岛 duration 之和，avg 为均值，count 为岛数，空数据返回全 0）；⑤ 同一 id 重复 begin 覆盖上次记录，end 只认最后一次 begin；⑥ 时间与性能 API 必须注入便于测试。请自足实现并给出可运行示例。

**答**：

```javascript
function createHydrationProfiler(now = () => Date.now()) {
  const records = new Map();
  return {
    begin(id) { records.set(id, { id, start: now(), end: null, duration: null }); },
    end(id) {
      const r = records.get(id);
      if (!r || r.end !== null) return;      // 未 begin 或已 end 忽略
      r.end = now();
      r.duration = r.end - r.start;
    },
    getWaterfall() {
      return [...records.values()].filter(r => r.duration != null)
        .sort((a, b) => a.start - b.start);
    },
    summary() {
      const done = [...records.values()].filter(r => r.duration != null);
      if (!done.length) return { total: 0, max: 0, maxId: null, avg: 0, count: 0 };
      const total = done.reduce((s, r) => s + r.duration, 0);
      const max = Math.max(...done.map(r => r.duration));
      const maxId = done.find(r => r.duration === max).id;
      return { total, max, maxId, avg: +(total / done.length).toFixed(2), count: done.length };
    },
  };
}
let t = 0;
const p = createHydrationProfiler(() => t);
p.begin('nav'); t = 5; p.end('nav');       // 5ms
p.begin('buy'); t = 10; p.end('buy');      // 5ms
p.begin('cart'); t = 25; p.end('cart');    // 15ms
console.log(p.getWaterfall().map(x => x.id)); // ['nav','buy','cart']
console.log(p.summary()); // { total:25, max:15, maxId:'cart', avg:8.33, count:3 }
```

**评分点**：
- begin/end 配对记录 duration，未 begin 的 end 被忽略。
- getWaterfall 按开始时间排序、过滤未完成项。
- summary 的 total/max/maxId/avg/count 计算正确，空数据返回全 0。
- 重复 begin 覆盖、end 只认最后一次（幂等健壮性）。
- now 注入便于测试，示例输出正确可运行。
