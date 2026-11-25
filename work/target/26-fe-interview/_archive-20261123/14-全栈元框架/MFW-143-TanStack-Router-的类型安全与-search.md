---
title: [MFW-143] TanStack Router 的类型安全到什么程度？search params 为什么难做？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-143：TanStack Router 的类型安全到什么程度？search params 为什么难做？
**答**：
- 覆盖面：路径 params、search params、loader 数据、navigate/Link 的 to 参数、`useSearch/useParams` 返回值全部类型化——`<Link to="/products/$id" params={{ id: 1 }}>` 数字会报错。
- search params 难在「类型 + 运行时双重问题」：URL query 是字符串、可选、可重复、可乱序；框架要做①字符串→类型的运行时校验（非法值 400 或降级）、②校验后的 TS 类型推导、③URL 状态与组件状态的双向同步。TanStack 的答案是 `validateSearch` + zod schema 内建。
- URL 即状态的理念：筛选/分页/Tab 全放 search params（可分享、可后退），router 把它们变成类型安全的状态源——替代 useState 散落。
- 副作用意识：search params 变化默认触发 loader 重跑（依赖追踪），必须区分「影响数据的参数」与「纯 UI 参数」。

```tsx
// 筛选列表页：URL 即状态
const Route = createFileRoute('/products')({
  validateSearch: z.object({
    q: z.string().optional(),                       // 搜索词
    sort: z.enum(['sales', 'price']).default('sales'),
    page: z.coerce.number().int().min(1).default(1), // "3" -> 3
    // 非法 page=-1：运行时校验拒绝，组件内类型保证合法
  }),
  loader: ({ search }) => search, // search 类型 = validateSearch 的输出
});

function ProductsPage() {
  const search = Route.useSearch();
  const navigate = Route.useNavigate();

  // 类型安全的更新：字段名拼错直接编译报错
  return (
    <input
      value={search.q ?? ''}
      onChange={(e) => navigate({ search: { ...search, q: e.target.value, page: 1 } })}
    />
  );
}

// 链接构造也是类型化的
// <Link to="/products" search={{ sort: 'price', page: 2 }}>按价格</Link>
```
