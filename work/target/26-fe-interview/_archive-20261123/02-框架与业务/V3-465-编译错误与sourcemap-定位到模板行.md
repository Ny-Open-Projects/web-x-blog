---
title: [V3-465] 编译错误与 sourcemap：错误如何定位回模板行
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-465：编译错误与 sourcemap：错误如何定位回模板行

**答**：
- 编译期错误分类：parse 错误（标签未闭合/非法嵌套）、transform 错误（v-model 非 lvalue、v-if 与 v-for 同层）、codegen 前校验——全部带 loc（行列），dev 下 Vite 直接显示源码帧
- 运行时错误定位链：渲染函数报错 → sourcemap 反解回 .vue 模板行——compileTemplate 生成 code + map（source 是 template 字符串），Vite 把 template sourcemap 与整体 .vue sourcemap 串联
- codegen 的 sourcemap 策略：每个 vnode 调用点标记原始 loc——stack trace 经 source-map 库还原，Volar/浏览器 DevTools 都消费同一份
- dev 产物带标记：渲染函数内嵌 `/*# sourceURL=xxx.vue template */` 注释——Chrome 把编译函数显示为独立「源文件」便于打断点
- 常见坑：压缩后 sourcemap 丢失 → 生产错误堆栈回不到模板行——发布链路保留 map（私有上传到监控平台而不是公开发布）

```text
Error: Cannot read properties of undefined (reading 'name')
  at render (App.vue template, line 3)      ← sourcemap 还原
  ↳ 模板第 3 行: {{ user.profile.name }}
定位链: runtime stack → code frame → template loc → 编辑器跳转
```
