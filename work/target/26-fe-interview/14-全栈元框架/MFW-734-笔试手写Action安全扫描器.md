---
title: [MFW-734] 笔试：手写 Action 安全扫描器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-734：笔试：手写 Action 安全扫描器

**答**：实现 `scanActionSecurity(code, { config })`。config: `{ requireAuth: boolean, requireValidation: boolean, sensitivePatterns: RegExp[] }`. 规则：1) hasServerDirective（'use server' 存在才扫描——非 server 文件跳过）；2) auth 检查（config.requireAuth 且无 auth/getSession 调用 → finding 'missing-auth'）；3) validation（config.requireValidation 且无 parse/safeParse → 'missing-validation'）；4) 敏感返回（sensitivePatterns 匹配 return 语句 → 'sensitive-return'）；5) 幂等检查（写操作关键词 insert/update/delete/create 且无 idempotency → warn 'no-idempotency'）；6) 返回 `{ findings: Array<{ check, severity, detail }>, ok }`（ok = 无 error）。边界：无 'use server'（跳过全部）；空 config（使用默认）；写操作检测（insert/update/delete/create/updateMany 等）。

```javascript
const WRITE_PATTERNS = /\.(insert|update|delete|create|upsert|updateMany|deleteMany)\(/;

function scanActionSecurity(code = '', { requireAuth = true, requireValidation = true,
  sensitivePatterns = [/password/i, /secret/i, /token/i, /apiKey/i] } = {}) {
  if (!code.includes("'use server'") && !code.includes('"use server"'))
    return { findings: [], ok: true, skipped: true };
  const findings = [];
  const isWrite = WRITE_PATTERNS.test(code);
  if (requireAuth && !/auth\(\)|getSession\(\)|requireAuth/.test(code))
    findings.push({ check: 'missing-auth', severity: 'error',
      detail: 'server action 未校验 session——任何人可调用' });
  if (requireValidation && !/\.parse\(|\.safeParse\(/.test(code))
    findings.push({ check: 'missing-validation', severity: 'error',
      detail: 'action 未使用 zod 校验输入' });
  const returnStmts = code.match(/return\s+(?:await\s+)?[^;]+/g) ?? [];
  for (const stmt of returnStmts)
    for (const pattern of sensitivePatterns)
      if (pattern.test(stmt))
        findings.push({ check: 'sensitive-return', severity: 'warn',
          detail: `返回值可能含敏感数据: ${stmt.slice(0, 50)}` });
  if (isWrite && !/idempotenc|idemKey/i.test(code))
    findings.push({ check: 'no-idempotency', severity: 'warn',
      detail: '写操作未使用幂等键——重试可能重复执行' });
  return { findings, ok: !findings.some(f => f.severity === 'error') };
}

// 自测
// 有 use server + 缺 auth + 缺 validation
const bad = `'use server';
export async function deleteUser(fd: FormData) {
  const id = fd.get('id');
  await db.users.delete({ where: { id } });
}`;
let r = scanActionSecurity(bad);
console.log(r.findings.some(f => f.check === 'missing-auth'));
console.log(r.findings.some(f => f.check === 'missing-validation'));
console.log(r.findings.some(f => f.check === 'no-idempotency'));   // delete = 写操作
console.log(r.ok === false);                             // 2 error

// 完整 action
const good = `'use server';
import { auth } from '@/lib/auth';
export async function updateProfile(fd: FormData) {
  const session = await auth();
  const data = ProfileSchema.safeParse(Object.fromEntries(fd));
  if (!data.success) return { error: 'invalid' };
  return await db.users.update({ where: { id: session.userId }, data: data.data });
}`;
r = scanActionSecurity(good);
console.log(r.ok === true && r.findings.length === 0);

// 敏感返回
const leaking = `'use server';
export async function getUser(id: string) {
  const user = await db.users.find(id);
  return { ...user, passwordHash: user.passwordHash };
}`;
r = scanActionSecurity(leaking, { requireAuth: false, requireValidation: false });
console.log(r.findings.some(f => f.check === 'sensitive-return' && f.severity === 'warn'));

// 非 server 文件跳过
console.log(scanActionSecurity('const x = 1;').skipped === true);
```

**评分点**：
- 五项检查（auth/validation/sensitive-return/idempotency/use-server 跳过）；写操作的幂等检测
- 严重度分级（auth/validation error；sensitive-return/idempotency warn——阻断与告警分离）
- 边界（非 server 文件跳过/完整 action 通过）；CI 自动化 + 人工 review 双防线
- 能说清「Server Action 的端点分散（每 'use server' 文件都是端点）——CI 自动扫描是安全审计的覆盖面保障」属于加分
