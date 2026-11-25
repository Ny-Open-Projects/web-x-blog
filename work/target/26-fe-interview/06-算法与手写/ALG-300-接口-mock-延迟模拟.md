---
title: [ALG-300] 接口 mock 延迟模拟：按真实分布采样（对数正态）+ 网络档位叠加——测试环境的真实性
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-300：mock 延迟按真实分布采样——固定延迟测不出竞态

**答**：mock 接口固定延迟 200ms 太假（真实耗时是长尾分布）——按对数正态采样 + 弱网档位叠加（PER-431），让测试环境的加载态/竞态/骨架屏行为接近真实。

**思路**：Box-Muller 正态采样 → log 变换（对数正态：median × e^(σ·z)）→ 档位系数乘（Good 1x/Mid 3x/Slow 8x）。

```javascript
function sampleLatency({ median = 200, sigma = 0.5, tier = 'good' } = {}) {
  const TIER = { good: 1, mid: 3, slow: 8 };              // PER-431 档位系数
  const u1 = Math.random() || 1e-9, u2 = Math.random();
  const z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);   // Box-Muller 标准正态
  const ms = median * Math.exp(sigma * z) * TIER[tier];   // 对数正态：中位数 × e^(σz)（天然长尾）
  return Math.max(20, Math.round(ms));                    // 下限保护（竞态语义依赖非零耗时）
}
// 对比固定 200ms：
// 对数正态：p50=200 / p90≈370 / p99≈750 —— 真实长尾形状（骨架屏/竞态/超时路径全被测到）
// 固定延迟：所有请求同速 —— 竞态 bug（快慢响应乱序覆盖）在 mock 环境永远测不出来
// 档位叠加：CI 跑 mid 档（慢 3 倍）—— 弱网加载态路径被覆盖（PER-431 标准档位）
// 下限 20ms：极端采样出 0ms 会让"响应乱序"竞态永不复现——竞态测试要求耗时方差非零
```

**评分点**：
- 对数正态采样（Box-Muller + log 变换）——本题核心（固定延迟测不出竞态）。
- 档位系数叠加（PER-431 联动，CI 档位可配）。
- 长尾形状对测试覆盖的价值（p99 路径/骨架屏/竞态全被触发）。
- 下限保护与采样参数（median/sigma）可配。
