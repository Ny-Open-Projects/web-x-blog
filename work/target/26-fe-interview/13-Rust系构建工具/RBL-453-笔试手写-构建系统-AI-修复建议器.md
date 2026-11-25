---
title: [RBL-453] 笔试：手写构建错误 AI 修复建议器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-453：手写构建错误 AI 修复建议器
**答**：实现 `createFixSuggester({ llm, registry })`：1) 流程：错误 → 结构化上下文（错误码+代码帧+相关配置）→ prompt 组装 → LLM → 建议结构化解析（{ explain, patch, confidence }）；2) prompt 注入注册表知识（错误码文档/历史修复案例 top3——RAG 式检索）；3) 建议可验证：patch 附带验证命令（如重新构建该模块）——AI 建议必须可验证；4) 人工确认门（不自动 apply——建议式）；5) 反馈闭环：用户采纳/拒绝记录 → 优化检索库；6) 降级：LLM 不可用 → 注册表静态建议兜底。

```javascript
export function createFixSuggester({ llm, registry, history }) {
  async function suggest(buildError, context) {
    const doc = registry.get(buildError.code)
    // RAG：历史相似案例 top3
    const cases = history.search(buildError.code, buildError.message, 3)
    const prompt = [
      `你是前端构建专家。请分析以下构建错误并给出修复。`,
      `错误码: ${buildError.code}（文档: ${doc?.doc ?? '无'}）`,
      `消息: ${buildError.message}`,
      `代码帧:\n${buildError.codeframe ?? context.code ?? '无'}`,
      `历史案例:\n${cases.map((c) => `- ${c.summary} → ${c.fix}`).join('\n')}`,
      `输出 JSON: { "explain": string, "patch": string, "confidence": 0-1, "verify": string }`,
    ].join('\n')
    try {
      const raw = await llm(prompt)
      const parsed = JSON.parse(raw)
      return { ...parsed, source: 'llm',
        guardrails: { autoApply: false, verifyCommand: parsed.verify } }   // 人工门 + 可验证
    } catch {
      return { explain: doc?.fix ?? '见文档', patch: null, confidence: 0.3,
        source: 'registry-fallback', guardrails: { autoApply: false } }    // 静态兜底
    }
  }

  function feedback(suggestionId, accepted) {
    history.record({ suggestionId, accepted, at: Date.now() })           // 采纳率进检索库权重
  }
  return { suggest, feedback }
}
```
**评分点**：
- 结构化上下文注入（错误码 + 代码帧 + RAG 历史案例——不是裸丢给 LLM）
- 可验证性（patch 附 verify 命令——AI 建议必须可验证）
- 人工确认门（autoApply: false——破坏性操作不自动执行）
- 双层降级（LLM 失败 → 注册表静态建议）+ 反馈闭环（采纳率驱动检索库）
