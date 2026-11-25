---
title: [MP-225] setData 大对象/深层路径的优化实战套路？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-225：setData 大对象优化实战？
**答**：
- 路径更新：`this.setData({ 'list[3].status': 'done' })` 代替整条 list——数据量从 O(list) 到 O(1)。
- 大对象拆分：图片列表等静态大数据放渲染层外（自定义组件 properties 分片、或 WXS 内处理），逻辑层只传 key。
- 列表首帧：骨架 + 分批 setData（首屏 10 条，滚动加载后续）。
- 反模式：setData 传函数/undefined（报错）、传超过 1MB 数据（丢失）、高频 setData 不合并。
- WXS/worker：纯展示计算（过滤排序大数组）放 WXS（渲染层执行），避免跨线程往返。
