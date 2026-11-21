---
title: [WCN-035] 笔试：手写一个 attribute 驱动的 Tabs 标签页组件（slot + 事件 + 样式隔离）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-035：笔试：手写一个 attribute 驱动的 Tabs 标签页组件

**题目**：`<wc-tabs active="1">`，light DOM 子节点为 `<section data-tab="标题">内容</section>`。要求：① 影子树渲染 tab 头部（点击切换）与内容区（用 slot 分配对应 section）；② `active` attribute 变化同步切换；③ 派发 composed 的 `wc-tab-change` 事件（detail.index）；④ 键盘左右键支持；⑤ 只显示激活 section。

**答**：

```javascript
class WcTabs extends HTMLElement {
  static observedAttributes = ['active'];
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `
      <style>
        [role=tab]{padding:6px 14px;border:0;background:none;cursor:pointer}
        [role=tab][aria-selected=true]{border-bottom:2px solid #2563eb;font-weight:600}
        section{display:none} section.on{display:block}
      </style>
      <div role="tablist" part="tabs"></div>
      <div part="panels"><slot id="panels"></slot></div>`;
    this.#root = root;
    this.#build();
    // 子节点后到/变化时重建（slotchange 触发时机在解析完成后）
    root.getElementById('panels').addEventListener('slotchange', () => this.#build());
  }
  #root;
  #build() {
    const panels = [...this.querySelectorAll(':scope > section')];
    const active = Math.min(Number(this.getAttribute('active')) | 0, panels.length - 1);
    const list = this.#root.querySelector('[role=tablist]');
    list.innerHTML = '';
    panels.forEach((p, i) => {
      const tab = document.createElement('button');
      tab.role = 'tab';
      tab.textContent = p.dataset.tab ?? `Tab ${i + 1}`;
      tab.setAttribute('aria-selected', String(i === active));
      tab.addEventListener('click', () => this.#select(i));
      list.append(tab);
      p.classList.toggle('on', i === active);       // 直接控制 light DOM section
    });
    this.#root.querySelector('[role=tablist]').addEventListener('keydown', (e) => {
      if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
      const next = (active + (e.key === 'ArrowRight' ? 1 : panels.length - 1)) % panels.length;
      this.#select(next);
    });
  }
  #select(i) {
    if (String(i) === this.getAttribute('active')) return;
    this.setAttribute('active', String(i)); // 触发 attributeChanged → 重建
    this.dispatchEvent(new CustomEvent('wc-tab-change', {
      bubbles: true, composed: true, detail: { index: i },
    }));
  }
  attributeChangedCallback() { if (this.#root) this.#build(); }
}
customElements.define('wc-tabs', WcTabs);
```

**评分点**：
- slotchange 兜底子节点解析时序（HTML 解析时 section 未就绪）。
- active 变化单一数据源：点击只 setAttribute，由 attributeChanged 驱动重建（避免双份状态）。
- `aria-selected`/role 语义与键盘循环导航。
- 事件 composed + detail.index 且值未变时不重复派发。
- 切换用 class 控制显示（visibility 保留 DOM，不重建内容）。
