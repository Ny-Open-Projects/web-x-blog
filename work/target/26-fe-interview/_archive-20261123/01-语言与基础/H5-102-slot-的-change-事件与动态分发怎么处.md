---
title: [H5-102] slot 的 change 事件与动态分发怎么处理？被分发节点归属谁？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-102：slot 的 change 事件与动态分发怎么处理？被分发节点归属谁？
**答**：
- `<slot>` 是"投影占位"：**被分发节点始终属于 light DOM**（事件冒泡起点、样式来源都是原始位置），slot 只决定"显示在哪"。
- `slotchange` 事件在**分配结果变化**时触发（增删节点、slot 属性改名、display:none 不算），`event.target.assignedElements/nodes` 拿到当前分发内容。
- 动态分发典型用途：tabs 组件监听新增 tab 并自动注册、列表组件对新子项补 class、校验 slot 内容合法性并告警。
- 反向查询：`element.assignedSlot` 查自己被分到哪个 slot；`slot.assignedElements({ flatten: true })` 含 fallback 内容。
- fallback：slot 标签内的子节点是"空位默认内容"，有分发内容时不渲染。

```html
<my-tabs>
  <button slot="tab">第一个</button>
  <button slot="tab">第二个</button>
  <section slot="panel">面板 A</section>
  <section slot="panel">面板 B</section>
</my-tabs>

<script>
  customElements.define('my-tabs', class extends HTMLElement {
    connectedCallback() {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <div class="tabbar"><slot name="tab"></slot></div>
        <slot name="panel"></slot>
        <slot>无内容时的默认文案</slot>`;

      // 监听分配变化：外部动态增删 tab 时自动感知
      const tabSlot = this.shadowRoot.querySelector('slot[name=tab]');
      tabSlot.addEventListener('slotchange', (e) => {
        const tabs = e.target.assignedElements();
        console.log('当前 tab 数：', tabs.length);
        tabs.forEach((tab, i) => {
          tab.classList.toggle('active', i === 0);
          tab.addEventListener('click', () => this.show(i));
        });
      });

      // 动态新增 tab：slotchange 会再次触发
      setTimeout(() => {
        const b = document.createElement('button');
        b.slot = 'tab';
        b.textContent = '第三个（JS 追加）';
        this.appendChild(b);
      }, 1000);
    }
    show(i) {
      this.querySelectorAll('[slot=panel]').forEach((p, idx) =>
        p.hidden = idx !== i);
    }
  });
</script>

<script>
  // 反向查询：light DOM 元素查自己被分到哪
  const btn = document.querySelector('my-tabs button');
  setTimeout(() => console.log('被分到：', btn.assignedSlot?.name), 500);
</script>
```
