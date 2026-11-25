---
title: [MP-229] 小程序 Worker 与 WXS 的分工边界？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-229：Worker 与 WXS 的分工？
**答**：
- WXS：渲染层执行的小函数——纯展示变换（格式化/过滤/动画联动），与 setData 同层无通信成本；不能调 wx API。
- Worker：独立线程跑 JS——重计算（加密/大数据解析）不阻塞逻辑层；与主线程通信是消息传递（异步、需序列化）。
- 分工原则：渲染相关的实时计算 → WXS；耗时的非 UI 计算 → Worker；常规业务 → 逻辑层。
- Worker 限制：单小程序最多 5 个、同 worker 串行、不能操作 DOM/网络受限（wx.request 不全支持）。
- 典型案例：IM 消息解析解密用 Worker，列表时间格式化用 WXS。
