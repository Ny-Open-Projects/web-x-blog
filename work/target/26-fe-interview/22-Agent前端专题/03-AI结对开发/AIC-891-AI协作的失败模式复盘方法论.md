---
title: [AIC-891] AI 协作出了事故，复盘时该问哪些不同于传统事故的问题？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-891：AI 协作出了事故，复盘时该问哪些不同于传统事故的问题？
**答**：
- 传统复盘问「谁改了什么、为什么 review 没发现」；AI 事故还要多问几个维度：**① 模型/提示词版本是什么**（代码没变但模型升级也可能出问题）；**② AI 的建议为什么看起来合理却错**（幻觉如何绕过人的判断）；**③ 上下文里缺了什么关键信息**（AI 不知道那个隐式约束）；**④ 门禁为什么没拦住**（评测集覆盖缺口）。
- 关键心态：**不甩锅 AI**（AI 不是责任主体，AIC-882），聚焦「人-流程-工具」系统为什么没防住——是提示词不清？上下文不全？评测没覆盖？review 疲劳？
- 复盘的产出必须是**可执行的守卫**：新增评测用例（回归守卫 AIC-830）、补规则文件的禁区、加门禁规则——而不是写一句「以后注意」。
- 要区分「个案 bug」和「系统性模式」：同一类 AI 失误出现第二次，说明上次复盘的守卫没生效，要升级措施。
- 追问钩子：能说出「AI 事故复盘要问模型/prompt 版本和上下文缺口，且产出必须变成可执行守卫」的候选人，把复盘变成了学习系统。

```typescript
type Incident = { id: string; modelVersion?: string; promptVersion?: string;
  missingContext: string[]; evalGap: string; guardAdded: boolean; recurrenceCount: number };

function postmortemChecklist(i: Incident) {
  const questions = [
    i.modelVersion ? `当时模型版本 ${i.modelVersion}，是否近期变更？` : '缺失模型版本记录！',
    i.promptVersion ? `提示词版本 ${i.promptVersion}，改动是否引入歧义？` : '缺失提示词版本！',
    i.missingContext.length ? `上下文缺失：${i.missingContext.join(',')} → 补进规则文件` : '上下文完整',
    `评测缺口：${i.evalGap} → 补 golden 用例`,
  ];
  return {
    questions,
    systemic: i.recurrenceCount >= 2, // 复发 → 系统性，需升级措施
    actionable: i.guardAdded,          // 是否产出了可执行守卫
    verdict: i.guardAdded ? '已沉淀守卫' : '不合格：只有"以后注意"',
  };
}
console.log(postmortemChecklist({ id:'INC-1', modelVersion:'v2', promptVersion:'p7',
  missingContext:['旧接口返回 null'], evalGap:'缺 null 边界用例',
  guardAdded:true, recurrenceCount:1 }));
```
