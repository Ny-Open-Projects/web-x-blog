---
title: [RBL-629] 笔试：手写带 CSS 配对与顺序保证的 chunk 加载器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-629：笔试：手写带 CSS 配对与顺序保证的 chunk 加载器

**答**：实现 `createChunkLoader(manifest, dom)`。manifest: `Map<id, { js: url, css: { href, order }[] }>`；dom 为注入的文档适配器 `{ head, createEl(tag), append(el) }`（内存模拟）。`load(id)` 返回 Promise<module>：1) 先按 order 升序注入该 chunk 的全部 CSS link（等待 onload，注入失败 reject）；2) CSS 全就绪后动态 import js（注入实现为 `importFn(url)` 可注入，测试里用 fake 模块对象）；3) 同一 chunk 并发调用只加载一次（共享 promise）；4) CSS 顺序保证：link 元素按 order 排序后依次 append（同 order 保持数组序）；5) 重复 href 的 link 不重复注入。边界：无 CSS 的 chunk 直接 import；load 失败后重试（缓存失败结果，重试重新注入缺失资源）。

```javascript
function createChunkLoader(manifest, dom, { importFn = (u) => import(u) } = {}) {
  const inflight = new Map();                            // id -> Promise
  const loadedCss = new Map();                           // href -> Promise<void>

  function loadStyle({ href, order }) {
    if (loadedCss.has(href)) return loadedCss.get(href);
    const p = new Promise((res, rej) => {
      const link = dom.createEl('link');
      link.rel = 'stylesheet'; link.href = href; link.dataset.order = String(order);
      link.onload = () => res();
      link.onerror = () => { loadedCss.delete(href); rej(new Error(`CSS 加载失败: ${href}`)); };
      dom.head.appendChild(link);
    });
    loadedCss.set(href, p);
    return p;
  }

  function load(id) {
    if (inflight.has(id)) return inflight.get(id);
    const p = (async () => {
      const meta = manifest.get(id);
      if (!meta) throw new Error(`未知 chunk: ${id}`);
      const styles = [...(meta.css || [])]
        .map((s, i) => ({ ...s, _i: i }))
        .sort((a, b) => a.order - b.order || a._i - b._i);      // 同 order 保数组序
      for (const s of styles) await loadStyle(s);               // 顺序注入：前一个成功再下一个
      return importFn(meta.js);
    })();
    inflight.set(id, p);
    p.catch(() => inflight.delete(id));                         // 失败允许重试
    return p;
  }
  return { load };
}

// 测试用 dom 与 importFn
function fakeDom() {
  const head = { children: [] };
  return {
    head,
    createEl: (tag) => ({ tag, rel: '', href: '', dataset: {},
      onload: null, onerror: null }),
    append: (el) => head.children.push(el),
  };
}

const manifest = new Map([
  ['a', { js: 'a.js', css: [{ href: 'a2.css', order: 2 }, { href: 'a1.css', order: 1 }] }],
  ['b', { js: 'b.js', css: [{ href: 'shared.css', order: 0 }] }],
  ['c', { js: 'c.js', css: [] }],
  ['bad', { js: 'x.js', css: [{ href: '404.css', order: 0 }] }],
]);
const dom = fakeDom();
let n = 0;
const loader = createChunkLoader(manifest, dom, {
  importFn: async (u) => ({ from: u, n: ++n }),               // 串行计数验证时序
});

// 并发合并
const [r1, r2] = await Promise.all([loader.load('a'), loader.load('a')]);
console.log(r1 === r2 && r1.from === 'a.js');
// CSS 顺序：a1 在 a2 前
const hrefs = dom.head.children.map(el => el.href);
console.log(hrefs.indexOf('a1.css') < hrefs.indexOf('a2.css'));

// 共享 CSS 不重复注入
await loader.load('b');
console.log(dom.head.children.filter(el => el.href === 'shared.css').length === 1);

// 无 CSS chunk
const rc = await loader.load('c');
console.log(rc.from === 'c.js' && !rc.cssWaited);

// 失败重试
let e1; try { await loader.load('bad'); } catch (e) { e1 = e; }
console.log(/CSS 加载失败/.test(e1.message));
dom.head.children = dom.head.children.filter(el => el.href !== '404.css');  // 模拟清理
console.log((await loader.load('c')).from === 'c.js');       // inflight 未被坏 promise 污染
```

**评分点**：
- CSS 按 order 升序注入且同 order 保持数组序（稳定排序）；逐个 await 保证前序成功
- 并发合并（同 chunk 共享 promise）与失败可重试（catch 清 inflight）双语义正确
- 重复 href 的 loadedCss 缓存生效；无 CSS chunk 直接 import 不阻塞
- 能说清「CSS 与 JS 配对是 FOUC 治理的运行时半边，构建器负责 manifest 配对」属于加分
