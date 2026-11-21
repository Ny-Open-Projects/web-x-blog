---
title: [XP-071] WebView 页面与原生页面的混合路由栈怎么设计？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-071：WebView 页面与原生页面的混合路由栈怎么设计？
**答**：
- 统一抽象：定义**路由协议**（页面 URI + 转场动画 + 参数），路由表声明每条 URI 由哪端承载（native/webview/weapp），路由器负责栈管理与容器创建。
- 栈的真相：原生页面栈是真正的栈（UINavigationController/Fragment 栈），H5 内部跳转只是 WebView 内 location 变化——必须区分**容器级路由**（新开/关闭 WebView）与**页内路由**（history.push），并把 H5 的 back 语义接入统一返回键。
- 关键场景：H5 → 原生（桥调用 openNative，原生 push）；原生 → H5（新 WebView 入栈）；跨容器返回传参（回调注册表/事件总线，页面 result 机制）；H5 多层内跳后按返回逐级回退而非直接关容器。
- 一致性：手势返回、物理返回键、导航栏返回按钮全部走同一个 `router.back()`，适配层处理各端默认行为差异。

```typescript
// packages/adapter/router —— 混合路由栈
export interface RouteEntry { uri: string; container: 'native' | 'webview'; params?: Record<string, unknown> }
export interface IRouter {
  push(uri: string, params?: Record<string, unknown>): Promise<void>;
  back(result?: unknown): void;                       // 跨容器返回带 result
  replace(uri: string): Promise<void>;
}

// Native Shell 路由器（伪码，RN 壳内也用同一协议）
class HybridRouter implements IRouter {
  #stack: RouteEntry[] = [];
  async push(uri: string, params?: Record<string, unknown>) {
    const target = routeTable.resolve(uri);           // { pattern: '/product/*', container: 'native' }
    if (target.container === 'webview') {
      const wv = await webviewPool.acquire(target.buildUrl(uri));  // XP-027 池化
      this.#stack.push({ uri, container: 'webview' });
      wv.pushNative(this.#stack.length);              // 原生侧压入一个持有 WebView 的页面
    } else {
      this.#stack.push({ uri, container: 'native' });
      nativeNavigator.push(target.screen, params);
    }
  }
  back(result?: unknown) {
    const top = this.#stack.pop()!;
    if (result && top.uri) resultBus.emit(`result:${top.uri}`, result);  // 返回传参
    if (top.container === 'webview') {
      // H5 有内部 history → 先 webView.goBack()，栈不动；到入口页才真正弹容器
      if (top.hasInnerHistory) { this.#stack.push(top); webviewPool.current.goBack(); return; }
      webviewPool.recycle(top.webview); nativeNavigator.pop();
    } else nativeNavigator.pop();
  }
}
// H5 侧：bridge.call('router.push', { uri: 'example://cart' }) → Native push；
// Android 物理返回键 → OnBackPressedCallback → router.back()，语义与手势返回一致
```
