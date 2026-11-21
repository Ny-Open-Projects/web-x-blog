---
title: [V3-422] 笔试：手写 Pinia 持久化插件（白名单 + 防抖 + 版本迁移）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-422：笔试：手写 Pinia 持久化插件（白名单 + 防抖 + 版本迁移）
**题**：实现 Pinia 插件：仅持久化 store.$id 在白名单中的 store；按 store 配置的 paths 白名单挑字段存储（防大对象/敏感字段）；写入防抖 300ms；存储带版本号，版本不匹配丢弃旧数据。

```javascript
const debounceMap = new Map()
export function piniaPersist({ version = 1 } = {}) {
  return ({ store, options }) => {
    const conf = options.persist
    if (!conf?.enable) return
    const key = `pinia:${store.$id}:v${version}`
    // 恢复
    try {
      const raw = localStorage.getItem(key)
      if (raw) {
        const saved = JSON.parse(raw)
        if (saved.v === version) store.$patch(pick(saved.data, conf.paths || []))
      }
    } catch { localStorage.removeItem(key) }
    // 写入
    let timer = debounceMap.get(store.$id)
    store.$subscribe(() => {
      clearTimeout(timer)
      timer = setTimeout(() => {
        const data = conf.paths ? pick(store.$state, conf.paths) : store.$state
        try { localStorage.setItem(key, JSON.stringify({ v: version, data })) } catch {}
      }, 300)
    }, { detached: true })
    debounceMap.set(store.$id, timer)
  }
}
function pick(obj, paths) {
  return paths.reduce((o, p) => { o[p] = obj[p]; return o }, {})
}
```
**评分点**：
- paths 白名单挑字段（防敏感数据/体积）。
- 防抖写入 + detached 订阅。
- 版本号不匹配丢弃（schema 变更安全）。
- 恢复用 $patch 而非整体替换（保留未持久化字段默认值）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-1b24dc37-88d7-4f9e-827b-5f3c11f2fde6-cwd'; fi
exit "$__zcode_status"
