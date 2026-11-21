---
title: [AGT-199] Agent 出错时「谁负责」——伦理与责任边界的产品设计怎么落地？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-199：Agent 出错时「谁负责」——伦理与责任边界的产品设计怎么落地？
**答**：
- 责任分配的产品化表达：在 UI 与交互契约上明确三种模式的责任归属——AI 建议 + 人执行（人负责）、AI 执行 + 人授权（授权者负责但产品有义务提供充分决策信息）、AI 自主执行（产品方对系统可靠性负责）——模式越高自动化，产品方的举证与保障义务越重。
- 免责不是免责声明一行字，而是「能力边界的前置披露」：明确告知用户 AI 在哪些场景不可靠（医疗/法律/投资建议），并在识别到此类场景时主动降级为「信息提供」模式。
- 出错响应设计：错误归因界面（展示决策链帮用户理解发生了什么，AGT-186）、补救通道（一键撤销/回滚/人工介入）、补偿机制（错误造成损失时的处理流程预先设计）。
- 组织侧：建立 AI 决策的申诉与复核流程，高风险决策保留人工复核权（不是技术兜底而是权利设计）；用 AGT-195 的白名单把「不可自动化」固化为产品约束而非口头共识。

```typescript
// 责任模式声明 + 出错补救流
import { z } from 'zod';

const ResponsibilityMode = z.enum(['suggest', 'act_with_approval', 'autonomous']);
type ResponsibilityMode = z.infer<typeof ResponsibilityMode>;

interface Action {
  mode: ResponsibilityMode;
  kind: string;
  reversible: boolean;
  riskLevel: 'low' | 'medium' | 'high';
}

export function responsibilityContract(a: Action): {
  whoBears: 'user' | 'approver' | 'platform'; obligations: string[] } {
  switch (a.mode) {
    case 'suggest':
      return { whoBears: 'user', obligations: ['AI 必须给出依据供用户独立判断', '高社会敏感领域（医疗/法律/投资）强制声明仅供参考'] };
    case 'act_with_approval':
      return { whoBears: 'approver', obligations: [
        '产品必须提供充分决策信息：影响面、回滚方案、置信度（AGT-164）',
        '授权记录可追溯，审批与执行人分离',
        a.riskLevel === 'high' && !a.reversible ? '不可逆高风险动作禁止进入此模式' : '常规护栏生效',
      ] };
    case 'autonomous':
      if (a.riskLevel === 'high') throw new Error('高风险动作不允许自主模式（红线，AGT-195）');
      return { whoBears: 'platform', obligations: [
        '平台对系统可靠性负责：评测通过率、SLA、监控告警',
        '错误响应链路：归因界面 + 一键回滚 + 补偿流程',
        a.reversible ? '必须支持自动回滚' : '半自主动作需事后抽样审计',
      ] };
  }
}

// 错误补救流：归因 → 回滚 → 补偿
export async function errorRemediation(runId: string, complaint: string) {
  const trace = await traceStore.load(runId);
  const rollback = await tryRollback(runId);
  await humanReviewQueue.push({ runId, complaint, trace, rollback, compensation: rollback.ok ? null : 'enter_compensation_flow' });
  return { rollback, traceId: trace.id };
}
const traceStore = { load: async (id: string) => ({ id }) };
async function tryRollback(runId: string) { void runId; return { ok: true }; }
const humanReviewQueue = { push: async (x: unknown) => { void x; } };
```
