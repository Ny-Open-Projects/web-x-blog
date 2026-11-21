---
title: [V3-181] Vue3 如何与 Service Worker / PWA 集成（vite-plugin-pwa 实战）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-181：Vue3 如何与 Service Worker / PWA 集成（vite-plugin-pwa 实战）？
**答**：
- vite-plugin-pwa 三件套：manifest（应用元信息）、workbox 生成 SW（预缓存构建产物 + 运行时缓存策略）、自动更新提示（registerType）。
- 缓存策略：预缓存（app shell）+ 运行时 StaleWhileRevalidate（图片/静态）+ NetworkFirst（接口数据）。
- 更新流程：SW 检测到新版本 -> 前端监听 needRefresh -> 弹窗提示 -> updateSW() 触发 reload，避免用户用旧资源。
- Vue 集成点：virtual:pwa-register 提供响应式 needRefresh 状态，直接接进组件做更新提示条。

```typescript
// vite.config.ts —— PWA 配置
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { VitePWA } from "vite-plugin-pwa";

export default defineConfig({
  plugins: [
    vue(),
    VitePWA({
      registerType: "prompt", // 有新版本时提示用户，而非静默刷新
      manifest: {
        name: "Vue3 商城",
        short_name: "商城",
        theme_color: "#409eff",
        icons: [{ src: "pwa-192.png", sizes: "192x192", type: "image/png" }],
      },
      workbox: {
        // 预缓存：构建产物全部进 SW（app shell 离线可用）
        globPatterns: ["**/*.{js,css,html,svg,png,woff2}"],
        runtimeCaching: [
          {
            // 图片：优先缓存，后台更新
            urlPattern: /\.(?:png|jpg|webp)$/,
            handler: "StaleWhileRevalidate",
            options: { cacheName: "images", expiration: { maxEntries: 200 } },
          },
          {
            // 接口：网络优先，失败兜底缓存（弱网可用）
            urlPattern: /\/api\//,
            handler: "NetworkFirst",
            options: { cacheName: "api", networkTimeoutSeconds: 3 },
          },
        ],
      },
    }),
  ],
});
```

```vue
<!-- src/components/UpdateBanner.vue —— 新版本提示 -->
<script setup lang="ts">
import { useRegisterSW } from "virtual:pwa-register/vue";

// 响应式更新状态：SW 检测到新版本时 needRefresh 变 true
const { needRefresh, updateServiceWorker } = useRegisterSW();
</script>

<template>
  <Transition name="slide">
    <div v-if="needRefresh" class="banner">
      系统有新版本
      <button @click="updateServiceWorker()">立即更新</button>
    </div>
  </Transition>
</template>

<style>
.banner {
  position: fixed; bottom: 16px; left: 50%; transform: translateX(-50%);
  background: #409eff; color: #fff; padding: 10px 20px; border-radius: 8px;
  display: flex; gap: 12px; align-items: center;
}
.slide-enter-active, .slide-leave-active { transition: all .3s; }
.slide-enter-from, .slide-leave-to { opacity: 0; transform: translate(-50%, 20px); }
</style>
```

## 第三十八章 综合大题

综合大题的答题公式：先一句话定位系统边界 -> 分层模块图（或状态机）-> 每个模块的关键技术选型 -> 一个最能体现复杂度的代码片段。代码是证据，架构叙述是得分主体。
