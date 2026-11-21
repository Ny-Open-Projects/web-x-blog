---
title: [DP-079] 控制反转 IoC 在前端如何实现？（装饰器 + 反射）（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-079：控制反转 IoC 在前端如何实现？（装饰器 + 反射）（高频）
**答**：
- IoC 是原则（依赖的创建权交给容器），DI 是实现手段；Angular/NestJS 用"装饰器 + Reflect Metadata"实现自动注入。
- 关键机制：`emitDecoratorMetadata` 让 TS 把参数类型写入元数据；容器读取 `Reflect.getMetadata('design:paramtypes', Target)` 获得依赖列表，递归实例化。
- 实现四步：`@Injectable()` 标记可注入 → 容器注册 token → 解析时反射拿构造参数 → 递归创建并缓存（单例）。
- 前端轻量版：React Context（运行时注入）、Vue 的 provide/inject——本质都是"消费方声明需求，容器供给"。

```typescript
import 'reflect-metadata';

// 1. @Injectable：标记类可被容器管理（本质只是打标记）
function Injectable() {
  return function <T extends new (...args: any[]) => any>(ctor: T) { return ctor; };
}
// 2. 容器：反射解析构造参数，递归注入，默认单例
class Container {
  #instances = new Map<Function, any>();
  resolve<T>(Target: new (...args: any[]) => T): T {
    if (this.#instances.has(Target)) return this.#instances.get(Target); // 单例缓存
    const paramTypes: any[] = Reflect.getMetadata('design:paramtypes', Target) || [];
    const deps = paramTypes.map((dep) => this.resolve(dep)); // 递归解析依赖
    const instance = new Target(...deps);
    this.#instances.set(Target, instance);
    return instance;
  }
}
// 3. 业务：只声明依赖类型，不创建任何实例
@Injectable()
class LoggerService {
  log(msg: string) { console.log('[logger]', msg); }
}
@Injectable()
class HttpService {
  constructor(private logger: LoggerService) {} // 反射读取到此依赖
  get(url: string) { this.logger.log(`GET ${url}`); return Promise.resolve({ ok: true }); }
}
@Injectable()
class UserService {
  constructor(private http: HttpService) {}     // 依赖链：UserService -> HttpService -> LoggerService
  async loadUser(id: number) {
    this.loggerBind();
    return this.http.get(`/users/${id}`);
  }
  loggerBind() {}
}
// 4. 容器装配：调用方完全不知道依赖链细节（控制已反转）
const container = new Container();
const userService = container.resolve(UserService);
userService.loadUser(1).then((r) => console.log(r));
// [logger] GET /users/1  { ok: true }
console.log(container.resolve(LoggerService) === container.resolve(LoggerService)); // true
// 对照：NestJS 的 @Module({ providers: [UserService, HttpService] }) 就是这个容器的生产级实现
```
