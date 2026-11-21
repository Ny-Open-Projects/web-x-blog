---
title: [FRP-142] Server Actions 的完整闭环是怎样的（RPC、序列化、revalidate）？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-142：Server Actions 的完整闭环是怎样的（RPC、序列化、revalidate）？

**答**：
- `"use server"` 函数被打包成**端点**：客户端拿到的函数引用被替换为 action id；调用时发起 POST（参数经 RSC 序列化协议编码，FormData 可直接传）。
- 服务端按 id 找回原函数执行；在 Next/React 集成里，执行完后会**重新渲染受影响的 RSC 树并流回客户端**，客户端 reconcile——不需要手写 refetch。
- `revalidatePath/revalidateTag` 的作用是让**数据缓存/路由缓存失效**，迫使下一次渲染取新数据——action 闭环 = RPC + 失效 + 自动重渲。
- 安全边界：action 的参数来自网络，必须当作不可信输入；返回值也受序列化协议约束（不能返回函数/类实例）。

```javascript
// 简化实现，帮助理解 Server Action 闭环
// —— 服务端：定义与注册 ——
async function createPost(formData) {
  'use server';
  const title = formData.get('title');            // 表单渐进增强：FormData 直达
  await db.post.create({ data: { title } });
  revalidatePath('/posts');                        // 让 /posts 的数据缓存与路由缓存失效
  // 无需返回值：框架重渲染 RSC 树并流回
}
registerServerAction('a1', createPost);            // 打包器生成 id -> 函数映射

// —— 客户端：action 引用 ——
function createPostRef(id) {
  return async (...args) => {
    const body = encodeFlightArgs(args);           // RSC 序列化协议编码参数
    const res = await fetch('/__actions', {
      method: 'POST',
      headers: { 'Next-Action': id },              // 端点定位
      body,
    });
    // 返回的流里包含：action 结果 + 重新渲染的 RSC 树增量
    const stream = decodeFlightStream(res.body);
    applyRscPatch(stream.rscTree);                 // 客户端 reconcile，UI 自动更新
    return stream.returnValue;
  };
}

// 组件里使用：
// <form action={createPost}>          提交即 POST，无需手写 fetch
// <button onClick={() => createPost(...)}> 编程式调用也走同一端点

// —— 服务端接收端点（简化） ——
app.post('/__actions', async (req, res) => {
  const id = req.headers['next-action'];
  const args = decodeFlightArgs(req.body);
  const returnValue = await actionMap[id](...args); // 执行原函数
  const rscTree = await rerenderAffectedRoutes();   // revalidatePath 已使缓存失效
  res.setHeader('content-type', 'text/x-component');
  streamFlight(res, { returnValue, rscTree });      // 一次性返回结果 + 新树
});
```
