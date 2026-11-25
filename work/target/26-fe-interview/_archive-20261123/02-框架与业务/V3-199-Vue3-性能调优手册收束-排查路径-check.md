---
title: [V3-199] Vue3 性能调优手册收束（排查路径 checklist）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-199：Vue3 性能调优手册收束（排查路径 checklist）？
**答**：
- 排查顺序固定：先测量（Lighthouse/Performance 面板定位 FCPLCP、Long Task）再动手，禁止凭感觉优化。
- 加载性能 checklist：路由懒加载、首屏接口并行、图片 webp+懒加载、关键 CSS 内联、HTTP 缓存与 CDN、按需引入组件库。
- 运行时 checklist：大列表虚拟滚动、computed 替代方法调用、深层 reactive 改 shallowRef、v-memo 与 v-once、事件与定时器清理。
- 渲染更新 checklist：key 稳定性、避免 v-if/v-show 误用、大对象不进响应式（markRaw）、KeepAlive 缓存重型组件。
- 工程化收束：bundle 分析（rollup-plugin-visualizer）、性能预算进 CI（Lighthouse CI 阈值卡点）。

```typescript
// scripts/perf-checklist.ts —— 调优手册：按排查路径逐项自检
export const perfChecklist = {
  // 第一步：测量定位（先测量后优化）
  measure: {
    tool: "Lighthouse / Performance 面板 / web-vitals 上报",
    targets: { LCP: "< 2.5s", INP: "< 200ms", CLS: "< 0.1", bundle: "首包 < 300KB gzip" },
  },
  // 第二步：加载性能
  loading: [
    "路由级 () => import() 懒加载，首屏无关页面全部分包",
    "组件库按需引入（unplugin-vue-components），echarts 按需注册",
    "首屏图片 preload + 商品图 webp + v-lazy",
    "接口并行 Promise.all，CSS 内联关键样式",
    "CDN + 强缓存（hash 文件名）",
  ],
  // 第三步：运行时
  runtime: [
    "万级列表虚拟滚动（vue-virtual-scroller / 自研窗口化）",
    "模板里不调用方法做过滤排序，全部收敛进 computed（有缓存）",
    "大数组大数据：shallowRef + triggerRef，避免深层代理开销",
    "静态内容 v-once，长列表子项 v-memo=[item.id, item.status]",
    "事件监听/observer/定时器必须在 onUnmounted 清理",
  ],
  // 第四步：渲染更新
  render: [
    "列表 key 用业务 id，禁用 index",
    "频繁切换的显隐用 v-show，条件渲染用 v-if",
    "第三方实例（echarts/地图）markRaw，不进响应式",
    "重型页面 KeepAlive 包裹 + include 白名单",
  ],
  // 第五步：工程化卡点
  ci: [
    "rollup-plugin-visualizer 分析产物构成",
    "Lighthouse CI 设定阈值，低于预算阻断合并",
    "性能指标真实用户上报（web-vitals），回归可观测",
  ],
};

// 快速自检脚本示例：构建后检查首包体积预算
// import { gzipSync } from "zlib";
// const budget = 300 * 1024;
// const distStat = getGzipSize("dist/assets/index-*.js");
// if (distStat > budget) { console.error("首包超预算"); process.exit(1); }
```
