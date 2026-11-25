---
title: [DP-125] composable 模式库如何设计？useXxx 的输入输出有什么规范？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-125：composable 模式库如何设计？useXxx 的输入输出有什么规范？（高频）
**答**：
- 输入规范：接受 ref/getter/原始值三类并用 `toValue` 归一（可响应也可不响应），可选 options 对象带默认值；输出规范：`{ 数据, 动作, 状态 }` 三件套，动作函数保持引用稳定。
- 生命周期内聚：订阅、定时器、 observer 全部在 composable 内 `onScopeDispose` 清理，调用方零清理负担（对比 mixin，DP-081）。
- 复用层级：纯逻辑 composable（useDebounceFn）→ 领域 composable（useCart）→ 页面组装；每层可独立单测。

```vue
<script setup>
// composable：输入宽容（ref/getter/裸值），输出三件套，自动清理
import { ref, computed, toValue, onScopeDispose } from 'vue';
export function useSearch(fetcher, keywordRef, { debounce = 300, immediate = true } = {}) {
  const results = ref([]);
  const status = ref('idle');                                  // idle loading error done
  const error = ref(null);
  let timer = null;
  async function run() {
    const kw = toValue(keywordRef);                            // 归一：ref 和裸值都能读
    status.value = 'loading';
    try { results.value = await fetcher(kw); status.value = 'done'; }
    catch (e) { error.value = e; status.value = 'error'; }
  }
  watch(() => toValue(keywordRef), () => {
    clearTimeout(timer);
    timer = setTimeout(run, debounce);                         // 内部细节不外泄
  }, { immediate });
  onScopeDispose(() => clearTimeout(timer));                   // 组件卸载自动清理
  return {
    results,                                                   // 数据
    status, error,                                             // 状态
    search: run,                                               // 动作（导出函数本身，引用稳定）
  };
}
// 调用方：一行接入，无任何清理代码
const keyword = ref('');
const { results, status, search } = useSearch((kw) => api.searchGoods(kw), keyword);
</script>
```
