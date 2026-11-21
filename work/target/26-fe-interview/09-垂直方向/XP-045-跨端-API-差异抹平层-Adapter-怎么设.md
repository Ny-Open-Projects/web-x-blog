---
title: [XP-045] 跨端 API 差异抹平层（Adapter）怎么设计？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-045：跨端 API 差异抹平层（Adapter）怎么设计？
**答**：
- 接口先行：定义 **TypeScript 接口**（能力契约），各端提供实现并在壳工程注册；业务只 import 接口不 import 实现（依赖倒置）。
- 差异处理三类：**语义等价**（直接映射，如 setStorage）、**语义近似**（包装补齐，如支付宝无某回调则模拟）、**能力缺失**（降级或抛明确错误码，见 XP-073）。
- 注册与分发：运行时按平台探测选择实现；编译期条件编译直接剔除他端代码，两者结合。
- 质量保障：接口层 100% 单测 + 每端契约测试（同一用例矩阵跑各端实现，行为一致性断言）。
- 演进安全：接口版本化（v2 加字段向后兼容），废弃走告警日志统计真实使用量再下线。

```typescript
// adapter/storage/index.ts —— 能力契约
export interface IStorage {
  get<T>(key: string): Promise<T | null>;
  set(key: string, value: unknown): Promise<void>;
  remove(key: string): Promise<void>;
}

// adapter/storage/weapp.ts
export const weappStorage: IStorage = {
  get: (k) => new Promise((res) => wx.getStorage({ key: k, success: (r) => res(r.result ?? null), fail: () => res(null) })),
  set: (k, v) => new Promise((res, rej) => wx.setStorage({ key: k, data: v, success: () => res(), fail: rej })),
  remove: (k) => new Promise((res) => wx.removeStorage({ key: k, complete: () => res() })),
};

// adapter/storage/h5.ts
export const h5Storage: IStorage = {
  get: async (k) => { const raw = localStorage.getItem(k); return raw ? JSON.parse(raw) : null; },
  set: async (k, v) => localStorage.setItem(k, JSON.stringify(v)),
  remove: async (k) => localStorage.removeItem(k),
};

// adapter/index.ts —— 平台探测注册（编译期条件编译剔除他端实现）
let impl: IStorage;
// #ifdef MP-WEIXIN
impl = weappStorage;
// #endif
// #ifdef H5
impl = h5Storage;
// #endif
export const storage: IStorage = new Proxy(impl, {           // 统一埋点/降级切面
  get(t, p) { reportApiCall('storage', String(p)); return Reflect.get(t, p); },
});
```
