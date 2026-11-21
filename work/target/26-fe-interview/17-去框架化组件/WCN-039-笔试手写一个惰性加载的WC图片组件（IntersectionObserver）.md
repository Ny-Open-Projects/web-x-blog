---
title: [WCN-039] 笔试：手写一个惰性加载的 WC 图片组件（IntersectionObserver + 占位）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-039：笔试：手写一个惰性加载的 WC 图片组件

**题目**：`<wc-img src="..." alt="..." ratio="16/9">`：① 进入视口前后 200px 才设置真实 src；② 加载中显示骨架占位（按 ratio 保持宽高比）；③ 加载完成淡入、失败显示重试按钮；④ disconnected 停止观察；⑤ 支持 `loading="eager"` 跳过观察直接加载。

**答**：

```javascript
class WcImg extends HTMLElement {
  static observedAttributes = ['src', 'alt', 'ratio', 'loading'];
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <style>
        :host { display:block; aspect-ratio: var(--r, 16/9); background:#f3f4f6;
                animation: pulse 1.2s infinite; }
        img { width:100%; height:100%; object-fit:cover; opacity:0; transition: opacity .3s; }
        img.ok { opacity:1 } :host { animation:none } .err { padding:8px; }
      </style>
      <img alt="${this.getAttribute('alt') ?? ''}">`;
    this.#img = root.querySelector('img');
    if (this.getAttribute('loading') === 'eager') return this.#load();
    this.#io = new IntersectionObserver((entries) => {
      if (entries.some((e) => e.isIntersecting)) this.#load();
    }, { rootMargin: '200px' });
    this.#io.observe(this);
  }
  #img; #io;
  disconnectedCallback() { this.#io?.disconnect(); this.#io = null; }
  #load() {
    this.#io?.disconnect();
    this.#img.src = this.getAttribute('src') ?? '';
    this.#img.onload = () => { this.#img.classList.add('ok'); this.#img.parentElement.style.animation = 'none'; };
    this.#img.onerror = () => {
      const btn = document.createElement('button');
      btn.className = 'err'; btn.textContent = '加载失败，点击重试';
      btn.onclick = () => { btn.remove(); this.#load(); };
      this.#img.replaceWith(btn);
    };
  }
}
customElements.define('wc-img', WcImg);
```

**评分点**：
- IntersectionObserver rootMargin 提前预载、回调里立即 disconnect（一次性触发）。
- disconnected 中 disconnect observer（泄漏意识）；eager 分支跳过观察。
- aspect-ratio + 占位动画防 CLS；失败态可重试。
- img.onload/onerror 均覆盖，淡入用 class 而非直接改 style 内联动画冲突。
