---
title: [MP-036] 初始渲染缓存 initialRenderingCache 是什么？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-036：初始渲染缓存 initialRenderingCache 是什么？
**答**：
- 页面配置 `"initialRenderingCache": "static"` 后，微信把**初始 data 渲染出的视图**缓存下来，下次冷启动直接展示缓存视图，逻辑层就绪后再用真实数据更新。
- 收益：冷启动白屏明显缩短，用户先看到"静态首屏"。
- 注意：缓存视图**不可交互**（点击事件不生效）、不含 setData 后的内容，适合纯展示骨架；动态数据区域要设计 loading 态。
- 可在页面 json 单页开启，也可 app.json 全局开启。

```json
{
  "initialRenderingCache": "static"
}
```
