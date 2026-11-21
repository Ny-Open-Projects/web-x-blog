---
title: [MP-033] 分包预下载 preloadRule 怎么配置？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-033：分包预下载 preloadRule 怎么配置？
**答**：
- 进入指定页面时，微信在后台**静默预下载**目标分包，跳转时零等待。
- 配置 `preloadRule`：key 为页面路径，`packages` 填分包 root 或 name，`network` 取 `all/wifi`。
- 限制：**同一个页面享有的预下载大小限额 2M**；预下载不影响主包加载优先级。
- 决策：把"当前页最可能跳转的下一站"配成预下载，如首页预下载核心业务分包。

```json
{
  "preloadRule": {
    "pages/index/index": { "network": "all",  "packages": ["packageA"] },
    "pages/mine/mine":   { "network": "wifi", "packages": ["shop"] }
  }
}
```

```mermaid
flowchart TB
  A[开始分包规划] --> B{业务是否极轻且营销直达}
  B -- 是 --> C[配置独立分包 不下载主包]
  B -- 否 --> D[普通分包]
  C --> E{是否使用插件或依赖主包}
  E -- 是 --> F[改回普通分包]
  E -- 否 --> G[保留独立分包]
  D --> H[主包只留 tab 页与公共资源]
  H --> I{跳转频率高的下游分包}
  I -- 是 --> J[配置 preloadRule 预下载]
  I -- 否 --> K[按需加载]
  J --> L{跨分包引用组件或 js}
  L -- 是 --> M[分包异步化 componentPlaceholder 与 require.async]
  L -- 否 --> N[完成]
  M --> N
```
