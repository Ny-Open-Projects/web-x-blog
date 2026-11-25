---
title: [ARC-176] 设计一个新闻流 H5（SSR + 流式 + 离线）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-176：设计一个新闻流 H5（SSR + 流式 + 离线）如何设计？
**答**：
- 渲染架构：SSR 流式输出——骨架与头部立即返回（TTFB 极小），推荐流按计算完成顺序以 Suspense 边界分块注水（先到先显示），个性化计算（召回排序）不阻塞首字节。
- 个性化分层：服务端只渲染"公共首屏（置顶/编辑精选）"，个性化流走客户端二次请求（缓存友好 + CDN 可缓存骨架），或边缘函数注入轻量个性化。
- 离线与弱网：Service Worker 预缓存壳与热门栏目列表，文章详情按 LRU 缓存（离线可读最近浏览）；请求失败读缓存并标记"离线内容"。
- 媒体优化：首屏配图 AVIF/WebP 协商 + LQIP 占位，视频封面懒加载；阅读页正文文字优先渲染（图片 progressive）。

```typescript
// SSR 流式 + 离线缓存核心
// 服务端：流式 SSR（React 18 pipe）
app.get('/', async (req, res) => {
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  const shell = renderToPipeableStream(
    <Root>
      <Header />                                  // 立即输出
      <Suspense fallback={<ListSkeleton />}>      // 个性化流：慢，fallback 先显示
        <RecommendFeed userId={req.userId} />     // 完成一块流一块
      </Suspense>
      <Suspense fallback={null}>
        <EditorPicks />                           // 公共块：CDN 可缓存
      </Suspense>
    </Root>,
    { onError: (e) => { log.error(e); } },        // 流内报错降级为客户端重试，不中断整页
  );
  shell.pipe(res);
});
// 客户端 Service Worker：文章 LRU 离线缓存
self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (url.pathname.startsWith('/article/')) {
    e.respondWith(
      networkFirst(e.request, {                    // 网络优先，失败回缓存
        cache: lruCache('articles', { max: 100 }),
        fallback: (req) => caches.match(req).then(r => r && markOffline(r)),  // 标记离线内容
      }),
    );
  }
});
```

**追问**：

1. 流式输出到一半用户已能点击、hydration 还没完成，点了没反应怎么处理？ → 关键交互用内联脚本先绑事件做渐进增强，非关键控件在 hydration 前 disabled 并显示加载态，不能存在可点但无响应的按钮。
2. SW 缓存了旧壳，发版后出现新 HTML 配旧 JS 怎么防？ → 壳走 network-first 且带版本号，HTML 不缓存，SW 更新用 skipWaiting 加提示刷新，静态资源用内容 hash 长缓存。
3. 个性化推荐放客户端二次请求，首屏 CLS 怎么控住？ → 服务端先渲染等高骨架占位，数据回来只替换内容不改容器高度，图片预留宽高比，避免插入后把下方内容顶走。
