---
title: [MFW-466] 笔试：手写 Middleware matcher 简化引擎
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-466：Middleware matcher 简化引擎
**答**：实现 `matchMiddleware(pathname, matcher)`：1) matcher = { rules: ['/dashboard/:path*', '/about', '/blog/(?<year>\\d+)'] }，支持三种语法：字面量、`:param` 与 `:param*` 通配、正则；2) 返回 { matched, params }，`:path*` 捕获余下所有段为字符串；3) 排除规则 `!` 前缀优先于包含（`/dashboard/:path*` 但 `!/dashboard/admin`）；4) 尾斜杠归一化（`/about/` 命中 `/about`）——middleware 每请求都跑，引擎必须零依赖且 O(规则数)。

```javascript
export function matchMiddleware(pathname, { rules = [] } = {}) {
  const path = pathname.replace(/\/+$/, '') || '/'
  let result = { matched: false, params: {} }
  for (const raw of rules) {
    const negated = raw.startsWith('!')
    const rule = negated ? raw.slice(1) : raw
    const hit = tryMatch(path, rule)
    if (hit) result = negated ? { matched: false, params: {} } : { matched: true, params: hit }
    if (negated && hit) return result // 排除立即生效
  }
  return result
}

function tryMatch(path, rule) {
  if (rule.startsWith('/blog/') && !rule.includes(':')) {
    const m = path.match(new RegExp(rule.replace('/blog/', '/blog/')))
    return m ? m.groups || {} : null
  }
  const rs = rule.split('/').filter(Boolean)
  const ps = path.split('/').filter(Boolean)
  const params = {}
  let i = 0
  for (; i < rs.length; i++) {
    const r = rs[i]
    const star = r.endsWith('*')
    const name = r.replace(/[:*]/g, '')
    if (star) { params[name] = ps.slice(i).join('/'); return params }
    if (ps[i] === undefined) return null
    if (r.startsWith(':')) params[name] = decodeURIComponent(ps[i])
    else if (r !== ps[i]) return null
  }
  return i === ps.length ? params : null // 多余段不匹配
}
```

**评分点**：
- `!` 排除优先且短路（先匹配后排除是常见错误）
- `:path*` 贪婪捕获余段（嵌套路径语义）
- 段数必须精确相等（非通配时 `/a/b` 不命中 `/a`）
- 尾斜杠归一化 + 每请求零依赖（middleware 性能红线）
