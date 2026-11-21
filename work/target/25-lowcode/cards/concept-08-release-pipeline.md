---
title: 发布链路：草稿、预览、发布三态
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 概念, 发布, 草稿, 预览]
---

## 发布链路：草稿、预览、发布三态

低代码平台的标准三态：**草稿 → 预览 → 发布**。发布 = 把编辑态 Schema 固化为对外可见版本。

**本项目实例**：
- **草稿**：存三份 store 状态（componentConfigs/sortableComponentConfig/currentComponentConfig），MobX 数据先 `toJS` 再 `JSON.stringify` 写 localStorage，并记 `storeTime` 时间戳。
- **预览**：点击先写草稿再跳 `/preview`，预览页恢复数据并复用编辑页渲染链路。
- **发布**：把 store 数据转后端入参调事务化 upsert 接口，成功记 `releaseTime` 并自动存一次草稿。
- **取舍逻辑**：`storeTime` vs `releaseTime` 比大小——本地草稿更新读本地，否则走服务端发布数据。这是"存草稿不发请求"体验的关键。
- **对第三方可见**：发布页 Next.js SSR 按 pageId 免登录渲染；重新发布不保留编辑历史；问卷数据行按最终仓库口径保留（课程原始实现会清空），但组件 id 每次发布重生成，历史答案只剩孤儿行。

商用级缺口：发布历史与一键回滚、灰度发布（按比例/人群生效）——课程版均未实现，属可讲清的改进方向。

出处「课程25 · 4-1、19-2~19-5；scan4 §7」
