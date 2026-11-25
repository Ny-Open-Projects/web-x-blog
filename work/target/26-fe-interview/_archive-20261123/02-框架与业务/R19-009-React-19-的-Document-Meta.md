---
title: [R19-009] React 19 的 Document Metadata 支持是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-009：React 19 的 Document Metadata 支持是什么？
**答**：
- 组件内可以直接渲染 `<title>`、`<meta>`、`<link>` 等标签，React 自动把它们提升到 `<head>`。
- 不再需要 react-helmet 之类的第三方库做 SEO 信息管理。
- 支持去重与提升：多个组件声明同名 meta 时由 React 决定最终生效的值。
- 需要针对流式渲染/特殊场景精细化控制的团队仍可用第三方库，但大多数场景内置能力已够用。

```jsx
function BlogPost({ post }) {
  return (
    <article>
      {/* 这些标签会被自动提升到 head，组件写在哪里都可以 */}
      <title>{post.title}</title>
      <meta name="description" content={post.summary} />
      <link rel="canonical" href={'https://example.com/posts/' + post.id} />
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </article>
  );
}
```
