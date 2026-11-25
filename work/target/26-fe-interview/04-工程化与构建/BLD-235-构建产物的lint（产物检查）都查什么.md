---
title: [BLD-235] 构建产物的 lint（产物级检查）都查什么？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-235：产物 lint 查什么？
**答**：
- 产物正确性：manifest 引用完整性（HTML 引用的 chunk 全存在）、双实例检测（同包多版本，SCN-ENG-290）、module.exports 与 ESM 混用错误、sourcemap 引用对齐。
- 产物安全性：无内联密钥（secret 扫描进产物）、sourcemap 未外泄（SCN-ENG-242）、动态 eval/Function 注入审计（CSP 兼容）。
- 产物兼容性：目标浏览器语法残留（browserslist 漏网——regenerator 残留检测）、可选链等现代语法在低版本目标的编译遗漏。
- 产物性能：超大 chunk（maxSize 告警）/重复大依赖/内联大图。
- 追问钩子：为什么产物 lint 要查「语法残留」而不是信任编译配置——browserslist 只作用于特定 loader 链（babel/swc 的 targets 选项独立配置），某条链（如 worker 的 loader）漏配 targets 时现代语法直接透传——低版本浏览器白屏；产物级语法扫描是编译配置错误的最后防线。

```javascript
// 产物语法扫描
const es2019Plus = scanSyntax(bundle);
if (es2019Plus.length && targetsInclude('ios 12'))
  fail(`产物含未编译语法: ${es2019Plus[0].feature}（检查 worker loader 的 targets）`);
// 双实例检测（SCN-ENG-290 复用）
const dup = detectDuplicateInstances(bundle);
```
