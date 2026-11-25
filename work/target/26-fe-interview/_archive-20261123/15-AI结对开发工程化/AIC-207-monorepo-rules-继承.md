---
title: [AIC-207] monorepo 下各包有各自规范，Cursor rules 如何做到「全局 + 包级」继承与合并？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-207：monorepo 下各包有各自规范，Cursor rules 如何做到「全局 + 包级」继承与合并？
**答**：
- 根目录放全局规则，各 package 放自己的 .cursor/rules，靠 glob 限定包路径天然隔离。
- 包级规则只写「差异」，不重复全局约定，避免合并后自相矛盾。
- 优先级显式化：冲突时约定「包级覆盖全局」，写进全局规则本身。
- CI 校验：扫描所有包规则，检测 glob 重叠区内的矛盾关键词（如一个说用 styled-components 一个说用 tailwind）。

```javascript
function collectRules(repoRoot: string, filePath: string) {
  const pkgs = findPackages(repoRoot, filePath); // 命中文件所在包
  const all = [...globalRules(repoRoot), ...pkgs.flatMap(p => pkgRules(p, filePath))];
  // 包级覆盖全局：同名主题（按 heading）包级优先
  const merged = new Map<string, string>();
  for (const r of all.sort(byPriority)) merged.set(r.topic, r.body);
  return [...merged.values()];
}
r
```
