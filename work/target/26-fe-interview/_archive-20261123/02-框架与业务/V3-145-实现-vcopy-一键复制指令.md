---
title: [V3-145] 实现 v-copy 一键复制指令？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-145：实现 v-copy 一键复制指令？
**答**：
- 优先 `navigator.clipboard.writeText`（异步 API，要求 https 或 localhost）。
- 降级方案：隐藏 textarea + `document.execCommand("copy")`，兼容 http 与旧内核 WebView。
- 通过 CustomEvent 把成功/失败抛给使用方，指令本身不耦合 toast 组件；也可提供可选的成功回调选项。
- 注意 handler 必须提取成具名引用，unmounted 才能 removeEventListener，避免内存泄漏。

```vue
<!-- directives/copy.ts + 使用示例 -->
<script setup lang="ts">
import { ref, type Directive } from "vue";

type CopyHandler = (e: MouseEvent) => void;

const vCopy: Directive<HTMLElement, string> = {
  mounted(el, binding) {
    const handler: CopyHandler = async (e) => {
      e.stopPropagation();
      const text = binding.value ?? el.textContent?.trim() ?? "";
      try {
        await navigator.clipboard.writeText(text); // 首选：async clipboard
        el.dispatchEvent(new CustomEvent("copy:success", { detail: text }));
      } catch {
        // 降级：隐藏 textarea + execCommand，兼容 http / 旧 WebView
        const ta = document.createElement("textarea");
        ta.value = text;
        ta.style.cssText = "position:fixed;opacity:0;pointer-events:none";
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        ta.remove();
        el.dispatchEvent(new CustomEvent("copy:success", { detail: text }));
      }
      el.classList.add("copied"); // 轻量视觉反馈
      setTimeout(() => el.classList.remove("copied"), 600);
    };
    (el as any)._copyHandler = handler;
    el.addEventListener("click", handler);
  },
  unmounted(el) {
    el.removeEventListener("click", (el as any)._copyHandler); // 必须用同一引用移除
  },
};

const sn = ref("VUE3-2026-0011");
const onCopied = (e: Event) => console.log("已复制：", (e as CustomEvent).detail);
</script>

<template>
  <span v-copy="sn" @copy:success="onCopied" class="sn">{{ sn }}（点击复制）</span>
</template>

<style>
.sn { cursor: pointer; border-bottom: 1px dashed #999; }
.sn.copied { color: #409eff; }
</style>
```
