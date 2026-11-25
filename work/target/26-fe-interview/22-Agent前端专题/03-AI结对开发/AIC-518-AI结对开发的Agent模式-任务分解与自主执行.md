---
title: [AIC-518] Agent 模式：任务分解与自主执行
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-518：Agent 模式的任务分解

**答**:
- Agent 模式的核心能力：1) **任务分解**（"重构认证模块" → AI 分解为：1. 读现有代码 2. 设计新架构 3. 逐步修改文件 4. 运行测试 5. 修 fix——自主执行多步骤；2) **工具调用**（AI 不只写码——还调用工具：读文件/写文件/运行命令/搜索代码/运行测试（多工具编排）；3) **自主修正**（测试失败 → AI 读错误 → 修复代码 → 重跑测试（迭代闭环——人不需要介入每步）；4) **人的介入点**（开始：任务描述；结束：审查 diff；中间：AI 卡住时请求帮助（RBL-501 的 Agent 模式深化）。
- Agent 的可靠性边界：1) **可验证的任务**（有测试覆盖 → Agent 自主可靠（测试通过 = 完成验证）；2) **不可验证的任务**（无测试/UI 变更 → Agent 不可靠（无法验证正确性——需要人审）；3) **Agent 的信任策略**：有测试 → 全自动；无测试 → AI 先写测试 → 人审测试 → Agent 执行；「测试覆盖率 = Agent 的信任上限」。
- 追问钩子：为什么「Agent 模式的可靠性」与「测试覆盖率」直接相关？——Agent 的核心循环 = 生成 → 测试 → 修正（测试是 Agent 的"眼睛"——Agent 通过测试结果感知对错）；无测试 = Agent 盲执行（不知道对错——只能靠 LLM 猜测）；「测试 = Agent 的传感器」：测试覆盖率 100% → Agent 每步都有传感器 → 可靠性高；0% → Agent 盲飞——「测试覆盖率不是代码质量指标而是 Agent 的基础设施」（Agent 时代测试的新意义）。

```typescript
// Agent 的任务执行循环
interface AgentStep { action: string; tool: string; result?: string; success?: boolean; }
async function agentLoop(task: string, tools: ToolRegistry, maxSteps = 20): Promise<AgentStep[]> {
  const steps: AgentStep[] = [];
  for (let i = 0; i < maxSteps; i++) {
    // AI 决定下一步
    const decision = await llm.decide(task, steps);      // 基于历史决定下一步
    if (decision.action === 'done') break;
    if (decision.action === 'need-help') {
      steps.push({ action: 'need-help', tool: 'human', detail: decision.question });
      break;
    }
    // 执行工具
    const result = await tools.execute(decision.tool, decision.args);
    steps.push({ action: decision.action, tool: decision.tool, result, success: result.ok });
    // 测试失败 → AI 自动修正
    if (decision.tool === 'run-tests' && !result.ok) {
      // AI 读测试错误 → 生成修复 → 重跑
    }
  }
  return steps;
}
```
