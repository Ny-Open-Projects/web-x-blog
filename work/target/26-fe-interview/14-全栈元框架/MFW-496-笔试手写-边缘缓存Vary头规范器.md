---
title: [MFW-496] 笔试：手写边缘缓存 Vary 头规范器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-496：边缘缓存 Vary 头规范器
**需求**：实现 `canonicalVary(headers, { allow })`：1) 收集响应所有 Vary 值（可能多行多值），拆分/去重/排序成规范形式（CDN 对 Vary 的匹配是字符串敏感的——`Vary: A, B` 与两行分别 A、B 语义相同但要规范化避免重复缓存条目）；2) 白名单过滤：不在 allow（如 ['Accept-Encoding','X-Experiment']）中的 vary 维度剔除并告警（Cookie 在 Vary 里等于放弃缓存——必须显式决策）；3) `*` 值直接判 no-cache（Vary: * 等于不可缓存）；4) 输出 { vary, removed, warnings }。

```javascript
export function canonicalVary(headers, { allow = ['Accept-Encoding', 'X-Experiment'] } = {}) {
  const raw = headers.getSetCookie ? undefined : undefined
  const values = headers.get('vary')?.split(',') ?? []
  const cleaned = [], removed = [], warnings = []
  for (const v of values) {
    const name = v.trim()
    if (!name) continue
    if (name === '*') {
      warnings.push('Vary: * means uncacheable; stripped and page marked no-cache')
      return { vary: null, noCache: true, removed, warnings }
    }
    if (!allow.includes(name)) {
      removed.push(name)
      warnings.push(name === 'Cookie'
        ? 'Cookie in Vary = per-user cache explosion; use private/no-store instead'
        : `${name} not in allowlist`)
      continue
    }
    cleaned.push(name)
  }
  return { vary: cleaned.length ? [...new Set(cleaned)].sort().join(', ') : null, removed, warnings }
}
```

**评分点**：
- 多行多值合并去重排序（规范化防 CDN 产生重复缓存条目）
- Cookie 进 Vary 特判告警（等于放弃缓存，必须引到 no-store）
- `*` 判 no-cache（Vary: * 是不可缓存信号，不能当普通维度处理）
- removed/warnings 输出（缓存策略收紧要有可解释的审计）
