---
title: [PER-235] CrUX 返回的 histogram 与 percentiles 字段怎么读？评估页面性能该看哪个？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-235：CrUX 返回的 histogram 与 percentiles 字段怎么读？评估页面性能该看哪个？

**答**：
- 每个 CWV 指标返回两部分：`percentiles.p75`（第 75 分位的具体值）与 `histogram`（good/needs-improvement/poor 三桶的用户占比）。官方验收标准：p75 落在 good 区间即达标。
- 两个一起看：p75 = 2.1s（LCP）看数值刚超线，histogram 里 good 占比可能只有 40%——说明"过线的 25% 之外还有一大片 poor 用户"，只看 p75 会低估问题面。
- 密度比总量重要：同一 p75 下，good 55% 与 good 95% 的页面治理策略完全不同；histogram 用于定"改善空间"，p75 用于定"达标与否"。
- 注意 formFactor 维度：桌面/手机分开看，移动端通常明显更差；做 SEO 风险评估时按 formFactor=PHONE 的数据判断（Google 排名以移动端为主）。

```javascript
// 解析 CrUX 响应，产出达标判定
function judgeCrUX(record) {
  const out = {};
  for (const [metric, data] of Object.entries(record.metrics)) {
    const p75 = data.percentiles.p75;
    const [good, ni, poor] = data.histogram.map(h => h.density); // 占比和为 1
    out[metric] = {
      p75,
      goodRatio: +(good * 100).toFixed(1),
      verdict: data.histogram[0].density > 0.75 ? 'PASS' : 'RISK',  // good 占比 > 75%
    };
  }
  return out;
}
// judgeCrUX(res) => { largest_contentful_paint: { p75: '2100', goodRatio: 48.2, verdict: 'RISK' }, ... }
// p75 达标但 good 占比 48% => 治理空间大，别急着庆祝
```
