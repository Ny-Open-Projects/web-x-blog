---
title: [PER-564] SLO 燃烧率告警怎么实现？为什么多窗口燃烧率能同时抓住突发和慢性？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-564：SLO 燃烧率告警怎么实现？为什么多窗口燃烧率能同时抓住突发和慢性？

**答**：
- 燃烧率 = 当前错误消耗速度 / 预算消耗速度（30 天窗口）；燃烧率 1 表示正好按预算速度烧，14.4 表示一天内烧完全月预算。
- 多窗口组合经典配置：**快窗口 5 分钟 + 慢窗口 1 小时，双超 14.4 倍 -> page（抓突发大事故）**；快窗口 30 分钟 + 慢窗口 6 小时，双超 6 倍 -> ticket（抓慢性劣化）。双窗口要求避免瞬时毛刺误报。
- 前端 SLO 的错误预算口径：JS 错误率、接口失败率、LCP 达标率不达 p75 的会话占比，三类可以合成一个体验错误率。
- 实现要点：错误预算 = (1 - SLO 目标) × 总请求；分窗口滑动计算；告警带燃烧率数值与预计烧尽时间，值班才知道紧急程度。

```javascript

function burnRate(errors, total, sloTarget, windowMinutes) {
  const budget = (1 - sloTarget) * total;                // 错误预算
  const consumed = errors / budget;                      // 已烧比例
  const expected = windowMinutes / (30 * 24 * 60);       // 窗口应烧比例
  return consumed / expected;                            // 燃烧率：1 = 正常速度
}
function sloAlert(rules) {
  const now = rules;                                     // { fast5, slow60, fast30, slow360, ... }
  const rate = (w) => burnRate(w.errors, w.total, 0.995, w.min);
  if (rate(rules.fast5) > 14.4 && rate(rules.slow60) > 14.4)
    return { level: 'page', reason: `突发: BR5=${rate(rules.fast5).toFixed(1)}` };  // 双窗口确认
  if (rate(rules.fast30) > 6 && rate(rules.slow360) > 6)
    return { level: 'ticket', reason: `慢性: BR6h=${rate(rules.slow360).toFixed(1)}` };
  return null;
}
// 双窗口的哲学：快窗口抓正在烧，慢窗口确认真的在大烧，毛刺过不了慢窗口
```
