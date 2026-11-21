---
title: [TS-192] 如何实现 express 风格的类型安全路由？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-192：如何实现 express 风格的类型安全路由？
**答**：
- Handler 的 req.params 类型由路径字符串推导：路径即类型源，注册时 handler 与路径绑定。
- 泛型 get<Route> 在注册点实例化 Params<Route>，内部存储降级为宽类型只做一次。
- 配合 TS-190 可扩展可选段与通配符。

```typescript
type Prettify<T> = { [K in keyof T]: T[K] } & {};

type Params<S extends string> =
  S extends `${string}:${infer P}/${infer Rest}`
    ? { [K in P]: string } & Params<`/${Rest}`>
    : S extends `${string}:${infer P}` ? { [K in P]: string }
    : {};

type Handler<Route extends string> = (
  req: { params: Prettify<Params<Route>>; query: Record<string, string> },
  res: { json: (data: unknown) => void },
) => void;

class App {
  private routes: [string, Handler<string>][] = [];
  get<Route extends string>(path: Route, handler: Handler<Route>): void {
    this.routes.push([path, handler as unknown as Handler<string>]);
  }
}

const app = new App();
app.get("/users/:id", (req, res) => {
  const id: string = req.params.id;  // 自动推导
  // req.params.nope;               // 报错：参数不存在
  res.json({ id });
});
app.get("/users/:uid/posts/:pid", (req) => {
  const { uid, pid } = req.params;   // 双参数全部推导
});
```
