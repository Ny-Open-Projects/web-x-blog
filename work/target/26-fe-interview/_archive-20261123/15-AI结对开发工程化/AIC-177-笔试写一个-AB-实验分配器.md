---
title: [AIC-177] 笔试：实现一个 Prompt A/B 实验分配器：稳定哈希分桶、实验互斥/共存与指标回传聚合？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-177：笔试：实现一个 Prompt A/B 实验分配器：稳定哈希分桶、实验互斥/共存与指标回传聚合？
**需求**：实现 `Experimenter`：
- `assign(userId, expId, buckets)`：稳定哈希分桶（同用户同实验永远同桶，0~99）；
- 实验元信息：`{expId, variants: {A: 0-49, B: 50-99}, layer}`；同层实验互斥（用户只能进同层一个实验），不同层可共存（正交）；
- `track(expId, variant, metric)` 回传指标；`report(expId)` 聚合各变体均值与样本量。

```javascript
import { createHash } from 'crypto';

function bucketOf(userId, expId, layer = 'default') {
  const h = createHash('md5').update(`${layer}:${expId}:${userId}`).digest();
  return h[0] * 256 + h[1]; // 0~65535 → %100 均匀
}
function inRange(b, [lo, hi]) { return b >= lo && b <= hi; }

class Experimenter {
  #exps = new Map(); #data = new Map(); // expId -> variant -> [values]
  register({ expId, variants, layer = 'default' }) {
    this.#exps.set(expId, { expId, variants, layer });
  }
  assign(userId, expId) {
    const exp = this.#exps.get(expId);
    if (!exp) return null;
    const b = bucketOf(userId, expId, exp.layer) % 100;
    for (const [variant, range] of Object.entries(exp.variants)) {
      if (inRange(b, range)) {
        this.#data.set(`${expId}:${variant}`, this.#data.get(`${expId}:${variant}`) ?? []);
        return { expId, variant, bucket: b };
      }
    }
    return null; // 不在任何区间 → 不参与
  }
  track(expId, variant, value) {
    const k = `${expId}:${variant}`;
    if (!this.#data.has(k)) throw new Error(`未知实验组合 ${k}`);
    this.#data.get(k).push(value);
  }
  report(expId) {
    const out = {};
    for (const [k, vals] of this.#data) {
      if (!k.startsWith(expId + ':')) continue;
      const variant = k.split(':')[1];
      out[variant] = { n: vals.length, mean: +(vals.reduce((a, b) => a + b, 0) / vals.length).toFixed(3) };
    }
    return out;
  }
}

// 测试：稳定分桶 + 指标聚合
const ex = new Experimenter();
ex.register({ expId: 'prompt-v2', variants: { A: [0, 49], B: [50, 99] } });
const asg1 = ex.assign('user-1', 'prompt-v2');
const asg2 = ex.assign('user-1', 'prompt-v2');
console.log(asg1.variant === asg2.variant); // true 稳定
for (let i = 0; i < 100; i++) {
  const a = ex.assign(`u${i}`, 'prompt-v2');
  ex.track('prompt-v2', a.variant, a.variant === 'B' ? 0.82 : 0.7);
}
console.log(ex.report('prompt-v2')); // B 均值更高
```

**评分点**：
1. 稳定哈希分桶（userId+expId 入哈希）而非随机——用户刷新后必须还是同一变体；
2. layer 分层设计：同层互斥防实验污染，跨层正交提升实验吞吐（说出理由加分）；
3. 分桶边界处理：未落在任何变体区间的用户显式返回 null（灰度放量场景）；
4. report 聚合含样本量 n——没有 n 的均值无法判断显著性；
5. 追问：样本不足时不能下结论，需配最小样本量与显著性检验。
