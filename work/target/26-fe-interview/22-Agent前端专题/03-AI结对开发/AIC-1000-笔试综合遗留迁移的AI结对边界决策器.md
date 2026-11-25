---
title: [AIC-1000] 笔试（收官）：实现「遗留迁移的 AI 结对边界决策器」（综合风险/可验证性/领域敏感度给出 AI 参与策略）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-1000：笔试（收官）：实现「遗留迁移的 AI 结对边界决策器」（综合风险/可验证性/领域敏感度给出 AI 参与策略）
**答**：
- 核心需求：实现 `decideAIBoundary(task, env)`。`task: { rewrites, coreChain, concurrency, domainSensitive, verifiable, mechanical }`（布尔）；`env: { peakSeason, hasTests, contextReady }`。返回 `{ mode, reason, guards }`。
- 决策规则（优先级从高到低）：① 封版期 + 核心链路 → mode="freeze"（不动）；② 不可验证 或 领域敏感且上下文不全 → "human-led"（人主导，AI 仅辅助理解）；③ 高并发/时序 或 核心逻辑 → "ai-draft-review"（AI 起草，强制人工逐行评审 + 差分验证）；④ 机械转换 + 可验证 + 上下文齐备 → "ai-autonomous"（AI 可自主，配自动校验）。
- guards 按 mode 给出守卫清单，如 ai-autonomous 需 ["特征化测试","差分校验","灰度"]，freeze 需 ["记录待迁移","大促后重评"]。
- 边界：所有字段缺失按 false 处理；env 缺失按最保守（peakSeason=true,hasTests=false,contextReady=false）；返回 reason 说明命中的规则（可解释）。
- 语义：这是整个「AI 结对在遗留迁移中的边界」主题的集大成——把散落的经验固化成一个可执行、可解释的决策器；它辅助决策而非替代决策，高风险时向上升级。
- 追问钩子：收官追问——「这个决策器最重要的设计是什么？」好答案：『把隐性经验变成显式、可解释、可执行的规则，同时在不确定时保守降级（fail-safe）』，这正是 AI 工程化的精髓：让能力有边界、让边界可治理。

```typescript
function decideAIBoundary(task={}, env={}) {
  const t={rewrites:false,coreChain:false,concurrency:false,domainSensitive:false,
    verifiable:false,mechanical:false,...task};
  const e={peakSeason:true,hasTests:false,contextReady:false,...env}; // 默认最保守
  let mode,reason,guards;
  if(e.peakSeason && t.coreChain){ mode='freeze'; reason='封版期核心链路', guards=['记录待迁移','大促后重评']; }
  else if(!e.hasTests || !t.verifiable || (t.domainSensitive && !e.contextReady)){
    mode='human-led'; reason='不可验证或领域敏感且上下文不全', guards=['先补测试与文档','AI仅辅助理解'];
  } else if(t.concurrency || t.coreChain || t.domainSensitive){
    mode='ai-draft-review'; reason='高风险需人工把关', guards=['AI起草','人工逐行评审','差分验证'];
  } else if(t.mechanical && t.verifiable && e.contextReady){
    mode='ai-autonomous'; reason='机械且可验证', guards=['特征化测试','差分校验','灰度放量'];
  } else { mode='ai-draft-review'; reason='默认保守', guards=['人工评审','回归验证']; }
  return { mode, reason, guards };
}
console.log(decideAIBoundary({mechanical:true,verifiable:true},
  {peakSeason:false,hasTests:true,contextReady:true})); // ai-autonomous
```
**评分点**：
- 四档决策（freeze/human-led/ai-draft-review/ai-autonomous）优先级顺序正确。
- env 默认最保守、task 字段缺失按 false，边界处理完整。
- guards 与 mode 对应的守卫清单合理、可执行，覆盖特征化/差分/灰度等手段。
- 返回 reason 可解释命中的规则，代码可运行、收官示例正确。
- 体现「fail-safe 保守降级 + 隐性经验显式化」的治理精髓（加分项）。
