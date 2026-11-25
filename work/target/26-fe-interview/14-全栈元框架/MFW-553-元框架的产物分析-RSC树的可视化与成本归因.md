---
title: [MFW-553] 元框架产物分析：RSC 树的可视化与成本归因
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-553：RSC 树可视化与成本归因

**答**:
- RSC 页面的成本维度（比 SPA 多一层）：1) **server 成本**（每请求渲染 CPU/数据查询——RBL-904 SLO）；2) **payload 体积**（Flight 传输字节——RSC 树的序列化成本）；3) **client JS**（client 组件 chunk）；4) **缓存命中**（全静态则 server 成本近零——静态/动态比例是成本的核心变量）。
- RSC 树可视化：组件树标注每节点的「渲染环境（server/client）× 成本（payload 字节/查询耗时/缓存状态）」——tree map（RBL-844 数据规范）；「静态/动态比例」是页面成本的一页总结。
- 成本归因的用途：动态洞的粒度（一个动态组件让整路由动态 = 成本失控——RBL-510；PPR 后是洞级）；「谁让路由动态了」的归因（动态 API 调用链追踪 RBL-510 排查）。
- 追问钩子：为什么「RSC 页面的成本单元」从「bundle 大小」变成「渲染请求」？——SPA 成本 = 一次性 JS 传输 + client 计算；RSC 成本 = 每请求的 server 计算 + payload——成本从「资产」变「流量」（静态化让流量近零、动态化让流量持续）——成本模型的转变要求「静态/动态配比」成为架构决策（PPR/ISR 的设计意义）：每请求成本的架构 = 缓存策略的架构。

```javascript
// RSC 树的成本标注（构建期分析）
interface NodeCost {
  env: 'server' | 'client';
  payloadBytes: number;                                  // Flight 序列化成本
  queryMs?: number;                                      // server 查询成本
  cached: 'static' | 'isr' | 'dynamic';
  children: NodeCost[];
}
// 静态/动态比例 = 页面成本画像
function pageProfile(root) {
  const flat = flatten(root);
  const dyn = flat.filter(n => n.cached === 'dynamic');
  return {
    dynamicRatio: dyn.length / flat.length,
    payloadKB: sum(flat, 'payloadBytes') / 1024,
    worstQuery: max(flat, 'queryMs'),                    // 最慢查询——优化靶点
    fullDynamic: dyn.some(n => n.env === 'server' && n.cached === 'dynamic'),
  };
}
// 输出：{"dynamicRatio":0.15,"payloadKB":42,"worstQuery":800,"fullDynamic":true}
// → 全动态 + 800ms 查询 = 服务端成本热点
```
