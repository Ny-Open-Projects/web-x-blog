---
title: [ZSM-023] 笔试：手写 Zustand 持久化中间件（persist + partialize + 版本迁移）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-023：手写 Zustand 持久化中间件（persist + partialize + 版本迁移）

**题目要求**：
- 实现中间件 `persist(config, { name, partialize, version, migrate })`，包装 creator：创建时从 localStorage 读回并合并（migrate 兼容旧版本），每次 set 后把 partialize 结果写入。
- JSON 解析失败、版本不匹配需兜底（migrate 或丢弃）。
- 不把函数字段写进 storage。

**边界说明**：localStorage 同步即可；无需处理跨标签页同步。

```javascript
export function persist(config, opts) {
  return (set, get, api) => {
    // 1. 读回旧数据（含版本迁移）
    let restored = {}
    try {
      const raw = localStorage.getItem(opts.name)
      if (raw) {
        const parsed = JSON.parse(raw)
        const oldVer = parsed.version ?? 0
        let data = parsed.state
        if (oldVer !== opts.version && opts.migrate) {
          data = opts.migrate(data, oldVer)
        } else if (oldVer !== opts.version) {
          data = {} // 无 migrate 且版本不符：丢弃
        }
        restored = data ?? {}
      }
    } catch { restored = {} } // JSON 损坏兜底

    // 2. 初始 state = 默认值 + 恢复值（恢复值优先）
    api.setState(restored, false)

    // 3. 包装 set：更新后落盘
    const wrappedSet = (partial, replace) => {
      set(partial, replace)
      const s = get()
      const data = opts.partialize ? opts.partialize(s) : s
      const safe = {}
      for (const k in data) if (typeof data[k] !== 'function') safe[k] = data[k]
      try { localStorage.setItem(opts.name, JSON.stringify({ version: opts.version, state: safe })) } catch {}
    }
    return config(wrappedSet, get, api)
  }
}
```

**评分点**：
- 读回在 creator 执行前完成，恢复值与初始 state 合并时恢复值优先。
- set 包装后先更新再落盘，partialize 挑字段且过滤函数。
- version 不一致走 migrate，无 migrate 丢弃；try/catch 兜底 JSON 异常。
- 恢复时不覆盖新增字段的默认值（restored 是部分合并）。
