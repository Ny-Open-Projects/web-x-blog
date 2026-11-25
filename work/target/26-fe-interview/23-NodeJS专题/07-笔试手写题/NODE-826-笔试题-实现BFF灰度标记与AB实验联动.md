---
title: [NODE-826] 笔试题——实现 BFF 灰度与 AB 实验联动（分流一致）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-826：手写灰度 AB 联动

**需求与边界**：
- 需求：灰度与 AB 联动（SCN-ENG-253）——① 分层正交（灰度桶与实验桶独立盐——SCN-ENG-253）；② BFF 侧实验分流（统一分流器——SCN-ENG-296）；③ 分流结果透传（下游实验一致——SCN-OPS-216 标记）；④ 组合爆炸防御（SCN-ENG-253 数量告警）。
- 边界：① 分流键统一（userId + layer salt——SCN-ENG-253）；② 分流结果持久（会话 sticky——SCN-OPS-244）；③ 实验结束的清理（SCN-OPS-224 代码化联动）。

**答**：
```javascript
function splitter(req) {
  const bucket = graySplit(req.user, { layer: 'release' });   // 灰度层（SCN-ENG-253）
  const experiments = {};
  for (const exp of activeExperiments()) {             // 实验层独立盐（正交——SCN-ENG-253）
    experiments[exp.id] = abSplit(req.user, { layer: `exp:${exp.id}` });
  }
  if (bucket × experiments.combos > 16)
    warn('组合爆炸——归因失效风险（SCN-ENG-253）');     // 数量防御
  tenantCtx.run({ ...ctx, gray: bucket, exp: experiments }, next);   // 透传下游（SCN-OPS-216）
}
```

**评分点**:
- 分层正交（灰度层与实验层独立盐——SCN-ENG-253）。
- 组合爆炸防御（数量告警——SCN-ENG-253）。
- 分流结果透传下游（标记贯穿——SCN-OPS-216）。
- 会话 sticky（SCN-OPS-244 分组稳定）。
