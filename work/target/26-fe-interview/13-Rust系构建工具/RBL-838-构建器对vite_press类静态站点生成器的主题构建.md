---
title: [RBL-838] 场景题：文档站/静态站点生成器的主题构建——MDX 管线与代码块处理
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-838：场景题：文档站/静态站点生成器的主题构建——MDX 管线与代码块处理

**答**:
- 文档站（MDX）构建管线：MDX = Markdown + JSX——构建链：remark（markdown AST）→ rehype（HTML AST）→ MDX 编译（JSX 语法→ 组件调用）；代码块处理是重点：语法高亮（shiki：构建期高亮产物含内联样式/span，零运行时成本）、代码块复制按钮（rehype 插件注入）、标题锚点生成（heading id 唯一化与重名处理）。
- 构建器的集成点：MDX 文件是模块（transform 钩子编译成 React 组件——虚拟导出 default 组件 + frontmatter 导出）；「代码块的产物一致性」（高亮器版本锁定——shiki 更换主题会全量 diff，构建缓存键含高亮主题）。
- 死链接检测：文档站的链接（站内相对链接）在构建期解析——死链（指向不存在的页面/锚点）是文档质量门禁（RBL-673 文档工程的一环）；「站点地图一致性」（sitemap 与实际页面集合 diff）。
- 增量构建：文档页面天然独立（md → html 页面级缓存，RBL-633）——但「全站导航/目录」跨页共享（目录树变化 → 全站导航重渲染——布局层与内容层的缓存边界）。
- 追问钩子：为什么代码块高亮选「构建期」（shiki）而不是「运行时」（highlight.js in browser）？——运行时高亮 = 每个读者重复付解析成本 + CLS 风险（高亮后代码块高度变化）；构建期一次付清，产物是纯 HTML（无 JS 依赖、SSR 友好）；代价是构建时间（shiki 慢）——用持久缓存（代码块文本 hash 为键）摊销。

```javascript
// MDX 管线（构建器插件视角）
async function transformMdx(code, id) {
  const vfile = await compile(code, {
    rehypePlugins: [
      rehypeShiki({ theme: 'github-dark' }),             // 构建期高亮
      rehypeSlug(),                                      // 标题锚点（重名自动 -1）
      rehypeCopyButton(),
    ],
  });
  return {
    code: vfile.code,                                    // React 组件
    exports: extractFrontmatter(code),                   // title/date 等导出
  };
}
// 死链检测
function auditLinks(pages) {
  const known = new Set(pages.map(p => p.path));
  const broken = [];
  for (const p of pages)
    for (const link of p.links ?? [])
      if (link.startsWith('/') && !known.has(link.split('#')[0]))
        broken.push({ from: p.path, to: link });
  return broken;                                         // 死链清单 -> 文档门禁
}
```
