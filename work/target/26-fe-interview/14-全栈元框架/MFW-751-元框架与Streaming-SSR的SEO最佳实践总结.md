---
title: [MFW-751] Streaming SSR 的 SEO 最佳实践总结
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-751：Streaming SSR SEO 最佳实践

**答**:
- 流式 SEO 的综合最佳实践（RBL-528 深化的总结版）：1) **关键内容进 shell**（title/description/h1/LCP 元素同步渲染——非渲染爬虫的首包可见；2) **OG 卡片同步**（generateMetadata 并行 fetch RBL-515——社交分享卡片首包内）；3) **fallback 语义化**（非空骨架——含语义文本 RBL-528）；4) **sitemap 的准确性**（RBL-636：lastmod 准确/URL 可渲染）；5) **canonical 处理**（URL 变体/分页/过滤的 canonical 指向 RBL-653）；6) **流式完成的验证**（CI 首包截断测试 RBL-528——非渲染爬虫视角验收）。
- SEO 的自动化门禁：CI 的 SEO 审计（首包内容/sitemap 一致性/canonical/meta 完整性——RBL-661 审计清单的 SEO 维度）。
- 追问钩子：为什么「流式 SSR 的 SEO」需要「首包设计」的架构意识而非「事后 SEO 优化」？——流式的 SEO 取决于「哪些内容在首包」（架构决策：shell 的粒度决定 SEO 可见性）；事后优化无法把流末尾的内容搬到首包（需要重构 Suspense 层级——架构级改动）；「首包设计」是流式 SSR 的架构约束（与 UX 的流式体验、server 成本共同决策）——SEO 约束从「后期检查」前置到「渲染架构设计」。

```tsx
// SEO 最佳实践的完整页面模板
export async function generateMetadata({ params }) {
  const product = await getProduct(params.id);           // 并行（RBL-515 request memo）
  return {
    title: product.name, description: product.summary,
    openGraph: { images: [product.ogImage] },            // OG 卡片同步
    alternates: { canonical: `/p/${params.id}` },        // canonical
  };
}
export default async function Page({ params }) {
  const product = await getProduct(params.id);           // request memo 去重
  return (
    <>
      <h1>{product.name}</h1>                            {/* H1 同步（首包） */}
      <p>{product.summary}</p>                           {/* 关键内容（首包） */}
      <img src={product.heroImage} width={800} height={600} alt={product.name} />
      {/* LCP 元素同步（首包） */}
      <Suspense fallback={<p>加载评价中…</p>}>           {/* 次要内容流式 */}
        <Reviews id={params.id} />
      </Suspense>
    </>
  );
}
// CI SEO 审计
// 首包截断 + sitemap 对账 + canonical + OG 卡片完整性
```
