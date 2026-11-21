---
title: [TST-052] 笔试：手写「顺序依赖检测」runner（随机顺序多次执行）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-052：笔试：手写「顺序依赖检测」runner（随机顺序多次执行）
**答**：
- 需求：同一个用例列表以不同随机顺序跑 N 轮，任何一轮出现「单独跑通过、混序失败」的组合即判定存在顺序依赖，输出最小失败组合辅助定位。
- 核心：Fisher-Yates 洗牌；每轮记录通过集合；对比首轮基线，diff 出「基线过、本轮挂」的用例即为顺序受害者；再逐个单独跑验证。
- 边界：随机种子固定（可复现）；N 轮取 5~10；共享状态污染常常是全局单例/mock 未 reset——报告里要给出嫌疑提示。

```javascript
function shuffle(arr, rng = Math.random) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

async function detectOrderDependence(cases, rounds = 5) {
  const runList = async (list) => {
    const passed = new Set();
    for (const c of list) {
      try { await c.fn(); passed.add(c.name); } catch { /* 记失败 */ }
    }
    return passed;
  };

  const baseline = await runList(cases);                       // 第 1 轮做基线
  const suspects = new Map();
  let seed = 42; const rng = () => (seed = (seed * 9301 + 49297) % 233280) / 233280; // 固定种子可复现

  for (let r = 0; r < rounds; r++) {
    const result = await runList(shuffle(cases, rng));
    for (const name of baseline) {
      if (!result.has(name)) suspects.set(name, r);            // 混序后挂掉的用例
    }
  }

  // 单独复跑嫌疑用例：单独过 → 确认是顺序依赖而非本身脆弱
  const confirmed = [];
  for (const name of suspects.keys()) {
    const c = cases.find((x) => x.name === name);
    try { await c.fn(); } catch { confirmed.push(name); continue; }
    confirmed.push(`${name}(单独通过 → 顺序依赖)`);
  }
  console.log(confirmed.length ? `顺序依赖嫌疑：${confirmed.join(', ')}` : '未检出顺序依赖');
  return confirmed;
}

// 用法：detectOrderDependence([{ name: 'a', fn }, ...], 5)
```
**评分点**：
- 基线 + 多轮洗牌 diff 的检测思路（不是简单 shuffle 一次）。
- 固定随机种子保证可复现。
- 「单独复跑确认」区分顺序依赖与本身脆弱。
- 对应 Vitest sequence.shuffle / Jest --randomize 的原生做法。
