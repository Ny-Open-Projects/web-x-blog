---
title: [XP-040] Electron 应用内存优化怎么做？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-040：Electron 应用内存优化怎么做？
**答**：
- 大头在**窗口与进程数量**：每窗口一个渲染进程（几十 MB 起步），策略是按需创建、单例复用、隐藏窗口延迟销毁或挂起（`webContents.setBackgroundThrottling`）。
- 渲染层：常规 Web 内存治理（事件解绑、大列表虚拟化、图片解码释放）；`<webview>`/BrowserView 用完立即销毁并监听 `destroyed`。
- 主进程：缓存设上限与 LRU 淘汰；避免持有大 Buffer 全局引用；`app.commandLine.appendSwitch('js-flags', '--max-old-space-size=512')` 收敛 V8 堆。
- 系统级：Windows 可释放工作集；后台时降低渲染频率；GPU 缓存大小限制。
- 观测：`process.memoryUsage()`/`app.getAppMetrics()` 定期采样上报，按进程类型聚合出内存水位看板。

```javascript
// main.ts —— 内存治理组合拳
// 1) 单例窗口复用，避免重复开渲染进程
ipcMain.handle('win:open-settings', () => wm.open('settings', { width: 720, height: 560 }, 'settings.html'));

// 2) 隐藏窗口内存回收：最小化/隐藏后清空闲缓存并挂起渲染
win.on('minimize', () => win.webContents.session.clearCache()); // 配合 setBackgroundThrottling(true)

// 3) V8 堆上限与 GPU 缓存收敛
app.commandLine.appendSwitch('js-flags', '--max-old-space-size=512');
app.commandLine.appendSwitch('gpu-program-cache-size-kb', '10240');

// 4) 内存水位监控与自愈
setInterval(() => {
  for (const m of app.getAppMetrics()) {
    const heapMB = (m.memory?.workingSetSize ?? 0) / 1024;
    if (heapMB > 400) {
      report('memory.high', { type: m.type, pid: m.pid, heapMB });
      if (m.type === 'Window' && isIdleWindow(m.pid)) recreateWindow(m.pid); // 空闲窗口重建释放
    }
  }
}, 60_000);
// 5) 渲染层：window.addEventListener('pagehide', disposeTimers) 防泄漏；大图 URL.revokeObjectURL
```

---

## 六、小程序容器与 uni-app 深度（041-046）
