---
title: [FRP-182] 手写 defineAsyncComponent：loading / error / retry 完整实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-182：手写 defineAsyncComponent：loading / error / retry 完整实现？

**答**：
- 状态机：`pending → loading（delay 后）→ resolved | error`；retry 是 error 分支的计数重试（attempts < retries 时递归 load）。
- 细节一：delay 控制 loading 组件出现——resolve 比 delay 快就不闪 loading（定时器可取消）。
- 细节二：resolved 后要**递归解析**嵌套异步组件（loader 返回的还是异步组件时继续 load）。
- 细节三：comp resolution 后挂到 instance 上触发自身重渲，把占位替换为真组件（见 FRP-070 的渲染器配合）。

```javascript
// 简化实现，帮助理解 defineAsyncComponent
function defineAsyncComponent(options) {
  if (typeof options === 'function') options = { loader: options };
  const {
    loader, loadingComponent, errorComponent,
    delay = 200, timeout, retries = 3, retryDelay = 100,
    onError,   // 自定义重试决策：(err, retry, fail, attempts) => void
  } = options;

  return {
    __async: true,
    setup(props, { slots, expose }) {
      const state = reactive({
        status: 'pending',            // pending | loading | resolved | error
        error: null,
        resolvedComp: null,
      });
      let delayTimer = null, timeoutTimer = null;

      async function load() {
        state.status = state.status === 'pending' ? 'pending' : 'loading';
        clearTimeout(delayTimer);
        delayTimer = setTimeout(() => {
          if (state.status === 'pending') state.status = 'loading';  // delay 后才显示 loading
        }, delay);
        if (timeout) {
          timeoutTimer = setTimeout(() => {
            if (state.status !== 'resolved') fail(new Error('加载超时'));
          }, timeout);
        }
        try {
          const comp = await loader();
          clearTimeout(timeoutTimer);
          state.resolvedComp = isAsyncComp(comp) ? await loadNested(comp) : comp; // 递归解析
          state.status = 'resolved';
        } catch (err) {
          handleError(err, 0);
        } finally {
          clearTimeout(delayTimer);
        }
      }

      function handleError(err, attempts) {
        clearTimeout(timeoutTimer);
        if (onError) {
          onError(err, () => retry(attempts), () => fail(err), attempts);
        } else if (attempts < retries) {
          retry(attempts);
        } else {
          fail(err);
        }
      }
      function retry(attempts) {
        setTimeout(() => loader().then(c => { state.resolvedComp = c; state.status = 'resolved'; })
          .catch(e => handleError(e, attempts + 1)), retryDelay); // 指数退避可在此扩展
      }
      function fail(err) {
        state.error = err;
        state.status = 'error';
      }
      load();

      expose({ retry: () => handleError(state.error, 0) });  // 外部可手动重试

      return () => {
        switch (state.status) {
          case 'resolved': return h(state.resolvedComp, props, slots);   // 真组件
          case 'error':    return errorComponent ? h(errorComponent, { error: state.error, retry: () => handleError(state.error, 0) }) : null;
          case 'loading':  return loadingComponent ? h(loadingComponent) : null;
          default:         return null;   // pending：延迟窗口内无占位（不闪 loading）
        }
      };
    }
  };
}
// 用法：
// const Chart = defineAsyncComponent({
//   loader: () => import('./Chart.vue'),
//   loadingComponent: Spinner, errorComponent: ErrBox,
//   delay: 200, timeout: 5000, retries: 2,
//   onError: (err, retry, fail, n) => (err.status === 503 && n < 5) ? retry() : fail(err),
// });
```
