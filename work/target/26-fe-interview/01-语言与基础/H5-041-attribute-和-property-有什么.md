---
title: [H5-041] attribute 和 property 有什么区别？组件该暴露哪个？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-041：attribute 和 property 有什么区别？组件该暴露哪个？
**答**：
- attribute 是 HTML 标签上的字符串特性，property 是 JS 对象上的属性；同名的 `value` 等在 input 上初始同步、后续互不自动跟随。
- attribute 只能是字符串，property 可以是任意类型（数组、对象、函数、布尔）。
- Web Components 惯例：attribute 承载初始声明（HTML 里写），property 承载复杂状态；复杂值只暴露 property，简单值两者同步。
- 需要响应 attribute 变化就把名字加进 `observedAttributes`；property 变化要自己写 setter。

```javascript
class MyChart extends HTMLElement {
  static observedAttributes = ['title'];

  constructor() {
    super();
    this._data = []; // 复杂状态走 property
  }

  get data() {
    return this._data;
  }
  set data(val) {
    this._data = val;
    this.render(); // property setter 里同步视图
  }

  attributeChangedCallback(name, oldV, newV) {
    if (name === 'title') this.render(); // attribute 变化走回调
  }

  render() {
    this.textContent = `${this.getAttribute('title') ?? ''} ${this._data.length} 条数据`;
  }
}
customElements.define('my-chart', MyChart);
```

```html
<!-- attribute：字符串，适合声明式初始值 -->
<my-chart title="月活跃用户"></my-chart>

<script>
  const chart = document.querySelector('my-chart');

  // property：任意类型，适合复杂状态
  chart.data = [12, 30, 45]; // 触发 setter 渲染
  chart.setAttribute('title', '日活跃用户'); // 触发 attributeChangedCallback

  // 经典差异案例：input 的 value
  const input = document.querySelector('input');
  // input.value = 'b'（property 变了）不会改变 HTML 的 value attribute
  // getAttribute('value') 永远是 HTML 里的初始值，property 才是当前值
</script>
<input value="a" />
```
