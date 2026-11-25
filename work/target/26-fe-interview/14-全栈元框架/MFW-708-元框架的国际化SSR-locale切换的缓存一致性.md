---
title: [MFW-708] i18n locale 切换的缓存一致性
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-708：locale 切换的缓存一致性

**答**:
- locale 切换（/en → /zh）的缓存面：1) **URL 变化**（/en/p/1 → /zh/p/1——不同 URL = 不同缓存键——天然隔离 RBL-548）；2) **cookie 变化**（NEXT_LOCALE cookie 更新——SSR 渲染 locale 翻译文本——cookie 变 = 同 URL 不同内容（无 locale 段的路由——缓存键不含 locale——串语言）；3) **Data Cache 的 locale 维度**（翻译数据的缓存：`fetch(url, { next: { tags: [`products-${locale}`] } }`——locale 进 tag：失效按 locale 粒度）。
- 无 locale 段的路由的缓存策略：cookie 驱动 locale（middleware 重写——URL 不变）→ 缓存键必须含 locale（Vary: cookie 或放弃 CDN 缓存）——「locale 段路由 vs cookie locale」的缓存友好性差异：段路由（URL 键含 locale——CDN 缓存友好）；cookie（同 URL 两语言——CDN 缓存键分裂）。
- 切换的一致性：切换 locale = URL 跳转 + cookie 更新（双动作）——「跳转与 cookie 的原子性」（middleware 先重写再 set cookie——一致）；切换后 payload 缓存（Router Cache 旧 locale payload——URL 变 = 新缓存键——自动隔离）。
- 追问钩子：为什么「locale 段路由」比「cookie locale」的缓存一致性更好？——段路由 = locale 进 URL = 进缓存键（/en/p vs /zh/p 是不同缓存条目——零串语言风险）；cookie = 同 URL 两内容（CDN 缓存按 URL——不同用户同 URL 不同语言 = 缓存串语言——需要 Vary: Cookie 或放弃 CDN）；「状态进 URL」原则（RBL-936/548）在 locale 的必然性：用户可见状态必须可寻址——locale 是用户可见状态。

```typescript
// locale 段路由的缓存策略
// app/[locale]/products/page.tsx
export async function generateStaticParams() {
  return locales.map(l => ({ locale: l }));
}
export async function generateMetadata({ params }) {
  return { alternates: {
    canonical: `/${params.locale}/products`,
    languages: Object.fromEntries(locales.map(l => [l, `/${l}/products`])),   // hreflang
  }};
}
// Data Cache 的 locale tag
fetch(apiUrl, { next: { tags: [`products-${locale}`] } });   // locale 进 tag
revalidateTag(`products-zh`);                            // 中文失效不影响英文
// cookie locale 的缓存陷阱（反模式）
// middleware 重写但 URL 不变 → CDN 缓存键不含 locale → 串语言
// 修正：Vary: Cookie（CDN 按 cookie 分桶）或改为段路由
```
