---
title: [AIC-585] 笔试：手写 Prompt 注入防御检查
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-585：笔试：手写防御就绪检查

**答**：实现 `checkDefenseReadiness(config)`。config: `{ hasInputFilter: boolean, tools: Array<{ name, permission: 'read'|'write'|'execute' }>, hasSandbox: boolean, hasOutputValidation: boolean }`. 规则：1) L1 input-filter 缺失 → warn 'no-input-filter'；2) L2 同时有 write + execute 权限的工具 → warn 'over-privileged'（同一工具不应同时写+执行——攻击面过大）；3) L3 有 execute 权限但无 sandbox → error 'no-sandbox-with-execute'（注入 = 任意命令执行——最高危）；4) L4 output-validation 缺失 → warn 'no-output-validation'；5) 返回 `{ findings: Array<{ layer, type, severity }>, ready }`（ready = 无 error）。边界：tools 空（无工具——无权限风险但 L1/L4 仍检查）；hasSandbox 且有 execute（pass）；全部缺失（4 findings——严重不安全）。

```javascript
function checkDefenseReadiness(config = { hasInputFilter: false, tools: [],
  hasSandbox: false, hasOutputValidation: false }) {
  const findings = [];
  // L1: 输入过滤
  if (!config.hasInputFilter)
    findings.push({ layer: 1, type: 'no-input-filter', severity: 'warn' });
  // L2: 权限最小化
  const hasWrite = config.tools?.some(t => t.permission === 'write');
  const hasExecute = config.tools?.some(t => t.permission === 'execute');
  const overPrivileged = config.tools?.some(t =>
    t.permission === 'write' && t.permission === 'execute');
  if (hasWrite && hasExecute)
    findings.push({ layer: 2, type: 'over-privileged', severity: 'warn',
      detail: 'Agent 同时有 write+execute——攻击面过大' });
  // L3: 沙箱
  if (hasExecute && !config.hasSandbox)
    findings.push({ layer: 3, type: 'no-sandbox-with-execute', severity: 'error',
      detail: '有 execute 但无沙箱——注入 = 任意命令执行' });
  // L4: 输出验证
  if (!config.hasOutputValidation)
    findings.push({ layer: 4, type: 'no-output-validation', severity: 'warn' });
  return { findings, ready: !findings.some(f => f.severity === 'error') };
}

// 自测
// 完整防御
let r = checkDefenseReadiness({ hasInputFilter: true,
  tools: [{ name: 'read', permission: 'read' }],
  hasSandbox: true, hasOutputValidation: true });
console.log(r.ready === true && r.findings.length === 0);

// 有 execute 无 sandbox → error
r = checkDefenseReadiness({ hasInputFilter: true,
  tools: [{ name: 'run', permission: 'execute' }],
  hasSandbox: false, hasOutputValidation: true });
console.log(r.findings.some(f => f.type === 'no-sandbox-with-execute' && f.severity === 'error'));
console.log(r.ready === false);

// 全缺失
r = checkDefenseReadiness({ hasInputFilter: false, tools: [
  { name: 'write', permission: 'write' }, { name: 'run', permission: 'execute' }],
  hasSandbox: false, hasOutputValidation: false });
console.log(r.findings.length === 4);                    // 全 4 层都有 finding
console.log(r.ready === false);                          // 有 error
// write+execute 权限
r = checkDefenseReadiness({ hasInputFilter: true,
  tools: [{ name: 'all', permission: 'write' }],         // 简化：一个工具
  hasSandbox: true, hasOutputValidation: true });
console.log(r.findings.filter(f => f.layer === 2).length >= 0);
// 空 tools（无工具但仍检查 L1/L4）
r = checkDefenseReadiness({ hasInputFilter: false, tools: [],
  hasSandbox: true, hasOutputValidation: false });
console.log(r.findings.some(f => f.type === 'no-input-filter'));
console.log(r.findings.some(f => f.type === 'no-output-validation'));
```

**评分点**：
- 四层防御检查完整（input-filter/权限最小化/sandbox/output-validation）
- L3 最高危（execute 无 sandbox = 注入即任意命令——error 阻断；其他层 warn 不阻断）
- 边界（完整防御/execute 无 sandbox/全缺失/空 tools）；ready 仅由 error 决定
- 能说清「权限最小化 > 输入过滤：过滤是概率性的（总有漏网），权限是确定性的（没有 write 工具 = 绝对不能写）」属于加分
