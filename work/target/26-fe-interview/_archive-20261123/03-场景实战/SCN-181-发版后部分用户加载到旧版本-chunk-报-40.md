---
title: [SCN-181] 发版后部分用户加载到旧版本 chunk 报 404（Loading chunk failed），hash 不一致如何排查与根治？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-181：发版后部分用户加载到旧版本 chunk 报 404（Loading chunk failed），hash 不一致如何排查与根治？
**答**：
- 根因几乎都是"HTML 与 chunk 的发布不是原子的"：CDN 上新 HTML 引用新 hash chunk，但 chunk 还没上传完；或老 chunk 被清理脚本删了，老 HTML（缓存/未关闭的页面）还在引用。
- 排查：拿报错 chunk 名反查发布记录与 CDN 存在性，确认是"HTML 先于 chunk 可见"还是"老 chunk 被提前清理"。
- 根治三件套：发布先传 chunk 后切 HTML（chunk 上传完成并预热后才发布 HTML）；保留最近 N 个版本的老 chunk 不删；运行时 chunk 加载失败自动拉最新 HTML 重载一次。
- SPA 长驻页面是重灾区：路由切换才懒加载的 chunk，在页面打开数小时后必然 404，必须有运行时降级。

```javascript
// chunk 404 根治：发布原子性约定 + 运行时降级重载
// webpack/vue-cli 侧：publicPath 与 CDN 同源，output 带 contenthash
// 发布脚本约定（CI 中）：
//   1. 先上传 assets/*.js（含老版本保留 10 个）
//   2. CDN 预热完成后，再上传 index.html
//   3. 清理脚本只删 "保留窗口" 之外的 chunk

// 运行时降级：懒加载 chunk 404 时拉最新 HTML 重建资源映射
export function installChunkFallback(router) {
  window.addEventListener('error', e => {
    const isChunkError = /Loading( CSS)? chunk .* failed/i.test(e.message);
    if (!isChunkError || sessionStorage.getItem('chunk-reloaded')) return;
    sessionStorage.setItem('chunk-reloaded', '1');     // 只自动重载一次，防循环
    // 用户停留在旧 HTML 上：其引用的 chunk 已被新版本清理
    // 方案：强刷到最新版本（保留当前路由路径）
    location.replace(`${location.pathname}#/__reloading__`);
    setTimeout(() => location.reload(), 0);
  });
  router.beforeEach(() => sessionStorage.removeItem('chunk-reloaded')); // 路由切换后允许再次兜底
}

// 服务端配合：HTML 响应头禁长缓存，保证版本切换即时生效
// nginx:
//   location = /index.html {
//     add_header Cache-Control "no-cache";   # 协商缓存：每次校验 etag
//   }
//   location ^~ /assets/ {
//     add_header Cache-Control "public, max-age=31536000, immutable";  # hash 资源永久缓存
//   }

// 发布校验：上线前检查 HTML 引用的 chunk 全部存在于 CDN（防"HTML 先行"）
export async function verifyRelease(htmlUrl) {
  const html = await fetch(htmlUrl).then(r => r.text());
  const chunks = [...html.matchAll(/(?:src|href)="(\/assets\/[^"]+\.(?:js|css))"/g)].map(m => m[1]);
  const missing = [];
  for (const c of chunks) {
    const res = await fetch(`https://cdn.example.com${c}`, { method: 'HEAD' });
    if (res.status !== 200) missing.push(c);           // 缺失即阻断发布
  }
  if (missing.length) throw new Error(`发布阻断，缺失产物：${missing.join(', ')}`);
}
```
