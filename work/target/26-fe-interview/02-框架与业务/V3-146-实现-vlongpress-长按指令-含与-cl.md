---
title: [V3-146] 实现 v-longpress 长按指令（含与 click 的冲突处理）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-146：实现 v-longpress 长按指令（含与 click 的冲突处理）？
**答**：
- 交互模型：mousedown/touchstart 启动定时器，超过时长（默认 500ms）触发回调；mouseup/touchend/touchleave 提前取消。
- 关键冲突点：长按成功后手指抬起还会产生一次 click，需在捕获阶段拦截并 stopImmediatePropagation。
- 移动端可用 navigator.vibrate 提供触觉反馈；touchstart 要加 passive 选项避免阻塞滚动。
- cleanup 统一封装，unmounted 时全部解绑。

```vue
<!-- directives/longpress.ts + 使用示例 -->
<script setup lang="ts">
import { type Directive } from "vue";

type LongpressHandler = (e: Event) => void;

const vLongpress: Directive<HTMLElement, LongpressHandler> = {
  mounted(el, binding) {
    const duration = 500; // 长按阈值，可扩展为 binding.arg 传入
    let timer: ReturnType<typeof setTimeout> | null = null;
    let longPressed = false;

    const start = (e: Event) => {
      longPressed = false;
      timer = setTimeout(() => {
        longPressed = true;
        navigator.vibrate?.(30); // 移动端触觉反馈
        binding.value(e);
      }, duration);
    };
    const cancel = () => {
      if (timer) clearTimeout(timer);
      timer = null;
    };
    // 长按成功后拦截随后的 click：捕获阶段阻止，避免既弹菜单又触发点击
    const onClick = (e: MouseEvent) => {
      if (longPressed) {
        e.stopImmediatePropagation();
        e.preventDefault();
        longPressed = false;
      }
    };

    el.addEventListener("mousedown", start);
    el.addEventListener("touchstart", start, { passive: true });
    ["mouseup", "mouseleave", "touchend", "touchcancel"].forEach((ev) =>
      el.addEventListener(ev, cancel)
    );
    el.addEventListener("click", onClick, true);
    (el as any)._lpCleanup = () => {
      cancel();
      el.removeEventListener("mousedown", start);
      el.removeEventListener("touchstart", start);
      ["mouseup", "mouseleave", "touchend", "touchcancel"].forEach((ev) =>
        el.removeEventListener(ev, cancel)
      );
      el.removeEventListener("click", onClick, true);
    };
  },
  unmounted(el) {
    (el as any)._lpCleanup?.();
  },
};

function showMenu() {
  console.log("弹出消息操作菜单：复制 / 撤回 / 转发");
}
</script>

<template>
  <!-- 常见场景：聊天消息长按弹菜单 -->
  <div class="msg" v-longpress="showMenu" @click="console.log('普通点击')">
    长按我弹出操作菜单
  </div>
</template>

<style>
.msg { padding: 12px 16px; background: #f4f4f5; border-radius: 8px; user-select: none; width: fit-content; }
</style>
```
