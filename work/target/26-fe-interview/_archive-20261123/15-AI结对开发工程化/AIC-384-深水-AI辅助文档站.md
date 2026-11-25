---
title: [AIC-384] 团队文档站与 AI 问答如何一体化建设（文档写给人读也写给 AI 读）？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-384：团队文档站与 AI 问答如何一体化建设（文档写给人读也写给 AI 读）？
**答**：
- 结构化优先：文档用清晰的结构（标题层级/表格/代码块），人和 AI 都受益。
- 元数据增强：每篇文档带 front-matter（owner/更新日期/关联系统），检索与新鲜度判断用。
- 过期检测：AI 定期比对文档与代码事实（配置项/流程步骤），过期自动提 PR 或标记。
- 问答反馈：文档站嵌入 AI 问答，未命中问题回流指导补文档——问答日志就是文档缺口清单。

```javascript
const docsForBoth = {
  meta: 'front-matter: owner/updated/related',
  freshness: 'AI 比对代码事实 → 过期 PR/标记',
  feedback: '站内 AI 问答未命中 → 文档缺口清单',
};
r
```
