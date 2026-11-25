---
title: [AGT-175] Agent 应用如何产品化，让非开发者也能配置自己的 Agent？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-175：Agent 应用如何产品化，让非开发者也能配置自己的 Agent？
**答**：
- 核心是把「写 prompt + 选模型 + 配工具」翻译成非开发者语言：角色（它是谁）、知识（它知道什么）、动作（它能做什么）、边界（它不能做什么）四步向导，配置项背后仍生成标准化的 Agent 描述。
- 配置分层：模板市场给 80% 场景开箱即用，表单级微调（语气/知识源/工具开关）覆盖 19%，只有 1% 真需要写 prompt——「默认好，可深入」。
- 危险配置的护栏：非开发者不能授予高危工具权限（写库/发款默认锁死需管理员开）、配置变更要走「测试对话预览 → 发布」流程，发布前自动跑冒烟评测集。
- 可观测闭环：给配置者看「任务完成率、常见失败原因、用户点踩聚类」的产品化报表，而不是技术 trace。

```typescript
// 面向非开发者的 Agent 配置模型 → 编译为标准 Agent 描述
import { z } from 'zod';

const NonDevConfig = z.object({
  name: z.string(), role: z.string(),                        // 角色：它是谁、什么语气
  knowledge: z.array(z.object({ source: z.enum(['faq', 'doclib', 'url']), ref: z.string() })),
  actions: z.array(z.object({
    toolId: z.string(), enabled: z.boolean(),
    riskLevel: z.enum(['read', 'write']).default('read'),
  })),
  boundaries: z.array(z.string()),                           // 边界：不能做什么（自然语言）
  escalation: z.enum(['none', 'human_handoff']).default('human_handoff'),
});
type NonDevConfig = z.infer<typeof NonDevConfig>;

export function compileConfig(cfg: NonDevConfig, adminUnlocked: string[]): CompiledAgent {
  // 写操作工具：未被管理员解锁的自动剔除（非开发者无权授予高危权限）
  const safeActions = cfg.actions.filter(
    (a) => a.enabled && (a.riskLevel === 'read' || adminUnlocked.includes(a.toolId)),
  );
  const system = [
    `你是${cfg.name}。${cfg.role}`,
    `知识来源：${cfg.knowledge.map((k) => k.ref).join('、')}，仅依据知识来源回答。`,
    `可用动作：${safeActions.map((a) => a.toolId).join('、') || '无，仅回答问题'}。`,
    `禁止：${cfg.boundaries.join('；')}。无法处理时转人工。`,
  ].join('\n');
  return { system, tools: safeActions.map((a) => a.toolId), smokeRequired: true };
}
interface CompiledAgent { system: string; tools: string[]; smokeRequired: boolean; }
```
