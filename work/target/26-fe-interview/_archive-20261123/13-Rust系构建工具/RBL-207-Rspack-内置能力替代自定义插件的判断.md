---
title: [RBL-207] 什么需求该用内置能力而不是写自定义插件
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-207：什么需求该用内置能力而不是写自定义插件

**答**:
- 判断顺序：配置项能表达（define/html 替换/banner）→ 内置插件（HtmlPlugin/DefinePlugin/CopyPlugin）→ experiments 能力 → 最后才是自定义 JS 插件
- 性能原因：内置能力跑在 Rust 侧零跨边界成本；同逻辑的自定义 JS 插件可能慢一个数量级
- 常见可替代清单：注入变量用 DefinePlugin、文本替换用内置 loader、产物清单用 `rspack-manifest-plugin`（社区适配版）、体积分析用 builtin:stats（Rsbuild 内置分析）
- 例外：强业务耦合逻辑（按业务规则改产物）才值得 JS 插件，且尽量收敛到 processAssets 单个钩子

```javascript
// ❌ 自定义插件做变量注入
class InjectApi extends Plugin { /* tap processAssets, regex replace __API__ */ }
// ✅ 内置
config.plugins.push(new rspack.DefinePlugin({ __API__: JSON.stringify(process.env.API_URL) }))
// ✅ 内置分析
config.experiments = { ...config.experiments }
// Rsbuild: output.asciiOnly / tools.rspack 直接透传；bundle 分析用 builtin:stats
```
