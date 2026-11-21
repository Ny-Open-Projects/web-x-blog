---
title: [DP-005] 依赖倒置原则 DIP 是什么？前端有哪些真实应用？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-005：依赖倒置原则 DIP 是什么？前端有哪些真实应用？（高频）
**答**：
- DIP：高层模块不依赖低层实现，双方都依赖抽象（接口）；"倒置"的是依赖方向——实现细节反过来依赖上层定义的接口。
- 前端实例：数据层依赖 `RequestClient` 抽象，可注入 axios 实现、fetch 实现、mock 实现；React 用 props/Context 注入依赖，Angular/NestJS 直接内置 IoC 容器。
- 收益：可替换（切后端/切环境）、可测试（单测注入 mock）、可隔离（SDK 不绑定具体网络库）。
- 与工厂/注入的关系：工厂是"DIP 的落地手段之一"，负责把具体实现的创建收拢到一处。

```typescript
// 高层只定义抽象，不 import 任何具体网络库（依赖方向被倒置）
interface IStorage {
  get(key: string): string | null;
  set(key: string, value: string): void;
}
// 依赖抽象的 高层业务
class AuthService {
  constructor(private storage: IStorage) {} // 构造器注入
  saveToken(token: string) { this.storage.set('token', token); }
  getToken() { return this.storage.get('token'); }
}
// 低层实现1：浏览器 localStorage
class LocalStorageAdapter implements IStorage {
  get(key: string) { return localStorage.getItem(key); }
  set(key: string, value: string) { localStorage.setItem(key, value); }
}
// 低层实现2：内存实现，专供单元测试
class MemoryStorage implements IStorage {
  private map = new Map<string, string>();
  get(key: string) { return this.map.get(key) ?? null; }
  set(key: string, v: string) { this.map.set(key, v); }
}
// 生产环境注入真实实现
const auth = new AuthService(new LocalStorageAdapter());
auth.saveToken('jwt-xxx');
// 测试环境注入内存实现，无需 jsdom
const authForTest = new AuthService(new MemoryStorage());
authForTest.saveToken('jwt-test'); // 断言无副作用
```
