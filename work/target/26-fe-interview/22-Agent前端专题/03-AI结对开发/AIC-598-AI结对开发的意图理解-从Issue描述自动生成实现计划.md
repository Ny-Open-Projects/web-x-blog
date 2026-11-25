---
title: [AIC-598] 从 Issue 描述自动生成实现计划
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-598：Issue 到实现计划

**答**:
- 从 Issue 描述到实现计划：1) **Issue 解析**（用户故事 / bug 报告 / feature request → 结构化任务（goal/constraints/acceptance criteria）；2) **代码库分析**（AI 读取相关文件 → 理解现有架构/依赖/模式（Agent 的第一步 read RBL-518）；3) **计划生成**：分解为步骤（文件级变更清单 + 每步的预期结果——RBL-519 分解器）；4) **计划审查**（人审计划而非直接审代码——"先审计划再执行"的流程（审查计划的成本低——审代码的成本高 RBL-532）。
- 计划的结构：1) **文件级步骤**（`1. 修改 src/auth/login.ts 添加 rate limit`；2. 新建 src/auth/rate-limit.ts`）；2) **每步的验证**（`步骤 1 后运行：pnpm test auth`——步骤级验证 RBL-558 安全守卫的分解版）；3) **回滚点**（每个步骤是一个回滚点——失败时回滚到最后一个成功步骤 RBL-722 Saga）。
- 追问钩子：为什么「先审计划再执行」比「直接执行后审代码」更高效？——直接执行：AI 生成 1000 行代码 → 人审 1000 行（发现方向错误 = 全部浪费）；先审计划：AI 先生成 20 行计划 → 人审 20 行（方向错误 = 修改计划——浪费最小化 RBL-532 意图验证的计划版）；「审查计划 = 意图的前置验证」：计划审批通过 → AI 执行 → 代码审查只需验证"执行是否匹配计划"（不是验证"方向是否正确"——方向已在计划阶段确认）——审查成本的瀑布式递减。

```typescript
// Issue 到实现计划
interface ImplementationStep {
  order: number;
  action: 'create' | 'modify' | 'delete';
  file: string;
  description: string;
  verify?: string;         // 步骤验证命令
}
interface ImplementationPlan {
  steps: ImplementationStep[];
  risks: string[];
  testPlan: string;
}
async function generateImplementationPlan(issue: string, codebase: CodebaseContext): Promise<ImplementationPlan> {
  // AI 分析 Issue + 代码库 → 生成计划
  const plan = await llm.generate(`
    Issue: ${issue}
    Codebase: ${codebase.summary}
    Related files: ${codebase.relatedFiles}
    
    Generate a step-by-step implementation plan with:
    1. File-level changes (create/modify/delete)
    2. Verification steps for each change
    3. Risk assessment
    4. Test plan
  `);
  return parsePlan(plan);
}
```
