---
title: [TST-006] 笔试：手写一个极简的模块 mock 机制（require 拦截）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-006：笔试：手写一个极简的模块 mock 机制（require 拦截）
**答**：
- 需求：实现 `mockModule(path, factory)` / `resetMocks()`，让后续 `requireModule(path)` 返回工厂产物而非真实模块，模拟 vi.mock 的注册表思路。
- 核心数据结构：`Map<path, factory>` 注册表；加载时先查注册表，命中则执行工厂（缓存结果），未命中走 require。
- 边界：工厂只执行一次（多次引用同一 mock 实例，保证 expect 作用其上）；reset 后清缓存与注册表；相对路径按调用方解析可简化为原样 key。

```javascript
// mini-mock.js
const registry = new Map();      // path -> factory
const cache = new Map();         // path -> 实例化后的 mock（工厂只跑一次）

function mockModule(path, factory) {
  registry.set(path, factory);
  cache.delete(path);            // 重新注册时丢弃旧实例
}

function resetMocks() {
  registry.clear();
  cache.clear();
}

function requireModule(path) {
  if (registry.has(path)) {
    if (!cache.has(path)) cache.set(path, registry.get(path)());
    return cache.get(path);      // 同一模块引用同一 mock 单例
  }
  return require(path);          // 未 mock 走真实加载
}

// ---- 用法演示 ----
mockModule('./config', () => ({ host: 'mock.example.com' }));
const config = requireModule('./config');
expect(config.host).toBe('mock.example.com');

const again = requireModule('./config');
expect(again).toBe(config);      // 单例：多次获取同一实例

resetMocks();
const real = requireModule('./config'); // 恢复真实模块
console.log(real.host);
```
**评分点**：
- 注册表 + 缓存两层结构，说出「工厂只实例化一次、多引用共享同一 mock」是核心得分点。
- reset 必须同时清注册表和缓存。
- 能提到 ESM 下需在加载阶段拦截（loader/转换期重写 import），说明知道 require 方案的局限。
