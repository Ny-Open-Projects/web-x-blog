---
title: [H5-045] iframe 的 sandbox 属性如何工作？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-045：iframe 的 sandbox 属性如何工作？
**答**：
- sandbox 给 iframe 内容套上"默认全部禁止"的能力沙箱，再逐项放行：`allow-scripts`（脚本）、`allow-same-origin`（保留自身 origin，否则被当成唯一源、连 localStorage/Cookie 都不能用）、`allow-forms`、`allow-popups`、`allow-top-navigation`。
- 沙箱值是"能力清单"：写 `sandbox` 空值 = 全禁；要遵循最小授权，比如第三方广告 iframe 常只给 `allow-scripts allow-popups`。
- 危险组合：`allow-scripts` + `allow-same-origin` 同时给且源与父页相同，脚本可移除 sandbox 属性逃逸，等于没沙箱。
- 同源 iframe 仍可操作父页面 DOM，不可信内容必须加 sandbox 或换跨域域名部署。

```html
<!-- 第三方内容：只给最小能力 -->
<iframe
  src="https://ads.example.com/banner"
  sandbox="allow-scripts allow-popups"
  loading="lazy"
  title="广告"
></iframe>

<!-- 完全静态预览：连脚本都不给 -->
<iframe srcdoc="<h1>纯静态预览</h1>" sandbox title="预览"></iframe>

<!-- 用户提交的富文本预览：禁脚本、禁表单、禁弹窗 -->
<iframe
  src="/preview/comment-123"
  sandbox="allow-same-origin"
  title="评论预览"
></iframe>
```

```javascript
// 动态创建带沙箱的 iframe 并传参：srcdoc + postMessage 组合
const frame = document.createElement('iframe');
frame.sandbox.add('allow-scripts'); // 注意：没有 allow-same-origin，内部无法访问父页存储
frame.srcdoc = `
  <script>
    window.addEventListener('message', (e) => {
      // 沙箱内无自身 origin，只能被动接收
      document.body.textContent = '收到: ' + e.data.count;
    });
  <\/script>
`;
document.body.appendChild(frame);
frame.onload = () => {
  frame.contentWindow.postMessage({ count: 42 }, '*'); // 不透明源场景只能 *
};
```
