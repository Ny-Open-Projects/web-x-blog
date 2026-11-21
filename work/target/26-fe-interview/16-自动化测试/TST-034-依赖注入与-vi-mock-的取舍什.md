---
title: [TST-034] 依赖注入和 vi.mock 两种解耦方式怎么选？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-034：依赖注入和 vi.mock 两种解耦方式怎么选？
**答**：
- 依赖注入（DI）：外部依赖作为参数/选项传入（`createCart({ clock, storage })`），测试传假实现。优点是与框架无关、显式可见、类型友好；缺点是源码要多一层参数透传。
- vi.mock：源码保持直依赖，测试期模块级拦截。优点是源码零侵入、适合三方库；缺点是 mock 与源码路径强耦合、提升语义有学习成本、隐藏了真实依赖关系。
- 选型经验：自己写的服务/端口（时间、存储、网络客户端）优先 DI，测试更稳且能复用 fake 实现；三方库（axios、路由、chart 库）用 vi.mock，不值得为它改源码结构。
- 混合：DI 为主、vi.mock 兜底（mock 全局副作用如 console、location）。
- 追问钩子：DI 天然带「接口边界」，E2E/集成测试还能注入不同实现，这是 vi.mock 做不到的复用。

```typescript
// DI：依赖显式传入
export function createCart({ clock = () => Date.now(), storage = localStorage } = {}) {
  return {
    add(item) { storage.setItem('cart', JSON.stringify({ t: clock(), item })); },
  };
}
// 单测传假实现，无需任何 mock 框架
const memStore = new Map();
const cart = createCart({ clock: () => 1000, storage: { setItem: (k, v) => memStore.set(k, v) } });

// vi.mock：三方库场景
vi.mock('axios', () => ({ default: { get: vi.fn() } })); // axios 不值得做 DI
```
