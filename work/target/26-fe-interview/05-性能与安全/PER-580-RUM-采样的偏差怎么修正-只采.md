---
title: [PER-580] RUM 采样的偏差怎么修正？只采样 10% 会话时，p75 等分位数可信吗？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-580：RUM 采样的偏差怎么修正？只采样 10% 会话时，p75 等分位数可信吗？

**答**：
- 会话级随机采样下分位数理论上无偏，但**实际偏差来自非随机因素**：爬虫/自动化流量被过度采样或剔除、低端机用户上报成功率不同（网络差丢包多）、长会话被采样概率高（命中采样机会多）。
- 修正手段：按可观测维度（设备档/网络/地区）做**事后分层重加权**——已知全量分布（来自服务器日志/CDN 日志）时，把样本分布向全量分布校正（raking）。
- 置信度意识：采样率 10%、日会话 5 万 -> 每天样本 5000，p75 置信区间较窄；但细分到某路由×低端机×3G"可能只剩几十样本，必须标记不可信而非直接输出。
- 实操建议：核心北极星指标用较高采样（30%+）保证细分可信；诊断指标低采样；所有细分看板强制显示样本量。

```javascript

function reweight(samples, trueDist) {                     // 分层重加权修正采样偏差
  const observed = {};
  samples.forEach(s => { const k = `${s.deviceTier}/${s.net}`;
    observed[k] = (observed[k] ?? 0) + 1; });
  const total = samples.length;
  const weighted = samples.map(s => {
    const k = `${s.deviceTier}/${s.net}`;
    const obsShare = (observed[k] ?? 0) / total;
    const trueShare = trueDist[k] ?? obsShare;
    return { ...s, w: trueShare / (obsShare || 1) };       // 权重 = 真实占比/观测占比
  });
  return weighted;                                          // 聚合时按 w 加权
}
// 警惕：权重极端（>10 倍）说明某分群被严重欠采样，优先修采样而非纯靠加权
```
