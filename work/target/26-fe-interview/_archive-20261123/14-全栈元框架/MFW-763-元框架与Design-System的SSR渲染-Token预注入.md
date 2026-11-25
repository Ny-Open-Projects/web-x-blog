---
title: [MFW-763] Design Token 的 SSR 预注入
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-763：Design Token SSR 预注入

**答**:
- Token 的 SSR 预注入（RBL-697/777 深化）：1) **CSS 变量的 SSR 内联**（token → `<style>` 内联在 head——首屏样式即时（无 FOUC RBL-777 theme boot）；2) **Token 与 Tailwind 的桥接**（Tailwind config 从 token 生成——`theme.extend.colors = tokenToTailwind(tokens)`——构建期生成（token → tailwind config → CSS）；3) **token 的运行时覆盖**（CSS 变量的优先级——inline style > [data-brand] > :root——品牌覆盖的层级）；4) **SSR 的 token 上下文**（品牌/主题从 cookie/host → RSC 读 → token 变量内联（RBL-668 主题 SSR 一致性的 token 版）。
- 追问钩子：为什么「Token 预注入到 SSR HTML」比「CSS 文件加载」更优？——CSS 文件 = 网络请求 + 解析延迟（FOUC 窗口：HTML 渲染先于 CSS 到达——无样式闪烁）；SSR 内联 = HTML 自带样式（零延迟——首屏即正确样式）；「内联的成本」：token CSS 体积（~2KB——可接受；大 token 集 → 抽取公共部分到 CSS 文件 + 关键 token 内联）；「内联 vs 文件」的权衡：关键 token 内联（首屏无 FOUC）+ 全量 token 在 CSS 文件（后续页面复用缓存）。

```tsx
// Token SSR 预注入
// lib/tokens.ts
const tokens = { primary: '#3b82f6', bg: '#fff', text: '#111', radius: '8px' };
// app/layout.tsx
export default function RootLayout({ children }) {
  const brand = headers().get('x-brand') ?? 'default';
  const themeTokens = getTokensForBrand(brand);          // 品牌变量 RBL-668
  const cssVars = Object.entries(themeTokens)
    .map(([k, v]) => `--${k}: ${v};`).join(' ');
  return (
    <html>
      <head>
        <style dangerouslySetInnerHTML={{ __html:
          `:root { ${cssVars} } [data-brand="${brand}"] { ${cssVars} }` }} />
      </head>
      <body data-brand={brand}>{children}</body>
    </html>
  );
}
// Token → Tailwind config（构建期生成）
// tailwind.config.js
const tokens = require('./tokens.json');
module.exports = { theme: { extend: { colors: {
  primary: tokens.primary, background: tokens.bg }, borderRadius: { DEFAULT: tokens.radius } } } };
// Tailwind 类 → CSS 变量引用（构建期生成）
// .bg-primary → background-color: var(--primary)   ← token 桥接
```
