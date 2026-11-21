---
title: [RBL-442] 笔试：手写产物导出兼容性检查器（exports 字段审计）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-442：手写产物导出兼容性检查器
**需求**：实现 `checkExports(pkgJson, distFiles)`：1) 校验 exports 条件完整性：types 顺序在最前（TS 双读）、import/require 指向文件存在；2) 每个导出路径存在性（exports 里声明的文件 dist 里必须有）；3) 反向：dist 里存在但 exports 未声明的文件（意外产物）列出；4) main/module/exports 一致性（老工具链回退路径也指向有效文件）；5) 双包陷阱检测：import 与 require 指向同一文件（同文件双语义——双实例风险）；6) 输出 { ok, errors, warnings }。

```javascript
function resolveExportPath(root, sub) {
  const p = sub.replace('.', root)
  return p
}

export function checkExports(pkgJson, distFiles /* Set<path> */) {
  const errors = [], warnings = []
  const exports = pkgJson.exports ?? { '.': pkgJson.main }
  const declared = new Set()

  for (const [key, cond] of Object.entries(exports)) {
    const conditions = typeof cond === 'string' ? { default: cond } : cond
    // types 必须在最前
    const keys = Object.keys(conditions)
    if ('types' in conditions && keys[0] !== 'types')
      warnings.push(`[${key}] types 条件应在最前（TS 双读正确性）`)
    for (const [c, file] of Object.entries(conditions)) {
      const resolved = resolveExportPath('.', file)
      declared.add(resolved)
      if (!distFiles.has(resolved))
        errors.push(`[${key}.${c}] 文件不存在: ${file}`)
      if (c === 'import' && conditions.require && conditions.require === file)
        errors.push(`[${key}] import 与 require 指向同一文件 — 双实例风险`)
    }
  }
  // main/module 回退一致性
  if (pkgJson.main && !distFiles.has(pkgJson.main)) errors.push(`main 文件不存在: ${pkgJson.main}`)
  // 未声明产物
  for (const f of distFiles)
    if (!f.endsWith('.map') && !declared.has(f) && !f.endsWith('.d.ts'))
      warnings.push(`产物未在 exports 声明: ${f}`)

  return { ok: errors.length === 0, errors, warnings }
}
```
**评分点**：
- types 顺序校验（TS 双读的正确顺序——exports 陷阱高频点）
- import/require 同文件双实例检测
- 双向审计（声明存在性 + 未声明产物清单）
- main/module 回退兼容（老工具链解析路径）
