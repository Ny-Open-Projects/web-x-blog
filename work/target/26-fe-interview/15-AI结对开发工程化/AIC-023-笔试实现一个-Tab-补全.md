---
title: [AIC-023] 笔试：实现一个简单的 Tab 补全节流器，模拟 IDE 补全请求的去抖与取消逻辑？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-023：笔试：实现一个简单的 Tab 补全节流器，模拟 IDE 补全请求的去抖与取消逻辑？
**题目**：实现 `createCompletionEngine({ debounceMs, fetch })`，返回 `onType(text)` 与 `dispose()`。要求：输入去抖后再请求；新请求发出前取消上一个未完成请求（AbortController）；dispose 后一切静默。20 行以内核心逻辑。

```typescript
function createCompletionEngine(opts: { debounceMs: number; fetch: (text: string, signal: AbortSignal) => Promise<string[]> }) {
  let timer: ReturnType<typeof setTimeout> | null = null;
  let ctrl: AbortController | null = null;
  let disposed = false;

  function onType(text: string) {
    if (disposed) return;
    if (timer) clearTimeout(timer);
    timer = setTimeout(async () => {
      ctrl?.abort();                     // 取消上一轮
      ctrl = new AbortController();
      try {
        const items = await opts.fetch(text, ctrl.signal);
        if (!ctrl.signal.aborted && !disposed) render(items);
      } catch (e: unknown) {
        if ((e as Error)?.name !== 'AbortError') throw e; // 取消不算错误
      }
    }, opts.debounceMs);
  }

  function dispose() {
    disposed = true;
    if (timer) clearTimeout(timer);
    ctrl?.abort();
  }
  return { onType, dispose };
}

// 模拟渲染占位
function render(items: string[]) { console.log('suggest:', items.slice(0, 3)); }

const engine = createCompletionEngine({ debounceMs: 200, fetch: async t => [`const ${t}`, `let ${t}`] });
engine.onType('goods'); engine.onType('goodsL'); // 第二次会取消/覆盖第一次的计时
setTimeout(() => engine.dispose(), 1000);
```
**评分点**：
- 去抖实现正确（清旧 timer 再设新 timer），能说出与节流的区别更好。
- 请求竞态处理：AbortController + `signal.aborted` 双检查（返回后再查一次防「取消已生效但响应已到」）。
- catch 里区分 AbortError 与真实错误，不能把取消当异常上报。
- dispose 覆盖三处：timer、in-flight 请求、后续 onType 全部短路。
