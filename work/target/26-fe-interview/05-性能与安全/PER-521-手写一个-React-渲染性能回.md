---
title: [PER-521] 手写一个 React 渲染性能回归测试：mock 1000 条数据渲染列表组件，断言单次 commit 耗时不超预算
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-521：手写一个 React 渲染性能回归测试：mock 1000 条数据渲染列表组件，断言单次 commit 耗时不超预算

**答**：
- 技术点：`Profiler` 的 onRender 回调拿 `actualDuration`；在 jsdom 里测渲染时间是相对值，要配合多轮渲染取中位数降低噪声。
- 边界：jsdom 无真实布局，测不出 reflow 成本，所以断言阈值要宽松（如预算 ×1.5），真正的布局回归交给浏览器端跑分；首帧渲染含编译开销要丢弃预热轮。
- 评分点：预热轮丢弃与中位数聚合是否体现抗噪意识。

```javascript

import { render } from '@testing-library/react';
import { Profiler } from 'react';
import ProductList from './ProductList';

function measureOnce(rows) {
  return new Promise(resolve => {
    render(
      <Profiler id="list" onRender={(_, phase, duration) => {
        if (phase === 'mount') resolve(duration);
      }}>
        <ProductList rows={rows} />
      </Profiler>
    );
  });
}

test('ProductList 1000 行 mount 耗时不超预算', async () => {
  const rows = Array.from({ length: 1000 }, (_, i) => ({ id: i, name: `p${i}`, price: i % 99 }));
  const WARM = 2, RUNS = 5;
  for (let i = 0; i < WARM; i++) await measureOnce(rows);   // 预热轮丢弃
  const costs = [];
  for (let i = 0; i < RUNS; i++) costs.push(await measureOnce(rows));
  costs.sort((a, b) => a - b);
  const median = costs[costs.length >> 1];
  const BUDGET = 120;                                        // jsdom 相对值，阈值放宽
  expect(median).toBeLessThan(BUDGET);                       // 超预算 -> CI 红灯
});
```
