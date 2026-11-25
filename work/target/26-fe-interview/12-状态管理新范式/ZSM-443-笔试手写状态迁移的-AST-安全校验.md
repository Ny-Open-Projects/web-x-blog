---
title: [ZSM-443] 笔试：手写迁移函数静态安全校验（禁止危险操作）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-443：手写迁移函数静态安全校验
**答**：实现 `validateMigrateFn(fnSource)`：对用户写的 persist migrate 函数做静态检查（基于正则的简化 lint）：1) 禁止 `Date.now`/`Math.random`（迁移必须确定性）；2) 禁止访问 `localStorage`/`document`/`window`（纯函数）；3) 禁止 `fetch`/`XMLHttpRequest`（无网络）；4) 禁止 `while(true)` 与无终止条件的递归自调用（防死循环）；5) 返回 `{ ok, violations: [{rule, line}] }`；6) 违规即拒绝注册该 migrate（fail-fast）。

```javascript
const RULES = [
  { rule: 'no-nondeterminism', re: /Date\.now|Math\.random|new Date\(\)/, msg: '迁移必须确定性' },
  { rule: 'no-env-access', re: /localStorage|sessionStorage|document|window\./, msg: '迁移必须纯函数' },
  { rule: 'no-network', re: /fetch\(|XMLHttpRequest|axios/, msg: '迁移内禁止网络' },
  { rule: 'no-infinite-loop', re: /while\s*\(\s*true\s*\)|for\s*\(\s*;\s*;\s*\)/, msg: '禁止无界循环' },
]

export function validateMigrateFn(fn) {
  const src = fn.toString()
  const violations = []
  const lines = src.split('\n')
  lines.forEach((line, i) => {
    for (const { rule, re, msg } of RULES) {
      if (re.test(line)) violations.push({ rule, msg, line: i + 1, snippet: line.trim().slice(0, 80) })
    }
  })
  // 递归自调用检查（简化：函数名在体内出现且无条件守卫的行）
  const name = fn.name || 'migrate'
  const selfCall = lines.findIndex((l) => l.includes(`${name}(`))
  if (selfCall >= 0) violations.push({ rule: 'recursive-call', msg: '检查递归终止条件', line: selfCall + 1 })

  return { ok: violations.length === 0, violations }
}

// 注册时门禁
function registerMigrate(fn) {
  const v = validateMigrateFn(fn)
  if (!v.ok) throw new Error(`不安全的 migrate: ${JSON.stringify(v.violations)}`)   // fail-fast
  return fn
}
```
**评分点**：
- 四类危险规则覆盖（不确定性/环境访问/网络/无界循环）——迁移函数的纯度要求
- 行级定位 + 违规片段（可行动的报错）
- fail-fast 注册门禁（违规 migrate 不上线）
- 诚实边界：正则 lint 是简化方案，生产建议 AST 解析（可作加分讨论）
