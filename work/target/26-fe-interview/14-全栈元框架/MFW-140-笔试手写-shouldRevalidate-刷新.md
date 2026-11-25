---
title: [MFW-140] 笔试：手写一个 shouldRevalidate 决策引擎
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-140：笔试：手写一个 shouldRevalidate 决策引擎
**答**：RRv7 的 `shouldRevalidate` 决定 mutation 后 loader 是否重跑。实现通用决策器 `decideRevalidate(ctx)`：① 默认 true（action 后全重跑）；② 提交的 intent 在 loader 声明的 `skipIntents` 里 → false；③ 导航到同 URL 且 formData 为空（无效导航）→ false；④ action 返回错误（actionResult 有 error）→ false（数据没变不必刷）；⑤ 强制刷新参数 `forceRevalidate` 出现 → 无条件 true。

```ts
type Ctx = {
  currentUrl: URL;
  nextUrl: URL;
  formData: FormData | null;      // 提交的数据（导航型）
  actionResult?: { ok?: boolean; error?: string };
  defaultShouldRevalidate: boolean;
};

type LoaderMeta = {
  skipIntents?: string[];         // 该 loader 不需要在这些 intent 后重跑
  forceRevalidate?: string[];     // 这些 query 参数变化时强制重跑
};

function decideRevalidate(ctx: Ctx, meta: LoaderMeta = {}): boolean {
  // ⑤ 强制条件优先级最高
  const keys = [...ctx.nextUrl.searchParams.keys()];
  if (meta.forceRevalidate?.some((k) => keys.includes(k))) return true;

  // ④ action 失败：数据未变，跳过刷新
  if (ctx.actionResult && ctx.actionResult.error) return false;

  // ③ 无效导航（同 URL 且无提交）：跳过
  const sameUrl = ctx.currentUrl.toString() === ctx.nextUrl.toString();
  if (!ctx.formData && sameUrl) return false;

  // ② intent 黑名单：提交意图与该 loader 无关
  if (ctx.formData) {
    const intent = ctx.formData.get('intent');
    if (typeof intent === 'string' && meta.skipIntents?.includes(intent)) return false;
  }

  // ① 默认
  return ctx.defaultShouldRevalidate;
}

// —— 用例 ——
const base = (over: Partial<Ctx>): Ctx => ({
  currentUrl: new URL('https://x.com/products'),
  nextUrl: new URL('https://x.com/products'),
  formData: null,
  defaultShouldRevalidate: true,
  ...over,
});

console.assert(decideRevalidate(base({ formData: new FormData() })) === true); // 空 formData 提交 -> 重跑
console.assert(decideRevalidate(base({}), { skipIntents: ['remove'] }) === true);
console.assert(
  decideRevalidate(base({ formData: fd('intent', 'remove') }), { skipIntents: ['remove'] }) === false,
);
console.assert(
  decideRevalidate(base({ actionResult: { error: '库存不足' } })) === false,
);
console.assert(
  decideRevalidate(base({ nextUrl: new URL('https://x.com/products?refresh=1') }), { forceRevalidate: ['refresh'] }) === true,
);
function fd(k: string, v: string) { const f = new FormData(); f.set(k, v); return f; }
```

**评分点**：
1. 优先级顺序清晰：force > error > 无效导航 > intent 黑名单 > 默认。
2. action 失败返回 false 的理由说得清（数据未变，刷新是浪费）。
3. sameUrl 判断用完整字符串比较（含 query），不是只比 pathname。
4. formData 为 null 与空 FormData 区分（空表单提交也要重跑）。
5. 决策器以纯函数呈现、可测试——工程素养体现。
