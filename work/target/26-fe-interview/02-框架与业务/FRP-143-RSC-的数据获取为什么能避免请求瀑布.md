---
title: [FRP-143] RSC 的数据获取为什么能避免请求瀑布？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-143：RSC 的数据获取为什么能避免请求瀑布？

**答**：
- 客户端取数的瀑布来源：组件**挂载后**才 fetch，父→子串行 await，每层多一个往返（网络延迟叠加）。
- RSC 把取数挪到**渲染期**：server component 直接 await，多个组件的 fetch 可并行启动（各自 await 不阻塞彼此，或显式 `Promise.all`）。
- 不想阻塞整页时：把 promise **不 await 直接往下传**，由 Suspense 边界接住——壳先返回，慢数据流式补上（见 FRP-144）。
- 服务端之间的请求走内网、且可与渲染并行调度，往返成本远低于浏览器逐级挂载取数。

```javascript
// 简化实现，帮助理解瀑布的形成与消除
// —— 反例：客户端取数瀑布 ——
// <Page> mount -> fetch('/api/user') 300ms
//   <Profile> mount（等 user 到）-> fetch('/api/posts') 300ms
//     <Comments> mount（等 posts 到）-> fetch('/api/comments') 300ms
// 总耗时 900ms，且每层都是"渲染完成才能开始下一层请求"

// —— RSC：并行启动 ——
async function Page() {
  const [user, postsPromise] = await Promise.all([   // 显式并行
    getUser(),
    getPosts(),          // 不 await，继续往下传 promise
  ]);
  return (
    <div>
      <Profile user={user} />
      <Suspense fallback={<PostsSkeleton />}>
        <Posts data={postsPromise} />   {/* 洞：posts 好了再流式填充 */}
      </Suspense>
    </div>
  );
}
// 即使不写 Promise.all，两个 async server 组件并行渲染时各自的 fetch 也会同时启动——
// 因为服务端渲染是"并发调度 promise"，不是"组件挂载后才有机会请求"

// —— 源码视角：server 渲染器对 async 组件的处理 ——
async function renderNode(node) {
  if (node.then) {                     // 是 promise：注册为"洞"，不阻塞兄弟节点
    pendingHoles.push(node);
    return { __hole: pendingHoles.length - 1 };
  }
  if (typeof node.type === 'function') {
    const result = node.type(node.props);   // async 组件：拿到 promise
    return renderNode(result);              // 递归处理
  }
  return node;
}
// 关键：pendingHoles 中的每个 promise 独立 resolve、独立流式输出 —— 慢洞不拖慢快洞
```
