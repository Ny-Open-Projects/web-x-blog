---
title: [MFW-537] 元框架与 View Transitions：软导航动画的协议集成
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-537：View Transitions：软导航动画协议

**答**:
- View Transitions API（document.startViewTransition）：浏览器截图旧状态 → DOM 更新 → 截图新状态 → 动画过渡——与软导航的集成：导航在 startViewTransition 回调内完成（React 18 的 unstable startTransition + flushSync 组合）。
- 集成的时序难题：软导航的数据获取是异步的（RSC payload 加载）——startViewTransition 的回调需要同步 DOM 更新——「先取数据、动画期间渲染」：导航前预取（prefetch）→ startViewTransition 内同步 setState → 新状态渲染。
- 粒度控制：`view-transition-name` CSS 属性标记独立动画元素（列表项单独过渡——MPA 的元素级过渡到 SPA）；动画与 RSC 流式的冲突（流式补丁在过渡中到达——过渡快照不含新内容）。
- 降级：API 不可用（Firefox/Safari 部分）→ 直接渲染无动画——特性检测包装（RBL-751 能力清单）。
- 追问钩子：为什么 View Transitions 与流式 SSR 的组合有「时序张力」？——过渡动画依赖「新旧快照」同步可得；流式 SSR 的新内容异步到达（动画启动时可能只有骨架）——策略：过渡用「预取完成的数据」（确定性）而非流式（不确定性）；「确定性快照」是动画的前提——与 RBL-921 游标/快照的「确定性状态」要求同源：视觉系统需要确定状态，数据流是概率性的——两者接口处要显式缓冲。

```javascript
// Next App Router 的 VT 集成（实验性）
import { unstable_ViewTransition as ViewTransition } from 'react';
export default function ProductList({ products }) {
  return (
    <ViewTransition>                                     {/* 列表容器：进入/退出动画 */}
      {products.map(p => (
        <Link key={p.id} href={`/p/${p.id}`}            // 导航即过渡
          style={{ viewTransitionName: `item-${p.id}` }}> {/* 元素级：卡片飞到详情 */}
          {p.name}
        </Link>
      ))}
    </ViewTransition>
  );
}
// 手动集成（无框架支持时）
const navigateWithTransition = async (href) => {
  await prefetch(href);                                  // 数据先行（确定性）
  if (!document.startViewTransition) return router.push(href);   // 降级
  document.startViewTransition(() => {
    flushSync(() => router.push(href));                  // 同步 DOM 更新
  });
};
```
