---
title: [SCN-016] 异步按钮的防重复点击与 loading 状态，如何优雅复用？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-016：异步按钮的防重复点击与 loading 状态，如何优雅复用？
**答**：
- 把"异步期间锁定"抽成组合式函数 useLock：包一层 run 自动管理 loading，组件里只负责绑定，避免每个按钮手写布尔开关。
- 点击后立即 disabled + 转圈，Promise 结束（无论成败）在 finally 释放锁定。
- 删除等危险操作叠加二次确认；支付等关键操作在 loading 期间加整页遮罩，防止误触其他按钮。

```vue
<script setup>
import { ref } from 'vue';
// 通用防连点：loading 期间重复调用直接忽略，结束后自动释放
function useLock(fn) {
  const loading = ref(false);
  return {
    loading,
    run: async (...args) => {
      if (loading.value) return;
      loading.value = true;
      try { await fn(...args); } finally { loading.value = false; }
    },
  };
}
const save = useLock(async () => {
  await api.updateProfile(form);
  ElMessage.success('已保存');
});
</script>

<template>
  <el-button type="primary" :loading="save.loading" :disabled="save.loading" @click="save.run">
    保存
  </el-button>
</template>
```
