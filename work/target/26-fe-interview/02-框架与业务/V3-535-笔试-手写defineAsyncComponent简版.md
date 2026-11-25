---
title: [V3-535] 笔试：手写 defineAsyncComponent 简版
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 编译器]
type: 笔试题
---

## V3-535：笔试：手写 defineAsyncComponent

**答**：实现 `defineAsyncComponent(loader, { loadingComponent, errorComponent, delay, timeout, retry })`：① 首次渲染显示 loading（delay 后才显示，防闪烁）；② loader resolve 后缓存组件（后续渲染同步）；③ reject 后显示 errorComponent + retry 重试；④ timeout 超时按错误处理；⑤ loader 结果支持 ES 模块（.default 解包）。写出实现。

```javascript
function defineAsyncComponent(loader, {
  loadingComponent, errorComponent, delay = 200, timeout = 0, retry = 1,
} = {}) {
  let resolvedComp = null, attempts = 0;

  return {
    name: 'AsyncComponentWrapper',
    setup(_, { slots }) {
      const state = ref(resolvedComp ? 'resolved' : 'loading');
      const comp = ref(resolvedComp);
      const showLoading = ref(false);
      let delayTimer, timeoutTimer;

      const load = async () => {
        state.value = 'loading';
        if (delay) delayTimer = setTimeout(() => showLoading.value = true, delay);
        if (timeout) timeoutTimer = setTimeout(() => fail(new Error('timeout')), timeout);
        try {
          let mod = await loader();
          clearTimeout(timeoutTimer);
          if (mod && mod.__esModule && mod.default) mod = mod.default;  // ES 模块解包
          resolvedComp = comp.value = mod;
          state.value = 'resolved';
        } catch (e) {
          clearTimeout(timeoutTimer);
          fail(e);
        } finally { clearTimeout(delayTimer); showLoading.value = false; }
      };
      const fail = async (e) => {
        if (attempts++ < retry) return load();          // 重试
        state.value = 'error'; state.error = e;
      };
      if (state.value === 'loading') load();

      return () => {
        if (state.value === 'resolved') {
          const c = comp.value;
          return h(c, null, { default: () => slots.default?.() });  // 透传插槽
        }
        if (state.value === 'error' && errorComponent) return h(errorComponent, { retry: load });
        if (showLoading.value && loadingComponent) return h(loadingComponent);
        return null;                                     // delay 前: 渲染占位(null)
      };
    },
  };
}
```

**评分点**：
- delay 前不显示 loading（防闪烁）与 timeout 超时竞速
- resolved 缓存（二次渲染同步，不再 loader）
- ES 模块 default 解包
- retry 计数与插槽透传
