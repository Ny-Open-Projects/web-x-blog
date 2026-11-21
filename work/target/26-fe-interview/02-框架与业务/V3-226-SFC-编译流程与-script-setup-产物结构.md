---
title: [V3-226] SFC 编译流程是怎样的？script setup 的最终产物结构长什么样？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-226：SFC 编译流程是怎样的？script setup 的最终产物结构长什么样？
**答**：
- 三段解析：`@vue/compiler-sfc` 把 .vue 拆为 descriptor（template/script/scriptSetup/style），各块独立交给对应编译器。
- script setup 编译：顶层变量自动收集为返回给模板的绑定（`_ctx` 省略，直接闭包引用）；import 的组件自动注册为组件选项。
- 产物形态：编译为单个 `defineComponent({ setup(__props) {...; return (_ctx) => ...} })`（或 Vapor 形态），顶层绑定按"setup return"暴露给 render。
- 样式：style 块编译为 JS 字符串 + 作用域 id（`data-v-xxx`），v-deep/slot 伪类做编译转换。
- 工程意义：理解产物才能读懂 HMR（按块局部更新）、调试 source map、排查"模板用了未定义变量"类报错。

```javascript
// <script setup> const msg = ref('hi') → 编译产物（简化）
export default /*#__PURE__*/ defineComponent({
  setup(__props, { expose: __expose }) {
    __expose();
    const msg = ref('hi');
    const __returned__ = { msg, ref };   // 顶层绑定收集：模板闭包直接用
    Object.defineProperty(__returned__, '__isScriptSetup', { value: true });
    return __returned__;
  },
});
// Vite 中同一文件请求会带 ?vue&type=template / &type=style 分别编译
// HMR：template 改动 → rerender（保留状态）；script 改动 → reload（丢状态）
```
