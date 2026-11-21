---
title: [BLD-146] rollup 插件实战：写一个 svg → Vue 组件的插件。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-146：rollup 插件实战：写一个 svg → Vue 组件的插件。
**答**：
- 目标：`import Icon from './logo.svg?component'` 直接得到 Vue SFC 组件（模板内嵌 svg，可继承 props）；核心是 transform 钩子里返回一个合法的 SFC 字符串，交给 @vitejs/plugin-vue 后续处理（vite 场景），rollup 场景直接产 render 函数。
- 实现要点：resolveId/load 不接管（资源已存在），只在 transform 拦截 `?component` query；用正则抽 svg 根标签与内部内容；生成的虚拟 SFC 加 `?lang.ts` 之类 id 规范（保持 sourcemap 无害）。
- rollup（非 vite）版本：直接产 `createStaticVNode`/`h` 调用代码，external 'vue'；vite 版本产 SFC 字符串最省事。
- 工程化：`?component&fill=currentColor` 扩展参数、缓存解析结果、对非法 svg 报错并给出文件路径。

```javascript
// rollup-plugin-svg-vue.mjs（vite 与 rollup 通用）
const QUERY_RE = /\.svg\?(component)(?:&(fill=([\w#%]+)))?$/;

export default function svgVue() {
  return {
    name: 'svg-to-vue',
    transform(code, id) {
      const m = id.match(QUERY_RE);
      if (!m) return null;                       // 不接管普通 svg
      const wantFill = m[3];                     // ?fill=currentColor 强制替换颜色
      const svg = code;
      const inner = svg
        .replace(/<svg[^>]*>/, '')               // 去根标签
        .replace(/<\/svg>\s*$/, '');
      const attrs = wantFill
        ? ` fill="${decodeURIComponent(wantFill)}"` : '';
      if (m[1] === 'component') {
        // vite 场景：产 SFC 字符串，交给 plugin-vue 的 transform 继续编译
        return {
          code: `<template><svg xmlns="http://www.w3.org/2000/svg" v-bind="$attrs"${attrs} v-html="__SVG_INNER__" /></template>
<script setup>defineOptions({ inheritAttrs: false });const __SVG_INNER__ = ${JSON.stringify(inner)};</script>`,
          map: { mappings: '' },
        };
      }
    },
  };
}
// 使用：
// import Logo from './logo.svg?component'   → <Logo class="w-4" />
// vite.config: plugins: [vue(), svgVue()]   → 注意 svgVue 要在 vue 之前（enforce: 'pre'）
// 进阶方向：svgo 压缩 svg（transform 内先跑 optimize）、产 web components、提取 viewBox 缓存
```
