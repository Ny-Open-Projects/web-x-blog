---
title: [MFW-131] RRv7 的 Form、action 和 useFetcher 各解决什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-131：RRv7 的 Form、action 和 useFetcher 各解决什么？
**答**：
- `<Form method="post">` 提交到**当前或指定路由的 action**：无 JS 时原生 POST、有 JS 时拦截为 fetch 并重新调用 loader（mutation 后数据自动刷新）。`useSubmit` 支持编程式提交。
- `useFetcher`：**不引起导航**的交互（点赞、下拉选择、删除行），同样走 action/loader，但不改 URL、不进历史栈。
- mutation 生命周期：`useNavigation`（导航型提交状态）与 `useFetcher` 各自的 `state: 'idle'|'submitting'|'loading'` + `formData`，做 pending 按钮与乐观 UI 的原料。
- 与 Server Action 对比：RRv7 的 action 必须挂在路由上（POST /path?index 或 ?/name），是「路由即端点」的 RESTful 心智；Next 的 Server Action 是函数级 RPC。前者 URL 语义更强，后者更自由。

```tsx
// app/routes/cart.tsx
export async function action({ request }: any) {
  const fd = await request.formData();
  const intent = fd.get('intent');      // 多 action 语义用 intent 区分
  if (intent === 'add') await db.cart.add(String(fd.get('productId')));
  if (intent === 'remove') await db.cart.remove(String(fd.get('itemId')));
  return { ok: true }; // 返回后 router 自动重跑该路由 loader
}

export default function Cart() {
  const navigation = useNavigation();
  const fetcher = useFetcher();
  return (
    <>
      {/* 导航型提交：整个页面进入 submitting 状态 */}
      <Form method="post">
        <input type="hidden" name="productId" value="p1" />
        <button name="intent" value="add" disabled={navigation.state === 'submitting'}>
          加入购物车
        </button>
      </Form>

      {/* 非导航：单行删除，页面不闪 */}
      <fetcher.Form method="post">
        <input type="hidden" name="itemId" value="c1" />
        <input type="hidden" name="intent" value="remove" />
        <button disabled={fetcher.state === 'submitting'}>删除</button>
      </fetcher.Form>
    </>
  );
}
```
