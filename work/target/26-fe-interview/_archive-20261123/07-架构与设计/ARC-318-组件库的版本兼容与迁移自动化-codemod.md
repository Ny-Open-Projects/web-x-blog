---
title: [ARC-318] 组件库的版本兼容与迁移自动化：codemod？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-318：组件库的版本兼容与迁移自动化：codemod？
**答**:
- 破坏性变更的代价随使用者规模放大：组件库大版本升级 = 全公司 N 个应用改代码。治理目标是**迁移成本 ≤ 半天**：deprecated 预警期 + codemod 自动化 + 兼容垫层。
- 流程：破坏性 API 先发 deprecation 版本（运行时 warn + 文档迁移指南 + codemod 脚本）→ 一个大版本周期并行支持 → 大版本移除，用户跑 codemod 一键迁移。
- codemod 工程化：基于 jscodeshift/gogocode 的迁移脚本进组件库仓库（与破坏性变更同一 PR 提交），CI 验证 codemod 对官方测试仓（兼容性金丝雀应用）的转换正确性。
- 兼容垫层：无法 codemod 的深度破坏（如渲染结构变化），提供兼容包（旧 API 转发到新实现）作为缓冲，文档标注废弃时限。

```javascript
// codemod 示例：Modal visible → open 迁移
module.exports = (file, api) => {
  const j = api.jscodeshift;
  return j(file.source)
    .findJSXElements('Modal')
    .forEach(p => {
      j(p).findJSXAttributesByName('visible').forEach(a => a.node.name.name = 'open');   // props 改名
      j(p).findJSXAttributesByName('onVisibleChange')
        .forEach(a => a.node.name.name = 'onOpenChange');
    })
    .toSource();
};
// CI 验证：fixtures/*.tsx → codemod → 与期望产物 diff → fail 则迁移脚本有 bug
```
