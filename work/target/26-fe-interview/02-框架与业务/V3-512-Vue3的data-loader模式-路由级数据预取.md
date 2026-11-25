---
title: [V3-512] Vue3 的 data-loader 模式：路由级数据预取
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 数据流]
type: 面试题
---

## V3-512：Vue3 的 data-loader 模式：路由级数据预取

**答**：
- 模式来源：Remix/Next 的 loader 思想在 Vue 生态落地（Nuxt useAsyncData / vue-router data loaders 实验）——数据在「导航完成前」开始拉取，减少「先跳转再等数据」的空窗
- 核心机制：路由定义 loader → beforeEach/resolve 时并行执行 → 结果注入组件（provide/状态）——组件 setup 直接消费，无内部 loading
- 与组件内拉取的取舍：loader 模式首屏快（导航期并行拉）但「跳转等待」感强（延迟导航）；组件内拉取「立即跳转 + 骨架」体感更好——按页面重要性混合（核心页 loader、长尾页组件内）
- 失败语义：loader 失败中断导航（跳错误页）还是降级进入（页面内错误态）——按 loader 关键性分级
- SSR 协同：loader 在服务端执行 + 结果序列化注入——同构数据流的关键环节

```javascript
// vue-router data loaders (实验) 示意
const route = defineBasicLoader(async (to) => {
  return api.goodsDetail(to.params.id);        // 导航期并行执行
});
// 组件内
const goods = useRouteLoader('goods');          // 无内部 loading 状态
```
