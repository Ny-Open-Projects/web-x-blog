---
title: [JS-139] 手写完整版 debounce？immediate 与 cancel 怎么加？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-139：手写完整版 debounce？immediate 与 cancel 怎么加？

**答**：
- 基础版：每次触发清掉旧定时器重设，静默 wait 后执行，this 与参数透传。
- immediate：首次触发立即执行，之后 wait 内的调用被吞；定时器到期必须把 timer 置 null，否则永远无法再次立即触发。
- cancel：清定时器并复位状态，用于组件卸载等场景防止“迟到执行”。
- 附加 flush：跳过等待立即执行挂起的最后一次调用（可选增强）。

```javascript
function debounce(fn, wait = 300, { immediate = false } = {}) {
  let timer = null;

  function debounced(...args) {
    const callNow = immediate && timer === null; // 立即版：仅在"空闲期"首次触发
    if (timer) clearTimeout(timer);
    timer = setTimeout(() => {
      timer = null;                              // 复位，下一次才能再次立即触发
      if (!immediate) fn.apply(this, args);      // 普通版：静默期结束后执行最后一次
    }, wait);
    if (callNow) fn.apply(this, args);           // 立即版：先执行再进入冷却
  }

  debounced.cancel = () => {
    clearTimeout(timer);
    timer = null;                                // 复位状态，组件卸载防泄漏
  };
  debounced.flush = function (...args) {
    debounced.cancel();
    fn.apply(this, args);                        // 跳过等待直接执行
  };
  return debounced;
}

// 立即版演示：按钮防重复提交
const submit = debounce((tag) => console.log('提交', tag), 500, { immediate: true });
submit('a');          // 立即输出 提交 a
submit('b');          // 500ms 冷却期内，被吞
setTimeout(() => submit('c'), 600); // 冷却已过 → 立即输出 提交 c

// 普通版 + cancel：输入框搜索
const search = debounce((kw) => console.log('搜索', kw), 300);
search('j'); search('ja'); search('jav');
search.cancel();      // 用户离开页面 → 取消挂起的调用
// 300ms 后无输出
```
