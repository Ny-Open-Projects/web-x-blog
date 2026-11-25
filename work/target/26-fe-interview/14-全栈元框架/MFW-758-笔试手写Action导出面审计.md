---
title: [MFW-758] 笔试：手写 Action 导出面审计
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-758：笔试：手写 Action 导出面审计

**答**：实现 `auditActionExports(code, { requireAuthForWrite })`。规则：1) 检测 'use server' 文件；2) 提取**导出函数**（export async function/export const = action 端点）与非导出函数（function 无 export = 内部函数）；3) **写操作的 auth 检查**：导出的写 action 是否调 auth/getSession（RBL-733 的导出维度）；4) **非导出函数不应有 'use server' 内部标注**（文件级标注已覆盖——内部标注 = 冗余）；5) **导出数量审计**：导出的 action 数量（暴露面统计——actions.ts 的导出面 = 安全面 RBL-757）。返回 `{ exported: string[], internal: string[], findings: Array<{ func, check, severity }>, ok }`。边界：无 'use server'（跳过）；无导出（纯内部函数——合法）；全部导出且无 auth（全 error）。

```javascript
function auditActionExports(code = '', { requireAuthForWrite = true } = {}) {
  if (!code.includes("'use server'") && !code.includes('"use server"'))
    return { exported: [], internal: [], findings: [], ok: true, skipped: true };
  const exported = [], internal = [], findings = [];
  // 提取函数声明
  const fnRegex = /^(?:export\s+)?(?:async\s+)?function\s+(\w+)/gm;
  const constFnRegex = /^export\s+const\s+(\w+)\s*=\s*async/gm;
  for (const m of code.matchAll(fnRegex)) {
    const isExport = code.match(new RegExp(`export\\s+(?:async\\s+)?function\\s+${m[1]}\\b`));
    if (isExport) exported.push(m[1]); else internal.push(m[1]);
  }
  for (const m of code.matchAll(constFnRegex)) exported.push(m[1]);
  // 写操作 auth 检查
  const WRITE = /\.(insert|update|delete|create|upsert)\(/;
  for (const fn of exported) {
    const fnBody = extractFnBody(code, fn);
    if (fnBody && WRITE.test(fnBody)) {
      if (requireAuthForWrite && !fnBody.includes('auth()') && !fnBody.includes('session'))
        findings.push({ func: fn, check: 'missing-auth', severity: 'error',
          detail: `导出的写 action ${fn} 未校验 session` });
    }
  }
  return { exported, internal, findings, ok: !findings.some(f => f.severity === 'error') };
}
function extractFnBody(code, fnName) {
  const regex = new RegExp(`(?:export\\s+)?(?:async\\s+)?function\\s+${fnName}\\b[\\s\\S]*?\\n\\}`, 'm');
  return regex.exec(code)?.[0] ?? null;
}

// 自测
const code = `'use server';
export async function placeOrder(data) {
  const session = await auth();
  const order = await db.order.create({ data: { ...data, userId: session.id } });
  await _updateInventory(data.sku, data.qty);
  return order;
}
export async function deleteAll() {                        // 缺 auth！
  await db.order.deleteMany({});
}
async function _updateInventory(sku, qty) {
  return db.inventory.update({ where: { sku }, data: { count: { decrement: qty } } });
}`;
let r = auditActionExports(code);
console.log(r.exported.join(',') === 'placeOrder,deleteAll');
console.log(r.internal.join(',') === '_updateInventory');
console.log(r.findings.some(f => f.func === 'deleteAll' && f.check === 'missing-auth'));
console.log(!r.findings.some(f => f.func === 'placeOrder'));   // 有 auth
console.log(r.ok === false);                             // deleteAll 缺 auth

// 非 server 文件
console.log(auditActionExports('const x = 1;').skipped === true);
// 纯内部
r = auditActionExports(`'use server';
async function internalHelper() { return db.query(); }`);
console.log(r.exported.length === 0 && r.internal.length === 1);
console.log(r.ok === true);                              // 无导出 = 无端点 = 无 auth 需求
```

**评分点**：
- 导出面提取（export async function + export const = 端点清单——安全面审计）；非导出区分
- 写操作的 auth 逐个检查（导出的写 action 缺 auth = error）；非 server 跳过
- 边界（纯内部函数/非 server/全导出）；导出面 = 安全面的设计原则
- 能说清「'use server' 文件级标注 = 所有导出函数都是 HTTP 端点——导出面就是安全面，非导出函数是内部实现」属于加分
