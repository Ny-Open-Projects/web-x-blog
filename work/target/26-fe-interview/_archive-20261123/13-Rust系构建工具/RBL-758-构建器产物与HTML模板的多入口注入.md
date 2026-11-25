---
title: [RBL-758] 多入口 HTML 模板注入：脚本顺序、公共 chunk 去重与 SEO 基础标签
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-758：多入口 HTML 模板注入：脚本顺序、公共 chunk 去重与 SEO 基础标签

**答**:
- 多入口（SPA + admin 两个入口）的 HTML 注入要点：1) **依赖顺序正确**（polyfill chunk → vendor → entry，runtime 内联或 defer）；2) **共享 chunk 去重**（两个入口共享 vendor 时，各自的 html 只引自己的依赖闭包——闭包重叠的 chunk URL 相同（同一 hash 产物），浏览器缓存自然去重）；3) modulepreload 闭包预算（RBL-625）按入口分别计算。
- 注入的实现形态：构建器输出「每入口的标签清单」（scripts/preloads/styles 分组），模板引擎消费——构建器不直接写 HTML（模板是用户的），只提供数据 + 默认模板；「入口 × 模板」的组合关系要显式（多页应用不同页面不同模板）。
- SEO 基础标签的构建期生成：title/description/canonical/og 标签——来自入口配置或路由元数据；SSG 场景每路由一份（预渲染时注入），SPA 场景入口级。构建器的职责是「防止遗漏」——诊断缺失的 og:image（分享卡片空白是运营高频投诉）。
- 注入的安全：模板变量（title 等）HTML 转义——构建器提供的注入 API 默认转义，原始 HTML 要显式 `html` 标记（防模板注入把用户数据变成 XSS）。
- 追问钩子：为什么「脚本顺序」在 module 时代仍重要？——`<script type="module">` 是 defer 语义（执行顺序按文档序），但「模块依赖」由 import 链决定；真正要排序的是**非模块资源**（polyfill 的 nomodule script、内联 runtime、CSS）——混合场景（RBL-724 分层）里 nomodule 在 module 前的顺序仍是必要的。

```javascript
// 入口标签清单生成
function emitTags(entry, manifest) {
  const closure = manifest.closureOf(entry);             // 依赖闭包（含顺序）
  return {
    styles: closure.filter(f => f.type === 'css').map(f => ({
      tag: 'link', rel: 'stylesheet', href: f.url, order: f.order })),
    scripts: [
      ...closure.filter(f => f.kind === 'polyfill').map(f => nomoduleTag(f)),
      ...closure.filter(f => f.type === 'js' && f.kind !== 'polyfill')
        .map(f => ({ tag: 'script', type: 'module', src: f.url })),
    ],
    preloads: generateModulePreloads(entry, manifest, { budgetKB: 100 }),
  };
}
// SEO 基础标签诊断
function diagnoseSeo(meta) {
  const required = ['title', 'description', 'canonical', 'og:image'];
  return required.filter(k => !meta[k]).map(k => `RBL5001: 缺失 ${k}（影响搜索/分享）`);
}
const esc = (s) => s.replace(/[<>&"']/g, c => `&#${c.charCodeAt(0)};`);   // 默认转义
```
