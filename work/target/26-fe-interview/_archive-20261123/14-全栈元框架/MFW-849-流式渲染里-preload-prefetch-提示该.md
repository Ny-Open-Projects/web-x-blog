---
title: [MFW-849] 流式渲染里 preload/prefetch 提示该在哪个时机注入才有效
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-849：流式渲染里 preload/prefetch 提示该在哪个时机注入才有效

**答**：
- 结论：资源提示必须在浏览器下载对应资源前注入才有效；流式 HTML 应在 shell 阶段尽早注入关键资源 preload，洞数据到达后再动态注入次级资源 prefetch。
- 落地：首屏图片/字体 preload 放 shell；次级资源用洞返回后 <link rel=prefetch> 动态插入 head。
- 追问钩子：注入太晚会怎样？——浏览器已开始下载，preload 失去意义甚至造成重复请求。

```javascript
// shell：尽早注入首屏关键资源
res.write(`<head>
  <link rel="preload" as="image" href="/hero.webp">
  <link rel="preload" as="font" href="/font.woff2" crossorigin>
</head>`);
res.flush();

// 洞到达后：按实际内容动态注入次级 prefetch
async function renderHole() {
  const data = await loadRecommendations();
  const links = data.map(d => `<link rel="prefetch" href="${d.url}">`).join('');
  document.head.insertAdjacentHTML('beforeend', links); // 客户端动态注入
  return render(data);
}
```
