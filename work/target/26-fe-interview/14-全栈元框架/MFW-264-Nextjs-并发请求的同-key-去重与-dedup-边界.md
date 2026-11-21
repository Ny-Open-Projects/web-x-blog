---
title: [MFW-264] fetch 去重的边界（什么时候不 dedup）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW-264：fetch 去重边界

**答**:
- 去重条件：同渲染 pass + 同 URL + 同选项（headers/body 一致）——React 缓存按参数全等
- 不去重的场景：不同 options（加了一个无关 header 就 miss——去重键过严的体感bug）、POST（变更语义不去重——正确）、手动 force-refresh、跨请求（新导航新 pass）
- 隐患：依赖隐式去重的代码在「选项微变」后请求翻倍——显式去重要求（同 key 工厂函数集中管理 fetch 调用——MFW-262 的 queryOptions 模式）
- 与 DB 层去重的分层：fetch 去重只管 HTTP——DB 查询去重要应用层（cache() 或请求级 Map MFW-219）

```javascript
// 显式化：集中工厂保证同 key 同选项
const api = {
  product: (id) => fetch(`/api/p/${id}`, { next: { tags: [`p:${id}`] }, ...FIXED })  // FIXED 冻结选项
}
// 页面与 metadata 都调 api.product(id) → 保证命中去重
```
