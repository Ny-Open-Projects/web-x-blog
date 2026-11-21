---
title: [FRP-263] computed 语义差异：Vue/Solid/MobX/React？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-263：computed 语义差异？
**答**：
- Vue computed：缓存 + 脏检查（3.5 版本计数），在 render/effect 中读取才有意义（孤立使用仅是函数）。
- Solid createMemo：eager 订阅图节点，上游变化即标记，读取时返回缓存——图计算语义更纯粹。
- MobX computed：惰性 + 事务批量，observe 可主动订阅。
- React：useMemo 非响应式（依赖数组人工、渲染期执行）——真正「派生」要靠 useEffect+state 或第三方 memo 库。
- 差异本质：响应式内核内建（前三者）vs 派生需外部机制（React）。
