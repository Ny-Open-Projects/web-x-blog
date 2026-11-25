---
title: [RBL-932] 综合深水：构建器升级的 codemod 自动化——从「改配置」到「改代码」的迁移面
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-932：综合深水：构建器升级的 codemod 自动化——从改配置到改代码

**答**:
- 构建器升级的迁移面不止配置：1) **配置 codemod**（RBL-666 翻译器）；2) **代码 codemod**（API 用法变更：`require.context` → `import.meta.glob`、webpack 特有魔法注释 → 标准语法、`process.env.X` → `import.meta.env.X`——AST 转换而非正则）；3) **依赖 codemod**（webpack 特有包替换：terser-webpack-plugin 删除）；4) **注释/文档 codemod**（魔法注释/CI 脚本）。迁移面的完整清单决定工时预估精度（RBL-822）。
- codemod 的质量工程：AST 转换的 fixture 测试（转换前/后快照）；「不可转换项」的显式报告（TODO 注释插入 + 清单——RBL-666 哲学：宁可少转换不静默错）；codemod 的 dry-run 模式（diff 预览）。
- codemod 的执行纪律：git 分支执行（可回滚）+ 分批提交（每个 codemod 一个 commit——review 粒度与回滚粒度）；「codemod 不可重入」的风险（跑两次重复转换——幂等性要求）。
- codemod 与 lint 的闭环：codemod 后的代码要过 lint（转换引入的新模式被 lint 校验）——「转换 → 校验 → 提交」的流水线。
- 追问钩子：为什么「代码 codemod 必须用 AST 而不是正则」？——正则会命中字符串/注释里的同形文本（'process.env.X' 在日志文案里被误改）；AST 按语法角色定位（MemberExpression process.env.X 才转换）；codemod 的错误是「静默改错代码」（比构建错误更糟）——转换工具的正确性要求与编译器同级（fixture + AST + 幂等）。

```javascript
// AST codemod 示意（jscodeshift 模式）
const transform = (file, api) => {
  const j = api.jscodeshift;
  const root = j(file.source);
  let changed = false;
  // process.env.X -> import.meta.env.X（跳过字符串内）
  root.find(j.MemberExpression, {
    object: { object: { name: 'process' }, property: { name: 'env' } },
  }).forEach((p) => {
    const prop = p.node.property.name;
    p.replace(j.memberExpression(
      j.memberExpression(j.identifier('import'), j.identifier('meta')),
      j.identifier(prop)));
    changed = true;
  });
  if (!changed) return null;
  return root.toSource({ quote: 'single' });
};
// 幂等性自测：跑两次结果相同
const once = transform({ source: src }, api);
expect(transform({ source: once }, api)).toBe(once);     // 幂等
```
