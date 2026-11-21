---
title: [H5-094] Battery Status API 为什么被废弃？Network Information API 现状如何？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-094：Battery Status API 为什么被废弃？Network Information API 现状如何？
**答**：
- Battery（`navigator.getBattery()`）存在**指纹识别风险**：电量+充电状态组合可短暂唯一标识设备并做跨站追踪，Firefox/Safari 已移除，Chrome 仍保留但属"待淘汰"。
- Network Information（`navigator.connection`）返回 `effectiveType`（slow-2g~4g）、`downlink`（Mbps 估算）、`rtt`、`saveData`；兼容 Chrome/Edge，Safari/Firefox 不支持。
- 两者共同点：都是"环境信号"而非精确数据，浏览器刻意模糊化（如 downlink 取整到 25 档位）防指纹。
- 实用价值主要在弱网优化：`saveData === true` 时关闭自动播放视频、`effectiveType` 慢时降级图片质量；务必按"增强"定位而非功能开关。
- 网络在线状态判断不依赖它：`navigator.onLine` + `online/offline` 事件（H5-037）才是通用方案。

```javascript
// 1) Network Information：弱网降级（仅 Chromium 有效）
const conn = navigator.connection;
if (conn) {
  if (conn.saveData) {
    document.querySelectorAll('video[autoplay]').forEach(v => v.removeAttribute('autoplay'));
  }
  if (['slow-2g', '2g'].includes(conn.effectiveType)) {
    // 慢网：换缩略图、关预加载
    document.querySelectorAll('img[data-thumb]').forEach(i => {
      i.src = i.dataset.thumb;
      i.removeAttribute('srcset');
    });
  }
  // 监听网络质量变化：地铁进出站切换基站时触发
  conn.addEventListener('change', () => {
    console.log('网络变化：', conn.effectiveType, conn.downlink, 'Mbps');
  });
}

// 2) Battery：仅 Chrome 系可用，注意能力检测
if (navigator.getBattery) {
  navigator.getBattery().then((b) => {
    console.log(`电量 ${(b.level * 100)}%，充电中：${b.charging}`);
    // 低电量 + 未充电：提示用户慎用耗电功能
    if (!b.charging && b.level < 0.15) showNotice('电量不足，建议关闭后台同步');
    b.addEventListener('levelchange', () => console.log('电量变化：', b.level));
  });
} else {
  console.info('当前环境不支持 Battery Status API'); // Safari / Firefox
}
```
