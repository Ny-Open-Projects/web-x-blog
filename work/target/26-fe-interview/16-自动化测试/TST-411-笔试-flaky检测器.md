---
title: [TST-411] 笔试：实现 flaky 用例检测（N 次重跑统计）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-411：笔试：实现 flaky 用例检测（N 次重跑统计）。
**答**：输入每用例 N 次运行结果。flaky = 通过率在 (0,1) 开区间（既不全过也不全挂）。输出 flaky 清单与通过率；连续失败（全挂）标记 broken 区分。

```javascript
function detectFlaky(runs) {
  return runs.map(r => {
    const rate = r.results.filter(Boolean).length / r.results.length;
    return { name: r.name, rate: +rate.toFixed(2),
      kind: rate === 1 ? 'stable-pass' : rate === 0 ? 'broken' : 'flaky' };
  }).sort((a, b) => Math.abs(a.rate - 0.5) - Math.abs(b.rate - 0.5));
}
console.log(detectFlaky([
  { name: 'a', results: [1, 1, 1, 1, 1] },
  { name: 'b', results: [1, 0, 1, 0, 0] },
  { name: 'c', results: [0, 0, 0, 0, 0] },
])); // b（flaky 0.4）排最前

```

**评分点**：
- 三分类：stable-pass/stable-fail/flaky。
- 通过率保留 2 位。
- flaky 判定严谨（0<rate<1）。
- 输出按通过率排序（接近 0.5 的最优先治理）。
