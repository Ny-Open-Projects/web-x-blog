---
title: [AGT-195] Agent 的安全红线清单——哪些操作必须留在「不可自动化」白名单外？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-195：Agent 的安全红线清单——哪些操作必须留在「不可自动化」白名单外？
**答**：
- 红线判定三问：错误是否不可逆（删库/转账/发公开声明）、是否有清晰可程序化的完成判据（没有 → 判定权必须留人）、出错的责任主体是否能承受自动化（法务/声誉风险）。
- 通用红线清单：资金操作（支付/退款/调价）、不可逆删除与批量变更、对外发布（邮件/公告/PR 合并）、法律效力动作（签合同/提交申报）、用户数据导出、权限与安全配置变更、自主联网下载执行代码。
- 白名单思想是反向的：默认全部禁止，逐项论证后加入白名单（每项写明适用范围/限额/审计方式），而不是「默认允许 + 黑名单拦截」。
- 边界内的自动化用「护栏参数」收窄：可自动退款但单笔 ≤ $50 且日累计 ≤ $500，超限即 HITL——红线是光谱不是开关。

```typescript
// 安全白名单闸门：默认拒绝 + 逐项准入 + 护栏参数
import { z } from 'zod';

const Guardrail = z.object({
  action: string3(),                                    // 动作类型
  maxAmountUsd: z.number().optional(),                  // 金额护栏
  dailyCumulativeUsd: z.number().optional(),
  maxRowsAffected: z.number().optional(),               // 影响面护栏
  requireEvidence: z.boolean().default(true),           // 必须附带执行依据
});
function string3() { return z.string(); }
type Guardrail = z.infer<typeof Guardrail>;

// 白名单：每项经过论证准入，未列出的动作一律拒绝
const WHITELIST: Guardrail[] = [
  { action: 'refund', maxAmountUsd: 50, dailyCumulativeUsd: 500, requireEvidence: true },
  { action: 'db.update', maxRowsAffected: 10, requireEvidence: true },
];

export async function guardAction(req: { action: string; amountUsd?: number; rows?: number; evidence?: string }, tenantSpentToday: number) {
  const rule = WHITELIST.find((g) => g.action === req.action);
  if (!rule) {
    // 红线动作：不留确认通道，直接拒绝并审计（区别于「确认后执行」）
    audit.alert({ event: 'action.not_in_whitelist', action: req.action });
    return { allowed: false, reason: '该动作不在自动化白名单内，需人工执行' };
  }
  if (rule.requireEvidence && !req.evidence) return { allowed: false, reason: '缺少执行依据' };
  if (rule.maxAmountUsd != null && (req.amountUsd ?? 0) > rule.maxAmountUsd) {
    return { allowed: false, reason: `超单笔限额，转人工审批（限 ${rule.maxAmountUsd}）` };   // 护栏外 → HITL，不是放行
  }
  if (rule.dailyCumulativeUsd != null && tenantSpentToday + (req.amountUsd ?? 0) > rule.dailyCumulativeUsd) {
    return { allowed: false, reason: '今日累计额度耗尽' };
  }
  if (rule.maxRowsAffected != null && (req.rows ?? 0) > rule.maxRowsAffected) {
    return { allowed: false, reason: '影响行数超限' };
  }
  audit.info({ event: 'action.allowed', ...req });
  return { allowed: true };
}
const audit = { alert: (x: unknown) => { void x; }, info: (x: unknown) => { void x; } };
```
