---
title: [R19-198] 如何收束 React 性能调优的完整排查路径（checklist）？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-198：如何收束 React 性能调优的完整排查路径（checklist）？
**答**：
- 排查顺序固定成链路：**度量**（先有数据：Profiler/Lighthouse/Performance 面板）-> **定位**（慢在渲染/网络/计算/绘制哪一层）-> **优化**（对层下药）-> **回归**（改完复测 + 看板）。
- 渲染慢：先看"谁导致重渲染"（Profiler火焰图）-> memo/key/状态下沉 -> 虚拟化大列表 -> React Compiler 收尾。
- 加载慢：网络瀑布（分包/预加载/预连接）、关键资源优先级（fetchpriority）、缓存策略（HTTP 缓存 + SWR）。
- 交互卡顿：长任务（切片/Worker）、布局抖动（读写分离）、大图动画（transform/opacity 合成层）。

```javascript
// perf-playbook.js —— 性能排查 checklist（代码即文档）
// 【第 0 步：度量基线】—— 没有数据不动手
// - Lighthouse 移动端跑分：FCP/LCP/INP/CLS 四指标
// - web-vitals 上报（R19-124）：真实用户分位数 P75
// - React Profiler（R19-168）：找出 actualDuration 最大的子树

// 【第 1 层：渲染过多/过重】
// 1.1 Profiler 找高频重渲染组件
// 1.2 三板斧：memo(纯展示) + useCallback(引用稳定) + 状态下沉(拆组件)
// 1.3 Context 风暴：value 记忆化 / 拆分 context / 订阅式 store(zustand)
// 1.4 大列表：虚拟化（R19-169）
// 1.5 重计算：useMemo 化 + 迁移到 Worker

// 【第 2 层：首屏加载慢】
// 2.1 包体：bundle 分析 -> 路由级 code splitting -> 大依赖替换(moment->dayjs 等)
// 2.2 网络：HTTP/2、预连接 dns-prefetch/preconnect、关键接口 SSR/预取
// 2.3 优先级：LCP 图片 fetchpriority=high + preload，非关键资源 defer/lazy
// 2.4 缓存：静态资源 immutable 一年 + index.html no-cache

// 【第 3 层：交互卡顿】
// 3.1 Performance 面板录制：找 >50ms 长任务
// 3.2 长任务：idle 切片（R19-171）/ Web Worker / useTransition（R19-138）
// 3.3 布局抖动：批量读 getBoundingClientRect 再批量写；动画只用 transform/opacity
// 3.4 输入响应：搜索防抖 + deferred value，键盘到回显 < 100ms

// 【第 4 层：回归防线】
// 4.1 CI 中 Lighthouse CI 对比上次分数，回退 >5 分阻断
// 4.2 web-vitals 看板持续监控 P75
// 4.3 Profiler API 生产采样，渲染超 16ms 自动上报

// 【反模式清单】
// - 无脑全局 memo/useCallback：维护成本 > 收益，先度量再优化
// - 用 useMemo 包所有计算：内存与比较本身有开销
// - 只看开发模式性能：StrictMode 双渲染与生产差异大，结论以生产 profile 为准
console.log('perf playbook loaded'); // checklist 落在 code review 时逐条对照
```
