---
title: [PER-059] Vue 的 v-html 和 React 的 dangerouslySetInnerHTML 边界在哪？默认转义为什么不保险？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-059：Vue 的 v-html 和 React 的 dangerouslySetInnerHTML 边界在哪？默认转义为什么不保险？

**答**：
- Vue 插值 `{{ }}` 与 React JSX 文本**默认全部转义**，但 `v-html` 和 `dangerouslySetInnerHTML` 会把字符串按 HTML 解析，等于主动打开 XSS 通道。
- 这两个 API 的边界约定：内容必须来自**可信源**（自家 CMS 经服务端净化、受控的 markdown 渲染管线），绝不能直接放用户输入或接口透传的第三方内容。
- 默认转义“不保险”的另一面：转义只防**标签逃逸**，防不住属性上下文（如 `<a href="javascript:...">`）和 `href` 里 `&#x6a;` 这类实体编码绕过，所以 URL 仍需协议校验。
- 团队规范：把 v-html/dangerouslySetInnerHTML 列入 lint 黑名单，白名单豁免必须经过富文本净化函数或评审。

```jsx
// React：dangerouslySetInnerHTML 的正确边界
function Article({ html }) {
  // html 必须来自净化管线，例如服务端 DOMPurify 处理后的富文本
  return <div className="article" dangerouslySetInnerHTML={{ __html: html }} />;
}
// 用户输入一律走默认转义，不要打开 dangerouslySetInnerHTML
function Comment({ text }) {
  return <div className="comment">{text}</div>; // JSX 自动转义 <script> 为文本
}
```

```html
<!-- Vue：v-html 的边界 —— 内容必须先经净化 -->
<template>
  <div class="article" v-html="sanitizedHtml"></div> <!-- 来自净化函数，可接受 -->
  <div class="comment">{{ comment }}</div>           <!-- 用户输入，只用插值转义 -->
</template>
<script>
import DOMPurify from 'dompurify';
export default {
  data() {
    return {
      sanitizedHtml: DOMPurify.sanitize(this.cmsRichText, { ALLOWED_TAGS: ['p', 'b', 'a', 'img'] }),
      comment: this.userInput, // 原样绑定，模板会转义
    };
  },
};
</script>
```
