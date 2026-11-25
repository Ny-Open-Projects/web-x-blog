---
title: [V3-250] 手写：Suspense + 错误边界 + 重试的完整兜底方案
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-250：手写：Suspense + 错误边界 + 重试的完整兜底方案
**答**：封装 `AsyncBoundary` 组件：内部组合 Suspense（依赖等待）+ onErrorCaptured（错误捕获）+ 自动重试（可重试错误指数退避最多 2 次）+ key 重置；要求暴露 loading/error/success 三态回调与 retry 方法。用 h/render 函数实现。
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

## 变体与延伸（补充）

**变体与延伸**：

1. onErrorCaptured 返回 true 与 false，差异在什么场景最关键？ → 嵌套三层 AsyncBoundary 时，false 表示本层已消化、不再上抛，局部兜底生效；返回 true 会一路冒到最外层，导致明明是局部失败却整页变错误页。
2. 为什么重试要换 key 而不是只清 error？ → 异步依赖与组件实例绑定，只清 error 会复用失败的 async setup 结果，仍然渲染错误；换 key 才真正销毁重建，重新发起请求。
3. 退避等待期间用户手动点重试怎么处理？ → 先 clearTimeout 掉排队中的重试、重置计数，再 key++；否则会出现两次重建，后到的响应覆盖前面的，状态错乱。
