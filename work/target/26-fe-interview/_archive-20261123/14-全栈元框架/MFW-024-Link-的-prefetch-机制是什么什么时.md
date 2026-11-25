---
title: [MFW-024] Link 的 prefetch 机制是什么？什么时候会预取、预取什么内容？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-024：Link 的 prefetch 机制是什么？什么时候会预取、预取什么内容？
**答**：
- `<Link>` 默认自动 prefetch：视口内可见即触发（生产环境；开发环境默认关闭），预取的是**目标路由的 RSC Payload**（不是整页 HTML）。
- 分级预取：静态路由预取**完整** Payload（点击零延迟切换）；动态路由只预取**到第一个动态挂起点为止**的 loading 壳（点击时再拉剩余，保证不预取过期数据）。
- `prefetch={false}` 完全关闭；`prefetch={null}`（Next 15）「部分预取」可显式声明只拿壳。
- 预取产物进 Client Router Cache，受 staleTime 控制过期后重新预取。
- 大量 Link 的列表页要防预取风暴：视口外不触发；必要时 `prefetch={false}` + 鼠标 hover 时手动 router.prefetch()。

```jsx
import Link from 'next/link';

export default function Nav() {
  return (
    <>
      {/* 默认：视口内自动预取 RSC Payload（静态页全量/动态页只到 loading 壳） */}
      <Link href="/products">商品</Link>

      {/* 动态页面：只预取壳，点击时再拉真实数据 */}
      <Link href="/orders/123" prefetch={null}>订单详情</Link>

      {/* 关闭预取：详情/重资源页，节省带宽 */}
      <Link href="/admin" prefetch={false}>管理后台</Link>
    </>
  );
}
```

```jsx
'use client';
// hover 时才预取：列表页大量链接时的流量控制
import { useRouter } from 'next/navigation';

function SmartLink({ href, children }) {
  const router = useRouter();
  return (
    <a
      href={href}
      onMouseEnter={() => router.prefetch(href)} // 用户有意图时才花流量
      onClick={(e) => { e.preventDefault(); router.push(href); }}
    >
      {children}
    </a>
  );
}
```
