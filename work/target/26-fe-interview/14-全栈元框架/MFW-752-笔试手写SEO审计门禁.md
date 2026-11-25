---
title: [MFW-752] 笔试：手写 SEO 审计门禁
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-752：笔试：手写 SEO 审计门禁

**答**：实现 `seoAudit(html, { route, requiredMeta, canonicalExpected })`。html: 首包截断的 HTML 字符串；requiredMeta: `{ title: true, description: true, ogImage: false, h1: true }`。规则：1) title：`<title>` 存在且非空 → ok；2) description：meta[name=description] 有 content；3) og:image：meta[property=og:image]（requiredMeta.ogImage=true 时必查）；4) h1：`<h1>` 存在且非空（LCP 元素在首包）；5) canonical：link[rel=canonical] 与 canonicalExpected 匹配；6) 首包内容：requiredMeta.h1 的 h1 在首包内（截断验证——HTML 参数就是首包截断的）。返回 `{ findings: Array<{ check, pass, detail }>, ok }`（ok = 全 pass）。边界：requiredMeta 全 false（只查 canonical）；HTML 为空（全 fail）；canonicalExpected 缺失（跳过 canonical）。

```javascript
function seoAudit(html = '', { route = '', requiredMeta = {}, canonicalExpected } = {}) {
  const findings = [];
  const get = (pattern) => { const m = pattern.exec(html); return m?.[1] ?? null; };
  // title
  if (requiredMeta.title) {
    const title = get(/<title>([^<]*)<\/title>/);
    findings.push({ check: 'title', pass: !!title?.trim(),
      detail: title ? `内容: ${title}` : 'title 缺失或空' });
  }
  // description
  if (requiredMeta.description) {
    const desc = get(/name="description"\s+content="([^"]+)"/);
    findings.push({ check: 'description', pass: !!desc?.trim(),
      detail: desc ? '有内容' : 'description 缺失' });
  }
  // og:image
  if (requiredMeta.ogImage) {
    const og = get(/property="og:image"\s+content="([^"]+)"/);
    findings.push({ check: 'og:image', pass: !!og, detail: og ?? 'og:image 缺失' });
  }
  // h1 在首包
  if (requiredMeta.h1) {
    const h1 = get(/<h1[^>]*>([^<]+)<\/h1>/);
    findings.push({ check: 'h1', pass: !!h1?.trim(),
      detail: h1 ? `"${h1.trim().slice(0, 30)}" 在首包` : 'h1 缺失或不在首包' });
  }
  // canonical
  if (canonicalExpected) {
    const canonical = get(/rel="canonical"\s+href="([^"]+)"/);
    findings.push({ check: 'canonical', pass: canonical === canonicalExpected,
      detail: canonical ? `指向 ${canonical}` : 'canonical 缺失' });
  }
  return { findings, ok: findings.every(f => f.pass) };
}

// 自测
const goodHtml = `<html><head>
<title>商品A</title>
<meta name="description" content="商品描述"/>
<meta property="og:image" content="https://x.com/og.jpg"/>
<link rel="canonical" href="/p/42"/>
</head><body><h1>商品A</h1><p>描述</p></body></html>`;
let r = seoAudit(goodHtml, { route: '/p/42',
  requiredMeta: { title: true, description: true, ogImage: true, h1: true },
  canonicalExpected: '/p/42' });
console.log(r.ok === true && r.findings.every(f => f.pass));

// 缺 title
r = seoAudit(goodHtml.replace('<title>商品A</title>', ''), { route: '/p/42',
  requiredMeta: { title: true, description: true, ogImage: true, h1: true },
  canonicalExpected: '/p/42' });
console.log(r.findings.some(f => f.check === 'title' && !f.pass));
console.log(r.ok === false);

// h1 不在首包（流式末尾）
r = seoAudit('<html><body><div class="skeleton">加载中</div></body></html>',
  { route: '/p/42', requiredMeta: { title: true, description: true, h1: true } });
console.log(r.findings.some(f => f.check === 'h1' && !f.pass));
console.log(r.findings.some(f => f.check === 'h1' && f.detail.includes('首包')));

// 全 false
r = seoAudit(goodHtml, { route: '/x', requiredMeta: {}, canonicalExpected: null });
console.log(r.ok === true);                              // 无要求 → 无检查 → 全过

console.log(seoAudit('', { route: '/x', requiredMeta: { title: true } }).ok === false);
```

**评分点**：
- 五项审计（title/description/og:h1/canonical——RBL-751 最佳实践的机械化）；首包截断语义
- h1 的「在首包」检查（流式 SEO 的关键验证——非渲染爬虫视角）；全 false 跳过
- 边界（空 HTML 全 fail/requiredMeta 全 false）；ok 语义（全 pass 才过门禁）
- 能说清「SEO 审计用首包截断的 HTML——流式内容在首包外对非渲染爬虫不可见」属于加分
