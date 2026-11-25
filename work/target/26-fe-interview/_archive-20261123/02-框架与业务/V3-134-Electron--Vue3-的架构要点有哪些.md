---
title: [V3-134] Electron + Vue3 的架构要点有哪些？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-134：Electron + Vue3 的架构要点有哪些？
**答**：
- 进程模型：main 主进程（Node 能力）、renderer 渲染进程（Vue 应用）、preload 桥接层。
- 安全底线：渲染进程开启 contextIsolation，preload 用 contextBridge 只暴露白名单 API，禁止 nodeIntegration 直接进渲染层。
- 通信走 IPC：renderer 调 preload 暴露的方法 → ipcRenderer.invoke → main 的 ipcMain.handle，请求-响应语义清晰。
- Vue 工程化：渲染层与 Web 端复用同一套组件与状态层；平台差异收敛在 preload/types 里。

```typescript
// electron/main.ts —— 主进程
import { app, ipcMain } from "electron";
import { readFile, writeFile } from "node:fs/promises";

app.whenReady().then(() => {
  // 请求-响应式 IPC：renderer invoke，这里 handle
  ipcMain.handle("config:read", async () => readFile("config.json", "utf-8"));
  ipcMain.handle("file:save", async (_e, content: string) => {
    await writeFile("output.txt", content, "utf-8");
    return true;
  });
});
```

```typescript
// electron/preload.ts —— 桥接层：只暴露白名单 API
import { contextBridge, ipcRenderer } from "electron";

contextBridge.exposeInMainWorld("api", {
  readConfig: () => ipcRenderer.invoke("config:read"),
  saveFile: (content: string) => ipcRenderer.invoke("file:save", content),
});
// webPreferences 必须 contextIsolation: true 且不开启 nodeIntegration
```

```vue
<!-- src/App.vue —— 渲染进程：像调用普通异步 API 一样使用 IPC -->
<script setup lang="ts">
import { onMounted, ref } from "vue";

// 类型收敛：在 shared/ipc.d.ts 里声明 Window["api"] 的类型
const config = ref("");
const content = ref("");

onMounted(async () => {
  config.value = await window.api.readConfig(); // 走 preload 白名单
});

async function save() {
  await window.api.saveFile(content.value);
}
</script>

<template>
  <p>{{ config }}</p>
  <textarea v-model="content" />
  <button @click="save">保存</button>
</template>
```
