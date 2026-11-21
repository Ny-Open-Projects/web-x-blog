---
title: [H5-100] 事件的 retarget 与 composedPath 是什么？如何在宿主侧拿到 shadow 内的真实点击目标？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-100：事件的 retarget 与 composedPath 是什么？如何在宿主侧拿到 shadow 内的真实点击目标？
**答**：
- shadow 边界上冒泡的事件发生 **retarget**：宿主外监听时 `event.target` 永远是宿主元素（内部元素被"隐藏"），这是封装隐私的机制。
- `event.composed` 为 true 的事件才能**穿越**边界（click、input、keydown 等 UI 事件）；`focus/blur/mouseenter` 是 false，替代品是 `focusin/focusout/mouseenter 的 composed 版`（focusin composed 为 true）。
- `event.composedPath()` 返回真实传播路径数组（含 shadow 内节点），**宿主侧监听器里调用它**即可拿到真实目标做委托。
- 自定义事件默认 composed: false，需要跨边界时 `new CustomEvent(evt, { composed: true, bubbles: true })`。
- 判断组件内部结构是否被窥探：composedPath 在 mode: 'closed' 的 shadow 外部调用只返回 `[host, ...]`。

```html
<user-list></user-list>

<script>
  customElements.define('user-list', class extends HTMLElement {
    connectedCallback() {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <ul>
          <li data-id="1">张三</li>
          <li data-id="2">李四</li>
        </ul>`;
      // 组件内部：直接委托，正常 target
      this.shadowRoot.addEventListener('click', (e) => {
        console.log('内部视角 target：', e.target.textContent); // 张三
      });
    }
  });
</script>

<script>
  // 宿主侧：target 被 retarget 成组件本身
  document.querySelector('user-list').addEventListener('click', (e) => {
    console.log('外部视角 target：', e.target.tagName);       // USER-LIST
    console.log('retarget 了：', e.target !== e.composedPath()[0]);

    // composedPath 第 0 项是真实点击的节点（open shadow 可见）
    const real = e.composedPath()[0];
    if (real.matches?.('li')) {
      console.log('真实目标：', real.dataset.id, real.textContent);
    }
  });

  // 跨边界派发自定义事件：必须 composed + bubbles
  customElements.define('send-box', class extends HTMLElement {
    connectedCallback() {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <button>发送</button>`;
      this.shadowRoot.querySelector('button').onclick = () => {
        this.dispatchEvent(new CustomEvent('send', {
          detail: { text: 'hi' },
          bubbles: true,       // 能沿 DOM 冒泡
          composed: true,      // 能穿越 shadow 边界
        }));
      };
    }
  });
  document.addEventListener('send', (e) => console.log('收到：', e.detail.text));
</script>
```
