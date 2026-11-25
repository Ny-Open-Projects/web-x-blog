---
title: [V3-016] 可写 computed 怎么用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-016：可写 computed 怎么用？
**答**：
- computed 传对象形式 { get, set } 即可支持写入，写入走 set 逻辑。
- 典型场景：父组件 v-model 一个派生值、全选状态联动子选项。
- set 里通常反向修改数据源，而不是存自己的值。
- TS 下可用 `computed<string>({...})` 显式标注类型。

```vue
<script setup lang="ts">
import { ref, computed } from "vue";

const firstName = ref("张");
const lastName = ref("三");

// 传对象形式即可支持写入
const fullName = computed<string>({
  get: () => firstName.value + lastName.value,
  set: (val) => {
    firstName.value = val.slice(0, 1);
    lastName.value = val.slice(1);
  },
});

function rename() {
  fullName.value = "李四"; // 触发 set，反向修改两个 ref
}
</script>

<template>
  <input v-model="fullName" />
  <button @click="rename">改名为李四</button>
</template>
```
