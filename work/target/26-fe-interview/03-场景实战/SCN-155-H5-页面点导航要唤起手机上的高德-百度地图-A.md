---
title: [SCN-155] H5 页面点"导航"要唤起手机上的高德/百度地图 App，失败还要能兜底，如何兼容？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-155：H5 页面点"导航"要唤起手机上的高德/百度地图 App，失败还要能兜底，如何兼容？
**答**：
- 各 App 唤起协议不同：iOS 用 URL Scheme / Universal Link，Android 用 intent:// 或 scheme，同一供应商还要区分版本，维护一张"目标 + 平台 → scheme"的配置表。
- 尝试唤起后无法直接知道成功与否：用 visibilitychange/pagehide 当作"唤起成功"信号，800~1200ms 后仍在本页则视为失败。
- 失败兜底两级：先试 App，再降级该地图的 H5 网页版 URI API，最后提示手动复制地址。
- Universal Link 优先于 scheme（iOS），因为未安装时不会报错弹窗；scheme 放在 iOS 低版本或 WebView 场景。

```javascript
// 唤起地图导航：平台 scheme 表 + 成功信号探测 + 两级兜底
const NAV_SCHEMES = {
  amap: {
    ios:    { universal: 'https://uri.amap.com/navigation?', scheme: 'iosamap://navi?' },
    android:{ scheme: 'amapuri://route/plan?' },
    web:    'https://uri.amap.com/navigation',         // 兜底网页版
  },
  baidu: {
    ios:    { scheme: 'baidumap://map/direction?' },
    android:{ scheme: 'bdapp://map/direction?' },
    web:    'https://api.map.baidu.com/direction',
  },
};

export async function navigateTo(dest, { prefer = 'amap' } = {}) {
  const target = NAV_SCHEMES[prefer];
  const query = `destination=${dest.lat},${dest.lng}&mode=driving&src=web`;
  const isIOS = /iPhone|iPad/.test(navigator.userAgent);

  if (isIOS && target.ios.universal) {
    location.href = target.ios.universal + query;      // Universal Link：未安装也不报错
    return;
  }
  const scheme = (isIOS ? target.ios?.scheme : target.android?.scheme);
  if (scheme) {
    const launched = await tryLaunch(scheme + query);  // 先试 App
    if (launched) return;
  }
  location.href = `${target.web}?${query}&coordtype=gcj02`; // 兜底网页版地图
}

// 唤起探测：页面隐藏视为成功，超时视为失败
function tryLaunch(url, timeout = 1000) {
  return new Promise(resolve => {
    let done = false;
    const onHide = () => { done = true; cleanup(); resolve(true); };
    const cleanup = () => {
      document.removeEventListener('visibilitychange', onVis);
      document.removeEventListener('pagehide', onHide);
      clearTimeout(timer);
    };
    const onVis = () => document.hidden && onHide();
    document.addEventListener('visibilitychange', onVis);
    document.addEventListener('pagehide', onHide);
    const timer = setTimeout(() => { if (!done) { cleanup(); resolve(false); } }, timeout);
    location.href = url;                               // 触发 scheme
  });
}

```

## 二十七、音视频场景
