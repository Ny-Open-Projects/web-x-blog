---
title: [PER-1136] 什么是 Privacy by Design？在需求评审怎么体现
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1136：什么是 Privacy by Design？在需求评审怎么体现

**答**：
- 七原则：主动预防非事后补救、默认隐私、隐私嵌入设计、全生命周期、端到端安全、可见性与透明、用户中心。
- 需求评审动作：数据流图（哪收、存哪、给谁）、最小化问答（每个字段：为什么需要/能否不要）、默认值检查（默认关闭分享/默认不公开）。
- 产出：隐私需求条目进验收标准（同安全需求 1120），缺失打回。
- 成本观：设计期改一行 vs 上线后返工，隐私左移是最便宜的合规。

```javascript
// 隐私评审数据流图（结构化）
function privacyReview(feature) {
  return {
    collect: feature.fields.map(f => ({ field: f, why: f.why ?? '必答', level: f.level ?? '待定' })),
    store: feature.storage.map(s => ({ where: s, encrypted: s.encrypted ?? false })),
    share: feature.thirdParties.map(t => ({ to: t, legalBasis: t.basis ?? '必须声明' })),
    gaps: feature.fields.filter(f => !f.why).map(f => `${f.name} 缺最小化说明`),
  };
}
// gaps 非空 -> 评审不通过
```
