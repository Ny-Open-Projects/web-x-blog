---
title: [V3-109] 如何实现命令面板（Ctrl+K 搜索）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-109：如何实现命令面板（Ctrl+K 搜索）？
**答**：
- 全局 keydown 监听 Ctrl/Cmd+K 切换面板，面板内监听上下键移动 activeIndex、Enter 执行、Escape 关闭。
- 命令列表数据驱动：id/label/run 三元组，keyword 过滤用 includes 起步，规模大再换模糊匹配库。
- activeIndex 要随过滤结果钳制，防止越界；执行后自动关闭面板。
- 组件卸载移除全局监听；打开时聚焦输入框提升体验。

```vue
<!-- components/CommandPalette.vue -->
<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref } from "vue";

interface Command {
  id: string;
  label: string;
  run: () => void;
}

const props = defineProps<{ commands: Command[] }>();

const visible = ref(false);
const keyword = ref("");
const activeIndex = ref(0);
const inputRef = ref<HTMLInputElement | null>(null);

const filtered = computed(() => {
  const kw = keyword.value.trim().toLowerCase();
  if (!kw) return props.commands;
  return props.commands.filter((c) => c.label.toLowerCase().includes(kw));
});

function onKeydown(e: KeyboardEvent) {
  // Ctrl/Cmd + K 全局切换
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
    e.preventDefault();
    visible.value = !visible.value;
    if (visible.value) nextTick(() => inputRef.value?.focus());
    return;
  }
  if (!visible.value) return;

  if (e.key === "Escape") visible.value = false;
  else if (e.key === "ArrowDown") {
    activeIndex.value = Math.min(activeIndex.value + 1, filtered.value.length - 1); // 钳制越界
  } else if (e.key === "ArrowUp") {
    activeIndex.value = Math.max(activeIndex.value - 1, 0);
  } else if (e.key === "Enter") execute();
}

function execute() {
  const cmd = filtered.value[activeIndex.value];
  if (!cmd) return;
  cmd.run();
  visible.value = false;
  keyword.value = "";
}

onMounted(() => window.addEventListener("keydown", onKeydown));
onBeforeUnmount(() => window.removeEventListener("keydown", onKeydown));
</script>

<template>
  <Teleport to="body">
    <div v-if="visible" class="palette-mask" @click.self="visible = false">
      <div class="palette">
        <input ref="inputRef" v-model="keyword" placeholder="输入命令…" @input="activeIndex = 0" />
        <ul>
          <li
            v-for="(cmd, i) in filtered"
            :key="cmd.id"
            :class="{ active: i === activeIndex }"
            @mouseenter="activeIndex = i"
            @click="execute"
          >
            {{ cmd.label }}
          </li>
        </ul>
      </div>
    </div>
  </Teleport>
</template>
```

## 第二十七章 性能实战

大表格、图片懒加载、长列表筛选、KeepAlive 缓存池、FLIP 动画与首屏优化，是性能方向的六个落地级考题。
