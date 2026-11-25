---
title: [V3-197] 设计一个播放器组件（video 封装：控制条/快捷键/倍速/全屏）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-197：设计一个播放器组件（video 封装：控制条/快捷键/倍速/全屏）？
**答**：
- 职责划分：原生 video 只负责播放；封装层管理状态（playing/time/volume/rate）并同步到 video 属性；控制条纯展示组件。
- 快捷键：keydown 监听在组件根上（tabindex=0 获焦），空格播放、方向键快进、F 全屏；输入框聚焦时不拦截。
- 倍速与全屏：playbackRate 直接赋值；全屏用 requestFullscreen 包整个容器（连控制条一起全屏），Safari 兼容 webkitEnterFullscreen。
- 事件出口：emit timeupdate/ended 进度类事件由父组件节流消费，避免每秒重渲染整个页面。

```vue
<!-- components/VideoPlayer.vue -->
<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";

const props = defineProps<{ src: string; poster?: string }>();
const emit = defineEmits<{ (e: "timeupdate", t: number, d: number): void; (e: "ended"): void }>();

const rootRef = ref<HTMLDivElement | null>(null);
const videoRef = ref<HTMLVideoElement | null>(null);
const playing = ref(false);
const currentTime = ref(0);
const duration = ref(0);
const volume = ref(1);
const rate = ref(1);
const rates = [0.5, 1, 1.25, 1.5, 2];

function toggle() {
  const v = videoRef.value!;
  playing.value ? v.pause() : v.play();
}

// 快捷键：输入框聚焦时不拦截
function onKeydown(e: KeyboardEvent) {
  if ((e.target as HTMLElement).tagName === "INPUT") return;
  const v = videoRef.value!;
  const map: Record<string, () => void> = {
    " ": toggle,
    ArrowRight: () => (v.currentTime += 5),
    ArrowLeft: () => (v.currentTime -= 5),
    ArrowUp: () => (volume.value = Math.min(1, volume.value + 0.1)),
    ArrowDown: () => (volume.value = Math.max(0, volume.value - 0.1)),
    f: fullscreen,
  };
  map[e.key]?.();
  e.preventDefault();
}

function fullscreen() {
  const root = rootRef.value!;
  if (document.fullscreenElement) document.exitFullscreen();
  else root.requestFullscreen?.() ?? (videoRef.value as any)?.webkitEnterFullscreen?.(); // Safari iOS
}

function setRate(r: number) {
  rate.value = r;
  videoRef.value!.playbackRate = r;
}

// timeupdate 高频：emit 交给父级，父级自己节流
function onTimeUpdate() {
  currentTime.value = videoRef.value!.currentTime;
  emit("timeupdate", currentTime.value, duration.value);
}

onMounted(() => (duration.value = videoRef.value!.duration || 0));
</script>

<template>
  <div ref="rootRef" class="player" tabindex="0" @keydown="onKeydown">
    <video ref="videoRef" :src="src" :poster="poster" @click="toggle"
      @play="playing = true" @pause="playing = false"
      @timeupdate="onTimeUpdate" @ended="emit('ended')" />

    <div class="controls">
      <button @click="toggle">{{ playing ? "暂停" : "播放" }}</button>
      <span>{{ currentTime.toFixed(0) }}s / {{ duration.toFixed(0) }}s</span>
      <input type="range" v-model.number="volume" min="0" max="1" step="0.1"
        @input="videoRef!.volume = volume" />
      <select :value="rate" @change="setRate(+($event.target as HTMLSelectElement).value)">
        <option v-for="r in rates" :key="r" :value="r">{{ r }}x</option>
      </select>
      <button @click="fullscreen">全屏</button>
    </div>
  </div>
</template>

<style>
.player { background: #000; color: #fff; }
video { width: 100%; display: block; }
.controls { display: flex; gap: 12px; align-items: center; padding: 8px; }
</style>
```
