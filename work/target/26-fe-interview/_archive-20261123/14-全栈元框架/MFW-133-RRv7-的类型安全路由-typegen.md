---
title: [MFW-133] RRv7 的类型安全路由（typegen）是怎么实现的？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-133：RRv7 的类型安全路由（typegen）是怎么实现的？
**答**：
- RRv7 从 `routes.ts` 配置**生成** `.react-router/types` 下的声明文件：每个路由模块获得专属的 `Route.LoaderArgs`、`Route.ComponentProps`、`Link` 的 `to` 参数类型等——路径拼写错误、params 字段错误在编译期报错。
- 原理：代码生成而非泛型魔法。routes.ts 是唯一事实源，dev/build 时跑 typegen，tsconfig include 该目录；链接 `to="/products/42"` 的类型检查靠生成的联合类型穷举。
- 与 TanStack Router 对比：TanStack 用文件路径直接泛型推导（更极致），RRv7 用显式 routes.ts + 生成（更可控、和 Vite 插件集成更稳）。
- 收益：重构路由零悬空引用；params 使用处全部类型安全；这也是 RRv7 主打的 DX 卖点。

```ts
// vite.config.ts
import reactRouter from '@react-router/dev/vite';

export default defineConfig({
  plugins: [reactRouter()],
});
```

```tsx
// app/routes/product.tsx —— 生成的类型直接用
import type { Route } from './+types/product';

export async function loader({ params }: Route.LoaderArgs) {
  // params.id: string —— 类型来自 :id 动态段
  return { product: await getProduct(params.id) };
}

export default function Product({ loaderData }: Route.ComponentProps) {
  // loaderData.product 完全类型化
  return <h1>{loaderData.product.name}</h1>;
}

// 任意位置：
// <Link to="/products/42">详情</Link>       ✓ 在 routes.ts 注册过
// <Link to="/prodcts/42">详情</Link>        ✗ 编译报错：路径不存在
```
