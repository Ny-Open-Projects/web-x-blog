---
title: [ARC-150] AI Agent 与前端应用集成架构（流式 UI / 工具调用 / 安全沙箱）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-150：AI Agent 与前端应用集成架构（流式 UI / 工具调用 / 安全沙箱）如何设计？
**答**：
- 流式协议设计：SSE 承载三类事件（token 增量、工具调用事件、最终结果与元数据），前端按事件类型分流渲染——token 进打字机区域、工具调用渲染成可展开的过程卡片、错误渲染成可重试状态。
- 中断与恢复：流式生成必须支持取消（AbortController 级联到服务端终止推理），长任务支持断点恢复（任务 id + 事件序号续传）。
- 工具调用安全：工具白名单注册（每个工具有 schema 与权限级别），高危工具（发消息/退款/删除）必须用户显式确认；前端渲染"将要执行的操作"卡片，确认后才回调执行。
- 沙箱边界：Agent 的输出永远以"数据"进入前端，渲染层做 XSS 防护（markdown 白名单渲染），绝不允许 LLM 输出直接 eval/innerHTML。

```typescript
// Agent 流式事件协议（SSE）
type AgentEvent =
  | { type: 'token'; delta: string }                                  // 内容增量
  | { type: 'tool_call'; id: string; name: string; args: unknown }    // 工具调用
  | { type: 'tool_result'; id: string; result: unknown; ok: boolean } // 工具结果
  | { type: 'done'; usage: Usage; messageId: string }
  | { type: 'error'; code: string; retryable: boolean };

// 前端消费：流式渲染 + 高危工具确认
async function runAgent(query: string, ui: AgentUI, signal: AbortSignal) {
  const res = await fetch('/agent/run', { method: 'POST', body: JSON.stringify({ query }), signal });
  for await (const ev of parseSSE(res.body!)) {
    switch (ev.type) {
      case 'token':      ui.appendToken(ev.delta); break;
      case 'tool_call':  // 高危工具 → 渲染确认卡片，等用户点击
        if (TOOL_ACL[ev.name] === 'dangerous') {
          const ok = await ui.confirmToolCall(ev);      // 用户显式确认，否则跳过该工具
          if (!ok) { await api.agent.skip(ev.id); break; }
        }
        ui.showToolProgress(ev); break;
      case 'tool_result': ui.completeToolCard(ev); break;
      case 'error':       ev.retryable ? ui.showRetry(ev) : ui.showError(ev); break;
    }
  }
}
// 渲染安全：LLM 输出统一走 sanitizeMarkdown（白名单标签），禁止 raw HTML 注入
```

## 追问（补充）

**追问**：

1. token 成本与首字延迟怎么权衡？→ 首字靠尽早 flush 并把简短计划先输出，成本靠裁剪历史与限制单轮长度，两者共用一条可观测链路。
2. 模型给出的引用是编的怎么办？→ 引用必须落到可校验的文档 id 与片段，点击能定位原文，校验不过就标注未验证而不是直接展示。
3. 工具调用失败怎么兜底？→ 区分参数错误与外部故障，参数错误回灌模型修正一次，外部故障降级为告知用户并给替代路径，禁止静默重试造成重复副作用。
