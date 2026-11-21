---
title: [WCN-026] 在 WC 中用 innerHTML 渲染用户数据有什么 XSS 风险？安全的替代方案有哪些？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-026：在 WC 中用 innerHTML 渲染用户数据有什么 XSS 风险？安全的替代方案有哪些？

**答**：
- 风险：innerHTML 会解析并执行标签与内联事件（`<img onerror=...>`、`<script>` 不执行但其子内容可能注册事件），评论/昵称等用户输入直接拼进模板即可注入。
- 方案一：结构静态化 + 数据走 textContent/属性——模板写死，用户数据只通过 `textContent`、`setAttribute` 注入，天然安全（首选）。
- 方案二：`Trusted Types`（CSP `require-trusted-types-for 'script'`）强制 innerHTML 只接收 TrustedHTML，配合 DOMPurify 等策略工厂在源头拦截。
- 方案三：需要富文本时经 sanitizer 白名单清洗后再赋值，且 sanitize 库要随组件一起打包，不能依赖宿主页面的版本。
- Shadow DOM 不减轻 XSS：注入发生在字符串解析阶段，与是否有影子树无关；closed shadow 更不是安全边界。

```javascript
class CommentItem extends HTMLElement {
  static observedAttributes = ['author'];
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    // 结构静态：不拼用户数据
    root.innerHTML = '<style>b{color:#111}</style><b id="a"></b><p id="c"></p>';
    this.#sync();
  }
  attributeChangedCallback() { this.#sync(); }
  #sync() {
    const a = this.shadowRoot.getElementById('a');
    a.textContent = this.getAttribute('author') ?? '';   // 安全：textContent
    const bodyNode = this.querySelector('template[slot=body]');
    const c = this.shadowRoot.getElementById('c');
    // 富文本走 slot 由宿主负责；绝不做 shadow.innerHTML = '<p>' + userBody
    c.textContent = this.getAttribute('summary') ?? '';
  }
}
customElements.define('comment-item', CommentItem);
```
