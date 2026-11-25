---
title: [V3-546] 笔试：手写 renderless 组件（无渲染组件模式）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## V3-546：笔试：手写 renderless 组件

**答**：实现 `RenderlessPagination`：① 无模板组件（setup 返回函数式渲染）——把全部逻辑（页码计算/禁用态/事件）通过 scoped slot 暴露；② 消费者完全控制 UI，逻辑零重复；③ props: total/pageSize/current + emit('update:current')；④ slot props 含 { pages, prev, next, goTo, canPrev, canNext }；⑤ 页码窗口计算（省略号逻辑：当前页±2，首尾保留）。写出实现与消费示例。

```javascript
const RenderlessPagination = defineComponent({
  name: 'RenderlessPagination',
  props: { total: Number, pageSize: { type: Number, default: 10 }, current: Number },
  emits: ['update:current'],
  setup(props, { slots, emit }) {
    const pageCount = computed(() => Math.ceil(props.total / props.pageSize));
    const pages = computed(() => {
      const n = pageCount.value, c = props.current, out = [];
      const win = 2;                                     // 当前±2
      for (let i = 1; i <= n; i++) {
        if (i === 1 || i === n || Math.abs(i - c) <= win)
          out.push(i);
        else if (out.at(-1) !== '…') out.push('…');      // 收敛省略号
      }
      return out;
    });
    const goTo = (p) => {
      if (p < 1 || p > pageCount.value || p === props.current) return;
      emit('update:current', p);
    };
    return () => slots.default?.({
      pages: pages.value,
      current: props.current,
      pageCount: pageCount.value,
      canPrev: props.current > 1,
      canNext: props.current < pageCount.value,
      prev: () => goTo(props.current - 1),
      next: () => goTo(props.current + 1),
      goTo,
    });
  },
});
// 消费: UI 完全自定义
// <RenderlessPagination :total="200" :current="page" @update:current="page = $event" v-slot="p">
//   <button :disabled="!p.canPrev" @click="p.prev">‹</button>
//   <button v-for="it in p.pages" :key="it" :class="{ on: it === p.current }" @click="p.goTo(it)">{{ it }}</button>
// </RenderlessPagination>
```

**评分点**：
- 函数式 setup 返回 slots.default(scope) 的 renderless 模式
- 页码窗口省略号收敛逻辑
- 逻辑（页码/边界/事件）与 UI（插槽）完全分离
- 边界守卫（goTo 越界/同页短路）
