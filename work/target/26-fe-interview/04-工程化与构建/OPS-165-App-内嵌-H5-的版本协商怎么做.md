---
title: [OPS-165] App 内嵌 H5 的版本协商怎么做？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-165：App 内嵌 H5 的版本协商怎么做？
**答**：
- Native 在 WebView 初始化时注入环境信息（UA 追加或 JSBridge）：App 版本、容器版本、可用能力清单。
- 协商语义双向：H5 声明所需最低 App 版本，旧 App 降级到兼容页；Native 下发可用离线包版本，H5 优先走离线包加载（OPS-166）。
- 能力探测优先于版本号探测：bridgeApis 清单决定功能开关，版本号只做兜底。
- 协商信息写入可观测性（日志带 appVersion），排障时"哪个 App 版本出的问题"一目了然。
- 兼容期策略：新能力在旧 App 上必须可降级（隐藏入口或降级实现），不允许白屏。

```typescript
// App 内嵌 H5 版本协商：Native 注入 + 双向降级
interface AppBridgeInfo {
  appVersion: string;          // 宿主 App 版本
  h5ContainerVersion: string;  // WebView 容器 / 离线包版本
  bridgeApis: string[];        // 可用 JSBridge 能力清单
}

function getAppInfo(): AppBridgeInfo | null {
  const m = navigator.userAgent.match(/MyApp\/(\d+\.\d+\.\d+)/);   // Native 在 UA 追加版本
  if (!m) return null;                                             // 非内嵌环境
  return {
    appVersion: m[1],
    h5ContainerVersion: (window as any).__H5_CONTAINER__ ?? 'inline',
    bridgeApis: (window as any).MyBridge?.list?.() ?? [],
  };
}

const MIN_APP_VERSION = '8.2.0';
function ensureSupported(): boolean {
  const info = getAppInfo();
  if (!info) return true;
  // 优先能力探测，版本号只做兜底
  if (compare(info.appVersion, MIN_APP_VERSION) < 0) {
    location.replace('/legacy/fallback.html');   // 旧 App 降级到兼容页，引导升级
    return false;
  }
  return true;
}
// 反向协商：Native 下发可用离线包版本列表，H5 优先走离线包加载（OPS-166）
// 可观测性：日志与报错统一携带 appVersion，排障按版本归因
```
