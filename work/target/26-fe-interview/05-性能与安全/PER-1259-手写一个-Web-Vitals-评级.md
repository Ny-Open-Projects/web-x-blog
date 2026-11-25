---
title: [PER-1259] 手写一个 Web Vitals 评级函数
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1259：手写一个 Web Vitals 评级函数

**答**：
- 需求：实现 rateVitals({ lcp, inp, cls, ttfb })。按 Chrome 口径分级 good/ni/poor：LCP <=2500/4000、INP <=200/500、CLS <=0.1/0.25、TTFB <=800/1800；输出每项评级与总体（最差项决定）；缺项跳过。
- 边界：负值按 poor；全缺返回 null；总体列最差项 id。
- 评分点：阈值分级；最差决定总体；缺项跳过；负值

```javascript
function rateVitals(v = {}) {
  const TH = { lcp: [2500, 4000], inp: [200, 500],
    cls: [0.1, 0.25], ttfb: [800, 1800] };
  const rank = { good: 0, ni: 1, poor: 2 };
  const out = {}; let worst = null;
  for (const [k, [g, p]] of Object.entries(TH)) {
    if (v[k] == null) continue;
    const val = v[k];
    const r = val < 0 || val > p ? 'poor' : val <= g ? 'good' : 'ni';
    out[k] = { value: val, rating: r };
    if (!worst || rank[r] > rank[out[worst].rating]) worst = k;
  }
  return { vitals: out, overall: worst,
    rating: worst ? out[worst].rating : null };
}
```

## 追问（补充）

**追问**：

1. CLS 的 0.1/0.25 是对单次偏移还是累计？ → 是对「会话窗口」累计值判级（连续偏移间隔小于 1 秒、总长不超过 5 秒算一个窗口，取最大窗口），直接拿单条 entry 判级会系统性低估。
2. LCP 什么时候上报才准？ → 要等用户首次交互后候选冻结，在 `visibilitychange` 转隐藏时用 `sendBeacon` 上报；过早上报拿到的是「暂时的 LCP」，会偏小。
3. 缺项跳过会不会掩盖真实故障？ → 会。要把「未采集（undefined）」和「不适用（null）」分开，并把采集率当独立指标；否则 SDK 挂掉时评级全绿。
4. 阈值可以写死成常量吗？ → 不能长期写死。Chrome 会调阈值（FID 被 INP 取代就是例子），应做成带版本号的配置表，与服务端聚合口径对齐，否则前后端算出的「好」比例对不上。
