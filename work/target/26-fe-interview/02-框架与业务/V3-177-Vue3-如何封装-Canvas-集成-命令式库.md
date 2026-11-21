---
title: [V3-177] Vue3 如何封装 Canvas 集成（命令式库的响应式包装模式）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-177：Vue3 如何封装 Canvas 集成（命令式库的响应式包装模式）？
**答**：
- 模式四件套：canvas 元素用 template ref 拿到；初始化放 onMounted；数据变化用 watch 深度触发重绘；ResizeObserver 处理容器尺寸变化（devicePixelRatio 适配高清屏）。
- 响应式与命令式的边界：props/数据 → watch → 命令式 API 单向流动；canvas 内部状态不反灌回响应式系统，避免双向纠缠。
- 高 DPI 适配：canvas.width = css 宽度 * dpr，再 ctx.scale(dpr, dpr)，否则 Retina 屏发虚。
- 清理：onUnmounted 移除 observer 与事件，cancelAnimationFrame 停动画。

```vue
<!-- components/LineCanvas.vue —— 响应式数据驱动的 Canvas 折线图 -->
<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from "vue";

const props = defineProps<{ points: number[] }>();

const canvasRef = ref<HTMLCanvasElement | null>(null);
const wrapRef = ref<HTMLDivElement | null>(null);
let ctx: CanvasRenderingContext2D | null = null;
let ro: ResizeObserver | null = null;

function resizeAndDraw() {
  const canvas = canvasRef.value, wrap = wrapRef.value;
  if (!canvas || !wrap || !ctx) return;
  // 高 DPI 适配
  const dpr = window.devicePixelRatio || 1;
  const { width, height } = wrap.getBoundingClientRect();
  canvas.width = width * dpr;
  canvas.height = height * dpr;
  canvas.style.width = `${width}px`;
  canvas.style.height = `${height}px`;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0); // 之后全部按 CSS 像素画
  draw(width, height);
}

function draw(w: number, h: number) {
  if (!ctx) return;
  ctx.clearRect(0, 0, w, h);
  const pts = props.points;
  if (pts.length < 2) return;
  const max = Math.max(...pts), min = Math.min(...pts);
  const stepX = w / (pts.length - 1);
  ctx.beginPath();
  pts.forEach((p, i) => {
    const y = h - 20 - ((p - min) / (max - min || 1)) * (h - 40);
    i === 0 ? ctx.moveTo(0, y) : ctx.lineTo(i * stepX, y);
  });
  ctx.strokeStyle = "#409eff";
  ctx.lineWidth = 2;
  ctx.stroke();
}

// 数据变化 -> 单向流入 canvas 重绘（命令式库不反向污染响应式）
watch(() => props.points, resizeAndDraw, { deep: true });

onMounted(() => {
  ctx = canvasRef.value!.getContext("2d");
  ro = new ResizeObserver(resizeAndDraw); // 容器尺寸变化自适应
  ro.observe(wrapRef.value!);
  resizeAndDraw();
});

onUnmounted(() => ro?.disconnect());
</script>

<template>
  <div ref="wrapRef" class="wrap">
    <canvas ref="canvasRef" />
  </div>
</template>

<style>
.wrap { width: 100%; height: 200px; }
canvas { display: block; }
</style>
```
