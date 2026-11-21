---
title: [ZSM-434] 笔试：手写 SSR 安全的 Store 注入（防串数据 + 复水校验）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-434：手写 SSR 安全的 Store 注入
**需求**：实现每请求隔离的 store 工厂 `createSSRStoreBridge()`：1) 服务端：`createReqStore()` 每请求新建 store（禁止模块级单例）；2) `extract(store)` 序列化为内嵌脚本（XSS 安全：`</script` 转义）；3) 客户端：`hydrateFromScript()` 解析注入数据初始化 store，校验 schema 版本；4) 解析失败/版本不符回退默认态并上报；5) 校验「注入不含函数字段」（深度扫描拒绝）；6) 提供 `assertNoSharedStore(fn)` 测试助手（检测模块级单例）。

```javascript
export function createSSRStoreBridge(defaultState, schemaVersion) {
  function createReqStore() {
    return { state: structuredClone(defaultState), version: schemaVersion }   // 每请求独立
  }

  function extract(store) {
    const json = JSON.stringify({ v: schemaVersion, state: store.state })
    return `<script>window.__STATE__=${json.replace(/</g, '\\u003c')}</script>`   // XSS 转义
  }

  function hydrateFromScript(win = window) {
    try {
      const raw = win.__STATE__
      if (!raw) return structuredClone(defaultState)
      if (raw.v !== schemaVersion) { report('hydrate_version'); return structuredClone(defaultState) }
      assertNoFunctions(raw.state)                       // 深度扫描
      return raw.state
    } catch { report('hydrate_fail'); return structuredClone(defaultState) }
  }

  function assertNoFunctions(o, path = '') {
    if (typeof o === 'function') throw new Error(`function in state at ${path}`)
    if (o && typeof o === 'object') for (const [k, v] of Object.entries(o)) assertNoFunctions(v, `${path}.${k}`)
  }

  function assertNoSharedStore(factory, iterations = 3) {
    const stores = Array.from({ length: iterations }, () => factory())
    return stores.every((s, i) => i === 0 || s !== stores[0])   // 每次创建应是不同实例
  }

  return { createReqStore, extract, hydrateFromScript, assertNoSharedStore }
}
```
**评分点**：
- 每请求新实例（串数据根因防御）；defaultState 深拷贝防共享引用污染
- XSS 转义 `</script`（内嵌 JSON 的经典漏洞点）
- 复水失败静默回退默认态 + 版本校验 + 函数字段深度扫描（不可信输入原则）
- assertNoSharedStore 测试助手防止回归
