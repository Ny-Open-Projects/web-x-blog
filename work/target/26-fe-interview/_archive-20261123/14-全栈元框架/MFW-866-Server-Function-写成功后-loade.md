---
title: [MFW-866] Server Function 写成功后，loader 缓存和 Query 缓存怎么一起失效
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-866：Server Function 写成功后，loader 缓存和 Query 缓存怎么一起失效

**答**：
- 结论：两套缓存各有失效入口，必须同时失效——Server Function 里 revalidate（loader 侧）+ 客户端 invalidateQueries（Query 侧），遗漏任一都会读旧数据。
- 落地：封装统一 invalidate 工具；写操作返回后两端一起失效，或让 loader 数据源与 Query 共享同一 tag。
- 追问钩子：能否只保留一个缓存？——SSR 首屏依赖 loader、交互依赖 Query，短期桥接是现实方案。

```javascript
// Server Function：服务端失效 loader 侧
const updatePost = createServerFn().handler(async ({ data }) => {
  const post = await db.posts.update(data);
  revalidatePath('/posts/' + data.id);              // loader / Full Route 侧
  return post;
});

// 客户端：提交成功后失效 Query 侧
async function onSave(data) {
  await updatePost({ data });
  await queryClient.invalidateQueries({ queryKey: ['posts'] }); // Query 侧
  router.invalidate();                                            // loader 侧重跑
}
// 原则：一次写入，两端失效，缺一不可
```
