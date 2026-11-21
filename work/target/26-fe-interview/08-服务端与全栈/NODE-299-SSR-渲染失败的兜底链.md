---
title: [NODE-299] SSR 渲染失败的兜底链？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-299：SSR 渲染失败的兜底链？
**答**:
- 兜底链四级：① 渲染超时 → 客户端骨架接管（CSR fallback）；② 数据部分失败 → 已有部分流式输出（Suspense 分段 NODE-261）；③ 框架级错误 → 静态 HTML 模板兜底（错误页也要可交互）；④ 服务不可用 → CDN 缓存的旧页面（ARC-272 容灾）。
- 每级都要上报降级原因（率）——降级率是 SSR 健康度核心指标。
- 用户感知排序：CSR fallback（功能完整）> 静态模板（可浏览）> 旧缓存 > 错误页。
- 实现要点：兜底选择在渲染入口决策（NODE-272 队列满时直接走 ②/③ 级，不等超时）。

```javascript
// 四级兜底入口
async function render(req, res) {
  try { return await renderApp(req, res); }                    // 正常
  catch (e) {
    report({ type: 'ssr-fallback', level: 'csr', err: String(e) });
    return serveCSRShell(res);                                  // ① 客户端接管
  }
}
function serveCSRShell(res) {
  res.set('Cache-Control', 'no-store');
  res.status(200).send(csrShellTemplate);                       // 骨架 + bundle 引用
}
// ④ CDN 旧页：源站 5xx 时 CDN 返回 stale（proxy_next_upstream + stale-while-error 配置）
```
