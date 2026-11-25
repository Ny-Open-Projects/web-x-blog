---
title: [MFW-662] 元框架与 CDN 的精细失效 API
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-662：CDN 精细失效 API

**答**:
- CDN 失效的 API 面：1) **purge by URL**（Cloudflare/Akamai 的精确 URL 失效——单页更新）；2) **purge by tag/surrogate-key**（CDN 级 tag：响应头 `Surrogate-Key: product:123` → purge by key——CDN 层的 revalidateTag RBL-577）；3) purge everything（全站失效——最后手段：缓存全灭回源风暴 RBL-638 雪崩）；「tag 失效在 CDN 层的等价物」：Surrogate-Key（Fastly/Varnish 的标准——元框架的 revalidateTag 透传到 CDN）。
- 失效的传播链：框架 revalidateTag（Data Cache）+ CDN purge by surrogate key（边缘缓存）——「双层失效的同步」（RBL-581 对齐的失效面）：漏 CDN 失效 = CDN 缓存旧内容（框架缓存新——用户拿旧）。
- CDN 失效的成本：Akamai/Cloudflare 的 purge 配额（免费层限量——失效风暴的配额瓶颈 RBL-599；purge 的合并（N URL 一次 API 调用——批量失效）。
- 追问钩子：为什么「CDN 失效要与框架 revalidate 同步」而不是「只依赖 TTL」？——TTL 长缓存（1h）+ 数据变更 = 用户最多看 1h 旧数据（不可接受——商品价格）；精确失效 = 变更即失效（秒级新鲜度）；「TTL 与事件的分工」：TTL 兜底（失效管线丢失时的最终一致）、事件失效为主（精确新鲜）——两层缓存的失效协议（RBL-590 管线 + CDN API = 完整失效链）。

```typescript
// CDN surrogate-key 失效
// 响应头：Surrogate-Key: product:123 products
// Next route handler 自动设置（框架的 tag → surrogate key）
export async function GET(req: Request) {
  const product = await getProduct(id);
  return NextResponse.json(product, { headers: {
    'Surrogate-Key': `product:${id} products`,           // CDN tag（RBL-577 映射）
    'Cache-Control': 's-maxage=3600',
  }});
}
// 失效：框架 + CDN 双层同步
async function invalidateProduct(id: string) {
  revalidateTag(`product:${id}`);                        // 框架层（Data Cache）
  await fetch(`https://api.fastly.com/service/${SID}/purge`, {
    method: 'POST',
    headers: { 'Fastly-Key': FASTLY_KEY },
    body: JSON.stringify({ 'surrogate-keys': [`product:${id}`] }),
  });                                                    // CDN 层（边缘缓存）
  // 双层同步：漏 CDN = 边缘旧内容（RBL-581 对齐）
}
```
