---
title: [RBL-602] Resolve 深水：tsconfig paths、package exports 与浏览器字段的优先级博弈
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-602：Resolve 深水：tsconfig paths、package exports 与浏览器字段的优先级博弈

**答**：
- 现代解析是多源叠加：`tsconfig paths`（类型层映射）→ `resolve.alias`（构建层映射）→ package `exports` 字段（包内自描述路由）→ `main/module/browser` 兜底。分层优先级设计错误的典型事故：tsconfig paths 只影响类型检查不影响构建 → 运行时找不到模块；构建器要把 paths 显式纳入 resolve 配置（或插件桥接）。
- exports 字段的语义深水：1) **封装性**——exports 未列出的子路径不可导入（包作者显式门面）；2) **条件导出**——`{ "import": ..., "require": ..., "default": ... }` 按 condition 匹配，构建器要按目标环境声明 conditions（如 `['import', 'browser']`）；3) 通配符模式 `./features/*`；4) `exports` 存在时 `main/module` 被忽略——三者并存时 exports 优先是明确规范。
- browser 字段的博弈：`"browser": "./dist/browser.js"` 让同一包给 Node 与浏览器不同实现（fetch/net 依赖差异）——构建器要按 platform 目标选择；打包工具默认 browser 优先、SSR 工具默认 node 优先，配错就「SSR 里跑进了浏览器代码」。
- 路径解析的确定性问题：同一 import 在两处出现解析结果不同（因目录级 tsconfig/最近 node_modules）——构建器要求 resolve 结果对 (id, importer, conditions) 是纯函数，并缓存键规范化（RBL-534）。
- 追问钩子：为什么 resolve 是构建性能的「隐形大头」？——大仓库 resolve 调用数 = 模块数 × import 数，每次可能 stat 十几个路径候选；四级缓存（id 常量/目录枚举/包 exports/文件存在性）+ 并行化是 rspack/rolldown 的标配优化。

```javascript
// 分层 resolve 伪码
async function resolveId(id, importer, ctx) {
  // 1) 构建层 alias（显式配置优先，用户意志最强）
  for (const [k, v] of ctx.alias) if (id === k || id.startsWith(k + '/')) return mapAlias(v, id);
  // 2) tsconfig paths（按 importer 最近 tsconfig）
  const ts = nearestTsconfig(importer);
  const mapped = ts?.matchPaths(id);
  if (mapped) return mapped;                            // paths 命中后仍可落到 node_modules
  // 3) 裸导入：包 exports / 兜底字段
  if (!id.startsWith('.') && !id.startsWith('/')) {
    const pkgDir = upwalk(importer, 'node_modules', id);
    const pkg = await readPkg(pkgDir);
    if (pkg.exports) {
      const entry = matchExports(pkg.exports, subpathOf(id), ctx.conditions); // 条件匹配
      if (!entry) throw new Error(`${id} 子路径被 exports 封装: ${subpathOf(id)}`);
      return path.join(pkgDir, entry);
    }
    return pkg.browser && ctx.platform === 'browser' ? pkgDir + pkg.browser
         : pkg.module || pkg.main;
  }
  // 4) 相对路径：扩展名试探 + 目录 index
  return tryExtensions(path.resolve(path.dirname(importer), id), ctx.extensions);
}
```
