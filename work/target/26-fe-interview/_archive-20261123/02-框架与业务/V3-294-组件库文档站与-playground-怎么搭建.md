---
title: [V3-294] 组件库文档站与 Playground 怎么搭建？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-294：组件库文档站与 Playground 怎么搭建？
**答**：
- 技术选型：VitePress（SFC 示例即文档）或 Storybook 8（隔离预览 + 控件面板）；组件库常用 VitePress + 自定义 demo 容器组件。
- 示例即测试：demo 容器（`<DemoPreview src="./basic.vue">`）编译时把示例源码注入页面（可复制查看），运行时真实渲染——文档、示例、回归三者同源。
- API 文档生成：从组件 TS 类型/defineProps 注释提取（vue-docgen-api / vue-tsc 输出）生成表格，杜绝手写 API 表过期。
- Playground：嵌入 StackBlitz/CodeSandbox 的在线编辑（模板预填充依赖），或本地 playground 包（热更新引用源码）。
- 版本化：文档按大版本分站（v2.xxx.com），当前版本默认 latest，旧版本可查（API 迁移必备）。

```vue
<!-- docs/.vitepress/theme/DemoPreview.vue -->
<script setup>
const props = defineProps({ src: String });             // docs/components/button/basic.vue
const comp = shallowRef(null);
const source = ref('');
onMounted(async () => {
  comp.value = (await import(`../../../../components/button/${props.src.split('/').pop()}`)).default;
  source.value = (await import(`../../../../components/button/${props.src.split('/').pop()}?raw`)).default;
});
</script>
<template>
  <div class="demo-preview">
    <div class="demo-render"><component :is="comp" /></div>
    <div class="demo-code"><pre><code>{{ source }}</code></pre></div>
  </div>
</template>
<!-- 文档 md：直接引用组件源码，单一数据源 -->
```
