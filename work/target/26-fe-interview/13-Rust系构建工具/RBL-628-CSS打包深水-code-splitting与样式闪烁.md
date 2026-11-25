---
title: [RBL-628] CSS 打包深水：代码分割下的样式加载时序与 FOUC 治理
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-628：CSS 打包深水：代码分割下的样式加载时序与 FOUC 治理

**答**:
- CSS 与 JS 分割的时序错位：JS chunk 是动态 import（浏览器知道依赖），CSS 是 link 标签注入——动态 chunk 的 CSS 若由 JS 运行时注入（insertBefore），会出现「页面先渲染无样式 → CSS 到达后重绘」的 FOUC；Vite 的解法是 dev 下 JS import CSS 模拟（style 注入同步阻塞渲染前完成有难度）→ prod 下构建器把动态 chunk 的 CSS 写成 `<link rel="stylesheet">` 由 HTML 或运行时在 import 前预载。
- 构建器的正确姿势：1) 动态 chunk 的 CSS 与 JS **配对产出**（chunk manifest 里 css 数组）；2) 运行时加载器（RBL-531 的 chunk loader）在 import 执行前先 `link.href` 预载并等待 onload——把 CSS 变成 chunk 依赖的一部分；3) modulepreload 不覆盖 CSS（语义只针对模块），需要单独 preload。
- 样式顺序稳定性：CSS 的级联依赖「顺序」——多 chunk 的 CSS 注入顺序必须与构建时的模块顺序一致，否则样式覆盖关系错乱（同名类后定义者赢）。构建器要为 CSS 注入维护「全局顺序计数」（构建时确定的插入序号写入 runtime），而不是按加载完成顺序插入。
- critical CSS 与首屏：构建器可输出首屏 chunk 的 CSS 清单（供 SSR 内联）——SPA 场景则依赖预载策略；关键权衡：内联减少 RTT 但丢失缓存（每个 HTML 重复传输）。
- 追问钩子：为什么 CSS-in-JS 在代码分割下会加重 FOUC？——运行时注入的样式依赖 JS 执行，chunk 懒加载后样式生成必然滞后于渲染；解决方向是「构建期提取」（vanilla-extract/linaria 编译期方案）——本质上把 CSS-in-JS 变回构建产物。

```javascript
// 运行时 chunk 加载器的 CSS 配对逻辑
async function loadChunk(id, manifest) {
  const meta = manifest.get(id);                         // { js, css: [] }
  // CSS 预载：等待全部 onload（或已加载）
  await Promise.all(meta.css.map(href => loadStyle(href)));
  return import(meta.js);                                // 样式就绪后再执行 JS
}
function loadStyle(href) {
  if (loaded.has(href)) return loaded.get(href);
  const p = new Promise((res, rej) => {
    const link = document.createElement('link');
    link.rel = 'stylesheet'; link.href = href;
    link.onload = res; link.onerror = rej;               // 失败也要 reject 触发守卫
    document.head.appendChild(link);
  });
  loaded.set(href, p);
  return p;
}
// 顺序保证：head 插入序号 = 构建时全局顺序（order 属性），插入时按序定位
// link.dataset.order = '3'; // runtime 按 order 升序 appendChild
```
