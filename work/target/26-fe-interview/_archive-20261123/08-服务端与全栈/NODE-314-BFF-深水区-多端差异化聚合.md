---
title: [NODE-314] BFF 深水区：多端差异化聚合？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-314：BFF 深水区：多端差异化聚合？
**答**:
- 同一业务多端（App/H5/小程序）对同一接口的字段需求不同——BFF 按 client-profile 裁剪（头 X-Client: app-ios-1.2）。
- 实现：字段集声明（profile → fields 白名单）+ 聚合器按白名单过滤下游响应；GraphQL 场景天然支持（字段级）。
- 版本治理：旧版本 App 的字段冻结期（不能随意删字段）——字段下线走 deprecation + 版本清扫。
- 性能收益：移动端 payload 减 30%~50%（弱网体验）。

```javascript
// profile 裁剪器
const PROFILES = {
  'app-ios': { fields: ['id', 'title', 'price', 'cover'], drop: ['descLong'] },
  'h5': { fields: ['id', 'title', 'price', 'cover', 'descLong'] },
};
function trim(profile, data) {
  const p = PROFILES[profile] ?? PROFILES.h5;
  return p.drop.reduce((o, k) => { delete o[k]; return o; }, pick(data, p.fields));
}
// 下线流程：字段标 deprecated → 监控该字段在各 profile 的访问量 → 0 访问 90 天 → 删除
```
