---
title: [V3-545] 笔试：手写 usePolling（自适应间隔轮询 composable）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## V3-545：笔试：手写 usePolling

**答**：实现 `usePolling(fetcher, { interval, backoff, maxInterval })`：① 立即拉取一次后按 interval 轮询；② 失败指数退避（interval × 2^n，封顶 maxInterval），成功重置；③ 页面隐藏暂停、恢复立即执行一次；④ 组件卸载停止；⑤ 暴露 error/lastResult/attemptCount。写出实现。

```javascript
export function usePolling(fetcher, { interval = 5000, maxInterval = 60_000 } = {}) {
  const lastResult = ref(null);
  const error = ref(null);
  const attemptCount = ref(0);
  let timer = null, fails = 0, stopped = false;

  async function tick(immediate = false) {
    if (stopped) return;
    try {
      lastResult.value = await fetcher();
      error.value = null;
      fails = 0;                                    // 成功重置退避
    } catch (e) {
      error.value = e;
      fails++;
      attemptCount.value++;
    }
    const delay = Math.min(interval * 2 ** fails, maxInterval);
    timer = setTimeout(() => tick(), delay);
  }
  function start() { stopped = false; tick(true); }
  function stop() { stopped = true; clearTimeout(timer); }

  onScopeDispose(stop);
  // 页面隐藏暂停 / 恢复立即执行
  useEventListener(document, 'visibilitychange', () => {
    if (document.hidden) { clearTimeout(timer); }
    else if (!stopped) tick(true);
  });
  if (immediateDefault()) start();
  return { lastResult, error, attemptCount, start, stop };
}
function immediateDefault() { return true; }
```

**评分点**：
- 失败指数退避 + 成功重置 + maxInterval 封顶
- 页面隐藏暂停 / 恢复立即拉取
- attemptCount 与 error 响应式暴露
- 卸载清理与 stopped 状态机
