---
title: [WCN-057] 笔试：手写 scrollspy 侧边导航 WC（IntersectionObserver 联动高亮）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-057：笔试：手写 scrollspy 侧边导航 WC

**题目**：`<scroll-spy target="#doc">`：① 观察 `target` 容器内所有 `h2[id]`；② 滚动时当前章节对应的导航项高亮（`aria-current`）；③ 点击导航平滑滚动到对应章节；④ 交叉变化时只取"视口顶部最近"的标题；⑤ disconnected 清理。

**答**：

```javascript
class ScrollSpy extends HTMLElement {
  static observedAttributes = ['target'];
  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML =
        '<nav part="nav"></nav>';
      this.#nav = this.shadowRoot.querySelector('nav');
    }
    this.#build();
  }
  #nav; #io; #items = [];
  #build() {
    const host = document.querySelector(this.getAttribute('target'));
    if (!host) return;
    const heads = [...host.querySelectorAll('h2[id]')];
    this.#nav.innerHTML = '';
    this.#items = heads.map((h) => {
      const a = document.createElement('a');
      a.href = `#${h.id}`;
      a.textContent = h.textContent;
      a.onclick = (e) => { e.preventDefault(); h.scrollIntoView({ behavior: 'smooth' }); };
      this.#nav.append(a);
      return { h, a };
    });
    this.#io?.disconnect();
    this.#io = new IntersectionObserver((entries) => {
      if (!entries.some((e) => e.isIntersecting)) return;
      // 取视口顶部最近的标题：boundingClientRect.top 最接近 0 且 <=0 或最小的正值
      const visible = entries.filter((e) => e.isIntersecting)
        .sort((x, y) => Math.abs(x.boundingClientRect.top) - Math.abs(y.boundingClientRect.top))[0];
      const hit = this.#items.find((it) => it.h === visible.target);
      if (!hit) return;
      this.#items.forEach(({ a }) => a.removeAttribute('aria-current'));
      hit.a.setAttribute('aria-current', 'location');
    }, { rootMargin: '-20% 0px -70% 0px' });   // 顶部收窄判定带
    heads.forEach((h) => this.#io.observe(h));
  }
  disconnectedCallback() { this.#io?.disconnect(); }
}
customElements.define('scroll-spy', ScrollSpy);
```

**评分点**：
- rootMargin 上下收窄构造"判定带"，比全视口判定准确。
- 多标题同时交叉时按 top 距离取最近（算法意识）。
- `aria-current="location"` 语义正确；点击 preventDefault + smooth scroll。
- rebuild 前先 disconnect 旧 observer（target 属性变更场景）。
- disconnected 清理。
