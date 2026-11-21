---
title: [XP-079] RN 与 Web 如何共享业务逻辑？monorepo 业务包怎么设计？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-079：RN 与 Web 如何共享业务逻辑？monorepo 业务包怎么设计？
**答**：
- 分层原则：**shared 只放与 UI 无关的逻辑**（领域模型、请求层、状态机、埋点协议、校验、常量），不 import react-native / react-dom，纯 TS 保证双端可构建。
- 平台差异用 **adapter 注入**：存储、路由跳转、toast 等能力由各端入口实现同一接口，shared 面向接口编程（依赖倒置）。
- monorepo 结构：`packages/shared`（业务逻辑）、`packages/api`（协议与类型，双端同源）、`apps/mobile`（RN）、`apps/web`（Next.js）；tsconfig paths + bundler 解析，构建产物 ESM。
- UI 层取舍：纯展示与逻辑组件可走 react-native-web 复用，复杂原生体验组件各端自绘，共享层限定到"无 UI"是性价比最高的一致性边界。
- 质量门禁：shared 覆盖率 ≥80% 单测、`import` 边界 lint（shared 禁止依赖端框架）、API 协议变更走 RFC（XP-075 契约先行）。

```typescript
// packages/shared/order —— 面向 adapter 接口编程，双端同源业务逻辑
import type { Storage } from './adapters';            // 只定义接口，不关心端实现

export interface OrderDraft { skuId: string; quantity: number; couponId?: string; }

export class OrderService {
  constructor(
    private http: HttpClient,                         // api 包统一请求层
    private storage: Storage,                         // 各端注入：RN=MMKV, Web=localStorage
  ) {}

  async submit(draft: OrderDraft) {
    validateDraft(draft);                             // 校验逻辑双端唯一实现
    const cached = await this.storage.get('last_order_fail');  // 失败补偿上下文
    const order = await this.http.post('/orders', { ...draft, retryOf: cached?.id });
    return order;
  }
}

// packages/shared/adapters/index.ts —— 能力接口，各端入口负责装配
export interface Storage {
  get(key: string): Promise<any>;
  set(key: string, value: any): Promise<void>;
}
// apps/mobile/container.ts（RN 侧装配）：
//   export const storage: Storage = { get: k => mmkvStorage.getString(k), ... }
// apps/web/container.ts（Web 侧装配）：
//   export const storage: Storage = { get: k => Promise.resolve(localStorage.getItem(k)), ... }
// 边界 lint：shared 内出现 "react-native"/"react-dom" import 直接 CI 报错
```
