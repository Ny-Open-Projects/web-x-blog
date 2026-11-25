---
title: [MFW-026] 拦截路由（intercepting routes）怎么实现「URL 即弹窗」？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-026：拦截路由（intercepting routes）怎么实现「URL 即弹窗」？
**答**：
- 拦截路由：客户端导航时把目标路由「拦截」到另一个位置渲染；直接访问 URL（刷新/分享）则走原路由。两种上下文两种 UI，一套代码。
- 约定语法：`(.)` 同级拦截、`(..)` 上一级、`(..)(..)` 上两级、`(…)` 根级。例如 `(.)photo` 拦截同级 `photo`。
- 标准组合：**@modal 并行 slot + (.) 拦截 + default.js 关闭态**。软导航（点卡片）在弹窗里渲染大图；硬导航（刷新、直链）进完整详情页——可分享、SEO 友好、浏览器后退=关弹窗。
- 关闭弹窗用 `router.back()`（回到列表 URL），而不是 push 回列表，保持历史栈一致。
- 陷阱：default.js 必须返回 null 或正确占位，否则刷新时 slot 报 404。

```
app/
  @modal/
    (.)photo/[id]/page.tsx   // 软导航时：弹窗版大图
    default.tsx              // 非拦截态：null（关闭）
  photo/[id]/page.tsx        // 硬导航/直链：完整详情页
  page.tsx                   // 列表
```

```jsx
// app/@modal/(.)photo/[id]/page.tsx
'use client';
import { useRouter } from 'next/navigation';

export default async function ModalPhoto({ params }) {
  const photo = await getPhoto(params.id);
  return (
    <div className="modal-overlay">
      <button onClick={() => router.back()}>×</button>
      <img src={photo.url} alt={photo.title} />
    </div>
  );
}
```
