---
title: [WCN-164] WCN 的安全基线：CSP、Trusted Types、供应链与组件沙箱怎么设计？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-164：WCN 的安全基线：CSP、Trusted Types、供应链与组件沙箱怎么设计？

**答**：
- CSP：组件服务声明 `script-src` 白名单（自身 CDN 域）、禁 `unsafe-inline`（组件样式走影子树内联 <style> 属于 CSS 不受 script-src 限制）；第三方宿主集成文档给出推荐 CSP 片段。
- Trusted Types：组件内部所有 innerHTML 赋值走统一 `sanitizer` 策略（`trustedTypes.createPolicy('acme-wc', ...)`），开启 `require-trusted-types-for 'script'` 后第三方宿主环境也强制安全；未配置 TT 的环境用 DOMPurify 兜底。
- 供应链：组件产物 SRI hash + 锁定版本（importmap 固定 URL）；依赖审计（npm audit/Socket）进 CI；不允许组件运行时从任意 URL 动态 import。
- 数据边界：组件消费的 props/detail 视为不可信输入——渲染前类型校验；对外事件 detail 只含声明字段（防数据泄露）。
- 沙箱边界认知：Shadow DOM 不是安全边界（WCN-006）；不可信代码用 iframe sandbox，可信任同源用 WC。

```javascript
// 组件内统一 HTML 策略
const policy = window.trustedTypes?.createPolicy('acme-wc', {
  createHTML: (input) => DOMPurify.sanitize(input, { ALLOWED_TAGS: ['b', 'i', 'a', 'span'], ALLOWED_ATTR: ['href'] }),
});
function safeSetHTML(el, html) {
  // TT 环境返回 TrustedHTML；无 TT 环境返回净化字符串——两种环境都安全
  el.innerHTML = policy ? policy.createHTML(html) : DOMPurify.sanitize(html);
}
```
