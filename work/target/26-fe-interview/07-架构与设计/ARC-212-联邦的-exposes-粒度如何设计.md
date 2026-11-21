---
title: [ARC-212] 联邦的 exposes 粒度如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-212：联邦的 exposes 粒度如何设计？
**答**：
- 粒度三层：组件级（Button/Card）、页面级（整页路由块）、领域级（领域服务+组件集合）。粒度越细，共享越灵活，但契约面越大、版本碎片化越严重。
- 建议默认：页面级为主 + 少量稳定组件级；"领域级"只给跨多个主应用复用的核心域（如用户中心）。不 expose 内部实现细节，只 expose 领域接口。
- 命名即契约：`shop@1.4/CartPage` 这类 ID 要稳定（不随重构改），所以 expose 路径必须进 CODEOWNERS 管控，重命名视为破坏性变更走大版本。
- 反模式：把 utils/公共函数也 expose 出去共享——这是用联邦做代码共享的滥用（应走 npm 包）；expose 只承载"运行时才决定用谁"的模块。

```javascript
// exposes 设计示例（shop 应用）
exposes: {
  './CartPage': './src/pages/Cart/index.tsx',        // 页面级：主应用路由挂载
  './OrderTrack': './src/pages/Order/Track.tsx',     // 页面级
  './UserBadge': './src/components/UserBadge.tsx',   // 组件级：仅跨多主应用复用的稳定组件
  // 反例（不要）：'./utils/date' —— 工具函数走 npm 包 @shop/utils，让构建器 tree-shaking
},
// 稳定性分层：expose 路径分 stable/（仅允许追加参数，不改签名）与 experimental/（随时可变），主应用引用 experimental 自担风险
```
