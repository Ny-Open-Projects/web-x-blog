---
title: [MFW-560] RSC Payload 体积优化：Flight 流的压缩策略
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-560：RSC Payload 体积优化

**答**:
- Flight payload 的体积构成：HTML 转义的重复（`<!--$-->` 标记/引号转义）+ props 的全量传输（每次导航传整棵树的变更段）+ 未裁剪的数据（组件取了整行返回但 UI 只用 3 字段——「查询即视图」的裁剪缺失）。
- 优化手段：1) **数据裁剪**（查询投影：SELECT 只取 UI 用字段——「组件定义查询」RBL-554 repo 的投影参数化）；2) **传输压缩**（br/gzip——Flight 是文本：压缩率高；HTTP/2 流式压缩：动态表大小——payload 与 HTML 双流同源压缩优化）；3) **重复引用共享**（同对象多次出现 → $引用去重（协议内建 RBL-501）——「props 树的去重」序列化器内建）；4) **段级 diff**（RBL-525 软导航只传变更段）。
- 体积度量：payload 体积的预算（RBL-934 预算分配的 payload 维度）——「payload > HTML」的页面画像（RSC 树数据重于展示——反模式信号）。
- 追问钩子：为什么「组件取整行数据」在 RSC 下是新反模式？——传统 API 场景「多余字段只占 API 响应」（前端不用不传给 UI）；RSC 场景「多余字段直接进 Flight payload 传给 client」（序列化整棵 props 树——多余字段 = 传输成本）；「查询即视图」原则（投影到 UI 所需）：数据层与 UI 层的距离越近，「取多了」的成本越直接可见——RSC 把数据浪费从「隐性」（API 层）变「显性」（payload 体积可测量）。

```typescript
// 数据裁剪：repo 投影参数化（RBL-554）
export const getProductCard = cache((id: string) =>
  db.product.findUnique({
    where: { id },
    select: { name: true, thumb: true, price: true },   // 只取 UI 用字段
  }));
// 反模式：整行返回
// db.product.findUnique({ where: { id } })               // description 长文也进 payload！
// payload 体积度量（RBL-940 物料）
function payloadBudget(route: string, bytes: number, limit = 60 * 1024) {
  if (bytes > limit)
    warn(`RSC payload ${kb(bytes)} 超预算 ${kb(limit)}——检查整行返回/未裁剪 props`);
}
// 重复引用去重（协议内建）：同 product 对象传给 3 个组件 → 1 份数据 + $ 引用 ×3
```
