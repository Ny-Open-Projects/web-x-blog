---
title: [RBL-749] ESM CDN 分发产物：import map、裸导入重写与版本协商的构建适配
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-749：ESM CDN 分发产物：import map、裸导入重写与版本协商的构建适配

**答**:
- ESM CDN（esm.sh/skypack 类）的分发模式：发布到 CDN 的包保留**裸导入**（import 'react' 由 import map 或 CDN 的重写服务解析）——构建器为「CDN 分发目标」的处理：external 全部裸导入 + 产物符合 CDN 重写规范（无相对路径泄漏、无 CJS 混入、顶层只依赖可解析的裸说明符）。
- import map 方案（自托管 CDN）：构建器生成 import map（裸导入 → 具体 URL 的映射，版本锁定）；map 的 hash 级联（RBL-598）：map 里引用的产物 hash 变 → map 变 → 引用 map 的 html 变。
- 版本协商的形态对比：import map（宿主集中控制版本——适合单页应用）vs per-URL 版本（`/react@18/es2022/react.mjs`——适合微前端/多版本共存）vs import maps + fallback（浏览器不支持 import map 的降级 shim）。构建器要按分发目标输出对应形态。
- 裸导入重写的安全边界：CDN 重写服务是第三方信任域（esm.sh 的响应被篡改 = 供应链攻击）——自托管 import map 是安全推荐；若必须用第三方 CDN，子资源完整性（SRI）与锁定具体 URL 是缓解。
- 追问钩子：为什么「CDN ESM 产物」必须保留裸导入而不能全部内联？——CDN 分发的价值是「跨应用共享同一 URL 的模块」（浏览器 HTTP 缓存跨站点复用）；全内联 = 每个应用重复携带 = 退化成普通 bundle。裸导入 + 集中 map 是「模块粒度共享」的关键——这是 ESM CDN 与传统 bundle 的本质差异。

```javascript
// import map 生成
function generateImportMap(manifest, { externalPkgs }) {
  const imports = {};
  for (const pkg of externalPkgs) {
    const entry = manifest.lookup(pkg);                  // 包 -> 产物 URL（版本锁定）
    if (!entry) throw new Error(`import map 缺失: ${pkg}`);
    imports[pkg] = entry.url;                            // '/@18/react.mjs' 具体版本
  }
  return { imports };
}
// 构建器 CDN 目标配置
const cdnConfig = {
  format: 'es',
  external: 'all-bare',                                  // 裸导入全外置
  entryFileNames: '[name]/index.mjs',                    // CDN 目录结构
  emit: [{ kind: 'import-map', file: 'import-map.json' }],
};
// HTML 注入（map 先于模块加载）
// <script type="importmap">{"imports":{"react":"/react@18/index.mjs"}}</script>
// <script type="module" src="/app/index.mjs"></script>
```
