---
title: [RBL-781] 构建器诊断与 AI 排查的衔接：结构化诊断如何喂给 AI 助手
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-781：构建器诊断与 AI 排查的衔接：结构化诊断如何喂给 AI 助手

**答**:
- 构建失败后 AI 排查（copilot/内部助手）的质量取决于「喂给它的上下文」——结构化诊断（RBL-568 的 Diagnostic：code/span/labels/hints/related）正是 AI 需要的最小充分上下文：错误码 → 文档语义、span → 代码位置、related → 因果链。构建器提供 `diagnosticsToJson()` 的机读出口（ai-friendly schema），而不是让 AI 去解析终端渲染的 ANSI 文本。
- 上下文裁剪：AI 的 token 预算有限——诊断输出的「AI 视图」做裁剪：1) 相关源码只带 span 前后 N 行；2) related 链只带第一层；3) 配置摘要（完整 config 太大）。裁剪策略本身要可配置（用户助手的能力不同）。
- 「已知问题库」的先验注入：诊断 → 内部 issue 库相似匹配（历史修复案例 top3）附加到 AI 上下文——把「组织记忆」喂给 AI，比纯模型推理准得多；匹配键是错误码 + 关键 token。
- 反馈回环：AI 建议是否有效（采纳/无效）回流诊断文档（RBL-673）——hint 的迭代数据来源。
- 追问钩子：为什么不让 AI 直接读全部构建日志？——日志噪声大（进度行/重复警告），关键信号被稀释；结构化诊断是「信噪比优化后的中间表示」——工具输出给机器消费的接口设计，和给人看的渲染同等重要。

```javascript
// AI 友好诊断出口
function diagnosticsForAI(diags, { ctxLines = 5, relatedDepth = 1 } = {}) {
  return diags.slice(0, 20).map(d => ({
    code: d.code,
    severity: d.severity,
    message: d.message,
    location: d.labels[0] && {
      file: d.labels[0].span.file,
      snippet: readLines(d.labels[0].span.file, d.labels[0].span.start.line, ctxLines),
    },
    hints: d.hints,
    related: d.related.slice(0, relatedDepth).map(r => r.code),
    knownIssues: issueLib.match(d.code, keywords(d.message)).slice(0, 3),  // 组织记忆
  }));
}
// 相似案例匹配（历史修复）
const issueLib = {
  match(code, tokens) {
    return db.query(`SELECT fix FROM fixes WHERE code = ? ORDER BY similarity DESC LIMIT 3`, code);
  },
};
```
