---
title: [WEB-579] 笔试：手写 h3 迁移 AB 实验数据聚合器
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 可观测]
type: 笔试题
---

## WEB-579：笔试：手写 h3 迁移 AB 实验数据聚合器

**答**：实现 `aggregate(samples)`：输入 `{ group, uid, proto, rtt, ttfb }` 采样流，输出：① 按组×RTT 桶的样本数与 ttfb p50/p75；② SRM 检查：两组样本比例与预期 0.5 偏差超过 5% 输出 `{ srm: true }`；③ 剔除规则：爬虫 uid（`bot_` 前缀）与 ttfb 非法值先过滤；④ 各桶样本数 <100 时标记 `low`。写出实现。

```javascript
function p(arr, q) {
  const s = [...arr].sort((a, b) => a - b);
  return s[Math.min(s.length - 1, Math.floor(q * (s.length - 1)))];
}

function aggregate(samples) {
  const clean = samples.filter(s =>
    !s.uid.startsWith('bot_') && Number.isFinite(s.ttfb) && s.ttfb >= 0);
  const buckets = {};
  const groups = {};
  for (const s of clean) {
    groups[s.group] = (groups[s.group] || 0) + 1;
    const rttBucket = s.rtt < 100 ? 'a' : s.rtt < 300 ? 'b' : 'c';
    const key = `${s.group}|${rttBucket}`;
    (buckets[key] ||= []).push(s.ttfb);
  }
  const out = {};
  for (const [key, arr] of Object.entries(buckets)) {
    out[key] = { n: arr.length, p50: p(arr, .5), p75: p(arr, .75), low: arr.length < 100 };
  }
  const [g1 = 0, g2 = 0] = Object.values(groups);
  const total = g1 + g2;
  const srm = total > 0 && Math.abs(g1 / total - 0.5) > 0.05;
  return { buckets: out, srm, groups };
}
```

**评分点**：
- 过滤规则在聚合前执行且条件完备（爬虫/非法值）
- SRM 用比例偏差判定并输出布尔，理解 SRM 是实验可信度的第一道检查
- 分桶 key 与分位数实现正确；小样本标记 low 防止误读
- 结果结构可支撑「弱网收益是否显著」的对比阅读
