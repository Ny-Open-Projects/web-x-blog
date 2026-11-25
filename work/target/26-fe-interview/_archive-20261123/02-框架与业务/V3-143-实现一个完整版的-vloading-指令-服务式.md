---
title: [V3-143] 实现一个完整版的 v-loading 指令（服务式调用 + 多实例）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-143：实现一个完整版的 v-loading 指令（服务式调用 + 多实例）？
**答**：
- 指令版：mounted/updated 按 binding.value 控制遮罩显隐，modifiers.fullscreen 支持全屏遮罩，binding.arg 传文案（`v-loading:导出中`）。
- 多实例关键：遮罩 append 到指令所在的目标元素（非全屏时给目标加 position: relative），而不是全局单例，多个区域可同时转圈。
- 服务版：提供 loading.show() / close()，适合请求拦截器、导出下载等"无锚点元素"的场景。
- 防重复挂载、zIndex 自增、unmounted 时清理 DOM，三个细节是面试加分点。

```vue
<!-- directives/loading.ts（指令 + 服务双形态）+ 使用示例 -->
<script setup lang="ts">
import { ref, type Directive } from "vue";

// ---------- 指令与服务实现 ----------
let zIndex = 2000;
const MASK_CLASS = "v-loading-mask";

function createMask(text: string, fullscreen: boolean) {
  const mask = document.createElement("div");
  mask.className = MASK_CLASS;
  mask.style.zIndex = String(zIndex++);
  if (fullscreen) mask.classList.add("is-fullscreen");
  mask.innerHTML = `<div class="v-loading-spinner"><div class="spin"></div><p>${text}</p></div>`;
  return mask;
}
function showMask(el: HTMLElement, text: string, fullscreen: boolean) {
  if (el.querySelector(`.${MASK_CLASS}`)) return; // 防重复
  if (!fullscreen) el.style.position ||= "relative"; // 局部遮罩需要相对定位
  el.appendChild(createMask(text, fullscreen));
}
function hideMask(el: HTMLElement) {
  el.querySelector(`.${MASK_CLASS}`)?.remove();
}

export const vLoading: Directive<HTMLElement, boolean> = {
  mounted(el, binding) {
    if (binding.value) showMask(el, binding.arg || "加载中", !!binding.modifiers.fullscreen);
  },
  updated(el, binding) {
    if (binding.value === binding.oldValue) return;
    binding.value
      ? showMask(el, binding.arg || "加载中", !!binding.modifiers.fullscreen)
      : hideMask(el);
  },
  unmounted(el) {
    hideMask(el); // 卸载清理，防 DOM 泄漏
  },
};

// 服务式：无锚点场景（拦截器、导出）
export const loadingService = {
  show(text = "加载中") {
    showMask(document.body, text, true);
    return { close: () => hideMask(document.body) };
  },
};

// ---------- 使用示例 ----------
const tableLoading = ref(false);
async function fetchData() {
  tableLoading.value = true;
  await new Promise((r) => setTimeout(r, 1000));
  tableLoading.value = false;
}
</script>

<template>
  <!-- 局部遮罩：只罩住 .card；v-loading:xxx 冒号后是文案 -->
  <div v-loading:拼命加载中="tableLoading" class="card">
    <p>表格内容...</p>
  </div>
  <button @click="fetchData">加载表格</button>
  <button @click="loadingService.show('导出中').close.bind(null)">全屏 loading（实际项目先存句柄）</button>
</template>

<style>
.v-loading-mask { position: absolute; inset: 0; background: rgba(255, 255, 255, 0.7); display: grid; place-items: center; }
.v-loading-mask.is-fullscreen { position: fixed; }
.v-loading-spinner .spin { width: 32px; height: 32px; border: 3px solid #409eff; border-top-color: transparent; border-radius: 50%; animation: v-spin 1s linear infinite; margin: 0 auto 8px; }
@keyframes v-spin { to { transform: rotate(360deg); } }
</style>
```
