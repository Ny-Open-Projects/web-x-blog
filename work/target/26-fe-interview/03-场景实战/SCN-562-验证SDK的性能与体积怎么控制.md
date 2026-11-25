---
title: [SCN-562] 验证 SDK 的加载性能与体积怎么控制？验证器怎么按需加载？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-562：验证 SDK 加载性能与体积怎么控制？
**答**：
- 主包最小化：SDK 核心（采集 + 决策调用 + 无感验证）< 15KB gzip；滑块/点选/人脸等重验证器按需动态 import，首次使用才加载。
- 预加载策略：进入高风险页面（收银台）时 idle 预取下一级验证器 chunk；缓存后二次秒开。
- 加载失败兜底：chunk 加载失败重试 1 次后走降级链（SCN-558）；CDN 多域名容灾。
- 指标：SDK 初始化耗时、验证器 chunk 加载耗时计入监控，P95 超 1.5s 告警。
- 追问钩子：为什么不用一个全量大包——验证 SDK 挂在登录/支付关键路径上，大包直接拖慢业务首屏。

```javascript
const loaded = new Map();
async function getVerifier(name) {
  if (!loaded.has(name)) {
    loaded.set(name, import(/* webpackChunkName: "verifiers" */ `./verifiers/${name}.js`)
      .then(m => m.default)
      .catch(() => { loaded.delete(name); throw new Error('CHUNK_FAIL'); })); // 失败可重试
  }
  return loaded.get(name);
}
// 预取：收银台路由进入后
requestIdleCallback(() => getVerifier('slider').catch(() => {}));
```
