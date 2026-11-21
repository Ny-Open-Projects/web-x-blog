---
title: [DP-254] 源码识别：Pinia 持久化插件源码中的观察者与序列化？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-254：源码识别：Pinia 持久化插件源码中的观察者与序列化？
**答**:
- 观察者：插件订阅 store.$subscribe（每次 mutation 通知）→ 防抖序列化到 Storage——"订阅即持久化"。
- 策略：序列化策略（JSON/加密/压缩）、存储策略（localStorage/sessionStorage/IndexedDB）、路径策略（persist: ['user.token'] 只存部分字段）都可配置。
- 水合（恢复）：初始化时从 Storage 读出 merge 进 state——版本号/schema 校验防脏数据。
- 识别要点：能说清"订阅回调解构（mutation 事件、afterHydration 标志防首次覆盖）"与存储配额失败的降级。

```javascript
// pinia-plugin-persistedstate 源码级简化
function persistPlugin({ store, options }) {
  const { key = store.$id, storage = localStorage, pick, serializer = JSON, ttl } = options.persist ?? {};
  // 1) 水合：恢复
  const raw = storage.getItem(key);
  if (raw) {
    const saved = serializer.parse(raw);
    if (ttl && Date.now() - saved.ts > ttl) storage.removeItem(key);   // 过期丢弃
    else store.$patch(pick ? pickFrom(saved.state, pick) : saved.state);
  }
  // 2) 订阅：写
  store.$subscribe((mutation, state) => {
    const data = pick ? pickFrom(state, pick) : state;                 // 路径策略
    try { storage.setItem(key, serializer.stringify({ ts: Date.now(), state: data })); }
    catch (e) { quotaFallback(e); }                                    // 配额降级：转 sessionStorage 或丢弃
  }, { detached: true });
}
// 主应用：pinia.use(persistPlugin) —— ARC-327 ConfigProvider 风格的全局扩展
```
