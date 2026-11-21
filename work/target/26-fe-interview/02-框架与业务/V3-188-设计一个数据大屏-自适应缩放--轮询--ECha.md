---
title: [V3-188] 设计一个数据大屏（自适应缩放 + 轮询 + ECharts 优化）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-188：设计一个数据大屏（自适应缩放 + 轮询 + ECharts 优化）？
**答**：
- 自适应：设计稿固定 1920x1080，外层容器 transform: scale() 按窗口宽高比等比缩放（取宽高缩放比最小值），图表内部逻辑坐标不变。
- ECharts 优化：实例复用不重复 init；setOption 用 notMerge:false 增量更新；resize 监听防抖；超长序列用 sampling/dataZoom。
- 数据刷新：usePolling（V3-164）统一管理，多图表共享一次批量接口；页面不可见自动暂停。
- 动效节制：数字滚动 + 图表过渡即可，避免大量 markPoint 动画掉帧；大屏建议关闭 tooltip（无人交互）。

```vue
<!-- views/dashboard/BigScreen.vue -->
<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import * as echarts from "echarts";
import { usePolling } from "@/composables/usePolling";

const DESIGN_W = 1920, DESIGN_H = 1080;
const screenRef = ref<HTMLDivElement | null>(null);
const chartRefs = ref<HTMLElement[]>([]);
const charts: echarts.ECharts[] = [];
const salesData = ref<number[]>([]);

// ---- 自适应缩放：等比 scale，保持设计稿坐标系 ----
function fitScreen() {
  const scale = Math.min(window.innerWidth / DESIGN_W, window.innerHeight / DESIGN_H);
  screenRef.value!.style.transform = `scale(${scale}) translate(-50%, -50%)`;
  charts.forEach((c) => c.resize()); // resize 防抖可加，这里仅两图直接刷
}

// ---- 轮询取数：一个批量接口喂全部图表 ----
const { data, start } = usePolling<Record<string, number[]>>(
  () => fetch("/api/dashboard/batch").then((r) => r.json()),
  10_000
);

function renderCharts() {
  // 实例复用：首次 init，之后 setOption 增量更新
  if (!charts.length) {
    chartRefs.value.forEach((el) => charts.push(echarts.init(el)));
  }
  const trend = data.value?.trend ?? [];
  charts[0]?.setOption({
    xAxis: { type: "category", data: trend.map((_, i) => i) },
    yAxis: { type: "value" },
    series: [{ type: "line", data: trend, smooth: true, sampling: "lttb" }], // LTTB 抽稀
    animationDurationUpdate: 600, // 数据刷新的过渡动画
  });
  salesData.value = data.value?.sales ?? [];
}

watch(data, renderCharts);

onMounted(() => {
  fitScreen();
  window.addEventListener("resize", fitScreen);
  start();
});
onUnmounted(() => {
  window.removeEventListener("resize", fitScreen);
  charts.forEach((c) => c.dispose()); // 必须 dispose
});
</script>

<template>
  <!-- 外层铺满视口，内层按设计稿尺寸 + scale 缩放 -->
  <div class="stage-outer">
    <div ref="screenRef" class="stage" :style="{ width: DESIGN_W + 'px', height: DESIGN_H + 'px' }">
      <div class="panel"><div ref="chartRefs" /></div>
      <div v-for="(v, i) in salesData" :key="i" class="kpi">{{ v }}</div>
    </div>
  </div>
</template>

<style>
.stage-outer { width: 100vw; height: 100vh; overflow: hidden; background: #001529; }
.stage { position: absolute; left: 50%; top: 50%; transform-origin: left top; }
.panel { width: 900px; height: 400px; }
.kpi { color: #409eff; font-size: 32px; }
</style>

<script lang="ts">
import { watch } from "vue";
</script>
```
