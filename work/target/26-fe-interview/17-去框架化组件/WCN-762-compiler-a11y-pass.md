---
title: [WCN-762] 编译器如何在编译期自动注入 a11y 属性并给出告警？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-762：编译器如何在编译期自动注入 a11y 属性并给出告警？

**答**：
- 结论：在模板编译的 AST pass 里做 a11y 检查——检测到 `<img>` 无 alt、可点击 `<div>` 无 role/tabindex、表单控件无 label 时，按配置自动注入默认属性或发出编译告警。
- 注入要克制：只补安全的默认值（如 `alt=""`），语义缺失（如按钮用途）只告警不猜测；告警分级（error/warn）并接入 CI 门禁。
- 追问钩子：自动注入的 alt="" 真的满足无障碍吗？考察「装饰性图片可空、信息性图片必须人工填写」的语义判断。

```javascript
function a11yPass(node, diagnostics) {
  if (node.type === 'El' && node.tag === 'img' && !node.attrs?.alt) {
    node.attrs = { ...node.attrs, alt: '' };           // 安全默认：装饰性图片
    diagnostics.push({ level: 'warn', msg: 'img 缺少 alt，已填空', line: node.loc?.line });
  }
  if (node.type === 'El' && node.attrs?.onClick && !node.attrs?.role) {
    diagnostics.push({ level: 'error', msg: '可点击元素缺少 role/tabindex', line: node.loc?.line });
  }
  if (node.children) node.children.forEach((c) => a11yPass(c, diagnostics));
  return node;
}
const diag = [];
const ast = { type: 'El', tag: 'img', attrs: {}, loc: { line: 3 } };
a11yPass(ast, diag);
console.log(ast.attrs, diag);
```
