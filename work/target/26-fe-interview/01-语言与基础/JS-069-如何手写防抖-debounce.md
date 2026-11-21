---
title: [JS-069] 如何手写防抖 debounce？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-069：如何手写防抖 debounce？

**答**：
- 核心思路：每次触发都重置定时器，停止触发 delay 毫秒后才真正执行。
- 增强一：立即执行版（首次触发马上执行，之后静默）。
- 增强二：返回的函数带 cancel 方法，组件卸载时清理。
- 典型场景：搜索输入联想、resize 计算布局。

```javascript
function debounce(fn, wait = 300, { leading = false } = {}) {
  let timer = null;
  function debounced(...args) {
    if (timer) clearTimeout(timer);
    if (leading && !timer) {
      fn.apply(this, args);           // 首次立即执行
    }
    timer = setTimeout(() => {
      timer = null;
      if (!leading) fn.apply(this, args);
    }, wait);
  }
  debounced.cancel = () => {
    clearTimeout(timer);
    timer = null;
  };
  return debounced;
}

const search = debounce((kw) => console.log('search:', kw), 500);
search('j'); search('js'); search('javascript'); // 500ms 后只输出 javascript

const onResize = debounce(() => console.log('resize'), 200, { leading: true });
window.addEventListener('resize', onResize);
// 卸载时 onResize.cancel();
```
