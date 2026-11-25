---
title: [AGT-488] 笔试题——实现多轮工具调用依赖检查（前置条件+缺失参数预检）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-488：手写依赖检查：工具前置条件声明、缺失参数预检、顺序校验

**需求与边界**：
- 输入：计划的工具调用序列、工具前置条件表；输出：可执行性检查结果。
- 边界要求：① 每工具声明前置（requires: {param, fromTool}）；② 预检缺失（前置工具不在序列中或顺序错误→提前报错不浪费调用）；③ 参数来源追踪（上游输出→下游输入的字段映射）；④ 可自动补全的（插入前置调用）给出建议。

**答**：
```javascript
const PRECONDITIONS = {
  send_email: [{ param: 'template', fromTool: 'get_template' },
               { param: 'recipient', fromTool: 'lookup_user' }],
  refund: [{ param: 'orderId', fromTool: 'query_order' }],
};
function checkDeps(sequence) {                    // [{tool, args}]
  const issues = [], fixes = [];
  const seen = new Map();                         // 已执行工具 → 输出字段
  for (let i = 0; i < sequence.length; i++) {
    const call = sequence[i];
    for (const pre of PRECONDITIONS[call.tool] ?? []) {
      const provided = call.args?.[pre.param] != null;
      if (provided) continue;                     // 显式提供则放行
      const upstream = seen.get(pre.fromTool);
      if (!upstream) {
        // 前置工具未执行：能否自动补全？
        if (!sequence.slice(0, i).some(c => c.tool === pre.fromTool)) {
          issues.push({ at: i, tool: call.tool,
            missing: pre.param, need: pre.fromTool });
          fixes.push({ insertBefore: i,
            call: { tool: pre.fromTool, args: {} } });
        } else issues.push({ at: i, tool: call.tool,
          missing: pre.param,
          reason: `${pre.fromTool} 在其后才执行（顺序错误）` });
      }
    }
    // 记录本工具产出字段（供下游依赖）
    for (const out of TOOL_OUTPUTS[call.tool] ?? [])
      seen.set(call.tool, out);
  }
  return { ok: issues.length === 0, issues,
    suggestedFixes: fixes,                        // 可自动插入前置调用
    orderFixed: fixes.length && issues.every(x => x.reason) };
}
// TOOL_OUTPUTS: { get_template: ['template'], query_order: ['orderId'] }
```

**评分点**:
- 前置条件表驱动检查：缺失参数、前置未执行、顺序错误三类问题区分。
- 自动补全建议（insertBefore 插入前置调用）——修复而不只报错。
- 工具产出字段追踪（上游输出→下游输入映射）。
- 提前预检（不浪费真实调用成本）。
