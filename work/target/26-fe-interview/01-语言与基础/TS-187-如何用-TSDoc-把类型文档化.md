---
title: [TS-187] 如何用 TSDoc 把类型文档化？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-187：如何用 TSDoc 把类型文档化？
**答**：
- TSDoc 标签（@param/@returns/@example/@see）在编辑器 hover 直接渲染，@link 可点击跳转。
- 公共 API（工具库、组件库、hook）强制注释，用 eslint-plugin-jsdoc/tsdoc 校验。
- 类型注释的价值在"决策"：为什么是 union、为什么允许 undefined，比复述类型本身重要。

```typescript
/**
 * 把分页响应逐页拉取并拍平为行数组。
 *
 * @param fetchPage - 拉取单页的函数，返回该页行与游标
 * @param maxPages - 最多拉取的页数，防止游标死循环
 * @returns 拍平后的行数组
 *
 * @see {@link Page} 行的结构定义
 * @example
 * const rows = await fetchAll((cursor) => api.list(cursor), 5);
 */
interface Page<Row> { rows: Row[]; next?: string }
declare function fetchAll<Row>(
  fetchPage: (cursor?: string) => Promise<Page<Row>>,
  maxPages: number,
): Promise<Row[]>;

// hover fetchAll 显示完整富文档；@link 的 Page 可点击跳转
// 团队规范：export 的函数/类型必须有 TSDoc；内部实现随意
```

## 第三十八章 综合大题（TS-188 ~ TS-200）
