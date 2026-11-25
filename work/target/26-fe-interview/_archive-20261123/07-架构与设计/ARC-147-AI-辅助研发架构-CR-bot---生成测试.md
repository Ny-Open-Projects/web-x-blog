---
title: [ARC-147] AI 辅助研发架构（CR bot / 生成测试 / 文档生成）如何集成到流水线？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-147：AI 辅助研发架构（CR bot / 生成测试 / 文档生成）如何集成到流水线？
**答**：
- 流水线集成原则：AI 是"并行建议者"而不是"串行守门员"——MR 触发时静态分析与 AI review 并行跑，AI 结论以评论形式输出（附置信度与定位），只有明确的高危项才升级为阻塞。
- 三个高价值场景：AI Code Review（风格/逻辑/安全问题提示）、测试草稿生成（为 diff 生成候选用例，人审核后入库）、文档生成（从 API diff 生成变更说明草稿）。
- 效果度量：采纳率（建议被接受比例）、误报率、平均修复提速——没有度量的 AI 集成会变成"流水线噪音"。
- 成本与边界：LLM 调用按 diff 大小分片、缓存重复上下文；安全红线：私有代码外发要走内部网关与脱敏，模型不落盘敏感数据。

```yaml
# AI 辅助研发流水线配置
ai_pipeline:
  triggers:
    on_mr:
      - name: static_analysis        # 确定性检查先行
        run: lint + type-check + security-scan
      - name: ai_review              # 与上面并行，不阻塞静态分析
        model: code-review-large
        input: diff + 相关文件上下文（最多 8 文件，按依赖裁剪）
        output: 评论（severity: info|warn|critical, 每条附行号定位与修复建议）
        blocking: critical           # 只有 critical 升级为阻塞，且需二次确认规则命中
        budget: { max_tokens: 50k, timeout: 120s }
      - name: test_draft             # 为 diff 生成测试草稿，不直接入库
        output: "MR 评论附加候选用例（含 @标记，人 review 后拷贝入测试文件）"
      - name: doc_draft              # API diff → 文档变更草稿
        output: docs PR（draft 状态，作者确认后提交）
  cache:
    strategy: 按文件内容 hash 缓存分析结果，重复 MR 免费重放
  security:
    - 代码经内部 LLM 网关（脱敏：密钥/内网域名/token 替换占位符后再外发）
  metrics: { 采纳率, 误报率, MR 平均修复时长变化 }
```
