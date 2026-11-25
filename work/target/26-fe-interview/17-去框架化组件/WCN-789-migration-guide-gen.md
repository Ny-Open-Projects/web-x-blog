---
title: [WCN-789] 组件属性发生变更时，如何自动生成迁移指南？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-789：组件属性发生变更时，如何自动生成迁移指南？

**答**：
- 结论：在组件元数据里为每次 breaking change 标注「旧名→新名、转换规则、示例」；发布时由生成器汇总成迁移文档与 codemod，按版本区间输出「从 v1 到 v2 怎么改」。
- 迁移指南包含：变更原因、影响范围、代码前后对比、自动迁移命令；与 semver 和 CHANGELOG 联动。
- 追问钩子：属性语义变了但名字没变（如 size 从枚举改像素）怎么提示？考察「语义变更也要显式标注迁移说明」。

```javascript
const changes = [
  { from: 'size', to: 'scale', map: (v) => ({ sm: 's', lg: 'l' }[v] || v), reason: '统一命名' },
  { from: 'onClick', to: 'onPress', map: (v) => v, reason: '事件语义对齐' },
];
function genMigration(changes) {
  return changes.map((c) => `
### ${c.from} → ${c.to}
- 原因：${c.reason}
- 改法：将 \`${c.from}\` 改为 \`${c.to}\`，值按规则转换
- 示例：${c.from}={sm} → ${c.to}={${c.map('sm')}}
`).join('\n');
}
console.log(genMigration(changes));
```
