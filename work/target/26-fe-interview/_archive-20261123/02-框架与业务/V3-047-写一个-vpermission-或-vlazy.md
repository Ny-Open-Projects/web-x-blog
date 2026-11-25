---
title: [V3-047] 写一个 v-permission 或 v-lazy 指令实战？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-047：写一个 v-permission 或 v-lazy 指令实战？
**答**：
- v-permission：mounted 时校验权限，无权限直接移除节点。
- v-lazy：IntersectionObserver 观察图片进入视口后再赋 src，节省流量与首屏时间。
- 指令适合"纯 DOM 行为"的横切逻辑，涉及响应式数据交互优先用组合函数。
- 全局注册在 main.ts 中 `app.directive(name, directive)`。

```vue
<script setup lang="ts">
import type { Directive } from "vue";

// v-permission：无权限直接移除节点
const vPermission: Directive<HTMLElement, string> = {
  mounted(el, binding) {
    const roles = ["admin"]; // 实际从用户信息读取
    if (!roles.includes(binding.value)) {
      el.parentNode?.removeChild(el);
    }
  },
};

// v-lazy：IntersectionObserver 实现图片懒加载
const vLazy: Directive<HTMLImageElement, string> = {
  mounted(el, binding) {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        el.src = binding.value;
        observer.disconnect();
      }
    });
    observer.observe(el);
  },
};
</script>

<template>
  <img v-lazy="'/img/avatar.png'" v-permission="'admin'" alt="头像" />
</template>
```

## 第十三章 插件机制
