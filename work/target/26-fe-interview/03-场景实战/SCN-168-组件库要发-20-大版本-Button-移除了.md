---
title: [SCN-168] 组件库要发 2.0 大版本（Button 移除了 type="ghost"），升级前如何量化评估影响面？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-168：组件库要发 2.0 大版本（Button 移除了 type="ghost"），升级前如何量化评估影响面？
**答**：
- 影响面评估不能靠 grep 拍脑袋：写 AST 扫描脚本，用 `@babel/parser` 遍历所有源码，定位目标组件的 import 与 JSX 使用点，再校验被废弃的 prop/枚举值。
- 产出物是"受影响文件 + 行号 + 违规用法 + 修复建议"清单，直接转成 codemod 或排期表。
- 扫描要覆盖字符串动态用法（如 `type={x}`），动态值单独标"需人工确认"，不误报也不漏报。
- 把扫描接进 CI：2.0 未升级前先"warn"，给出迁移窗口；升级后变"error"卡合入。

```javascript
// 组件库升级影响面评估：AST 扫描废弃 API 用法
import { parse } from '@babel/parser';
import traverse from '@babel/traverse';
import fs from 'fs';
import fg from 'fast-glob';

const DEPRECATED = {
  Button: { removedProps: { type: ['ghost'] }, renameProps: {} }, // type="ghost" 已移除
};

export async function scanImpact(srcDirs = ['src']) {
  const findings = [];
  for (const file of await fg(`${srcDirs}/**/*.{js,jsx,ts,tsx}`)) {
    const code = fs.readFileSync(file, 'utf8');
    const ast = parse(code, { sourceType: 'module', plugins: ['jsx', 'typescript'] });
    const localNames = new Map();                      // import { Button as Btn } 的本地别名
    traverse.default(ast, {
      ImportDeclaration(path) {
        if (path.node.source.value !== '@corp/ui') return;
        path.node.specifiers.forEach(s => {
          if (s.imported && DEPRECATED[s.imported.name])
            localNames.set(s.local.name, s.imported.name);
        });
      },
      JSXOpeningElement(path) {
        const comp = localNames.get(path.node.name.name);
        if (!comp) return;
        path.node.attributes.forEach(attr => {
          if (attr.name?.name !== 'type') return;
          if (!attr.value) return;
          if (attr.value.type === 'StringLiteral' &&
              DEPRECATED[comp].removedProps.type.includes(attr.value.value)) {
            findings.push({ file, line: attr.loc.start.line, comp,
              usage: `type="${attr.value.value}"`,
              fix: `改用 ${comp} 新的视觉层级 API（参考迁移指南 v2）` });
          } else if (attr.value.type !== 'StringLiteral') {
            findings.push({ file, line: attr.loc.start.line, comp,
              usage: 'type 为动态表达式', fix: '需人工确认取值范围' }); // 动态值标人工
          }
        });
      },
    });
  }
  return findings;                                     // 输出受影响清单，转 codemod 或排期
}
```
