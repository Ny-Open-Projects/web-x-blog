---
title: [MFW-528] 流式 SSR 的 SEO：爬虫对流式内容的兼容性策略
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-528：流式 SSR 的 SEO：爬虫兼容性策略

**答**:
- 爬虫对流式的兼容分层：Googlebot 完全支持流式（渲染流并等待完成——但等待有超时）；部分爬虫/社交分享（微信/Telegram 的链接卡片）只读首包 HTML——「流式内容在首包外的部分」对非渲染爬虫不可见。
- 风险与对策：1) **关键 SEO 内容进 shell**（标题/描述/核心字段同步渲染——Suspense 外）；2) OG 卡片用同步 metadata（generateMetadata 并行 RBL-515——爬虫首包拿到）；3) fallback 文本化（骨架屏的 aria/文字——fallback 也是内容——别用空 div）。
- 检测矩阵：用「首包截断测试」（curl 不等流结束看内容）模拟非渲染爬虫——「哪些内容必须进首包」的验收测试。
- 追问钩子：为什么「fallback 是空 div」对流式 SEO 特别危险？——非渲染爬虫拿到首包 = shell + fallback：空 fallback = 爬虫看到空页面（内容全在流末尾）；fallback 带语义文本（标题骨架写「加载商品A」不如直接写商品名——能同步就同步）——流式的 SEO 策略本质是「为最弱的读者设计首包」，与渐进增强（RBL-512）的分层读者哲学一致。

```javascript
// SEO 安全的流式页面
export async function generateMetadata({ params }) {
  const p = await getProduct(params.id);                 // 并行 fetch（RBL-515）
  return { title: p.name, description: p.summary,
    openGraph: { images: [p.ogImage] } };                // OG 卡片同步进首包
}
export default async function Page({ params }) {
  const p = await getProduct(params.id);                // memoized（同请求去重）
  return (
    <>
      <h1>{p.name}</h1>                                  {/* 关键内容进 shell：同步 */}
      <p>{p.summary}</p>
      <Suspense fallback={<p>评价加载中…</p>}>            {/* fallback 有语义文本 */}
        <Reviews id={p.id} />                            {/* 非关键内容流式 */}
      </Suspense>
    </>
  );
}
// 首包截断测试（CI SEO 门禁）
const first = await fetch(url).then(r => r.text().then(t => t.slice(0, 30000)));
expect(first).toContain('商品标题');                     // 非渲染爬虫视角
```
