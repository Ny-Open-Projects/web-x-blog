---
title: [WCN-111] 笔试：手写 Vue 3 的 WC 包装器（v-model 桥 + 事件透传 + 类型声明）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 跨框架复用]
type: 笔试题
---

## WCN-111：笔试：手写 Vue 3 的 WC 包装器

**题目**：实现 Vue 3 包装器 `defineWcBridge(tag, { events })`：① 返回函数式/组合式组件：透传 attrs 到 WC 元素；② `v-model` 支持：监听 WC 的 `input`/自定义事件，detail.value emit 回宿主，同时把 modelValue prop 写回元素 property；③ 事件 kebab-case → camelCase prop（`onTagAdd`）；④ onBeforeUnmount 解绑；⑤ 导出配套的全局组件类型声明写法。

**答**：

```ts
// defineWcBridge.ts
import { defineComponent, h, onBeforeUnmount, onMounted, ref } from 'vue';

export function defineWcBridge(tag, { events = [] } = {}) {
  return defineComponent({
    name: tag.replace(/(^\w|-\w)/g, (s) => s.replace('-', '').toUpperCase()),
    props: { modelValue: { type: null, default: undefined } },
    emits: ['update:modelValue', ...events],
    setup(props, { attrs, emit }) {
      const el = ref(null);
      const unbinders = [];
      onMounted(() => {
        // v-model 双向桥：写回 property
        if (props.modelValue !== undefined && el.value)
          el.value.value = props.modelValue;
        for (const ev of events) {
          const camel = `on${ev[0].toUpperCase()}${ev.slice(1).replace(/-(\w)/g, (_, c) => c.toUpperCase())}`;
          const fn = attrs[camel];
          if (typeof fn === 'function') {
            el.value.addEventListener(ev, fn);
            unbinders.push(() => el.value.removeEventListener(ev, fn));
          }
        }
      });
      onBeforeUnmount(() => unbinders.forEach((u) => u()));
      const onInput = (e) => emit('update:modelValue', e.detail?.value ?? e.target.value);
      return () => h(tag, { ...attrs, ref: el, onInput });
    },
  });
}

// main.ts
import { XSearch } from './bridge';
export const WcSearch = defineWcBridge('x-search', { events: ['search-input'] });

// env.d.ts：全局类型
// declare module 'vue' { export interface GlobalComponents {
//   WcSearch: typeof import('./bridge')['WcSearch'] } }
```

**评分点**：
- v-model 双向桥：modelValue 写回 property + input 事件 emit 上行（两个方向都实现）。
- kebab/camel 事件名转换正确；解绑在 onBeforeUnmount。
- attrs 透传保留（class/style/aria 不丢）。
- GlobalComponents 类型声明让 `<WcSearch>` 获得 TS 支持。
