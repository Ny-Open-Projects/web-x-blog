---
title: [SOFT-837] 手写 peerFeedback：横向反馈的结构化生成（行为+影响+建议）、私密化提醒、接收方防御性预警？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-837：手写 peerFeedback：横向反馈的结构化生成（行为+影响+建议）、私密化提醒、接收方防御性预警

**需求与边界**：
- 实现 peerFeedback(observation)。
- 边界要求：① 输入观察 { behavior, impact, suggestion? }；② 输出结构化反馈：行为描述（非人格评判——过滤人格词：检测“马虎/不负责”类词替换为行为重述）+影响+建议（缺建议标 SUGGESTION_NEEDED）；③ 私密化提醒（一对一场景提示）；④ 接收防御预警：若历史该接收方对反馈反应防御（defensive: true）——建议“请求式开启”（先请对方给自己反馈 SOFT-822）。

**答**：
```javascript
const PERSONALITY = /马虎|不负责|懒|态度差|敷衍/;
function peerFeedback(o, { receiverDefensive = false } = {}) {
  let behavior = o.behavior;
  if (PERSONALITY.test(behavior))
    return { blocked: true,
      fix: `检测到人格评判——重述为行为：具体做了什么/没做什么` };
  const out = {
    behavior,
    impact: o.impact ?? 'SUGGESTION_NEEDED: 影响必须具体（谁被影响/损失了什么）',
    suggestion: o.suggestion ?? 'SUGGESTION_NEEDED',
    channel: '一对一私密（公开场合的横向批评杀伤力大 SOFT-809）',
  };
  if (receiverDefensive)
    out.strategy = '接收方偏防御：用请求式开启——先请对方给你反馈（SOFT-822互惠），再提你的观察';
  out.checklist = ['事实准确？（对方会承认这个行为发生过吗）',
    '影响具体？', '建议可执行？'];
  return out;
}
```

**评分点**:
- 人格评判过滤（强制行为化重述——SOFT-812 语言纪律工具化）。
- 影响/建议缺失显式要求补（结构完整性）。
- 防御性接收方的请求式策略（互惠开启 SOFT-822）。

