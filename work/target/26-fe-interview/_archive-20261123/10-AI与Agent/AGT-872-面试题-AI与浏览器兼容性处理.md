---
title: [AGT-872] AI 辅助兼容性问题（新 API 降级/polyfill 决策），如何避免过度兼容？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-872：AI 辅助兼容性问题（新 API 降级/polyfill 决策），如何避免过度兼容

**答**：
- 数据驱动：AI 的兼容建议必须基于「真实用户浏览器分布」（RUM 数据），不是"为了 Safari 12 写 polyfill"——没人用的旧浏览器不做兼容（过度兼容是代码债）。
- 分层决策：纯语法转换交给构建工具（browserslist 驱动，确定性强），API 缺失的 polyfill 按需（usage-based import），交互行为差异（iOS 橡皮筋等）才需要 AI/人工写适配代码。
- AI 的增值：从报错分布发现"某浏览器特有的问题簇"，生成适配方案草稿+验证矩阵。

```javascript
function compatStrategy(feature) {
  const usage = rum.browserShare({ minUsage: 0.5 });  // 只兼容真实用户
  const supported = caniuse(feature, usage.browsers);
  return {
    syntax: 'browserslist',                        // 交给构建
    polyfill: supported.missing.length ? usePolyfill(feature, 'usage-based') : null,
    behavioral: supported.quirks.map(q => aiDraftFix(q)), // 行为差异才AI
  };
}
```

