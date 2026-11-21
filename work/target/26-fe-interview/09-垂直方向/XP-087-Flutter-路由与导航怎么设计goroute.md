---
title: [XP-087] Flutter 路由与导航怎么设计？go_router 与深链怎么处理？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-087：Flutter 路由与导航怎么设计？go_router 与深链怎么处理？
**答**：
- go_router（声明式路由）：路径模板 + 类型安全参数、`redirect` 做登录守卫、`ShellRoute` 搭建底部导航多 tab 共存栈、`StatefulShellRoute` 保持各 tab 独立导航栈。
- 深链三件套：平台配置（Android intent-filter / iOS Universal Links）、go_router 自动解析 path/query、未登录/无权限场景 `redirect` 统一处理（先路由后登录，回跳原目标）。
- 路由与埋点：`NavigatorObserver`（RouteObserver）统一 PV 埋点与页面曝光；路由表集中声明，禁止散落的 `Navigator.push` 字符串拼接。
- 传参与刷新：`extra` 传对象仅限内存态，深链冷启动必走 path/query；列表→详情→编辑后用返回值或刷新信号（go_router 的 `push` 返回 Future）驱动更新。
- 与混合栈衔接：Add-to-App 场景路由由容器框架托管（XP-085），go_router 配置需注册为子路由，避免双栈冲突。

```dart
// app/router.dart —— 声明式路由 + 深链 + 守卫
final router = GoRouter(
  navigatorKey: _rootKey,
  initialLocation: '/home',
  redirect: (context, state) {
    final loggedIn = ref.read(authProvider).loggedIn;
    final onLogin = state.matchedLocation == '/login';
    if (!loggedIn && !onLogin) return '/login?from=${state.uri}';  // 深链守卫：记住来路
    if (loggedIn && onLogin) return state.uri.queryParameters['from'] ?? '/home';
    return null;
  },
  routes: [
    StatefulShellRoute.indexedStack(          // 底部导航：各 tab 独立导航栈
      builder: (_, __, shell) => MainScaffold(shell),
      branches: [
        StatefulShellBranch(routes: [GoRoute(path: '/home', builder: (_, __) => HomePage())]),
        StatefulShellBranch(routes: [GoRoute(path: '/mine', builder: (_, __) => MinePage())]),
      ],
    ),
    GoRoute(
      path: '/article/:id',                   // 深链目标：scheme 配置好后自动解析
      builder: (_, s) => ArticlePage(id: s.pathParameters['id']!),
    ),
  ],
  observers: [RouteTrackingObserver()],       // 统一 PV 埋点（XP-134 采集协议）
);
// Android: intent-filter 配 https 深链；iOS: Associated Domains + apple-app-site-association
```
