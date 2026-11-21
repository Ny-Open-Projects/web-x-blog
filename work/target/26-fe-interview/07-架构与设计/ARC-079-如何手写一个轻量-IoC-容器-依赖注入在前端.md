---
title: [ARC-079] 如何手写一个轻量 IoC 容器（依赖注入在前端）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-079：如何手写一个轻量 IoC 容器（依赖注入在前端）？
**答**：
- 最小实现三件套：Token（服务标识）、Provider（怎么构造：类/工厂/值）、Container（注册与解析，默认单例）。
- 关键设计：解析时递归注入构造参数（按 Token 元数据），支持 `inject` 装饰器或显式参数数组；惰性实例化。
- 前端适用面：SDK/大型应用的跨层服务注入（logger/http/config），小应用用模块导入即可，别过度设计。

```typescript
// 轻量 IoC 容器核心（~50 行思想）
type Token<T> = symbol & { __type?: T };
const createToken = <T,>(name: string) => Symbol(name) as Token<T>;

interface Provider<T> { useClass?: new (...args: never[]) => T; useFactory?: (c: Container) => T; useValue?: T; }

class Container {
  private registry = new Map<Token<unknown>, Provider<unknown>>();
  private cache = new Map<Token<unknown>, unknown>();          // 单例缓存
  register<T>(t: Token<T>, p: Provider<T>) { this.registry.set(t, p); }
  resolve<T>(t: Token<T>): T {
    if (this.cache.has(t)) return this.cache.get(t) as T;      // 惰性单例
    const p = this.registry.get(t);
    if (!p) throw new Error(`未注册的服务 ${String(t.description)}`);
    const inst = p.useValue ?? p.useFactory?.(this)
      ?? new p.useClass!(...depsOf(p.useClass).map(d => this.resolve(d)));  // 递归注入
    this.cache.set(t, inst);
    return inst as T;
  }
}
// 使用：构造参数 Token 元数据（或 reflect-metadata 装饰器）
const LoggerT = createToken<Logger>('Logger'), HttpT = createToken<Http>('Http');
const depsOf = (c: Function): Token<unknown>[] => (c as any).deps ?? [];
class OrderService { static deps = [LoggerT, HttpT]; constructor(l: Logger, h: Http) {} }
container.register(OrderServiceT, { useClass: OrderService });
```
