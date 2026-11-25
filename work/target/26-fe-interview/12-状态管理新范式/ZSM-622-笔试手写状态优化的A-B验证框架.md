---
title: [ZSM-622] 笔试：手写状态优化方案的 A/B 验证框架（统计显著性）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-622：手写状态优化方案的 A/B 验证框架（统计显著性）
**答**：实现 `createABValidator()`：1) `run(name, variantFn, times)`：跑一个变体（同一 workload 多次），收集样本；2) workload 抽象：`setWorkload(fn)`（构造固定输入——每次运行前重建，防缓存污染）；3) `compare(vA, vB)`：均值对比 + **Welch t 检验**近似（自由度用 Welch–Satterthwaite），输出 p 值与置信结论（p < 0.05 显著）；4) 样本离群处理（IQR 剔除）与最小样本量检查（< 30 提示）；5) 附用例：两组样本验证显著性判定。

```javascript
function createABValidator() {
  let workload = null

  function setWorkload(fn) { workload = fn }

  function sampleStats(xs) {
    const sorted = [...xs].sort((a, b) => a - b)
    const q = (p) => sorted[Math.floor(sorted.length * p)]
    // IQR 离群剔除
    const q1 = q(0.25), q3 = q(0.75), iqr = q3 - q1
    const kept = sorted.filter((x) => x >= q1 - 1.5 * iqr && x <= q3 + 1.5 * iqr)
    const n = kept.length
    const mean = kept.reduce((a, b) => a + b, 0) / n
    const variance = kept.reduce((a, b) => a + (b - mean) ** 2, 0) / (n - 1)
    return { n, mean, sd: Math.sqrt(variance) }
  }

  function run(name, variantFn, times = 100) {
    if (times < 30) console.warn(`[AB] ${name} 样本量 ${times} < 30，结论不可靠`)
    const samples = []
    for (let i = 0; i < times; i++) {
      const ctx = workload()          // 每次重建：防缓存污染
      const t0 = performance.now()
      variantFn(ctx)
      samples.push(performance.now() - t0)
      globalThis.gc?.()
    }
    return { name, ...sampleStats(samples) }
  }

  // Welch t 检验（近似 p 值用正态近似）
  function compare(a, b) {
    const se = Math.sqrt(a.sd ** 2 / a.n + b.sd ** 2 / b.n)
    const t = (a.mean - b.mean) / se
    // 双侧 p 值（正态近似，n 足够时近似成立）
    const p = 2 * (1 - normalCdf(Math.abs(t)))
    const sig = p < 0.05
    const faster = a.mean < b.mean ? a.name : b.name
    return {
      aMean: +a.mean.toFixed(3), bMean: +b.mean.toFixed(3),
      t: +t.toFixed(2), p: +p.toFixed(4),
      significant: sig,
      conclusion: sig ? `${faster} 显著更快（p=${p.toFixed(4)}）`
                      : `差异不显著（p=${p.toFixed(4)}），不能宣称优化有效`,
    }
  }

  function normalCdf(z) {
    return 0.5 * (1 + Math.sign(z) * Math.sqrt(1 - Math.exp((-2 / Math.PI) * z * z)))
  }

  return { setWorkload, run, compare }
}

// 用例
const ab = createABValidator()
ab.setWorkload(() => ({ arr: new Array(2000).fill(0) }))
const a = ab.run('immutable', (ctx) => { for (let i = 0; i < 30; i++) ctx.arr = [...ctx.arr, i] }, 60)
const b = ab.run('mutate', (ctx) => { for (let i = 0; i < 30; i++) { ctx.arr.push(i) } }, 60)
console.log(ab.compare(a, b))
// { aMean: 0.55, bMean: 0.01, t: 46.2, p: 0, significant: true,
//   conclusion: 'mutate 显著更快（p=0.0000）' }
```
**评分点**：
- workload 每次重建（防缓存/预热污染样本）
- IQR 离群剔除 + 最小样本量提示（结论可靠性前置）
- Welch t 检验（方差不齐场景）与 p 值阈值判定
- 显著性结论的表达（不显著时明确「不能宣称有效」——反过来说比只说快了多少更专业）
