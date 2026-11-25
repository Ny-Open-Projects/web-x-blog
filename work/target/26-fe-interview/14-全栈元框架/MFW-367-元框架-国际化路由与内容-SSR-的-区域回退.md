---
title: [367] 元框架的国际化路由如何设计区域回退与内容降级
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, i18n, SSR]
type: 面试题
---

## MFW-367：元框架的国际化路由如何设计区域回退与内容降级？

**答**：
- 路由层级两段式：`/[locale]/...`，locale 缺失时由中间件按 `Accept-Language` + Cookie 协商重定向，默认 locale 用 308 永久重定向利于 SEO。
- 回退链要显式：`zh-TW -> zh-CN -> en`，词典查不到 key 时沿链降级并在构建期告警缺失率，而不是运行时静默显示 key。
- 内容（非 UI 文案）的本地化在 Server 层做：CMS 按区域取数失败时返回英文兜底 + 响应头标注 `x-content-fallback`，便于监控统计覆盖率。
- hreflang 标签在 Server 组件里生成，指向全部等价 locale URL，避免多区域页面互相抢排名。
- 追问钩子：为什么不用子域名做 i18n？——Cookie 域、部署成本、SSR 缓存按域名分片都会复杂化。

```tsx
// 词典回退：zh-TW -> zh-CN -> en
const chain = ['zh-TW', 'zh-CN', 'en'];
export function t(locale: string, key: string): string {
  for (const l of chain.slice(chain.indexOf(locale))) {
    const v = dict[l]?.[key];
    if (v) return v;
  }
  reportMissing(locale, key);      // 构建期/运行期统计缺口
  return dict['en'][key] ?? key;   // 最后兜底：英文或 key 本身
}

// hreflang 生成（Server Component）
export function Hreflang({ path, locales }: { path: string; locales: string[] }) {
  return (
    <>
      {locales.map(l => (
        <link key={l} rel="alternate" hrefLang={l} href={`https://x.com/${l}${path}`} />
      ))}
      <link rel="alternate" hrefLang="x-default" href={`https://x.com/en${path}`} />
    </>
  );
}
```
