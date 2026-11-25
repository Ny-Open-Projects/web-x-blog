---
title: [BLD-202] 模块解析（resolver）的查找顺序怎么工作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-202：resolver 怎么工作？
**答**：
- 解析顺序：① alias 替换；② 相对路径（基于 importer 目录）或裸模块（node_modules 逐级向上查找）；③ 尝试扩展名（resolve.extensions）；④ package.json 的 exports（现代）→ main/module/browser（legacy）；⑤ symlinks 处理（preserveSymlinks 差异）。
- exports 字段的语义：条件导出（import/require/types）+ 子路径限制（未声明即不可导入）——「exports 之外路径不可达」是 modern 包打包报错的新来源。
- mainFields 差异：module（ESM tree-shakeable）优先于 main（CJS）——顺序错误会打包出 CJS 版本（体积大）。
- pnpm 的 symlink 结构对 resolver 的要求（resolve.symlinks: true 默认把真实路径归一化）。
- 追问钩子：为什么同一个包「浏览器里对、构建时错」——运行时用浏览器字段（browser），构建 resolver 可能选中 main（CJS 版本）或 exports 的 node 条件；理解条件匹配顺序（browser→module→main）才能解释双端差异。

```javascript
// resolver 伪代码
function resolve(specifier, importer) {
  if (alias[specifier]) specifier = alias[specifier];
  let base = specifier.startsWith('.') ? path.join(dirname(importer), specifier)
    : findUp('node_modules/' + specifier, dirname(importer));
  const pkg = readPkg(base);
  const target = pkg.exports
    ? matchCondition(pkg.exports, conditions)        // import/browser/development
    : pickMainField(pkg, ['browser', 'module', 'main']);
  return tryExtensions(target, extensions);          // .tsx .ts .jsx .js
}
```
