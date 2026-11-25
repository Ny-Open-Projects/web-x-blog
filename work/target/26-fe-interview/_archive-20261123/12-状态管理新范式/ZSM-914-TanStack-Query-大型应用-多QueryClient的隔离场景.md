---
title: [914] 什么场景需要多个 QueryClient，怎么隔离
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 隔离]
type: 面试题
---

## 914：什么场景需要多个 QueryClient，怎么隔离

**答**：
- 隔离场景：微前端（子应用独立 QueryClient——缓存/配置互不污染）、测试（每用例独立 client 防串扰）、多租户 SPA（租户切换 clear 或独立实例——独立更干净但内存成本高）。
- 微前端主子架构：子应用自持 client（挂载创建/卸载销毁——防缓存常驻泄漏），主应用不共享缓存但共享「认证 token 获取方式」；通信用事件而非共享缓存。
- 隔离的代价：同实体主子各自缓存（重复请求）——可接受（微前端隔离优先），或用共享 fetch 层 + HTTP 缓存兜底。
- 追问钩子：单例 QueryClient 必须吗？——必须（多 client 会让 devtools/context 注入混乱），除隔离场景外全应用一个 client，用配置分层而非多实例解决差异。

```ts
// 微前端子应用生命周期
export function mount(el) {
  const qc = new QueryClient({ defaultOptions: subDefaults });
  const root = createRoot(el);
  root.render(<QueryClientProvider client={qc}><App /></QueryClientProvider>);
  return () => { root.unmount(); qc.clear(); };   // 卸载清缓存防泄漏
}
```

