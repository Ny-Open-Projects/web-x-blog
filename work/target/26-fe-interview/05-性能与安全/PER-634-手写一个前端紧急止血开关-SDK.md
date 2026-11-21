---
title: [PER-634] 手写一个前端紧急止血开关 SDK：配置中心下发的 kill switch，支持按路由/功能一键降级
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-634：手写一个前端紧急止血开关 SDK：配置中心下发的 kill switch，支持按路由/功能一键降级

**答**：
- 设计：SDK 启动时拉取远程开关配置（带本地缓存兜底），轮询/推送更新；开关粒度：全局/路由/功能点三级；消费方用 `kill.isActive('pay-page')` 判断是否降级。
- 要点：配置拉取失败用上次缓存（不能因为配置服务挂了开关失效）；开关变更要落审计日志（谁在何时关了什么）；缓存带版本号防回滚到旧配置。
- 边界：开关判断不能阻塞主流程（内存读取，不做网络）；默认安全（配置缺失时核心功能放行、非核心可配置默认关）。
- 评分点：缓存兜底与默认安全策略。

```javascript

class KillSwitch {
  constructor(configUrl, { pollMs = 30000 } = {}) {
    this.flags = JSON.parse(localStorage.getItem('ks-cache') ?? '{}');
    this.configUrl = configUrl;
    this.refresh(); setInterval(() => this.refresh(), pollMs);
  }
  async refresh() {
    try {
      const res = await fetch(`${this.configUrl}?v=${this.flags.version ?? 0}`, { cache: 'no-store' });
      if (res.status === 304) return;                     // 版本未变
      const cfg = await res.json();
      if (cfg.version >= (this.flags.version ?? 0)) {     // 防旧配置覆盖新配置
        this.flags = cfg;
        localStorage.setItem('ks-cache', JSON.stringify(cfg));
      }
    } catch { /* 拉取失败 -> 沿用缓存，开关不失效 */ }
  }
  isActive(key, route = location.pathname) {
    const f = this.flags.flags?.[key];
    if (!f) return false;                                 // 默认放行（默认安全）
    return f.global === true || (f.routes ?? []).some(r => route.startsWith(r));
  }
}
// 用法：if (ks.isActive('pay-page')) renderMaintenance(); else renderPay();
```
