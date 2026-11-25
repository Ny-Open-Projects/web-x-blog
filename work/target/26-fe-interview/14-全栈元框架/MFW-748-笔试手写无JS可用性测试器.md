---
title: [MFW-748] 笔试：手写无 JS 可用性测试器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-748：笔试：手写无 JS 可用性测试

**答**：实现 `createNoJsAudit(pages, { fetchFn })`。pages: `{ path, expectedElements: string[], expectedFormActions?: string[] }[]`（每页的必需元素与表单）。规则：1) **无 JS 渲染验证**：fetch 页面 HTML（不执行 JS）→ 检查必需元素存在（CSS 选择器匹配——cheerio/glob）；2) **表单可用性**：form 的 action 属性存在（action={serverAction} 编译后 = method=POST + action=路径——可提交）；3) **链接可导航**：页面内的 <a href> 至少一个（无 JS 导航路径——不是 button[onclick]）；4) 返回 `{ pages: Array<{ path, passed, missing: string[] }>, ok }`（ok = 全 pass）。边界：空 pages；expectedElements 空（只查 form/link）；HTML 为空（全 fail）。

```javascript
function createNoJsAudit(pages = [], { fetchFn = fetch, cheerio } = {}) {
  return {
    async run() {
      const results = [];
      for (const p of pages) {
        const res = await fetchFn(p.path);
        const html = await res.text();
        const missing = [];
        // 必需元素检查
        for (const selector of p.expectedElements ?? []) {
          if (!html.includes(selectorFrom(selector)))     // 简化：文本/类名匹配
            missing.push(`element: ${selector}`);
        }
        // form action 检查
        if (p.expectedFormActions?.length) {
          const hasForm = p.expectedFormActions.every(action =>
            html.includes(`action="${action}"`) || html.includes('method="post"'));
          if (!hasForm) missing.push('form: 无可提交表单');
        }
        // link 导航检查
        if (!/<a\s+[^>]*href=/.test(html))
          missing.push('link: 无 <a href> 导航');
        results.push({ path: p.path, passed: missing.length === 0, missing });
      }
      return { pages: results, ok: results.every(r => r.passed) };
    },
  };
}
// selector 的简化匹配（生产用 cheerio）
const selectorFrom = (s) => {
  if (s.startsWith('text=')) return s.slice(5);           // 文本
  if (s.startsWith('#')) return `id="${s.slice(1)}"`;     // id
  return s;                                               // 原样
};

// 自测
const audit = createNoJsAudit([
  { path: '/products',
    expectedElements: ['text=Search', 'text=Add to Cart'],
    expectedFormActions: ['/products'] },
  { path: '/p/42',
    expectedElements: ['text=Product Name'] },
], { fetchFn: async (path) => new Response(
  `<html><body>
    <form action="/products" method="GET"><input name="q"/><button>Search</button></form>
    <a href="/p/1">Product Name</a>
    <form action="/cart" method="POST"><button>Add to Cart</button></form>
  </body></html>`) });
let r = await audit.run();
console.log(r.ok === true);                              // 元素+form+link 全有

// 缺元素
const badAudit = createNoJsAudit([
  { path: '/broken', expectedElements: ['text=Missing'] },
], { fetchFn: async () => new Response('<html><body>empty</body></html>') });
r = await badAudit.run();
console.log(r.ok === false && r.pages[0].missing[0].includes('element'));

// 无 link
const noLink = createNoJsAudit([
  { path: '/nolinks', expectedElements: [] },
], { fetchFn: async () => new Response('<html><body><div>no links</div></body></html>') });
r = await noLink.run();
console.log(r.pages[0].missing[0].includes('link'));
console.log(createNoJsAudit([]).run().then(x => x.ok === true));
```

**评分点**：
- 三项检查：必需元素/form action/链接导航——无 JS 可用性的完整验证
- form 的 server action 编译形态（method=POST + action 路径——渐进增强的产物 RBL-512）
- 边界（空 pages/空 HTML/无 link）；结果结构（missing 清单——可修复）
- 能说清「无 JS 可用性测试 = RSC 渐进增强的底线验证：form/link/action 的原生 HTML 通道」属于加分
