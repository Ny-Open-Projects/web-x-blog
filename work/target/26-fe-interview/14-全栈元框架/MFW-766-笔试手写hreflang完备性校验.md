---
title: [MFW-766] 笔试：手写 hreflang 完备性校验
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-766：笔试：手写 hreflang 校验

**答**：实现 `validateHreflang(pages, supportedLocales)`。pages: `{ path, locale, hreflangs: Record<locale, url> }[]`. 规则：1) **双向对称**：A 声明 B → B 必须声明 A（单向 = finding 'asymmetric'）；2) **自引用**：每页应声明自身 locale（self-reference——A(en) 应有 hreflangs.en = 自身 URL）；3) **locale 完备**：每页应声明所有 supportedLocales（漏 locale → 'incomplete'——x-default 不算 locale）；4) **URL 一致**：hreflangs 指向的 URL 应在 pages 中存在（死链 → 'broken-hreflang'）；5) x-default 声明：至少一个页面有 x-default → 'missing-default'。返回 `{ findings: Array<{ page, type, detail }>, ok }`（ok = 无 error 级——asymmetric/broken 为 error；incomplete/missing-default 为 warn）。边界：pages 空；单 locale（无需 hreflang——所有 pass）；supportedLocales 空（跳过校验）。

```javascript
function validateHreflang(pages = [], supportedLocales = []) {
  if (!supportedLocales.length || pages.length <= 1)
    return { findings: [], ok: true, skipped: true };
  const findings = [];
  const byPath = new Map(pages.map(p => [p.path, p]));
  for (const page of pages) {
    // 双向对称
    for (const [locale, url] of Object.entries(page.hreflangs ?? {})) {
      if (locale === 'x-default') continue;
      const target = byPath.get(url);
      if (!target) {
        findings.push({ page: page.path, type: 'broken-hreflang', severity: 'error',
          detail: `hreflang ${locale} 指向不存在的 ${url}` });
        continue;
      }
      const backRef = target.hreflangs?.[page.locale];
      if (backRef !== page.path)
        findings.push({ page: page.path, type: 'asymmetric', severity: 'error',
          detail: `声明 ${locale}:${url} 但对方未回指 ${page.locale}` });
    }
    // locale 完备
    const declared = Object.keys(page.hreflangs ?? {}).filter(l => l !== 'x-default');
    const missing = supportedLocales.filter(l => !declared.includes(l));
    if (missing.length)
      findings.push({ page: page.path, type: 'incomplete', severity: 'warn',
        detail: `缺 locale: ${missing.join(',')}` });
    // x-default
    if (!Object.keys(page.hreflangs ?? {}).includes('x-default'))
      findings.push({ page: page.path, type: 'missing-default', severity: 'warn' });
  }
  return { findings, ok: !findings.some(f => f.severity === 'error') };
}

// 自测
const locales = ['en', 'zh'];
const pages = [
  { path: '/en/p1', locale: 'en',
    hreflangs: { en: '/en/p1', zh: '/zh/p1', 'x-default': '/en/p1' } },
  { path: '/zh/p1', locale: 'zh',
    hreflangs: { en: '/en/p1', zh: '/zh/p1', 'x-default': '/en/p1' } },  // 对称 ✓
];
let r = validateHreflang(pages, locales);
console.log(r.ok === true && r.findings.length === 0);

// 单向（不对称）
const asymmetric = [
  { path: '/en/p1', locale: 'en', hreflangs: { en: '/en/p1', zh: '/zh/p1' } },
  { path: '/zh/p1', locale: 'zh', hreflangs: { zh: '/zh/p1' } },   // 未回指 en
];
r = validateHreflang(asymmetric, locales);
console.log(r.findings.some(f => f.type === 'asymmetric' && f.severity === 'error'));
console.log(r.ok === false);

// 死链
const broken = [
  { path: '/en/p1', locale: 'en', hreflangs: { en: '/en/p1', zh: '/zh/ghost' } },
];
r = validateHreflang(broken, locales);
console.log(r.findings.some(f => f.type === 'broken-hreflang'));

// 单 locale 跳过
console.log(validateHreflang(pages, ['en']).skipped === true);
```

**评分点**：
- 双向对称检测（A→B 必须有 B→A——hreflang 互惠协议）；死链检测（hreflang URL 不存在）
- locale 完备性（missing warn）与 x-default（warn）分级（asymmetric/broken error 阻断）
- 边界（单 locale skipped/空 locales）；对称的回指 URL 比对
- 能说清「hreflang 是互惠协议：A→B 必须有 B→A——单向声明让爬虫的语言图不完整」属于加分
