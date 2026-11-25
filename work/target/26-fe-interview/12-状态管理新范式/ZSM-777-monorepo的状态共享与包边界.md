---
title: [ZSM-777] monorepo 的状态共享：跨包 store 的边界与版本策略
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-777：monorepo 的状态共享：跨包 store 的边界与版本策略

**答**：
- monorepo（pnpm workspace）里状态库的分包：`@app/state-core`（provider/registry/工具）、`@app/state-domain`（业务 store）、`@app/state-types`（共享 TS 类型）。分包的价值：类型单点、变更可追踪（独立 CHANGELOG）、多 app 复用；代价：跨包更新的同步成本。
- 跨包 store 的规则：1) **实例归属**——store 实例在 app 层创建（core 提供 factory），包内只导出 factory 与类型，防多 app 各自单例的「包内状态泄漏到另一个 app」；2) **类型先行**——store 的 state 类型独立包（state-types），消费包只依赖类型不依赖实现（解耦编译顺序）；3) **私有 store 不出包**——包内 feature store 只在包内消费。
- 版本策略：monorepo 内部包用 `workspace:*`（总是同版本，原子变更）；对外发布的包用 semver + changesets。状态包的 breaking change（store 字段结构）要在 changeset 里写 migrate 指引。
- 循环依赖检测：`madge --circular` 或 pnpm 的依赖图检查进 CI——状态包之间的循环 import 会导致「初始化顺序不确定」的经典难查 bug。
- 追问钩子：跨包状态共享的替代方案——「不共享 store，共享事件」：包间通过事件总线/服务端事件解耦（包 A dispatch、包 B subscribe），比直接 import 对方 store 的耦合低一个量级，适合团队边界清晰的 monorepo。

```javascript
// packages/state-core/src/factory.ts —— 包只出 factory，实例归 app
import { createStore } from './create'

export function createCartStore(initial) {
  const store = createStore((set) => ({ items: [], ...initial }))
  return store
}

// apps/web/src/stores/cart.ts —— app 层创建实例
import { createCartStore } from '@app/state-core'
export const cartStoreApi = createCartStore()       // 单例归属 app
export const useCartStore = /* hook 绑定 cartStoreApi */

// packages/state-types/src/cart.ts —— 类型独立包
export interface CartItem { sku: string; qty: number; price: number }
export interface CartState { items: CartItem[]; total: number }

// pnpm-workspace.yaml
// packages:
//   - 'packages/*'
//   - 'apps/*'
// 依赖：@app/state-domain → workspace:* 版本（原子变更）

// CI：循环依赖检测
// madge --circular packages/state-*/src
```
