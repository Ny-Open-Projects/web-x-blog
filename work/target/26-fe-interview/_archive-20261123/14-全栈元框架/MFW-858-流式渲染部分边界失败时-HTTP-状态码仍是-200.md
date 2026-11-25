---
title: [MFW-858] 流式渲染部分边界失败时 HTTP 状态码仍是 200，怎么权衡错误预算
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-858：流式渲染部分边界失败时 HTTP 状态码仍是 200，怎么权衡错误预算

**答**：
- 结论：流一旦开始输出（200 + chunked）就无法改状态码，部分失败只能在 UI 内降级（错误占位），不能返回 500。
- 落地：关键内容失败要「尽早失败」——在首次 flush 前决定；非关键失败用边界内错误 UI 兜底并上报；用错误预算控制允许失败比例。
- 追问钩子：关键内容 flush 后才失败怎么办？——用客户端补丁替换该区域为错误态，并记为事故。

```javascript
async function renderBoundary(name, fn) {
  try { return await fn(); }
  catch (e) {
    report({ boundary: name, error: e.message });    // 上报错误预算
    return `<div data-error="${name}">内容加载失败，重试</div>`;
  }
}
// 关键内容：flush 前决定，失败则整体降级
const critical = await renderBoundary('price', loadPrice);
if (critical.includes('data-error')) return renderFallbackPage(); // 尽早失败
res.write(critical); res.flush();                    // 之后不可改 200
// 非关键：边界内降级
res.write(await renderBoundary('comments', loadComments));
```
