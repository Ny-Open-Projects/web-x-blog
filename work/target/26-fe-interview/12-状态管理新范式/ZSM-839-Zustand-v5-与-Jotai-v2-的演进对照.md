---
title: [ZSM-839] 状态库演进对照：Zustand v5 / Jotai 2.x / Valtio 2 的版本趋势
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-839：状态库演进对照：Zustand v5 / Jotai 2.x / Valtio 2 的版本趋势

**答**:
- 三库近年的演进方向一致——**并发渲染适配与体积收敛**：
- **Zustand v5**：移除默认 export（强制命名 import）、移除 create 的 equalityFn 第三参（改 useShallow）、默认 export 删除带来的 tree-shaking 收益；`useShallow` 成为一等公民。趋势：API 更严格（防误用），内部全面基于 useSyncExternalStore 的稳定契约。
- **Jotai 2.x**：`getDefaultStore` 替代内部单例（可注入）、store API 扩展（`store.get/set/sub` 三件套组件外可用）、Suspense 集成细化、`atomWithRefresh` 等 util 生态。趋势：store 作为一等公民对象（DI 友好，SSR 每请求实例 ZSM-513 更自然）。
- **Valtio 2**：访问跟踪性能优化（Proxy 拦截收敛）、`ref` 语义强化、derive/watch API 稳定化。趋势：保持「可变书写」体验的同时收紧边界（ref/快照纪律 ZSM-673）。
- 跨库共同趋势对状态工程的影响：1) **DI 化**（store 实例可注入）——测试/SSR/微前端的实例隔离更容易；2) **API 严格化**（删魔法参数）——团队 lint 规则与官方演进一致，维护成本降；3) **并发语义内建**——手写防撕裂 polyfill 可删（ZSM-503 的教学价值仍在）。
- 追问钩子：版本演进的「读 changelog 纪律」——每次大版本升级前读 migration guide + grep 项目内受影响 API 用法统计（ZSM-714 五步法第一步），别凭感觉升级。

```javascript
// 三库演进趋势对照
const VERSION_TRENDS = {
  zustand_v5: {
    breaking: ['移除默认 export', 'create 第三参 equalityFn 移除 → useShallow'],
    trend: 'API 严格化（防误用）+ useSyncExternalStore 稳定契约',
    benefit: 'tree-shaking 收益 + 误用提前暴露',
  },
  jotai_2: {
    changes: ['getDefaultStore 注入', 'store.get/set/sub 组件外一等', 'atomWithRefresh 等 util'],
    trend: 'store DI 化——SSR 每请求实例（513）更自然',
  },
  valtio_2: {
    changes: ['访问跟踪性能优化', 'ref 语义强化', 'derive/watch 稳定'],
    trend: '保持可变书写 + 收紧边界（673 纪律）',
  },
  共同趋势: {
    DI化: 'store 实例可注入 → 测试/SSR/微前端实例隔离更容易',
    严格化: '团队 lint 与官方演进一致，维护成本降',
    并发内建: '手写防撕裂 polyfill 可删（503 教学价值仍在）',
  },
  纪律: '升级前读 migration guide + grep 受影响 API 用法统计（714 五步法）',
}
```
