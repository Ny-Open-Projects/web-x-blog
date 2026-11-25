---
title: [AIC-042] AI Review 的 Prompt 该怎么设计？为什么「给它检查清单」比「帮我看看代码」有效得多？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-042：AI Review 的 Prompt 该怎么设计？为什么「给它检查清单」比「帮我看看代码」有效得多？
**答**：
- 「帮我看看」会产出泛泛的满分作文式意见；清单式审查让模型逐项对照输出 PASS/FAIL + 位置 + 证据，意见可执行、可统计。
- 清单构成：本仓库的高频 bug 模式（从历史事故沉淀）、通用边界（空值/竞态/清理/错误处理）、安全项（注入/敏感信息/越权）、性能项（N+1/重渲染/大包）。
- 结构要求：每条意见必须带「文件:行号 + 问题描述 + 修复建议 + 置信度」，模型做不到结构化输出的就是噪音，直接丢弃。
- 上下文给什么：diff + diff 涉及文件的完整内容（不是只有 diff，模型看不到未改动区域的配合就会误报）。
- 追问钩子：把「误报样本」定期回流进 prompt 的反例区，这是 AI review 持续调优的核心手段。

```javascript
// review prompt 组装：清单驱动 + 结构化输出
const reviewPrompt = `
你是资深前端评审。逐项检查 <diff>（结合 <full_file> 上下文）：
1. 空值/空数组/空对象边界
2. 异步竞态（连续请求、组件卸载后 setState）
3. 错误处理与用户反馈
4. 类型安全（any/断言滥用）
5. 安全：XSS、敏感信息硬编码
输出 JSON 数组：[{file, line, level: "blocker|suggestion|nit", issue, fix, confidence: 0-1}]
confidence < 0.7 的意见不输出。
`;
```
