---
title: [R19-219] Action 返回大对象（列表页 5000 条）怎么拆分？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-219：Action 返回大对象怎么拆分？
**答**：
- 分页优先：action 只返回当前页 + 总数/游标，滚动加载增量拉取——大 payload 的根本解法。
- 裁剪字段：列表页只返回展示列（id/title/cover），详情字段进详情接口；DTO 化而非裸传 ORM 实体。
- Server Action 的返回会走 Flight 序列化 + 内联到 RSC payload，大对象会拖慢 action 响应与页面交互。
- 客户端大数据渲染交给虚拟列表，服务端只保证「单屏数据」。
- 对比 REST：Action 不适合做「导出全量」类接口，导出走专门端点（流式 CSV）。
