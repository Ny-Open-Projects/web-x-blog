---
title: [AIC-063] AI 能辅助哪些前端性能优化？为什么它擅长「找模式」而弱于「做测量」？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-063：AI 能辅助哪些前端性能优化？为什么它擅长「找模式」而弱于「做测量」？
**答**：
- AI 擅长的模式类优化：识别重渲染根因（props 未 memo、大对象引用每次新建）、找出可 code-split 的重依赖、列表无 key/全量渲染、未做图片懒加载、同步阻塞脚本。
- 做法：喂性能问题线索（React DevTools 火焰图截图描述、bundle 分析 JSON、长任务栈）让它输出「嫌疑清单 + 修复 diff」。
- 弱在测量：AI 不能真实运行页面，bundle 体积、LCP 数值、真实用户分布都拿不到——测量必须用 Lighthouse/Performance 面板/RUM，AI 只消费测量结果。
- 正确流程：人测量出问题点 → AI 给修复方案与代码 → 人改后再测量对比验证。闭环的「测量」端永远是真实环境。
- 追问钩子：bundle 分析的 JSON 喂给 AI 解释「为什么这么大」效果很好——它能顺着依赖链指出该换/该拆的包。

```javascript
// 喂给 AI 的 bundle 分析摘要提取（保留大块，裁碎块）
function summarizeBundle(analysis, topN = 15) {
  const mods = Object.entries(analysis.modules)
    .sort((a, b) => b[1].size - a[1].size).slice(0, topN)
    .map(([name, m]) => `${name} ${m.size}KB (deps: ${m.deps.join(', ')})`);
  return `top ${topN} modules:\n${mods.join('\n')}\ntotal: ${analysis.total}KB`;
}
```
