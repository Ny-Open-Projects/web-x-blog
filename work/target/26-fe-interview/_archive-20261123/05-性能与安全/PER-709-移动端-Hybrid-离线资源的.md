---
title: [PER-709] 移动端 Hybrid 离线资源的版本一致性：HTML 与离线包版本错配导致的白屏如何防？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-709：移动端 Hybrid 离线资源的版本一致性：HTML 与离线包版本错配导致的白屏如何防？

**答**：
- 错配场景：HTML 引用的 JS hash 是新包的，但本地拦截命中旧离线包（或反之）-> 404/旧代码混新接口 -> 白屏或逻辑错乱；多发于发版窗口与离线包异步更新期间。
- 防线三条：**版本协商**（HTML 头带包版本标记，拦截层校验引用资源是否属于当前包，不匹配则放行真网）、**原子切换**（离线包整包切换 + 旧包保留 2 个版本，正在使用的旧 HTML 仍能命中旧资源）、**兜底重载**（关键 chunk 404 时自动清离线缓存走真网重载，见 591）。
- 排查工具：错配现场采样（拦截层记录请求的资源版本 vs 当前包版本不一致样本），上报统计错配率。
- 原则：离线是加速不是唯一依赖——任何离线命中失败都要有真网兜底且用户无感。

```javascript

const offlineVersionGuard = {
  negotiate: 'HTML 带 buildId，拦截层校验资源归属包，不匹配放行真网',
  atomic: '整包原子切换 + 旧包保留 2 版（在用旧 HTML 仍命中旧资源）',
  fallback: '关键资源 404 -> 清离线缓存 -> 真网重载（用户无感）',
  observe: '拦截层记录版本错配样本，错配率进发版健康看板',
};
function shouldIntercept(req, currentPkg) {
  const resBuild = req.resourceBuildId;                         // HTML 侧标记
  if (resBuild && currentPkg.buildId !== resBuild) {
    return null;                                                // 版本错配：放行真网
  }
  return currentPkg.files[req.path] ?? null;                    // 命中返回本地映射
}
```
