---
title: [RBL-645] 构建中间产物快照：为什么「能看到每一步的输入输出」是调试刚需
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-645：构建中间产物快照：为什么「能看到每一步的输入输出」是调试刚需

**答**:
- 构建器调试的最大痛点是「黑盒」：用户拿到最终产物错误，无法知道错在哪个 pass（哪个插件改坏了代码）——中间产物快照（每 pass 的输入/输出代码 + map）是定位手段，等价于「构建管线的时间旅行调试」。
- 快照设计：1) **按需开启**（debug 模式，全量快照体积爆炸——一个 1MB 模块 × 10 pass × 1000 模块 = 10GB）；2) 模块级过滤（只快照指定模块/含关键词的代码）；3) 快照结构 `{ module, pass, before, after, map, duration }`，输出到目录树（`.rolldown-debug/module-id/01-load.js`）供 IDE 打开对比。
- 事后 diff 诊断：两个快照间 diff（`diff 01-load.js 02-transform.js`）直接显示插件改动——「哪个插件引入了 undefined」一目了然；配合「禁用单个插件重跑」的 bisect（插件二分），定位故障插件 O(log n)。
- 与 sourcemap 链的关系：快照保留各 pass 的 map，可以在最终产物错误位置上**逐级反解**到最早出错的位置（哪一 pass 的 map 变换开始「错位」）——这是 sourcemap 链调试的实战形态。
- 追问钩子：为什么不能总是开着快照？——内存与 IO 成本；折中方案是「环形缓冲快照」（只保留最近 N 个模块的快照）+ 错误触发时自动 dump 相关模块链——把成本控制在「出错时才付」。

```javascript
// pass 级快照收集器
class Snapshot {
  #on; #root; #filter;
  constructor({ on = process.env.BUILD_DEBUG === '1', root = '.build-debug', filter } = {}) {
    this.#on = on; this.#root = root; this.#filter = filter;
  }
  record(mod, pass, before, after, map, ms) {
    if (!this.#on) return;
    if (this.#filter && !this.#filter.test(mod.id)) return;
    const dir = `${this.#root}/${mod.id.replace(/[^\w]/g, '_')}`;
    fs.mkdirSync(dir, { recursive: true });
    const idx = String(this.seq(dir)).padStart(2, '0');
    fs.writeFileSync(`${dir}/${idx}-${pass}.in.js`, before);
    fs.writeFileSync(`${dir}/${idx}-${pass}.out.js`, after);
    if (map) fs.writeFileSync(`${dir}/${idx}-${pass}.map`, JSON.stringify(map));
    fs.appendFileSync(`${dir}/_profile.txt`, `${idx} ${pass} ${ms}ms\n`);
  }
}

// 插件二分：禁用一半插件重跑直到定位
async function bisectPlugin(baseline, plugins, run) {
  let pool = [...plugins];
  while (pool.length > 1) {
    const half = pool.slice(Math.floor(pool.length / 2));
    const out = await run(pool.filter(p => !half.includes(p)));
    if (out.bad) pool = pool.filter(p => half.includes(p));
    else pool = half;
  }
  return pool[0];                                        // 嫌疑插件
}
```
