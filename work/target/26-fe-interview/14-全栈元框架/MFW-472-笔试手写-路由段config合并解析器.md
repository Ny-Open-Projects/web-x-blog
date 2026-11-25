---
title: [MFW-472] 笔试：手写路由段 config 合并解析器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-472：路由段 config 合并解析器
**答**：实现 `resolveSegmentConfig(segments)`：1) segments 为嵌套路径各层的 `export const` 集：{ dynamic: 'force-static'|'force-dynamic'|'auto', revalidate, runtime, fetchCache }；2) 继承规则：子段未设置继承父段；`force-dynamic` 不可被子孙翻回 static（向下锁定）；`revalidate` 取祖先链最小值（最保守）；3) 冲突检测：父 force-static 而子段出现 `cookies()/headers()` 动态 API 调用标记 `usesDynamic: true` → 整链升级为 dynamic 并出 warning；4) 输出最终 { dynamic, revalidate, runtime, warnings }。

```javascript
export function resolveSegmentConfig(segments) {
  let dynamic = 'auto', revalidate = Infinity, warnings = []
  let runtime
  for (const seg of segments) {
    if (seg.dynamic) {
      if (dynamic === 'force-dynamic' && seg.dynamic === 'force-static') {
        warnings.push(`dynamic locked: cannot revert to static`) // 锁定
        continue
      }
      dynamic = seg.dynamic
    }
    if (seg.revalidate !== undefined)
      revalidate = Math.min(revalidate, seg.revalidate) // 最保守
    if (seg.runtime) runtime = seg.runtime
    if (dynamic === 'force-static' && seg.usesDynamic) {
      dynamic = 'force-dynamic' // 冲突升级
      warnings.push(`static segment uses dynamic API, upgraded`)
    }
  }
  return { dynamic, revalidate: revalidate === Infinity ? false : revalidate, runtime: runtime ?? 'nodejs', warnings }
}
```

**评分点**：
- 子段继承父段、显式设置覆盖
- force-dynamic 向下锁定（动态不可翻回静态——渲染语义单向门）
- revalidate 取最小值（多段并存取最保守，否则短缓存泄漏长缓存页）
- 动态 API 标记触发整链升级 + warning（矛盾配置要显式裁决）
