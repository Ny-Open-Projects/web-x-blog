---
title: [WCN-787] 设计系统 token 的灰度发布与回滚机制怎么设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-787：设计系统 token 的灰度发布与回滚机制怎么设计？

**答**：
- 结论：token 变更走 feature flag 分流——先对内部/小流量租户下发新 token，观察视觉回归、错误率与指标无异常再全量；配置中心支持秒级切回旧值。
- token 带版本号，运行时按租户/用户 hash 选择版本；灰度期同时保留新旧 token，切换时原子替换（一次 CSS 变量批量写入）避免中间态。
- 追问钩子：灰度中用户跨页面跳转变成了不同 token 版本怎么办？考察「版本绑定用户维度而非请求维度」保证一致性。

```javascript
const TOKEN_VERSIONS = {
  v1: { '--primary': '#06f' },
  v2: { '--primary': '#1a73e8' },
};
function pickVersion(userId, grayRatio = 0.1) {
  let h = 0; for (const c of userId) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  return (h % 100) < grayRatio * 100 ? 'v2' : 'v1';   // 按用户稳定分流
}
function applyTokens(version) {
  const t = TOKEN_VERSIONS[version];
  const root = document.documentElement;
  for (const [k, v] of Object.entries(t)) root.style.setProperty(k, v); // 原子批量
}
applyTokens(pickVersion('user-123'));
```
