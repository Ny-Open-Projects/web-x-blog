---
title: [H5-098] 自定义元素"升级"是怎么回事？customized built-in element 现状如何？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-098：自定义元素"升级"是怎么回事？customized built-in element 现状如何？
**答**：
- 升级：元素标签先于 `customElements.define` 出现在文档中，define 之后浏览器把它**补建成**自定义元素实例（调用 constructor），`customElements.whenDefined` 可等待。
- `customElements.get(name)` 查已注册类；`upgrade(node)` 手动补升；define 前的元素是 `HTMLUnknownElement` 或普通 HTMLElement。
- customized built-in（`is="my-button"` 扩展原生 button）**Safari 拒绝实现**，兼容性不可用；跨浏览器方案是 wrapper（普通自定义元素内包原生控件）。
- constructor 约束：不能访问 attributes/子元素（升级时属性还没就绪），只做 shadowRoot 挂载；把 DOM 相关逻辑放 `connectedCallback`。
- 重复 define 同名/同 tag 会抛错，多入口 bundle 需守卫 `if (!customElements.get(name))`。

```html
<my-card title="先写标签，后定义"></my-card>
<button is="count-btn">native-is 扩展（Safari 不支持）</button>

<script>
  // 防重复注册守卫：多 chunk 打包场景必备
  if (!customElements.get('my-card')) {
    customElements.define('my-card', class extends HTMLElement {
      constructor() {
        super();
        console.log('升级：constructor 只建 shadow');
        this.attachShadow({ mode: 'open' }).innerHTML = `
          <div class="card"><slot></slot>
            <b class="t"></b></div>`;
      }
      connectedCallback() {
        // 属性读取放这里：constructor 阶段 attribute 未就绪
        this.shadowRoot.querySelector('.t').textContent = this.getAttribute('title') ?? '';
      }
    });
  }

  // 升级时序演示
  console.log(customElements.get('my-card'));  // class（已注册）
  customElements.whenDefined('my-card').then(() => {
    document.querySelectorAll('my-card').forEach(el =>
      console.log('确认升级完成：', el.shadowRoot !== null));
  });

  // 手动升级游离节点（innerHTML 里的未定义标签）
  const tmp = document.createElement('div');
  tmp.innerHTML = '<my-card title="手动升级"></my-card>';
  customElements.upgrade(tmp.firstElementChild);
</script>
```
