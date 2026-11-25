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

## 补充：边界与追问

**边界与易错**：

- `@param` 的名字必须与形参完全一致，改了参数名忘了改注释，TSDoc 校验会报错，hover 里参数说明也会错位。
- 注释必须紧贴声明且中间不能空行，否则不会被关联到该符号，编辑器 hover 时显示为空。
- `@example` 里的代码不参与类型检查，示例和签名漂移是文档过时的最大来源，最好配 doctest 或至少做示例类型校验。

**追问**：

1. TSDoc 和 JSDoc 有什么实质区别？ → TSDoc 是 TS 生态的严格规范（如 `@returns` 而非 `@return`），VS Code 原生解析并渲染，JSDoc 更宽松、面向纯 JS。
2. 怎么标一个 API 已废弃并让调用处出现删除线？ → 用 `@deprecated` 加说明，TS 语言服务会给该符号和调用处加删除线与提示。
3. 内部类型也要写 TSDoc 吗？ → 只对 export 的公共 API 强制；内部实现靠命名和类型自解释，全量注释会变成噪声且难维护。
