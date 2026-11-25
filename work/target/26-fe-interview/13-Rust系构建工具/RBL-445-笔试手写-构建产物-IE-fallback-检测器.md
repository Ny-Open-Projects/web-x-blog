---
title: [RBL-445] 笔试：手写产物语法兼容性检测器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-445：手写产物语法兼容性检测器
**答**：实现 `checkSyntaxCompat(code, targets)`：1) targets：browserslist 目标（简化为特性集合：es2015/es2017/es2020）；2) 检测产物是否含超纲语法（简化：正则特征——可选链 ?.、??、class fields、top-level await）；3) 每个特征标注其 ES 版本与目标支持状态；4) 转译缺失告警（产物含超纲语法 = 转译配置没覆盖目标）；5) 输出 { ok, found: [{ feature, es, supportedByTargets }] }；6) 与 browserslist 一致性：目标声明与产物实际语法的交叉验证。

```javascript
const FEATURES = [
  { name: 'optional-chaining', re: /\?\./, es: 2020 },
  { name: 'nullish-coalescing', re: /\?\?/, es: 2020 },
  { name: 'top-level-await', re: /^\s*await\s+/m, es: 2022 },
  { name: 'class-fields', re: /^\s*\w+\s*=/m, es: 2022 },
]
const SUPPORT = { 2015: 2015, 2017: 2017, 2020: 2020, 2022: 2022 }

export function checkSyntaxCompat(code, targets) {
  const maxTarget = Math.max(...targets.map((t) => SUPPORT[t] ?? 2015))
  const found = []
  for (const f of FEATURES) {
    if (f.re.test(code)) {
      const supported = f.es <= maxTarget
      found.push({ feature: f.name, es: f.es, supportedByTargets: supported })
      if (!supported)
        console.warn(`产物包含 ${f.name}（ES${f.es}）但目标最高 ES${maxTarget} — 转译配置未覆盖`)
    }
  }
  return { ok: found.every((f) => f.supportedByTargets), found,
    maxTarget, note: '正则为近似检测，严格检测用 AST（oxc parse 后按节点类型）' }
}
```
**评分点**：
- 特征检测与目标支持交叉（超纲语法 = 转译缺失的信号）
- 近似检测的诚实标注（正则误报——严格版应 AST 节点级检测）
- 与 browserslist 一致性思路（目标声明 ↔ 产物实际语法双向验证）
- found 结构支持 CI 报告消费
