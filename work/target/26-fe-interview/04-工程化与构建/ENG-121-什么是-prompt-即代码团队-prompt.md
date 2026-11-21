---
title: [ENG-121] 什么是 prompt 即代码？团队 prompt 仓库怎么版本化？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-121：什么是 prompt 即代码？团队 prompt 仓库怎么版本化？
**答**：
- 把高频场景的 prompt（review、生成测试、文案、迁移）沉淀为仓库内文件，像代码一样走 PR 评审与版本号。
- 收益：最佳实践复用、prompt 改动可 review 可回滚、可被脚本/网关按名引用（prompt://code-review@v3）。
- 文件结构：场景名 + 指令正文 + 输出格式约定 + 版本与变更记录，与代码同仓或独立 prompts 仓。
- 演进方向：prompt 文件被 CI 与工具链消费（review bot 加载 code-review.md），改 prompt 等于改工具行为。

```markdown
<!-- prompts/code-review.md，纳入 git 管理，变更走 PR 评审 -->
# 场景：前端代码审查
# 版本：v3（变更记录见 prompts/CHANGELOG.md）

你是一名资深前端 reviewer，按以下顺序审查：
1. 正确性：边界条件、异步竞态、类型安全
2. 可维护性：命名、重复逻辑、模块边界
3. 安全：XSS 风险、凭证泄漏、依赖风险

输出格式：每条意见标注严重级别 block 或 suggest，
必须包含文件与行号，并给出最小修复示例。
```
