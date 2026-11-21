---
title: [PER-724] 移动端 scheme/Universal Link 唤起 App 的性能与可靠性：唤起失败降级与耗时统计怎么做？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-724：移动端 scheme/Universal Link 唤起 App 的性能与可靠性：唤起失败降级与耗时统计怎么做？

**答**：
- 唤起方式对比：自定义 scheme（兼容好但未装 App 时报错页）、Universal Link/App Link（体验好但依赖域名配置与网络）、intent URL（Android 精确控制 fallback）——组合策略按平台分发。
- 可靠性设计：唤起失败检测（页面 visibilitychange 未触发 = 未离开 -> 定时器 2s 后降级到下载页/H5 兜底）；降级只触发一次（防循环唤起）；已装判断（cookie 记录历史唤起成功）调整策略。
- 性能点：唤起动作要在用户手势同步上下文中执行（异步链后调用会被拦截）；Universal Link 首次验证耗时由系统控制，前端要容忍失败重试。
- 度量：唤起成功率（离开页面比例）、降级触发率、唤起->首屏总耗时（App 侧回传闭环）。

```javascript

const appLinkPolicy = {
  strategy: { ios: 'Universal Link 优先 + scheme 兜底', android: 'intent URL + fallback 包名' },
  fallback: { detect: 'visibilitychange 2s 未触发 = 唤起失败', once: '降级只触发一次防循环',
    memory: 'cookie 记录唤起成功历史，调整优先级' },
  sync: '唤起必须在用户手势同步调用链中执行，异步后调用会被浏览器拦截',
  metrics: ['唤起成功率', '降级触发率', '唤起->App 首屏耗时（Native 回传闭环）'],
};
function openApp(uri, fallbackUrl) {
  const t0 = Date.now();
  let fell = false;
  location.href = uri;                                          // 手势同步链中调用
  setTimeout(() => {
    if (!document.hidden && !fell) {                            // 2s 未离开 = 失败
      fell = true;
      report('applink-fallback', { uri, waitedMs: Date.now() - t0 });
      location.href = fallbackUrl;                              // H5 兜底/下载页
    }
  }, 2000);
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) report('applink-success', { ms: Date.now() - t0 });
  }, { once: true });
}
```
