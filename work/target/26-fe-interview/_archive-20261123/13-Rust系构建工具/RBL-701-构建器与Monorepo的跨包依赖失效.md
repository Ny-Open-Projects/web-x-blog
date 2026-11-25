---
title: [RBL-701] Monorepo 跨包构建失效：workspace 协议、source 引用与产物引用的一致性
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-701：Monorepo 跨包构建失效：workspace 协议、source 引用与产物引用的一致性

**答**:
- monorepo 包间引用三种形态：1) **source 直引**（app import packages/ui/src —— dev 免构建但语义耦合）；2) **产物引用**（ui 的 dist，需先构建 ui——顺序依赖）；3) **workspace 协议**（package.json `"@org/ui": "workspace:*"`，包管理器 symlink + resolve 指向源码）。三者的失效传播与构建编排完全不同——混用是 monorepo 构建事故的主因。
- source 直引的失效面最大：ui 源码改一行，所有引用它的 app 全量重建（没有产物层隔离）；产物引用失效面最小但要求「产物新鲜」（ui 改了没重建，app 用旧产物——stale 危险）。工程实践：dev 走 source（快），CI/发布走产物（稳），两者用构建器条件切换（build mode 决定 resolve 策略）。
- 增量失效的正确姿势：包级输入指纹（turbo 的 inputs 声明）+ 依赖闭包传播（ui 变 → ui build 失效 → 依赖 ui 的 app build 失效）——传播只在「产物引用」链上，source 直引会绕过包边界让图变成模块级（退化成大仓库）。
- workspace 协议的发布语义：`workspace:*` 发布时被替换成真实版本号——构建器要理解发布态与开发态的 resolve 差异；dual mode（dev source、prod dist）用 package.json 的 `exports` 条件（development 条件）实现。
- 追问钩子：为什么「ui 改了没重建，app 用旧产物」是静默 bug？——stale 产物不报错（一切正常跑旧代码），与「缓存污染」同构；防线是「构建前新鲜度校验」（包产物 manifest 的 buildId 与源码 hash 比对，过期即拒绝构建上游）。

```javascript
// 构建器条件 resolve（dev/prod 双模式）
function resolvePackage(id, mode) {
  const pkg = findWorkspacePkg(id);
  if (!pkg) return null;
  if (mode === 'dev' && pkg.source) return pkg.source;    // source 直引（快）
  // prod：校验产物新鲜度
  const manifest = readJson(`${pkg.dir}/dist/manifest.json`);
  const srcHash = hashDir(pkg.sourceDir);
  if (manifest.sourceHash !== srcHash)
    throw new Error(`${id} 产物过期（源码已变未重建）——请先构建 ${id} 或改用 workspace source 模式`);
  return `${pkg.dir}/dist`;
}
// 编排传播（turbo 语义）
// packages/ui build -> apps/web build（依赖闭包自动排序）
// source 直引时闭包被打破：web build 的输入包含 ui 源码 -> 指纹含 ui/**（退化正确但失效面大）
```
