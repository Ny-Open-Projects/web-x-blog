---
title: [XP-025] Flutter Web 的取舍与现状？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-025：Flutter Web 的取舍与现状？
**答**：
- 两种渲染器：**canvaskit**（Skia wasm，像素级一致、性能较好，但体积大、SEO/无障碍弱）与 **html**（映射为 DOM/CSS，文本选择/SEO 好，但样式兼容差、已逐步弃用）。
- 定位结论：Flutter Web 适合**已有 Flutter 代码的低成本复用**（内部工具、产品演示），不适合以 Web 为第一公民的站点。
- 硬伤：首屏体积（canvaskit wasm + 数据）、文本渲染与浏览器习惯不一致、无障碍依赖 canvas 帧循环成本高。
- 工程建议：Web 端做条件适配（`kIsWeb` 分支）、按需 deferred components、移动端路由/URL 同步（go_router + browser history）。
- 若 Web 是主要目标，直接选 React/Vue 生态，别硬上 Flutter Web。

```yaml
# flutter web 构建与渲染器选择
targets:
  web:
    build:
      command: flutter build web
      args:
        - --release
        - --wasm                   # 3.22+ 可选 wasm 产物（Dart 编译到 WasmGC）
        - --web-renderer canvaskit # canvaskit 或 html（html 已不推荐）
        - --pwa-strategy=offline-first
    # 条件适配示例（lib/pay/pay_button.dart）：
    #   if (kIsWeb) { window.open(payUrl) }   // Web 无支付 SDK，跳转支付页
    #   else { MethodChannel('app/pay').invokeMethod(...) }
    # 路由同步：MaterialApp.router + go_router，URL 与移动端路由表共用一份定义
    # 体积优化：deferred components（延迟加载组件库）、canvaskit 走 CDN 缓存
```

---

## 四、Hybrid 与 WebView（026-032）
