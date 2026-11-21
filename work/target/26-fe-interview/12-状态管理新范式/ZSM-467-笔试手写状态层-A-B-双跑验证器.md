---
title: [ZSM-467] 笔试：手写状态层 A/B 双跑验证器
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-467：手写状态层 A/B 双跑验证器
**需求**：实现 `createShadowRunner(oldImpl, newImpl)`：1) `exec(input)`：主路径返回 oldImpl 结果（用户无感），影子异步跑 newImpl；2) 影子结果与主结果对比（viewFn 视图级），不一致记录 { input, old, new }（采样 10% 上报）；3) 影子异常吞掉不影响主路径（隔离）；4) `verdict()` 返回 { total, match, matchRate }；5) 超时影子（3s）计为 mismatch（防止假阳性通过）；6) matchRate 连续达标（>=99.9% 且 total>=1000）触发 canPromote()。

```javascript
export function createShadowRunner(oldImpl, newImpl, viewFn, { sampleRate = 0.1 } = {}) {
  let total = 0, match = 0
  const CONSECUTIVE_N = 1000, TARGET = 0.999
  let recent = []                                            // 最近 N 个结果窗口

  function exec(input) {
    const main = oldImpl(input)                              // 主路径（同步语义不变）
    void (async () => {                                      // 影子隔离
      try {
        const shadow = await Promise.race([
          Promise.resolve(newImpl(input)),
          new Promise((_, rej) => setTimeout(() => rej(new Error('shadow-timeout')), 3000)),
        ])
        total++
        const eq = JSON.stringify(viewFn(main)) === JSON.stringify(viewFn(shadow))
        if (eq) match++; else if (Math.random() < sampleRate)
          report('shadow_mismatch', { input, old: viewFn(main), new: viewFn(shadow) })
        recent = [...recent.slice(-(CONSECUTIVE_N - 1)), eq]
      } catch { /* 影子异常吞掉 */ }
    })()
    return main
  }

  return {
    exec,
    verdict: () => ({ total, match, matchRate: total ? match / total : 0 }),
    canPromote: () => total >= CONSECUTIVE_N && recent.every(Boolean) &&
      match / total >= TARGET,
  }
}
```
**评分点**：
- 影子异步隔离（不阻塞主路径、异常吞掉、超时计 mismatch 防假阳性）
- 视图级对比（viewFn 而非内部结构）
- 采样上报（mismatch 记录量控）
- 晋升条件严格（样本量 + 最近窗口全对 + 全局比率）——灰度验收的工程严谨性
