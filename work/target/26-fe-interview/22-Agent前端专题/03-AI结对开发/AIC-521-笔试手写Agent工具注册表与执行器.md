---
title: [AIC-521] 笔试：手写 Agent 工具执行器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-521：笔试：手写 Agent 工具执行器

**答**：实现 `createToolExecutor(registry, { permission })`。registry: `Tool[]`（RBL-520 格式）。规则：1) `execute(name, args)`：查找工具 → schema 校验 → 权限检查（permission='read' 直接执行；'write' → 日志记录（log tool call）+ 执行；'execute' → sandbox 标记（隔离执行——不允许写宿主文件系统））→ 执行；2) 未知工具 → 抛错；3) schema 校验失败 → 返回错误（不执行——LLM 可重试）；4) **权限日志**：write/execute 的调用被记录（审计链 RBL-519）；5) `list()` 返回工具清单（LLM 的 system prompt 的一部分——让 LLM 知道有哪些工具）。边界：registry 空；schema 校验失败的 args（null/undefined）；execute 抛错（透传给 LLM——错误也是信息）。

```javascript
function createToolExecutor(registry = [], { permission = 'all', logger = console.log } = {}) {
  const auditLog = [];
  return {
    async execute(name, args) {
      const tool = registry.find(t => t.name === name);
      if (!tool) throw new Error(`Unknown tool: ${name}. Available: ${registry.map(t => t.name).join(', ')}`);
      const parsed = tool.schema.safeParse(args);
      if (!parsed.success)
        return { error: true, message: `Invalid args: ${parsed.error.message}`, retry: true };
      // 权限检查
      if (tool.permission === 'write') {
        auditLog.push({ tool: name, args, ts: Date.now() });
        logger(`[WRITE] ${name}(${JSON.stringify(args)})`);
      }
      if (tool.permission === 'execute') {
        auditLog.push({ tool: name, args, ts: Date.now(), sandbox: true });
        logger(`[EXECUTE] ${name}(${JSON.stringify(args)})`);
      }
      try {
        const result = await tool.execute(parsed.data);
        return { error: false, result };
      } catch (e) {
        return { error: true, message: e.message, retry: false };   // 执行错误：透传
      }
    },
    list() {
      return registry.map(t => ({ name: t.name, description: t.description, permission: t.permission }));
    },
    auditLog: () => [...auditLog],
  };
}

// 自测
const { z } = { z: { object: (s) => ({ safeParse: (d) => {
  const keys = Object.keys(s);
  for (const k of keys) if (d[k] === undefined) return { success: false, error: { message: `missing ${k}` } };
  return { success: true, data: d };
}})}, string: 'string' };
const registry = [
  { name: 'read', description: 'Read file', permission: 'read',
    schema: { safeParse: (d) => d.path ? { success: true, data: d } : { success: false, error: { message: 'path required' } } },
    execute: async ({ path }) => `content of ${path}` },
  { name: 'write', description: 'Write file', permission: 'write',
    schema: { safeParse: (d) => d.path && d.content ? { success: true, data: d } : { success: false, error: { message: 'path+content required' } } },
    execute: async ({ path, content }) => `written ${path}` },
];
const exec = createToolExecutor(registry);
// read：直接执行
let r = await exec.execute('read', { path: '/a.ts' });
console.log(r.result === 'content of /a.ts' && !r.error);
// schema 校验失败
r = await exec.execute('read', {});
console.log(r.error === true && r.retry === true);       // LLM 可重试
// 未知工具
e = null; try { await exec.execute('ghost', {}); } catch (x) { e = x; }
console.log(/Unknown tool/.test(e.message));
// write：审计日志
await exec.execute('write', { path: '/b.ts', content: 'x' });
console.log(exec.auditLog().length === 1);               // write 有审计
console.log(exec.auditLog()[0].tool === 'write');
// list
console.log(exec.list().length === 2);
```

**评分点**：
- schema 校验前置（无效参数不执行——返回 retry 让 LLM 重试）；未知工具的错误信息含可用清单
- 权限分级：read 直接执行 / write 审计日志 / execute 沙箱——RBL-520 的权限分级落地
- 边界（空 registry/缺参数/execute 抛错透传——错误也是 LLM 的信息）；auditLog 可审计
- 能说清「Agent 工具的 schema = LLM 与工具的安全网：无效参数被拦截并返回错误让 LLM 重试」属于加分
