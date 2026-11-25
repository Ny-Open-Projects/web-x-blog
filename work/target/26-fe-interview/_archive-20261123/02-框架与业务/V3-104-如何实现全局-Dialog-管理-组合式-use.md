---
title: [V3-104] 如何实现全局 Dialog 管理（组合式 useDialog + Promise 化）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-104：如何实现全局 Dialog 管理（组合式 useDialog + Promise 化）？
**答**：
- 模式：一个挂在 App 根部的 DialogHost 组件 + 一个全局响应式队列 + useDialog 函数。
- `await useDialog().confirm({...})` 返回 Promise：调用处把异步确认写成同步风格，消灭回调地狱。
- 队列天然支持连续弹出（先来先展示），resolve 存在队列项上，点击时取队首执行。
- 好处：业务组件不再各自维护 visible 状态，弹窗样式全局统一。

```typescript
// components/dialog/useDialog.ts
import { reactive } from "vue";

export interface DialogOptions {
  title: string;
  message: string;
  confirmText?: string;
  cancelText?: string;
}

interface PendingDialog extends DialogOptions {
  resolve: (ok: boolean) => void;
}

// 全局响应式队列：DialogHost 据此渲染
export const dialogState = reactive<{ queue: PendingDialog[] }>({ queue: [] });

export function useDialog() {
  function confirm(options: DialogOptions): Promise<boolean> {
    return new Promise((resolve) => {
      dialogState.queue.push({ ...options, resolve }); // resolve 存进队列，等用户点击
    });
  }
  return { confirm };
}

// DialogHost 点击回调：取队首执行 resolve
export function resolveTop(ok: boolean) {
  const top = dialogState.queue.shift();
  top?.resolve(ok);
}

// 业务代码使用：
// const ok = await useDialog().confirm({ title: "删除", message: "确认删除该订单？" });
// if (ok) deleteOrder(id);
```

```vue
<!-- components/dialog/DialogHost.vue —— 根组件挂载一次即可 -->
<script setup lang="ts">
import { dialogState, resolveTop } from "./useDialog";
</script>

<template>
  <Teleport to="body">
    <div v-if="dialogState.queue.length" class="dialog-mask">
      <div class="dialog">
        <h3>{{ dialogState.queue[0].title }}</h3>
        <p>{{ dialogState.queue[0].message }}</p>
        <div class="actions">
          <button @click="resolveTop(false)">{{ dialogState.queue[0].cancelText ?? "取消" }}</button>
          <button class="primary" @click="resolveTop(true)">
            {{ dialogState.queue[0].confirmText ?? "确定" }}
          </button>
        </div>
      </div>
    </div>
  </Teleport>
</template>
```
