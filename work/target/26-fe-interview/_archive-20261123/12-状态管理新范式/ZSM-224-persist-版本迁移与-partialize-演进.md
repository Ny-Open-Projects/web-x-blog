---
title: [ZSM-224] persist 的 version migrate 机制在源码里怎么执行
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-224：persist 的 version migrate 机制在源码里怎么执行

**答**：
- 写入时把 `version` 一起序列化：`{ state: partialize(s), version: n }`；读取时对比存储 version 与代码 options.version
- 版本不一致时调用 `migrate(persisted, fromVersion)`，返回迁移后的 state 再合并；未提供 migrate 则丢弃持久化数据并告警（防旧结构污染）
- migrate 返回 undefined/抛错按失败处理，走 onRehydrateStorage 的 error 分支，store 保持初始值
- 多版本连续升级建议迁移链（逐版本 migrate），并对无法识别的旧版本做「重置 + 上报」而不是猜测合并

```javascript
persist((set) => ({...}), {
  name: 'cart', version: 3,
  migrate: (persisted, from) => {
    let s = persisted
    if (from < 2) s = { ...s, items: s.products }        // v1→v2 字段重命名
    if (from < 3) s = { ...s, coupon: null, currency: 'CNY' }  // v2→v3 新增字段
    return s
  },
})
```
