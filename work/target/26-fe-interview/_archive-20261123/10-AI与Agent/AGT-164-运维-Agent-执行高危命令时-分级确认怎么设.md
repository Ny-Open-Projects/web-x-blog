---
title: [AGT-164] 运维 Agent 执行高危命令时，分级确认怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-164：运维 Agent 执行高危命令时，分级确认怎么设计？
**答**：
- 命令分级矩阵：L0 只读（cat/df/status）自动执行；L1 变更可逆（重启应用、改配置且可回滚）单次确认；L2 高危不可逆（删数据、改 DNS、扩缩容生产库）双人确认 + 变更窗口；L3 禁区（rm -rf、chmod 777 /、生产库 drop）直接拒绝，不提供确认通道。
- 确认信息要「可决策」：展示完整命令、影响面（哪些机器/服务）、回滚方案、爆炸半径评估——只弹「确定执行吗？」是不合格的确认设计。
- 执行防护：命令模板化（参数化执行而非拼接自由文本）、执行前后快照（配置 diff 自动留档）、执行通道用最小权限账号（Agent 的 SSH key 只有目标操作的权限）。
- 审计要求：谁批准的、依据什么证据、执行输出全量留痕，审批与执行人分离（Agent 可以是执行人，不能是批准人）。

```typescript
// 运维命令分级确认
import { z } from 'zod';

type Level = 0 | 1 | 2 | 3;
const CLASSIFY: { pattern: RegExp; level: Level }[] = [
  { pattern: /\b(rm\s+-[rf]{1,2}\b|chmod\s+777|drop\s+(table|database)|shutdown|mkfs)/i, level: 3 },
  { pattern: /\b(delete\s+from|truncate|update\s+\w+\s+set|kubectl\s+(scale|delete)|dns\s+update)/i, level: 2 },
  { pattern: /\b(systemctl\s+restart|nginx\s+-s\s+reload|kubectl\s+rollout)/i, level: 1 },
];
function classify(cmd: string): Level {
  return (CLASSIFY.find((c) => c.pattern.test(cmd))?.level ?? 0);
}

export async function runCommand(cmd: string, ctx: { requesterId: string; evidence: string }) {
  const level = classify(cmd);
  if (level === 3) return { executed: false, reason: '禁区命令，永久拒绝且不做确认提示', level };

  const impact = await assessImpact(cmd);
  if (level === 0) return { executed: true, output: await exec(cmd), level };

  // L1/L2：进入人工审批队列，审批人必须 ≠ 发起人
  const approval = await approvalQueue.request({
    cmd, level, impact,
    evidence: ctx.evidence,            // Agent 必须给出执行依据
    rollback: await buildRollbackPlan(cmd, impact),
    requesterId: ctx.requesterId,
    requireDoubleConfirm: level === 2,
    expiresAt: Date.now() + 10 * 60_000, // 审批过期作废，防止积压后误批
  });
  if (!approval.granted) return { executed: false, reason: '未获批准', level };

  const before = await snapshot(impact.hosts);                       // 执行前后快照 diff 留档
  const output = await exec(cmd);
  const after = await snapshot(impact.hosts);
  audit({ cmd, level, approver: approval.approverId, before, after });
  return { executed: true, output, diff: diffSnapshots(before, after), level };
}

async function assessImpact(cmd: string) { void cmd; return { hosts: ['app-1'], services: ['web'] }; }
async function buildRollbackPlan(cmd: string, impact: any) { void cmd; void impact; return '回滚方案已生成'; }
async function exec(cmd: string) { return `simulated: ${cmd}`; }
async function snapshot(hosts: string[]) { void hosts; return {}; }
function diffSnapshots(a: unknown, b: unknown) { return { a, b }; }
const approvalQueue = { request: async (x: any) => ({ granted: true, approverId: 'ops-001' }) };
const audit = (x: unknown) => { void x; };
```
