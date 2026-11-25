---
title: [AGT-646] 手写 srmCheck：分流比偏离检测、卡方检验近似、污染检测？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-646：手写 srmCheck：分流比偏离检测、卡方检验近似、污染检测

**需求与边界**：
- 实现 srmCheck(exp, window)：检测实验组/对照组分流比是否偏离配置。
- 边界要求：① 偏离度 = |实际占比 - 配置占比|，>2% 告警；② 用卡方统计量判定显著性（样本大时 2% 也显著）；③ 污染检测：同一用户出现在两组（会话粘性被破坏）数量 >0 即告警；④ 样本不足（<1000）返回 pending。

**答**：
```javascript
function srmCheck(exp, window) {
  const { treat, ctrl } = window.groups;
  const n = treat + ctrl;
  if (n < 1000) return { status: 'pending', n };
  const expected = n * exp.ratio;                // 期望实验组数
  const chi = (treat - expected) ** 2 / expected
    + (ctrl - (n - expected)) ** 2 / (n - expected); // 卡方统计量
  const sig = chi > 3.84;                        // df=1, p=0.05
  const dev = Math.abs(treat / n - exp.ratio);
  return {
    status: sig || dev > 0.02 ? 'alarm' : 'ok',
    dev, chi,
    polluted: window.crossUsers,                 // 跨组用户数
    action: window.crossUsers > 0
      ? 'fix_sticky_bucket' : sig ? 'check_hash_salt' : null,
  };
}
```

**评分点**:
- 卡方 + 偏离度双判据（样本大时微小偏离也显著）。
- 污染检测独立（粘性破坏比分流偏离更严重），给出对应修复动作。
- 样本不足 pending 不误报。

