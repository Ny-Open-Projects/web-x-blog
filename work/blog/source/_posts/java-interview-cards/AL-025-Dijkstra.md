---
title: "[AL-025] 图·Dijkstra（最短路）"
date: 2026-11-18
categories: [Java面试, 算法]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 图 · Dijkstra（最短路）

- **事实**：Dijkstra：单源最短路（非负权），优先队列 O((V+E)logV)
- **原理**：贪心每次取最近未定节点，负权失效（Bellman-Ford 处理），网络路由/地图导航基础，与负载均衡（响应时间加权）概念关联
- **常见误区**：
  1. Dijkstra 支持负权（错）
  2. Dijkstra 是 BFS 加权版（错）
  3. 复杂度 O(V²) 是最优（错）
- **工程用法**：图算法进阶
- **版本锚点**：理论共识
