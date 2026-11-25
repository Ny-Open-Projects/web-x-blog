---
title: [ZSM-456] 笔试：手写状态库 API 兼容层（新旧 API 并存 + deprecation）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-456：手写状态库 API 兼容层
**答**：实现 `withCompat(store, legacyMap)`：1) legacyMap 声明旧 API → 新实现映射：`{ addItem: { to: (store, ...args) => {...}, deprecatedIn: 'v2' } }`；2) 调用旧 API：转译执行 + 首次调用打 deprecation 警告（每调用点只警告一次，带堆栈定位）；3) `usage()` 返回旧 API 调用统计（迁移验收数据：哪个旧 API 还在被用）；4) `removeIn` 到期的旧 API 直接抛错（带迁移指引文案）；5) 新 API 直通不包装。

```javascript
export function withCompat(store, legacyMap, { removeIn } = {}) {
  const usage = new Map()
  const warnedAt = new Set()

  const proxy = new Proxy(store, {
    get(target, prop) {
      const legacy = legacyMap[prop]
      if (!legacy) return target[prop]                        // 新 API 直通
      return (...args) => {
        usage.set(prop, (usage.get(prop) ?? 0) + 1)
        const loc = callerLoc()
        if (!warnedAt.has(loc)) {
          warnedAt.add(loc)                                   // 每调用点一次
          console.warn(`[deprecated] ${prop} 在 ${legacy.deprecatedIn} 弃用，请迁移至新 API。来源: ${loc}`)
        }
        if (removeIn && legacy.deprecatedIn <= removeIn)      // 到期移除
          throw new Error(`${prop} 已在 v${removeIn} 移除。迁移：${legacy.migrateHint}`)
        return legacy.to(target, ...args)                     // 转译执行
      }
    },
  })

  return { api: proxy, usage: () => Object.fromEntries(usage) }
}

function callerLoc() {
  return new Error().stack?.split('\n')[3]?.trim().slice(0, 80) ?? 'unknown'
}
// 用法：usage() 驱动迁移验收——为 0 的旧 API 即可从 legacyMap 删除
```
**评分点**：
- 转译而非双实现（旧 API 是薄适配，逻辑只有一份）
- deprecation 警告按「调用点」去重（不刷屏，但每个使用处都能被发现）
- usage 统计驱动迁移验收（数据闭环：统计→清零→删 API）
- removeIn 到期抛错带迁移指引（硬门禁 + 可行动报错）
