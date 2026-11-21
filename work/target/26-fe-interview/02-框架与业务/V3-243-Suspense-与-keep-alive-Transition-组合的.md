---
title: [V3-243] Suspense 与 KeepAlive、Transition 组合时的行为与坑是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-243：Suspense 与 KeepAlive、Transition 组合时的行为与坑是什么？
**答**：
- 官方推荐嵌套顺序：KeepAlive > Transition > Suspense > 组件，即 Suspense 放在内层；反序会导致 Suspense 的 fallback 干扰 Transition 动画。
- 与 KeepAlive：缓存的是**组件实例与 DOM**，Suspense resolve 一次后再次激活直接复用，不再 pending（异步 setup 只在首次实例化时执行）。
- 与 Transition：Suspense 切换 default/fallback 时可作为 Transition 的 children 参与动画；fallback → default 的切换动画需 `mode="out-in"` 避免双元素同屏。
- 坑 1：Suspense 内容包裹在 KeepAlive 里时，`async setup` 二次激活不再执行，刷新数据的逻辑要放 onActivated。
- 坑 2：Transition + Suspense 需要给切换内容统一单根节点，frag 多根时动画不触发。

```vue
<template>
  <RouterView v-slot="{ Component }">
    <KeepAlive>
      <Transition name="page" mode="out-in">
        <Suspense :key="$route.fullPath">       <!-- key 强制切换重进 pending -->
          <component :is="Component" />
          <template #fallback><PageLoader /></template>
        </Suspense>
      </Transition>
    </KeepAlive>
  </RouterView>
</template>
<!-- 子页面内：onActivated 做数据刷新，因为 async setup 只跑一次 -->
```
