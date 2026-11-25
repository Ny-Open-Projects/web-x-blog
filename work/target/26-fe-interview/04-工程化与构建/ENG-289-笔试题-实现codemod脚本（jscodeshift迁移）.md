---
title: [ENG-289] 笔试题——实现 codemod（旧 API → 新 API 批量迁移脚本）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## ENG-289：手写 codemod：旧 API 批量迁移

**需求与边界**：
- 迁移目标：`import { OldButton } from '@org/ui'` → `import { Button } from '@org/ui'`，且 `<OldButton type="primary">` → `<Button variant="primary">`。
- 边界：① 重命名 import 同时更新所有 JSX 引用；② 属性改名（type→variant）仅当值为已知枚举（primary/default），其他值保留并插 TODO 注释；③ 幂等（重复运行无 diff）。

**答**：
```javascript
// codemod/old-button-v2.js（jscodeshift）
const KNOWN = new Set(['primary', 'default']);
module.exports = (file, api) => {
  const j = api.jscodeshift, root = j(file.source);
  let changed = false;
  root.find(j.ImportSpecifier, { imported: { name: 'OldButton' } })
    .forEach(p => { p.node.imported.name = 'Button'; changed = true; });
  root.find(j.JSXOpeningElement, { name: { name: 'OldButton' } })
    .forEach(p => {
      p.node.name.name = 'Button';
      for (const attr of p.node.attributes) {
        if (attr.name?.name === 'type') {
          const val = attr.value?.value;
          if (KNOWN.has(val)) { attr.name.name = 'variant'; }      // 已知枚举改名
          else {
            attr.name.name = 'variant';
            attr.comments = [j.commentBlock(` TODO: 校验 variant 值 ${val} `, true, false)];
          }
        }
      }
      changed = true;
    });
  return changed ? root.toSource() : undefined;      // 未变更返回 undefined = 幂等
};
// test: fixture 输入/输出快照，重复运行 diff 为空
```

**评分点**:
- import 与 JSX 引用同步改（漏一边产生编译错）。
- 未知枚举值插 TODO 不静默替换（人审兜底）。
- 幂等（未变更返回 undefined，jscodeshift 约定）。
- fixture 快照测试配套意识。
