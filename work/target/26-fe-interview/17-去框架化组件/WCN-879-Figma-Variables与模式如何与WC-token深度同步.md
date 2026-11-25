---
title: [WCN-879] Figma Variables / Mode 如何与 WC 的 token 深度同步？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-879：Figma Variables / Mode 如何与 WC 的 token 深度同步？

**答**：
- 结论先行：Figma Variables（变量）与 Mode（模式，如 Light/Dark）天然对应设计系统的「token + 主题」——深度同步的目标是从设计源头单向或双向生成 CSS 变量，让设计稿与线上代码永远一致。
- 概念映射：Figma Variable 集合 ↔ token 分组（color/spacing/typography）；Mode ↔ 主题（Light/Dark/高对比）；Variable 的 alias（引用其他变量）↔ token 的语义别名（`--color-primary` → `--color-brand-500`）。
- 单向同步（推荐起点）：用 Figma REST API / Plugin API 导出 Variables JSON → 转换成 token JSON（DTCG 格式）→ 生成 CSS 变量与 TS 类型；设计改了重新生成，CI 校验代码中的 token 与 Figma 一致。
- 双向同步的坑：代码里改 token 反向写回 Figma 容易冲突（谁是谁的真相源）——一般确定「设计是唯一真相源」，代码只读；确需双向要有冲突检测与合并策略。
- 与 WCN 结合：生成的 CSS 变量通过 `:root`/`::part` 穿透 Shadow DOM；Mode 切换映射成运行时切换 token 样式表（`adoptedStyleSheets`），保证设计稿的 Light/Dark 与代码一致。
- 追问钩子：面试官会问「Figma 里删了个变量代码怎么办」——答：CI 比对发现 token 被删 → 生成 deprecation 警告并保留旧别名一个周期，避免组件突然变丑；同时通知设计团队确认。

```javascript
// Figma Variables JSON → token JSON → CSS 变量（简化）
const figmaVars = {
  'Color/Brand/500': { values: { Light: '#2563eb', Dark: '#60a5fa' } },
  'Semantic/Primary': { alias: 'Color/Brand/500' },
};
function figmaToTokens(vars, mode = 'Light') {
  const tokens = {};
  for (const [name, def] of Object.entries(vars)) {
    const key = '--' + name.toLowerCase().replace(/\//g, '-');
    tokens[key] = def.alias ? tokens['--' + def.alias.toLowerCase().replace(/\//g, '-')] : def.values[mode];
  }
  return tokens;
}
function tokensToCSS(tokens) {
  return `:root { ${Object.entries(tokens).map(([k, v]) => `${k}: ${v};`).join(' ')} }`;
}
console.log(tokensToCSS(figmaToTokens(figmaVars, 'Dark')));
```
