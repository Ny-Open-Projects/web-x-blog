---
title: [PER-275] Vue 应用有哪些典型内存泄漏点？组合式 API 下怎么保证清理完整？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-275：Vue 应用有哪些典型内存泄漏点？组合式 API 下怎么保证清理完整？

**答**：
- 泄漏点：① onMounted 里挂的 window/document 监听没有对应 onBeforeUnmount 解绑；② 组件里 setInterval/Observer 未清理；③ provide 大对象或全局 reactive 缓存累积；④ 自定义指令绑事件不 unbind；⑤ keep-alive 缓存列表无上限（配合 max）；⑥ v-if 切换的组件内部全局订阅残留。
- 组合式 API 的治理优势：清理函数可以在 setup 里与创建逻辑"就地配对"（watch 返回 stop 函数、EffectScope 统一收集）——把"配对纪律"变成 API 习惯。
- 关键工具：`EffectScope`（/ `onScopeDispose`）——一个 scope 里注册的所有副作用在 scope stop 时全部清理，常用于封装"可整体销毁的功能模块"。
- 验证：Vue DevTools 高亮已卸载组件实例是否仍被引用；线上用 detached DOM 检测 + heap baseline 回归。

```javascript
import { effectScope, onScopeDispose } from 'vue';

// EffectScope：一个模块的所有副作用一次清理
export function useRealtimePrice(symbol) {
  const scope = effectScope();                     // 收集器
  const price = ref(0);
  scope.run(() => {
    const ws = connectWS(`/price/${symbol}`);
    ws.on('tick', (v) => (price.value = v));
    watch(price, log);                              // watch 也被 scope 收集
    onScopeDispose(() => ws.close());               // 就地配对关闭
  });
  onUnmounted(() => scope.stop());                  // 组件卸载 = 全部清理
  return price;
}
// keep-alive 缓存上限：<KeepAlive :max="10"> —— 防实例堆积
```
