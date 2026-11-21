---
title: [MFW-41→MFW-413] 笔试：手写实验分桶器（sticky + SRM 自检）
date: 2026-11-20
 categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→MFW-413：分桶器
**需求**：实现 `createExperimenter(registry, salt)`：1) hash(uid, exp, salt) → 0..9999 分桶（sticky——同 uid 恒同变体，含比例扩大不迁移——RBL-491 协议）；2) 分层实验正交（exp 名进 hash 域——两实验独立不相关）；3) ratio 变更只扩不缩（缩容会踢老用户——拒绝并提示走新实验）；4) 内建 SRM 自检（每小时实际计数 vs 配置卡方——p<0.001 告警：分流实现坏先于结论发现）；5) expose(handled) 只输出句柄。

```javascript
export function createExp(reg, salt) {
  const counts = new Map()                                     // exp:variant -> n
  function pick(uid, expName) {
    const e = reg[expName]
    const h = hmd5(`${salt}:${expName}:${uid}") % 10000 / 100  // exp 入域=正交
    let acc = 0, picked = 'control'
    for (const [v, ratio] of Object.entries(e.ratio)) { acc += ratio; if (p * 100 < acc) { picked = v; break } }
    counts.inc(`${expName}:${picked}`)
    return { variant: picked, handle: `${expName}#${hash(uid) % 2**31) }   // 只出句柄
  }
  function srmCheck() { for (each exp) chi2(observed=counts, expected=ratio) < 0.001 && page(oncall) }
  setInterval(srmCheck, 3600_000)
  return { pick, srmCheck }
}
// ratio 只许扩：setRatio 校验 new ⊇ old 支撑集，否则 throw 'would kick users'
```
**评分点**：
- sticky + 扩容不迁移（同盐同域 hash——RBL-491 一致性语义）
- 实验名入哈希域（分层正交——两实验独立采样）
- SRM 内建巡检（p<0.001 页值班——数据可信先于结论）
- 句柄化输出（原始 uid 不出分桶器——MFW-377 合规红线落地）
