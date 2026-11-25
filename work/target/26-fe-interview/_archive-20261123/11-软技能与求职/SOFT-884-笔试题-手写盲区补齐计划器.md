---
title: [SOFT-884] 手写 blindspotPlanner：盲区四分类（真/半/表达/深度）、补齐策略路由、费曼验证项生成？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-884：手写 blindspotPlanner：盲区四分类（真/半/表达/深度）、补齐策略路由、费曼验证项生成

**需求与边界**：
- 实现 blindspotPlanner(blindspots, freqData)。
- 边界要求：① 盲区四分类输入：{ topic, class: 'true'|'half'|'expression'|'depth', freq }；② 策略路由：true→评估必要性（freq≥3 才投入——SOFT-866 频率驱动）/half→补到能讲原理/expression→话术模板/depth→补“为什么层”（SOFT-689）；③ 费曼验证项：每个补齐计划配“讲给别人听”的验证动作；④ 按频率排序输出。

**答**：
```javascript
function blindspotPlanner(blindspots) {
  const STRATEGY = {
    true: (f) => f >= 3
      ? { plan: '系统学习（课程/文档+实践小项目）', weeks: 4 }
      : { plan: '暂不投入（低频盲区放过）', weeks: 0 },
    half: () => ({ plan: '补到能讲清原理（文档精读+输出小结）', weeks: 2 }),
    expression: () => ({ plan: '话术模板：框架+要点+时长版本（SOFT-867）', weeks: 1 }),
    depth: () => ({ plan: '补“为什么层”：原理溯源+对比方案（SOFT-689）', weeks: 3 }),
  };
  const rows = blindspots
    .sort((a, b) => b.freq - a.freq)               // 频率优先
    .map(b => {
      const s = STRATEGY[b.class](b.freq);
      return { topic: b.topic, class: b.class, freq: b.freq,
        ...s,
        feynman: s.weeks > 0
          ? `费曼验证：给同事讲一遍${b.topic}，对方能复述=补齐（SOFT-784）`
          : null };
    });
  return { rows,
    note: '盲区暴露=免费的市场化摸底（SOFT-866）——清单滚动更新' };
}
```

**评分点**:
- 四分类策略路由（true 类频率门槛 ≥3 才投入——低成本优先）。
- 费曼验证项强制（能讲给别人听=补齐的客观标准）。
- 频率排序（高频盲区先补）。

