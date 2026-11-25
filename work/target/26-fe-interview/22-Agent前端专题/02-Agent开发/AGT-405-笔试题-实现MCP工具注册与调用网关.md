---
title: [AGT-405] 笔试题——实现 MCP 工具注册与安全调用网关？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-405：手写工具网关：注册校验、命名空间、权限分级、审计

**需求与边界**：
- 输入：工具定义数组、调用请求 {user, tool, args}；输出：调用结果或拒绝原因。
- 边界要求：① 工具名重复/非法字符注册即拒绝；② 按用户 ACL 过滤可见工具与可调用工具（读/写分级）；③ 调用超时与结果脱敏；④ 每次调用审计留痕（成功与拒绝都记）。

**答**：
```javascript
class ToolGateway {
  constructor() { this.tools = new Map(); this.audit = []; }
  register(def) {
    if (!/^[a-z][a-z0-9_.]*$/i.test(def.name))
      throw new Error(`非法工具名: ${def.name}`);
    if (this.tools.has(def.name))
      throw new Error(`工具重名: ${def.name}`);           // 命名空间冲突
    if (!def.schema) throw new Error('缺少参数 schema');
    this.tools.set(def.name, { ...def, timeout: def.timeout ?? 5000 });
    return this;
  }
  async call({ user, tool, args }) {
    const def = this.tools.get(tool);
    const deny = (reason) => { this.audit.push(
      { ts: Date.now(), user: user.id, tool, ok: false, reason });
      return { error: reason }; };
    if (!def) return deny('TOOL_NOT_FOUND');
    if (!user.acl.includes(tool) && !user.acl.includes('*'))
      return deny('NO_PERMISSION');                      // 工具级权限
    if (def.kind === 'write' && !user.canWrite)
      return deny('WRITE_FORBIDDEN');                    // 读写分级
    const safe = def.schema.safeParse(args ?? {});
    if (!safe.success) return deny('BAD_ARGS: ' + safe.error.message);
    const result = await withTimeout(def.run(safe.data), def.timeout)
      .catch(e => ({ error: 'TOOL_ERROR: ' + e.message }));
    const clean = redact(result);                        // PII 脱敏
    this.audit.push({ ts: Date.now(), user: user.id, tool,
      ok: !result.error, argsHash: hash(args) });        // args 只存 hash
    return clean;
  }
  list(user) {                                           // 可见工具（给 LLM）
    return [...this.tools.values()]
      .filter(t => user.acl.includes(t.name) || user.acl.includes('*'));
  }
}
const withTimeout = (p, ms) => Promise.race(
  [p, new Promise((_, rej) => setTimeout(() => rej(new Error('超时')), ms))]);
```

**评分点**:
- 注册期校验（非法名/重名/缺 schema）与调用期校验（权限/读写分级/参数）分层清晰。
- 审计完整：拒绝也留痕；args 只存 hash（敏感参数不落明文）。
- 超时用 Promise.race 强制；结果输出前统一 redact 脱敏。
- list(user) 按权限过滤可见工具（上下文注入前的过滤）。
