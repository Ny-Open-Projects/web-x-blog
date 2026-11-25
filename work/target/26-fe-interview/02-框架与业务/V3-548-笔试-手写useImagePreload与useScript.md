---
title: [V3-548] 笔试：手写 useImagePreload 与 useScript（资源加载 composable）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## V3-548：笔试：手写 useImagePreload

**答**：实现：① `useImagePreload(urls)`：批量预加载（并发上限 4），返回 { loaded, progress, failed }；② `useScript(src, { attrs })`：脚本注入（去重：同 src 全局单例 promise——多组件共享加载），返回 { status, load }；③ 失败重试一次；④ 卸载：已注入的 script 不移除（全局副作用），但 pending promise 清理；⑤ useScript 的全局去重 Map（模块级）。写出实现。

```javascript
export function useImagePreload(urls) {
  const loaded = ref(0), failed = ref(0);
  const progress = computed(() => (loaded.value + failed.value) / urls.length);
  const ready = ref(false);

  onMounted(async () => {
    let next = 0;
    const worker = async () => {
      while (next < urls.length) {
        const u = urls[next++];
        try {
          await new Promise((res, rej) => {
            const img = new Image();
            img.onload = res; img.onerror = rej; img.src = u;
          });
          loaded.value++;
        } catch { failed.value++; }
      }
    };
    await Promise.all(Array.from({ length: Math.min(4, urls.length) }, worker));
    ready.value = true;
  });
  return { loaded, failed, progress, ready };
}

const scriptMap = new Map();    // 全局去重: 同 src 共享加载
export function useScript(src, { attrs = {} } = {}) {
  const status = ref(scriptMap.get(src) ? 'done' : 'idle');
  async function load() {
    if (scriptMap.has(src)) { status.value = 'done'; return scriptMap.get(src); }
    const p = new Promise((resolve, reject) => {
      const s = document.createElement('script');
      Object.assign(s, attrs, { src, async: true });
      s.onload = () => resolve(s);
      s.onerror = () => { scriptMap.delete(src); reject(new Error(`script fail: ${src}`)); };
      document.head.appendChild(s);
    });
    scriptMap.set(src, p);                       // 单例 promise
    status.value = 'loading';
    try { await p; status.value = 'done'; }
    catch { status.value = 'error'; throw new Error('script failed'); }
  }
  return { status, load };
}
```

**评分点**：
- 并发上限的批量预加载（游标 worker 模式）
- useScript 模块级 Map 全局去重（多组件共享同一 promise）
- ES 模块解包与失败清理（delete 后可重试）
- 预注入脚本不卸载的全局副作用认知
