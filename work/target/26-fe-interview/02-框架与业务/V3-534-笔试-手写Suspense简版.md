---
title: [V3-534] 笔试：手写 Suspense 简版
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 编译器]
type: 笔试题
---

## V3-534：笔试：手写 Suspense 简版

**答**：实现 `MySuspense` 组件：① default slot 内组件的 async setup() 产生 Promise——通过组件实例的 asyncDep 标记收集；② 收集所有 pending 依赖，全 resolve 后切换显示真实内容；③ 未就绪显示 fallback；④ 超时（timeout prop）后强制切换 fallback；⑤ resolve/fallback 事件 emit。写出实现（利用 getCurrentInstance 的 asyncDep 机制简化）。

```javascript
import { ref, h, onMounted, getCurrentInstance } from 'vue';

const MySuspense = {
  name: 'MySuspense',
  props: { timeout: Number },
  emits: ['resolve', 'fallback'],
  setup(props, { slots, emit }) {
    const pendingDeps = [];
    const ready = ref(false);
    const inst = getCurrentInstance();

    // 简化: 约定子组件在 setup 里调用 registerAsync(promise)
    provideRegister();
    function provideRegister() {
      inst.provides.registerAsync = (p) => pendingDeps.push(p);
    }
    onMounted(() => {
      if (!pendingDeps.length) { ready.value = true; emit('resolve'); return; }
      let timer;
      if (props.timeout) timer = setTimeout(() => {
        if (!ready.value) { ready.value = true; emit('fallback'); }
      }, props.timeout);
      Promise.all(pendingDeps.map(p => Promise.resolve(p).catch(() => {})))
        .then(() => {
          clearTimeout(timer);
          ready.value = true;
          emit('resolve');
        });
    });
    return () => ready.value ? slots.default() : slots.fallback?.();
  },
};
// 子组件:
// const inst = getCurrentInstance();
// inst.provides.registerAsync?.(asyncLoadData());
```

**评分点**：
- 异步依赖收集机制（registerAsync 约定 / asyncDep 标记）
- 全部 resolve 才切换（原子出现，无中间态）
- timeout 强制 fallback 的竞速
- resolve/fallback 事件与错误兜底（catch 防悬挂）
