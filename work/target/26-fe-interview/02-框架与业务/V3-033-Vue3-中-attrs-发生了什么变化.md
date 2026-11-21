---
title: [V3-033] Vue3 中 $attrs 发生了什么变化？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-033：Vue3 中 $attrs 发生了什么变化？
**答**：
- Vue2 的 \$listeners 在 Vue3 被合并进 \$attrs，透传属性和事件统一处理。
- setup 中用 useAttrs() 访问，它是非响应式对象（但整体是浅响应跟踪的）。
- 默认继承到根元素；设置 inheritAttrs: false 后可手动 v-bind="attrs" 控制挂载位置。
- 多根节点组件不会自动继承 attrs，需要显式绑定或关闭告警。

```vue
<script setup lang="ts">
import { useAttrs } from "vue";

// Vue2 的 $listeners 在 Vue3 被合并进 $attrs
const attrs = useAttrs();
console.log(attrs.class, attrs["data-id"]);

function onClick() {
  // 透传的事件也在 attrs 中：attrs.onClick
  typeof attrs.onClick === "function" && (attrs.onClick as Function)();
}
</script>

<template>
  <!-- 未声明为 props 的属性都会进入 attrs，这里手动控制挂载位置 -->
  <div v-bind="attrs" @click="onClick">继承属性</div>
</template>
```

## 第七章 v-model 双向绑定
