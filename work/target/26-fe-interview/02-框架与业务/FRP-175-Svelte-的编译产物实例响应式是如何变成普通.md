---
title: [FRP-175] Svelte 的编译产物实例：响应式是如何变成"普通赋值"的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-175：Svelte 的编译产物实例：响应式是如何变成"普通赋值"的？

**答**：
- Svelte 组件编译成普通 JS 函数：模板变成 `create_fragment` 返回的 mount/update/unmount 操作集，响应式变量是**普通的局部变量**（存在 ctx 数组里）。
- 关键产物是 `$$invalidate`：编译器知道**每个赋值点**（`count++`），直接在赋值后插入失效调用——标记 dirty、调度更新（微任务批量）。
- `$: doubled = count * 2` 编译为 update 函数里重新计算 + dirty 比对——没有 Proxy、没有依赖收集，**编译期静态知道所有依赖**。
- 这就是"编译时框架"的本质：把运行时框架的 track/trigger 全部替换成编译期插桩。

```javascript
// 简化实现，帮助理解 Svelte 产物
// —— 输入（.svelte） ——
// <script>
//   let count = 0;
//   $: doubled = count * 2;
//   const inc = () => count++;
// </script>
// <button on:click={inc}>{count} / {doubled}</button>

// —— 编译产物（简化） ——
function instance($$self, $$props, $$invalidate) {
  let count = 0;                                  // 普通变量！没有 Proxy/ref
  const inc = () => $$invalidate(0, count++, count);  // 每个赋值点都被插桩
  return [count, inc];
}

function create_fragment(ctx) {
  let button, t0, t1, t2_value, mounted;
  return {
    c() {  // create：一次性建 DOM
      button = element('button');
      t0 = text('');
      t1 = text(' / ');
      t2 = text('');
    },
    m(target, anchor) {  // mount
      mount(button, target, anchor);
      mounted = listen(button, 'click', ctx[1]);
    },
    p(ctx, [dirty]) {  // update：dirty 位图决定更新哪些节点
      if (dirty & /*count*/ 1 && t0_value !== (t0_value = ctx[0])) {
        set_data(t0, t0_value);                    // 只更新变化的文本节点
      }
      if (dirty & /*count*/ 1 && t2_value !== (t2_value = ctx[0] * 2)) {
        set_data(t2, t2_value);                    // $: 依赖在编译期已知 = count
      }
    },
    d(detaching) { /* unmount + 移除监听 */ }
  };
}

// —— $$invalidate 的核心 ——
let dirty = 0;
function $$invalidate(i, value) {
  if (dirty & (1 << i)) return value;             // 已脏：跳过
  dirty |= 1 << i;                                 // 标记第 i 个变量脏
  schedule_update(() => {                          // 微任务批量
    const mask = dirty; dirty = 0;
    fragment.p(ctx, mask);                         // 按 dirty 位图精准更新
  });
  return value;
}
// 对比 Vue：Proxy get/set 运行时收集；Svelte：编译期就写死了"哪个赋值影响哪些节点"
```
