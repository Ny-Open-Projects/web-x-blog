---
title: [MFW-550] 元框架的 BFF 裁剪：后端聚合路由与协议适配
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-550：元框架的 BFF 裁剪：聚合路由与协议适配

**答**:
- 元框架作为 BFF 的三职责：1) **聚合**（page 数据来自 N 个后端服务——RSC 组件级并行 fetch 组合（RBL-930 trace））；2) **协议适配**（老后端 SOAP/XML → 前端友好 JSON——route handler 的转换层）；3) **安全边界**（密钥留在 server（第三方向 key）、限流、鉴权（RBL-803））。
- 聚合的形态选择：RSC 组件自取（分散式——每个组件自己 fetch 自己的数据：耦合低、瀑布风险）vs route handler 聚合（集中式——单端点返回组合数据：页面级编排）。RSC 时代倾向「组件自取 + cache() 去重」（数据与 UI 同源——组件自治 RBL-547）；「编排逻辑的归属」：跨组件数据依赖 → route handler/单一数据函数。
- BFF 的版本管理：后端 API 变化 → BFF 适配层隔离（前端类型只看 BFF 契约 RBL-946——BFF 是防腐层 antifray layer）。
- 追问钩子：为什么「RSC 组件自取」没有让 BFF 模式失效反而更精细？——传统 BFF = 集中式聚合端点（page 一次 fetch 组合数据）；RSC = 聚合逻辑分散到组件（每个组件的 fetch 就是「微 BFF」）——聚合没有消失而是「下沉到组件粒度」；全局编排（跨组件依赖）仍需集中（cache() 共享/RSC 顶层取）；BFF 的进化是「从端点聚合到组件聚合」——UI 与数据的耦合粒度更细（组件自治 RBL-547）。

```javascript
// BFF 的三职责示例
// 1) 聚合（组件自取 + cache 去重）
const getProduct = cache(async (id) => {
  const [base, price, stock] = await Promise.all([       // 并行聚合三服务
    catalogService.get(id), pricingService.get(id), inventoryService.get(id),
  ]);
  return { ...base, ...price, ...stock };                // 组合
});
// 2) 协议适配（防腐层）
export async function GET(req) {
  const legacy = await legacySoap.call('getOrder', id);  // 老 SOAP
  return NextResponse.json(mapToModern(legacy));         // 转现代契约——前端只见新契约
}
// 3) 安全边界（key 不出 server）
export async function GET() {
  const res = await fetch(`https://3rd-party.com/api?key=${process.env.THIRD_KEY}`);
  return NextResponse.json(stripSecrets(await res.json()));   // 密钥不过边界 RBL-803
}
```
