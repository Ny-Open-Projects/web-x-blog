---
title: [AIC-225] AI 架构评审误报太多，开发开始忽略报告，怎么治理？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-225：AI 架构评审误报太多，开发开始忽略报告，怎么治理？
**答**：
- 分级：高危（依赖方向/安全）阻塞、中危提示、低危折叠进附录——避免全部平铺。
- 白名单机制：显式登记的例外（legacy 区、生成代码）不报。
- 误报回流：每个误报标记原因（规则缺陷/例外未登记/上下文缺失），按周修提示词与白名单。
- 指标治理：跟踪「报告采纳率」，低于 30% 就收缩评审范围而不是扩大。

```javascript
const triage = (finding: Finding) => {
  if (inWhitelist(finding.file)) return 'suppressed';
  if (finding.severity === 'high' && finding.confidence > 0.8) return 'blocking';
  if (finding.severity === 'medium') return 'comment';
  return 'appendix'; // 低危折叠
};
r
```
