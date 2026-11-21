---
title: [HW-014] 手写防抖（含 immediate / cancel）
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-014：手写防抖（含 immediate / cancel）

**答**：
- 评分点：闭包保存 timer，每次触发先 clearTimeout 再重设；immediate（leading）模式：第一次立即执行、之后的连续触发在静默期内全部丢弃，静默期过后恢复可触发；cancel 要同时清 timer **并置空变量**（否则 immediate 判断会错乱）；this 与参数都要正确透传（返回普通函数而不是箭头函数，用 `fn.apply(this, args)`）；能说出典型场景：输入搜索、resize 计算、按钮防连点。

```javascript
// ===== 5 分钟速写版 =====
function debounce(fn, wait, immediate = false) {
  let timer = null;
  function debounced(...args) {
    if (timer) clearTimeout(timer);
    if (immediate && !timer) {
      fn.apply(this, args);            // 首次立即执行
    }
    timer = setTimeout(() => {
      timer = null;
      if (!immediate) fn.apply(this, args); // 默认：静默期结束后执行最后一次
    }, wait);
  }
  debounced.cancel = () => { clearTimeout(timer); timer = null; };
  return debounced;
}

// ===== 标准完整版（含边界处理）=====
function debouncePro(fn, wait = 300, { immediate = false, resultCallback } = {}) {
  if (typeof fn !== 'function') throw new TypeError('fn must be a function');
  let timer = null;
  function debounced(...args) {
    if (timer) clearTimeout(timer);
    if (immediate && !timer) {
      const result = fn.apply(this, args);
      typeof resultCallback === 'function' && resultCallback(result);
    }
    timer = setTimeout(() => {
      timer = null;
      if (!immediate) {
        const result = fn.apply(this, args);
        typeof resultCallback === 'function' && resultCallback(result);
      }
    }, wait);
  }
  // cancel：组件卸载 / 路由切换时调用，防止闭包里的 timer 继续触发已销毁逻辑
  debounced.cancel = function () {
    if (timer) { clearTimeout(timer); timer = null; }
  };
  // flush：立即结束等待并执行挂起的调用（表单提交前兜底很有用）
  debounced.flush = function (...args) {
    if (timer) {
      clearTimeout(timer);
      timer = null;
      fn.apply(this, args);
    }
  };
  return debounced;
}
// 使用示例：
// const onSearch = debouncePro(q => fetchList(q), 300, { immediate: false });
// onInput(e => onSearch(e.target.value));
// 组件卸载：onSearch.cancel()
```

---
