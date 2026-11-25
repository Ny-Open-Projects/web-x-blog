---
title: [MP-291] 笔试：手写多端适配层（Taro 条件编译收敛）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-291：笔试：手写多端适配层
**答**：实现 platform.ts 适配层：统一 storage/request/share 三组 API——内部按 process.env.TARO_ENV 分支（weapp/h5/rn），对外零平台差异签名；TS 类型按环境收窄；禁止业务层直接调 wx.*（ESLint 约束）。

```javascript
// adapter/storage.ts
export const storage = {
  get<T>(key: string): T | null {
    if (process.env.TARO_ENV === 'weapp') {
      const v = Taro.getStorageSync(key)
      return v === '' ? null : v
    }
    if (process.env.TARO_ENV === 'h5') {
      const raw = localStorage.getItem(key)
      return raw ? JSON.parse(raw) : null
    }
    return null // rn: AsyncStorage 异步版需另一接口，此处示意
  },
  set(key, value) {
    if (process.env.TARO_ENV === 'weapp') Taro.setStorageSync(key, value)
    else if (process.env.TARO_ENV === 'h5') localStorage.setItem(key, JSON.stringify(value))
  }
}
// adapter/share.ts
export async function share(title, path) {
  if (process.env.TARO_ENV === 'weapp') return Taro.showShareMenu({})
  if (process.env.TARO_ENV === 'h5') return copyLink(buildShareUrl(path)) // H5 复制链接降级
}
```
**评分点**：
- 差异收敛在适配层（业务零分支——核心理念）。
- weapp getStorageSync 空串语义处理。
- H5 降级方案（分享→复制链接）。
- ESLint no-restricted-globals 禁 wx 的治理手段。
