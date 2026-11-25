---
title: [NODE-712] BFF 层的端裁剪与多端适配怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-712：多端适配怎么做？
**答**：
- 端抽象：端 profile（pc/app-ios/app-android/mini——各端的字段集/裁剪规则/行为差异）声明化——BFF 按端 profile 渲染响应（SCN-联想-578 多端一致性的服务端侧）。
- 裁剪实现：schema 级裁剪（字段白名单 per 端——SCN-NODE-644 字段裁剪的系统化）；版本差异（App 老版本的字段兼容——端版本维度）。
- 一致性约束：多端同一业务语义统一（价格/状态码——端差异只在呈现字段，不在语义——语义双端漂移是事故源）。
- 端探测：UA/客户端头（x-client-ver）——端 profile 路由。
- 追问钩子：为什么「语义统一、呈现分端」是 BFF 多端适配的纪律——端差异如果包括语义（iOS 优惠券含义与 Android 不同），业务逻辑双写（两端口径不一——运营口径混乱）；BFF 只裁剪字段与形态（移动端省字段），业务语义单源（服务端权威）——语义单源是 BFF 的存在理由，端差异止步于呈现层。

```javascript
const profiles = {
  'app-ios:3.2': { fields: ['id', 'title', 'price', 'cover'], drop: ['desc'] },   // 端 profile
  'pc': { fields: '*' },
};
app.get('/goods', (req) => {
  const profile = detectProfile(req);                  // UA + x-client-ver
  return trim(goodsData, profiles[profile]);           // schema 级裁剪
});
```
