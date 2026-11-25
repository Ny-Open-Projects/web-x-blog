---
title: [XP-091] Flutter 如何处理平台生命周期？AppLifecycleState 怎么用对？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-091：Flutter 如何处理平台生命周期？AppLifecycleState 怎么用对？
**答**：
- 挂监听：`WidgetsBindingObserver` + `didChangeAppLifecycleState`；Flutter 3.13 起 `inactive`/`hidden` 语义完善，跨平台状态机统一（`hidden` 是 paused 前的过渡）。
- 状态语义：`resumed`（可见可交互）、`inactive`（iOS 来电/分屏过渡，Android 较少）、`paused`（后台不可见）、`hidden`（所有平台过渡到隐藏）、`detached`（引擎与宿主分离，Add-to-App 场景常见）。
- 典型用法：进后台暂停动画/轮询/视频、`resumed` 刷新 token 与拉取增量消息、`paused` 时机上报（最后可靠的打点窗口，需 sync 上报）、隐私合规（后台不可截屏等）。
- 平台差异要防坑：iOS 的 inactive 出现频繁（下拉通知栏、权限弹窗），暂停逻辑别只挂 paused；Android 进程被杀后恢复需走冷启动恢复态，与 `WidgetsBinding` 冷启动参数区分。
- 与混合开发联动：Add-to-App 下容器页可见性由宿主驱动（XP-085），不能只依赖 App 级生命周期；页面级用 `RouteAware`/`RouteObserver` 补足。

```dart
// app_lifecycle.dart —— App 生命周期编排：暂停/恢复/上报/刷新
class AppLifecycleTracker with WidgetsBindingObserver {
  DateTime? _pausedAt;

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    switch (state) {
      case AppLifecycleState.inactive:      // iOS 过渡频繁：轻暂停（别做重逻辑）
        animationTickerMuted = true;
      case AppLifecycleState.hidden:        // 所有平台进入隐藏的统一过渡态
        _stopPolling();
      case AppLifecycleState.paused:
        _pausedAt = DateTime.now();
        sessionReporter.flushSync();        // 最后可靠打点窗口：同步上报会话时长
      case AppLifecycleState.resumed:
        _resumeWork();                      // 时长统计/刷新 token/拉增量消息
      case AppLifecycleState.detached:      // 引擎脱离宿主（Add-to-App 场景）
        _releaseEngineResources();
    }
  }

  void _resumeWork() {
    final bg = DateTime.now().difference(_pausedAt!);
    if (bg > const Duration(minutes: 5)) {  // 长后台：会话切片 + 强制刷新
      sessionReporter.newSession();
      tokenRefresher.refresh();
      messageRepo.pullIncremental();
    }
    animationTickerMuted = false;
    _startPolling();
  }
}
// main() 中注册：WidgetsBinding.instance.addObserver(AppLifecycleTracker());
// 页面级可见性另用 RouteObserver<RouteAware>，Add-to-App 容器可见性由宿主驱动（XP-085）
```

---

## 十一、Hybrid 深度实战（092-098）
