---
title: [AIC-584] Prompt 注入的防御体系
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-584：Prompt 注入防御体系

**答**:
- Prompt 注入的四层防御（RBL-546 的体系化）：1) **输入过滤**（检测注入模式——RBL-547 的检测器（"ignore previous" → 拒绝或标记）；2) **权限最小化**（Agent 的工具白名单——只暴露必要的工具（不需要 write 就不暴露 write RBL-520）；3) **沙箱执行**（Agent 代码在沙箱中运行——即使注入成功也限制破坏 RBL-528；4) **输出验证**（AI 的输出过安全扫描——检查是否包含恶意代码/敏感数据泄露 RBL-942 的运行时版）。
- 防御的优先级：输入过滤（第一道——最便宜）→ 权限最小化（第二道——减少攻击面）→ 沙箱（第三道——隔离爆炸半径）→ 输出验证（第四道——最终把关）；「纵深防御」：每一层的绕过都被下一层拦截。
- 追问钩子：为什么「权限最小化」比「输入过滤」更重要？——输入过滤 = 模式匹配（注入模式千变万化——总有漏网的：base64 编码/多语言/间接引用——new patterns 不断出现）；权限最小化 = 减少攻击面（即使注入成功——Agent 没有危险工具可调用——破坏范围受限于权限集）；「过滤的不完备性」vs「权限的确定性」：权限是确定性的（没有 write 工具 = 绝对不能写文件）；过滤是概率性的（可能有漏网注入）——确定性防御 > 概率性防御。

```typescript
// 四层 Prompt 注入防御
const DEFENSE_LAYERS = {
  1: { name: 'input-filter', tool: detectInjection, cost: 'low', reliability: 'medium' },
  2: { name: 'permission-minimization', tool: 'tool-registry', cost: 'setup',
       reliability: 'high', note: '确定性：无 write 工具 = 绝对不写' },
  3: { name: 'sandbox', tool: 'sandbox-execute', cost: 'medium',
       reliability: 'high', note: '隔离：破坏限制在沙箱内' },
  4: { name: 'output-validation', tool: 'security-scan', cost: 'medium',
       reliability: 'medium' },
};
// 纵深防御检查
function checkDefenseReadiness(config: {
  hasInputFilter: boolean; toolPermissions: string[];
  hasSandbox: boolean; hasOutputValidation: boolean;
}) {
  const issues = [];
  if (!config.hasInputFilter) issues.push('L1: 无输入过滤——注入模式未检测');
  if (config.toolPermissions.includes('write') && config.toolPermissions.includes('execute'))
    issues.push('L2: Agent 同时有 write+execute 权限——攻击面过大');
  if (!config.hasSandbox && config.toolPermissions.includes('execute'))
    issues.push('L3: 有 execute 但无沙箱——注入 = 任意命令执行');
  if (!config.hasOutputValidation)
    issues.push('L4: 无输出验证——AI 输出未经过安全扫描');
  return { issues, ready: issues.length === 0 };
}
```
