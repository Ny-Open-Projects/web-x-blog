---
title: [MFW-027] 笔试：实现并行 slot + 拦截路由的 Modal 方案（含 default 处理）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-027：笔试：实现并行 slot + 拦截路由的 Modal 方案（含 default 处理）
**题目**：给定列表页 `/feed` 与详情页 `/feed/[id]`，要求：软导航点列表项时详情以 Modal 覆盖在列表上（URL 变为 /feed/[id]）；直接刷新 /feed/[id] 时渲染完整详情页；点遮罩或后退键关闭 Modal。给出完整目录结构与关键代码。

```
app/
  feed/
    page.tsx               // 列表
    [id]/page.tsx          // 完整详情（硬导航/直链）
    @modal/
      (.)id/page.tsx       // 拦截同级 [id]：软导航弹窗
      default.tsx          // 默认关闭态
    layout.tsx             // 承接 children + modal
```

```jsx
// app/feed/layout.tsx
export default function FeedLayout({ children, modal }) {
  return (
    <>
      {children}
      {modal /* @modal slot：拦截态渲染 Modal，默认态为 null */}
    </>
  );
}

// app/feed/@modal/default.tsx —— 无匹配拦截时必须显式返回 null
export default function Default() { return null; }

// app/feed/@modal/(.)id/page.tsx
import { useRouter } from 'next/navigation';
import { Modal } from '@/components/modal';

export default async function InterceptedItem({ params }) {
  const item = await getItem(params.id);
  return (
    <Modal onClose={() => router.back()}>
      {/* 1. 关闭统一走 back()：URL 回到 /feed 且历史栈正确 */}
      <ItemView item={item} compact />
    </Modal>
  );
}

// app/feed/page.tsx —— 列表项用 Link（软导航触发拦截）
import Link from 'next/link';
export default async function Feed() {
  const items = await getFeed();
  return items.map((i) => (
    <Link key={i.id} href={`/feed/${i.id}`}>{i.title}</Link> // 触发 (.) 拦截
  ));
}

// **评分点**
// 1. 目录结构四件套齐全：@modal slot + (.) 拦截段 + default.tsx + 完整详情页。
// 2. default.tsx 返回 null 的必要性：缺失会导致刷新 /feed 时 slot 报错（高频失分点）。
// 3. 关闭用 router.back() 而非 push('/feed')：保持历史栈，浏览器后退键行为正确。
// 4. 能说清软/硬导航分野：Link 点击走拦截段，刷新/直链走 [id] 完整页——可分享可 SEO。
```
