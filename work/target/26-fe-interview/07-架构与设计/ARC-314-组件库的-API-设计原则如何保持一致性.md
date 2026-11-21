---
title: [ARC-314] 组件库的 API 设计原则：如何保持一致性？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-314：组件库的 API 设计原则：如何保持一致性？
**答**：
- API 一致性规则（可 lint 化）：命名统一（visible vs open 不能混用，定词典维护）、受控/非受控双模式规范（`value/onChange` 与 `defaultValue`）、size 全库统一枚举（sm/md/lg）、事件命名 onXxx、透传约定（rest props 透传到根元素）。
- API 审查：RFC 机制（ARC-038）+ API 报告 CI——用 api-extractor 生成 API 报告文件，PR 改动 API 必须 diff review，防止无意破坏。
- 弃用流程：`@deprecated` 注释 + console.warn + 迁移指南 + codemod（ARC-036 兼容管理），两个大版本后移除。
- 文档即契约：JSDoc 生成文档站（typedoc/dumi），文档缺失的 API 不允许发布（CI 检查 export 均有注释）。

```typescript
// API 词典 lint（自定义 eslint rule 的目标清单）
const API_DICT = {
  visibility: ['visible', 'defaultVisible', 'onVisibleChange'],  // 统一用 visible 而非 open
  size: ['sm', 'md', 'lg'],
};
export interface ButtonProps extends Omit<HTMLAttributes<HTMLButtonElement>, 'onClick'> {
  /** 主题类型 @default 'default' */
  type?: 'default' | 'primary' | 'danger';
  /** 尺寸 @default 'md' */
  size?: `${keyof typeof API_DICT.size}`;
  /** 受控值 */
  visible?: boolean;
  defaultValue?: boolean;
  onChange?: (v: boolean) => void;
}
// CI：api-extractor run → diff api-report.md → 破坏性变更需 RFC 链接
```
