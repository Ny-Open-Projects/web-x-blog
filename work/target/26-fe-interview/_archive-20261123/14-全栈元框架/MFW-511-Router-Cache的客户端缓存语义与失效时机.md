---
title: [MFW-511] Router Cache 的客户端语义：staleTime 分层与失效时机
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-511：Router Cache 客户端语义：staleTime 分层与失效时机

**答**:
- Router Cache 的 staleTime 分层（Next 14 语义）：静态路由 payload 缓存 5 分钟（prefetch）/动态路由 30 秒——「返回导航瞬时显示」的来源；失效时机：路由变化（新的导航写新条目）、页面刷新（全清）、revalidate 调用（服务端触发客户端失效）、router.refresh()。
- 常见困惑：「为什么返回导航数据还是旧的」——Router Cache 命中即不重新请求（30s 内）；要强制新鲜 → 导航时 `router.refresh()` 或 prefetch=false；「数据更新了但 UI 不变」→ 服务端 revalidate 后客户端 payload 要重新拉（Router Cache 失效通知的前提是同 tag 订阅）。
- 内存管理：Cache 上限（Next 内部 LRU——大量路由导航后旧条目淘汰）；软导航的历史栈与 payload 缓存的协调（history.state 存 payload 引用 RBL-936 的框架版）。
- 追问钩子：为什么 prefetch 的 staleTime（5 分钟）比访问后的（30 秒）长？——prefetch 是「可能性投资」（用户可能不来——长缓存让投资保值）；访问后是「确定性消费」（用户在此页面——数据新鲜度更敏感）；缓存 TTL 的「投资/消费」分层与 RBL-769 预取预算同构：可能性资源用长 TTL、确定性资源用短 TTL。

```javascript
// Router Cache 行为速查
// 1) prefetch<Link prefetch={true}> 静态路由 → payload 缓存 5min
// 2) 进入页面后 → 动态 payload 30s 后过期
// 3) router.refresh() → 当前路由重新渲染（保留 client state）
// 4) 页面 reload → Router Cache 全清
// 强制新鲜的导航模式
import { useRouter } from 'next/navigation';
function FreshLink({ href, children }) {
  const router = useRouter();
  return (
    <a href={href} onClick={(e) => {
      e.preventDefault();
      router.push(href);
      router.refresh();                                  // 导航后强制重渲染
    }}>{children}</a>
  );
}
// 服务端失效通知的前提
// revalidateTag 后客户端要在「下一次导航」才拉新 payload
// 当前页面的实时性 → router.refresh() 或 useSyncExternalStore + polling
```
