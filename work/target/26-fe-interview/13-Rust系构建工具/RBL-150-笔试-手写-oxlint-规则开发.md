---
title: [RBL-150] 笔试：手写自定义 lint 规则（no-direct-fetch-in-model）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-150：笔试：手写自定义 lint 规则（模型层禁止裸调 fetch）

**答**：写规则 no-fetch-in-service：1) 遍历源码 AST；2) 当文件路径含 `services/` 且出现裸 `fetch(url)` 调用（非经过封装的 http.get/post）时报错；3) 错误信息带行号（由 span 换算）；4) 支持豁免：调用点前一行有 `// oxlint-disable-next-line no-fetch-in-service` 注释则跳过；5) 输出诊断数组 [{file, line, message}]，可对接任意 lint 引擎（思路等价 oxlint/ESLint 的 visitor 规则）。

```typescript
// rules/no-fetch-in-service.ts
import { parseSync } from 'oxc-parser';

interface Diag { file: string; line: number; message: string }

export function noFetchInService(file: string, source: string): Diag[] {
  if (!file.includes('services/')) return [];
  const diags: Diag[] = [];
  const ast = parseSync(file, source, { sourceType: 'module', lang: 'ts' }).program;
  const lineStarts = [...source.matchAll(/\n/g)].map(m => m.index! + 1).concat(source.length);
  const toLine = (offset: number) => lineStarts.findIndex(s => s > offset) + 1;

  walk(ast, {
    CallExpression(n: any) {
      const callee = n.callee;
      const isFetch = callee?.type === 'Identifier' && callee.name === 'fetch';
      if (!isFetch) return;
      // 豁免：检查调用所在行上一行是否有 disable 注释
      const line = toLine(n.span.start);
      const lines = source.split('\n');
      const prev = lines[line - 2] ?? '';
      if (prev.includes('oxlint-disable-next-line no-fetch-in-service')) return;
      diags.push({ file, line, message: 'services 层禁止裸调 fetch，请使用封装的 http 客户端' });
    },
  });
  return diags;
}
// 测试用例思路：
// 1) services/a.ts 里 fetch('/api') → 报错；2) 带 disable 注释 → 不报；
// 3) 非 services 目录 → 不报；4) http.get(...) → 不报（callee 非裸 fetch）。
```
**评分点**：
- 目录过滤前置（不在 services 直接返回，避免无谓解析）。
- span → 行号换算正确。
- disable-next-line 豁免机制。
- callee 类型判断严格（Identifier 而非任意调用）。
- 能说明规则测试要覆盖正/反/豁免/边界四类用例。
