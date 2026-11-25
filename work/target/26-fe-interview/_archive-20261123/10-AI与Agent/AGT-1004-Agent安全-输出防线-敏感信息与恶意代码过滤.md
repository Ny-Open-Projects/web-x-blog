---
title: [1004] Agent 输出侧防线怎么建
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 输出防线]
type: 面试题
---

## 1004：Agent 输出侧防线怎么建

**答**：
- 输出审查三类：敏感信息（密钥、PII、内部系统名——DLP 正则 + NER 双扫）、恶意内容（可执行恶意代码、钓鱼文案）、合规内容（政策红线词）。
- 结构化输出白名单：对外输出限定格式（如 markdown 不含 script 标签、代码块语言白名单），从格式层面消灭 XSS 注入——Agent 输出直接渲染前端是经典 XSS 源。
- 双通道输出：面向用户和面向下游 Agent 用不同的输出过滤器（用户侧防 XSS/泄露，下游侧防注入传播）。
- 追问钩子：过滤器误杀怎么处理？——放行流程人工审核 + 记录误杀样本优化规则，宁可慢不能漏；高危类（密钥）零容忍。

```ts
function outputFilter(text, { channel }) {
  const issues = [];
  if (DLP_PATTERNS.some(p => p.test(text))) issues.push('sensitive');
  if (/<script|onerror\s=/i.test(text)) issues.push('xss');
  if (channel === 'user' && hasExecSnippet(text)) issues.push('exec');
  if (issues.length) return { blocked: true, issues, safe: redact(text, issues) };
  return { blocked: false, safe: text };
}
```
