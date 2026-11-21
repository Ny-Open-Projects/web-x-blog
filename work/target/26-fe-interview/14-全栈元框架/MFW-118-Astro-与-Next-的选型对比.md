---
title: [MFW-118] Astro 和 Next.js 怎么选？内容站和应用站的分界在哪里？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-118：Astro 和 Next.js 怎么选？内容站和应用站的分界在哪里？
**答**:
- 分界轴是「**交互密度**」而不是框架好坏：内容占比 >70%（营销、博客、文档、官网）→ Astro 的零 JS + 岛模型收益最大；应用占比高（后台、IM、重表单工作流）→ Next/Nuxt 的 SPA 级交互与状态管理更顺手。
- 数据层差异：Astro 构建期取数（getStaticPaths）+ Server Islands/Actions 补动态；Next 是请求时 RSC + 丰富缓存指令。数据频繁变化的页面 Astro 要靠 on-demand 重建或岛，心智成本上升。
- 团队因素：Astro 允许多框架混写（React/Vue/Svelte 岛共存），适合内容团队渐进迁移；Next 锁定 React 单栈。
- 混合现实：大厂常见解是「Astro 做站、Next/Nuxt 做应用」分域部署，中间用统一设计系统包——面试能给出这种分治方案是加分项。

```astro
---
// 判断题：这个页面该用谁？
// 1. 产品落地页（图文+一个询价按钮）      -> Astro（0 JS + 1 个岛）
// 2. 商品管理后台（表格筛选/批量操作）    -> Next/Nuxt（重交互 SPA）
// 3. 技术文档站（正文+搜索+评论区）       -> Astro（pagefind + visible 岛）
// 4. 商品详情页（实时库存/抢购倒计时）    -> Next（RSC + 动态缓存）或 Astro Server Islands

// Astro 落地页模板
import AskPriceButton from '../components/AskPriceButton.jsx';
---
<section class="hero">…图文内容：构建期渲染，0 JS…</section>
<AskPriceButton client:visible />  <!-- 唯一交互岛 -->
```

```tsx
// Next 应用页模板：重状态交互
'use client';
export default function ProductAdmin() {
  const [selection, setSelection] = useState<Set<string>>(new Set());
  const { data, mutate } = useSWR('/api/products');
  // 批量操作、表格虚拟滚动、复杂筛选状态…… SPA 心智更适合
  return <DataTable data={data} selection={selection} onSelect={setSelection} />;
}
```
