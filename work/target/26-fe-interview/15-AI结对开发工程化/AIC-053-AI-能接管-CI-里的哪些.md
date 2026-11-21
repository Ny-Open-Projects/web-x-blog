---
title: [AIC-053] AI 能接管 CI 流水线里的哪些工作？哪些 AI 任务适合放在 CI、哪些必须留在本地？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-053：AI 能接管 CI 流水线里的哪些工作？哪些 AI 任务适合放在 CI、哪些必须留在本地？
**答**：
- 适合进 CI 的：失败日志归因（把报错翻译成人话 + 指向可疑提交）、AI review 门禁（AIC-041）、commit 规范校验、文档增量更新、生成的产物快照对比。
- 特点是「确定性输入 + 可判定输出 + 失败可重试」，且结果以评论/检查项形式回流 PR，不阻塞主流程太久。
- 必须留本地的：交互式开发中的补全与 chat、需要来回澄清的设计任务——CI 是批处理环境，不适合对话式工作。
- CI 里的 AI 要点：预算与超时（每次 review 限时限量）、密钥管理（LLM key 不进日志）、幂等（重跑结果一致）、降级（LLM 挂了门禁怎么走——建议「降级为仅确定性检查并标注」而非全放行）。
- 追问钩子：CI AI 任务的成本要并入构建成本核算，防止某天账单爆炸（呼应 AIC-173 预算守卫）。

```yaml
# CI 中的 AI 任务示例（GitHub Actions 语意）
ai-tasks:
  on-failure:
    - name: 日志归因
      prompt: prompts/ci-failure.md
      output: PR comment
  on-pr:
    - name: ai-review
      timeout: 120s
      budget_tokens: 100000
      fallback: only-deterministic-checks   # LLM 不可用时降级
```
