---
title: [H5-393] 蓝牙与 Web NFC：近场能力在 H5 的可用性边界
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 设备能力]
type: 面试题
---

## H5-393：蓝牙与 Web NFC：近场能力在 H5 的可用性边界

**答**：
- Web Bluetooth（BLE）：Chrome 系支持（iOS Safari 不支持），只支持 GATT 设备（手环/传感器），需要用户手势触发 requestDevice 弹授权——App 内 WebView 通常不透传，需桥
- Web NFC：仅 Android Chrome 支持且需 NFC 芯片，NDEFReader 读标签；iOS 走原生桥（CoreNFC）——H5 场景能力碎片化严重
- 架构建议：能力探测 + 双通道实现（Web API 可用走 Web API，否则桥调原生），对业务层暴露统一接口——「能力注册表」模式
- 安全约束：蓝牙/NFC 都要求 HTTPS + 用户手势 + 每次会话授权（无持久授权），批量操作要处理授权中断
- 实战场景取舍：IoT 配网/扫码类功能如果浏览器支持差，直接引导 App 是更优解——不要硬做全兼容

```javascript
async function readTag() {
  if ('NDEFReader' in window) {              // Android Chrome
    const nfc = new NDEFReader();
    await nfc.scan();                         // 必须用户手势内调用
    nfc.onreading = ({ message }) => {
      for (const r of message.records) handleText(r.data ? new TextDecoder().decode(r.data) : '');
    };
    return true;
  }
  if (window.__HYBRID__) { bridge.call('nfc.read'); return true; } // App 内走桥
  return false;                               // 引导 App
}
```

**追问**：

1. 为什么 iOS Safari 一直不做 Web Bluetooth？ → WebKit 出于隐私与平台策略未实现，iOS 只有原生 CoreBluetooth；H5 只能走 App 桥，不能指望 polyfill。
2. 蓝牙授权是持久的还是每次都要重新弹？ → 每次会话都要，`requestDevice` 必须在用户手势里且刷新即失效；想复用设备要靠 `getDevices()`（需实验开关）配合 device.id。
3. NFC 在页面切到后台后还能继续读吗？ → 不能，`scan()` 要求页面可见且在用户手势内启动，切后台会中断，要监听 `visibilitychange` 回前台时重新扫描。
