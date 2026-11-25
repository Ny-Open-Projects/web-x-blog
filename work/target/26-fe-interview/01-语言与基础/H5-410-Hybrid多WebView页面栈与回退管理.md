---
title: [H5-410] Hybrid 多 WebView 页面栈与回退管理
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 路由]
type: 面试题
---

## H5-410：Hybrid 多 WebView 页面栈与回退管理

**答**：
- 栈模型：App 维护「页面栈」（Native 页与 H5 容器混排），H5 内部又有自己的 history 栈——回退语义要分清「H5 内回退」与「栈顶出栈」
- 回退劫持协议：H5 popstate 优先消费（单页应用内部路由），栈空时桥调 native.back() 出栈；iOS 侧滑手势与 H5 内路由冲突要协商（App 配置 interactivePopGestureRecognizer 按容器开关）
- 多实例 vs 单实例：每页面一个 WebView（隔离好、内存高）vs 单 WebView SPA（省内存但状态复杂）——按页面深度与内存预算选，主流是「每栈层级一个容器 + 复用池」
- 参数传递：页面栈间参数走 bridge（push 时带 params）+ 返回结果协议（backWithResult(result)），避免通过 localStorage 跨实例传
- 栈异常恢复：App 杀进程恢复时按持久化的栈描述（路由+参数快照）重建，深度限制（>10 层提示收敛）

```javascript
// 统一回退 SDK
function goBack() {
  if (history.state?.__h5routed && history.length > 1) history.back();   // H5 内部路由
  else bridge.call('back');                                              // 出栈
}
// 携带结果返回(页面栈)
async function selectGoods() {
  await bridge.call('push', { path: '/goods-select', params: { multi: true } });
}
bridge.on('page.result', ({ path, result }) => {
  if (path === '/goods-select') applySelection(result);   // 上页接收返回值
});
// Native 侧: backWithResult → 广播 page.result 给栈内前一容器
```
