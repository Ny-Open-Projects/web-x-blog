---
title: [MFW-595] SSG 增量更新协议：内容变更到产物更新的对账
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-595：SSG 增量更新协议

**答**:
- 纯 SSG（Astro/Next export）的内容更新：产物是静态的——变更 = 重新构建；「增量构建」协议：1) **内容指纹**（每页的内容 hash——源数据（Markdown/CMS）变更检测 RBL-535）；2) 变更页重渲染（只渲染变化页——diff 驱动）；3) 产物发布（原子替换 + CDN 失效 RBL-694）。
- 增量的触发：git push（内容在仓——Markdown 博客）vs CMS webhook（内容在 CMS——Astro 的 content layer 集成）；「触发源的延迟」决定内容新鲜度（git push CI 5 分钟 / CMS webhook 即时）。
- 增量构建的失效传播：引用页的级联（组件变更 → 所有用它的页失效；数据变更 → 引用该数据的页——依赖闭包 RBL-635 的 SSG 版）；「页面 → 数据/组件依赖图」是增量精度的前提（Astro content collections 的依赖追踪）。
- 追问钩子：为什么 SSG 的「增量」比 ISR 的「增量」更需要依赖图？——ISR 的失效 = tag 精确（revalidateTag 实时触发）；SSG 的增量 = 构建时 diff（无运行时信号——只能靠「内容指纹比对」推断变化）；「无运行时失效信号」→ 依赖闭包的静态分析是唯一手段（哪个页面用了哪个 Markdown/组件——构建期的 import 图）；增量精度 = 依赖图的完备性：漏依赖 = 变更页未重渲染（静默旧内容 RBL-956）。

```javascript
// 内容指纹与增量 diff
async function incrementalBuild({ pages, lastManifest, render }) {
  const changed = [], removed = [];
  for (const p of pages) {
    const hash = await contentHash(p.source);            // Markdown 文件 hash
    const prev = lastManifest[p.path];
    if (prev?.hash === hash && prev.renderHash === p.renderHash) continue;   // 内容与模板都没变
    changed.push(p);
  }
  for (const path of Object.keys(lastManifest))
    if (!pages.find(p => p.path === path)) removed.push(path);
  for (const p of changed) {
    const html = await render(p);
    await atomicWrite(p.path, html);                     // 原子写 RBL-583
  }
  await saveManifest(pages.map(p => ({ path: p.path, hash: await contentHash(p.source),
    renderHash: p.renderHash })));
  return { rendered: changed.length, removed };
}
// 依赖闭包：组件变更 → 引用页失效
// Astro: getCollection 依赖追踪 / Next: import 图
function invalidateByComponent(component, pages, depGraph) {
  return pages.filter(p => depGraph[p.path]?.includes(component));   // 引用该组件的页全部重渲染
}
```
