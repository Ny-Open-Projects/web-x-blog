---
title: [AIC-049] AI Review 的意见怎么写才让人愿意改？「意见写作」质量如何评估？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-049：AI Review 的意见怎么写才让人愿意改？「意见写作」质量如何评估？
**答**：
- 好意见四要素：精确位置（file:line）、问题后果（不说「不优雅」而说「竞态会导致重复提交订单」）、最小修复建议（最好给代码片段）、置信度。
- 反面模式：泛泛而谈（「建议增强健壮性」）、教学式长篇（讲原理不指位置）、一堆 nit 淹没 blocker。
- prompt 层约束：禁止输出无位置的抽象建议；每条意见必须能「直接执行」——reviewer 可以照着改而无需再问。
- 写作质量评估指标：采纳率、被要求「再说清楚」的比例、意见平均长度（过长通常是废话信号）。
- 追问钩子：把好评意见沉淀成 few-shot 例子放进 review prompt——意见风格也是可以被训练的。

```javascript
// 意见渲染模板：保证四要素齐活
function renderFinding(f) {
  if (!f.file || f.line == null) return null; // 无位置的意见直接丢弃
  return `[${f.level}] ${f.file}:${f.line}
问题：${f.issue}（后果：${f.consequence}）
建议：${f.fix}
置信度：${f.confidence}`;
}
```
