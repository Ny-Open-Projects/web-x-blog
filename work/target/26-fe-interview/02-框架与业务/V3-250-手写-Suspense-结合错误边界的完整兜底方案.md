---
title: [V3-250] 手写：Suspense + 错误边界 + 重试的完整兜底方案
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-250：手写：Suspense + 错误边界 + 重试的完整兜底方案
**需求**：封装 `AsyncBoundary` 组件：内部组合 Suspense（依赖等待）+ onErrorCaptured（错误捕获）+ 自动重试（可重试错误指数退避最多 2 次）+ key 重置；要求暴露 loading/error/success 三态回调与 retry 方法。用 h/render 函数实现。
**评分点**：
- onErrorCaptured 返回 false 阻断冒泡的用法
- 重试计数与"不可重试错误"短路（4xx 不重试）
- key 变化驱动子树重建的机制说明
- 三态回调齐全且异常时 error 面板可手动重试

```javascript
import { defineComponent, ref, h } from 'vue';
export const AsyncBoundary = defineComponent({
  name: 'AsyncBoundary',
  props: { maxRetry: { type: Number, default: 2 } },
  setup(props, { slots, emit, expose }) {
    const key = ref(0);
    const errors = ref(0);
    const retriable = (e) => !/^(4\d\d)/.test(String(e.status ?? ''));
    function retry() { errors.value = 0; key.value++; emit('loading'); }
    expose({ retry });
    onErrorCaptured((err) => {
      emit('error', err);
      if (retriable(err) && errors.value < props.maxRetry) {
        errors.value++;
        setTimeout(retry, 2 ** errors.value * 500); // 指数退避：500ms/1s
        return false;                                // 阻断冒泡，本边界消化
      }
      return true; // 超限继续上抛到全局兜底
    });
    return () => h('div', { class: 'async-boundary', key: key.value }, [
      h(resolveComponent('Suspense'), null, {
        default: () => slots.default?.(),
        fallback: () => slots.fallback?.() ?? h('div', '加载中…'),
      }),
    ]);
  },
});
// 使用
// <AsyncBoundary @loading="..." @error="(e) => ...">
//   <template #default><Dashboard /></template>
// </AsyncBoundary>
```
