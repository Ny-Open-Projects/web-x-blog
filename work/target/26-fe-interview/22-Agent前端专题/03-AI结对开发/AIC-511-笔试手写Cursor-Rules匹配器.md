---
title: [AIC-511] 笔试：手写 Cursor Rules 匹配器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-511：笔试：手写 Cursor Rules 匹配器

**答**：实现 `matchRules(rules, filePath)`。rules: `{ file, globs?: string[], content: string }[]`（file 是规则文件路径）。规则：1) 全局规则（无 globs）→ 始终匹配；2) 目录规则（有 globs）→ filePath 匹配任一 glob → 匹配；3) **返回匹配的规则列表**（按 specificity 排序：文件级 > 目录级 > 全局）；4) specificity 计算：globs 匹配的 glob 数量多 = 更 specific。边界：rules 空（空匹配）；filePath 空；规则无 globs 且无 content（空规则——跳过）；多个目录规则同时匹配（全部返回——按 specificity 排序）。

```javascript
function matchGlob(pattern, path) {
  if (pattern.endsWith('/**')) return path.startsWith(pattern.slice(0, -4));
  if (pattern.endsWith('*')) return path.startsWith(pattern.slice(0, -1));
  return path === pattern || path.startsWith(pattern + '/');
}
function matchRules(rules = [], filePath = '') {
  const matched = [];
  for (const rule of rules) {
    if (!rule.content) continue;
    if (!rule.globs?.length) {
      matched.push({ rule, specificity: 0 });           // 全局
      continue;
    }
    const matches = rule.globs.filter(g => matchGlob(g, filePath));
    if (matches.length) {
      matched.push({ rule, specificity: matches.length });   // 目录级
    }
  }
  matched.sort((a, b) => b.specificity - a.specificity);  // specificity 降序
  return matched.map(m => m.rule);
}

// 自测
const rules = [
  { file: 'global.md', content: 'Use TypeScript strict' },                        // 全局
  { file: 'auth.md', globs: ['src/auth/**', 'lib/auth/**'], content: 'Use JWT' }, // auth 目录
  { file: 'api.md', globs: ['app/api/**'], content: 'Include error handler' },    // api 目录
  { file: 'empty.md', content: '' },                                       // 空内容跳过
];
// auth 文件 → 全局 + auth 规则
let r = matchRules(rules, 'src/auth/login.ts');
console.log(r.length === 2);                             // 全局 + auth
console.log(r.some(x => x.content === 'Use JWT'));
console.log(r.some(x => x.content === 'Use TypeScript strict'));

// api 文件 → 全局 + api 规则
r = matchRules(rules, 'app/api/users/route.ts');
console.log(r.length === 2);
console.log(r.some(x => x.content === 'Include error handler'));
// 无关文件 → 只有全局
r = matchRules(rules, 'src/components/Button.tsx');
console.log(r.length === 1);                             // 仅全局

// specificity 排序：auth 在 global 前
r = matchRules(rules, 'src/auth/login.ts');
console.log(r[0].file === 'auth.md');                    // 目录级 > 全局

// 空
console.log(matchRules([], 'x.ts').length === 0);
```

**评分点**：
- 匹配逻辑正确：全局（无 globs）始终匹配 + 目录 glob 匹配；空内容跳过
- specificity 排序（匹配数多的目录规则优先——上下文更精确）；无关文件只有全局
- 边界（空 rules/空 path/多目录规则同时匹配）；与 RBL-502 上下文裁剪的规则维度
- 能说清「目录级 rules 的上下文匹配 = token 效率与遵守度双赢：只注入相关规则」属于加分
