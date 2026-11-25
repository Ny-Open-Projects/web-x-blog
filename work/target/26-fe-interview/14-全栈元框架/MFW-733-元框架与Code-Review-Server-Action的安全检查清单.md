---
title: [MFW-733] Server Action 安全检查清单
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-733：Server Action 安全检查清单

**答**:
- Server Action 的 Code Review 检查清单：1) **鉴权**（action 内是否调用 auth()/session 校验——RBL-558：前端隐藏 ≠ server 无权限）；2) **参数校验**（zod schema 校验输入——formData 的字段验证 RBL-946）；3) **CSRF**（Origin 校验——框架默认 + 业务补充 RBL-544）；4) **幂等**（写操作是否幂等（RBL-567 idempotencyKey）；5) **敏感数据**（action 返回值不含密钥/内部路径——RBL-803）；6) **rate limit**（敏感 action 的限流配置（RBL-690）；7) **审计日志**（关键写操作的 audit log（谁做了什么——RBL-803 合规）。
- 检查清单的自动化：CI 的「Action 安全扫描」（静态分析：'use server' 文件的 AST 检查——auth() 调用存在/zod 校验存在）；「自动化扫描 + 人工 review」的双防线。
- 追问钩子：为什么「Server Action 的安全检查」比传统 API 更关键？——Action 的端点是「编译生成的」（URL 不可预测但可枚举——Next-Action header 的 id 猜测）；Action 的参数是「Flight 格式」（序列化复杂数据——校验面更大）；「安全边界的新形态」：传统 API 的 URL 明确（/api/xxx 路由清晰）；Action 的端点分散（每个 'use server' 文件都是端点）——「安全审计的覆盖面」需要清单化（每项检查有明确的工具/代码位置）。

```typescript
// CI 安全扫描（'use server' 文件的 AST 检查）
function auditServerAction(file: { code: string, hasServerDirective: boolean }) {
  const findings = [];
  if (!file.hasServerDirective) return findings;
  // 1) auth() 调用
  if (!file.code.includes('auth()') && !file.code.includes('getSession()'))
    findings.push({ check: 'auth', detail: 'action 未校验 session' });
  // 2) zod 校验
  if (!file.code.includes('.parse(') && !file.code.includes('.safeParse('))
    findings.push({ check: 'validation', detail: 'action 未使用 zod 校验输入' });
  // 3) 敏感返回
  if (/return.*(?:password|secret|token|key)/i.test(file.code))
    findings.push({ check: 'sensitive-return', detail: 'action 返回值可能含敏感数据' });
  return findings;
}
// review 清单（人工部分）
const REVIEW_CHECKLIST = [
  '✓ auth()/getSession() 在 action 内调用',
  '✓ zod schema 校验 formData',
  '✓ 幂等键（写操作）',
  '✓ 返回值不含敏感数据',
  '✓ rate limit 配置（敏感 action）',
  '✓ audit log（关键操作）',
];
```
