---
title: [MP-256] Pinia（Taro）与全局状态的持久化怎么做？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-256：Pinia 状态持久化？
**答**：
- 持久化插件：store.$subscribe 防抖写 storage（选白名单字段：user/config/cart），启动时 $patch 恢复。
- 容量：storage 上限 10MB/单 key 1MB——只存关键状态；图片/大列表不持久化。
- 时序：App onLaunch 恢复（异步）——首屏渲染可能拿不到持久化值，关键路径用同步 getStorage 先恢复核心字段。
- 版本迁移：持久化数据带 version，不匹配丢弃重置（schema 变更安全）。
- 敏感数据：token 加密或不持久化（静默重登），手机号等明文敏感信息禁止落 storage。
