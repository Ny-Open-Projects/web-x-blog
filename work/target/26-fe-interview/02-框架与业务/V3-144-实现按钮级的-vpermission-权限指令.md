---
title: [V3-144] 实现按钮级的 v-permission 权限指令？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-144：实现按钮级的 v-permission 权限指令？
**答**：
- 从用户 store 取权限码集合，与 binding.value（单码或数组）比对，无权限则隐藏元素。
- 隐藏用 display:none + dataset 标记，而不是 removeChild：保持 vnode 树与 DOM 的对应关系稳定，权限变化时还能恢复。
- modifiers.all 支持"必须拥有全部权限码"模式，默认 some（任一满足即可）。
- 指令工厂 createPermissionDirective 注入权限来源，方便不同项目复用；同时强调按钮级权限只是前端体验，接口层必须后端再校验。

```vue
<!-- directives/permission.ts + 使用示例 -->
<script setup lang="ts">
import { type Directive } from "vue";

// 模拟用户权限（真实项目来自 pinia 的 useUserStore）
const userCodes = ref<string[]>(["system:user:add", "order:export"]);

// 指令工厂：权限来源可注入，便于复用与测试
function createPermissionDirective(
  getCodes: () => string[]
): Directive<HTMLElement, string | string[]> {
  return {
    mounted(el, binding) {
      const need = Array.isArray(binding.value) ? binding.value : [binding.value];
      const owned = getCodes();
      const pass = binding.modifiers.all
        ? need.every((c) => owned.includes(c)) // all 修饰符：必须全部拥有
        : need.some((c) => owned.includes(c)); // 默认 some：任一满足即可
      if (!pass) {
        el.style.display = "none";   // 隐藏而非移除：保持 DOM 与 vnode 对应
        el.dataset.permHidden = "1"; // 标记，便于调试与恢复
      }
    },
    updated(el, binding) {
      // 权限码运行期变化（切换租户/角色）时同步显隐
      const need = Array.isArray(binding.value) ? binding.value : [binding.value];
      const owned = getCodes();
      const pass = need.some((c) => owned.includes(c));
      el.style.display = pass ? "" : "none";
    },
  };
}

const vPerm = createPermissionDirective(() => userCodes.value);
</script>

<template>
  <button v-perm="'system:user:add'">新增用户</button>
  <!-- 无 system:user:delete 权限，按钮被隐藏 -->
  <button v-perm="'system:user:delete'">删除用户</button>
  <!-- 必须同时拥有两个权限码 -->
  <button v-perm.all="['order:export', 'order:audit']">导出并审核</button>
</template>
```
