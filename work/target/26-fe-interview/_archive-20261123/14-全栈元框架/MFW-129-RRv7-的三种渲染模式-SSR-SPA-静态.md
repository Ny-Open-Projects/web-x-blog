---
title: [MFW-129] RRv7 的 SSR、SPA、静态三种模式怎么切换和取舍？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-129：RRv7 的 SSR、SPA、静态三种模式怎么切换和取舍？
**答**：
- 一个开关族：`ssr: false` 进 SPA/预渲染模式；`ssr: true` 全量 SSR；`prerender: [...]` 指定构建期静态化路径。同一份代码三种产物，部署形态随开关变——这是 RRv7 对 Next「默认智能化」的回应：把渲染模式做成显式配置。
- SPA 模式（ssr:false）：`serverLoader` 不可用，取数全走 `clientLoader`；产物可托管到任意静态 CDN。
- 预渲染模式：指定路径构建期跑 loader 生成 HTML（注意此时 loader 不能读请求上下文）；适合营销页/文档。
- SSR 模式：完整 Remix 心智，loader 服务端执行 + 请求级数据（cookies 可用）。
- 取舍判断：内容站 → prerender；后台 → SPA；电商/个性化 → SSR；且可以混着来（prerender 列表 + SSR 其余）。

```ts
// react-router.config.ts —— 三模式
import type { Config } from '@react-router/dev/config';

// ① 纯 SPA
export const spaConfig = { ssr: false } satisfies Config;

// ② 全量 SSR
export const ssrConfig = { ssr: true } satisfies Config;

// ③ 混合：静态 + SSR
export const hybridConfig = {
  ssr: true,
  prerender: async ({ getStaticPaths }) => {
    const paths = await getStaticPaths(); // 已知静态路径
    return ['/', '/about', ...paths.filter((p) => p.path.startsWith('/blog'))];
  },
} satisfies Config;
```

```tsx
// SPA 模式下的 route module：serverLoader 不可用
export async function clientLoader() {
  return fetch('/api/products').then((r) => r.json()); // 浏览器取数
}
// ssr: false 时若写 serverLoader，构建期直接报错——错误前移
```
