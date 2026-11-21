---
title: [PER-323] Safari 与 Chrome 的存储配额/淘汰差异有多大？跨浏览器离线策略怎么写才稳？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-323：Safari 与 Chrome 的存储配额/淘汰差异有多大？跨浏览器离线策略怎么写才稳？

**答**：
- 关键差异：Safari（WebKit）历史上对"7 天不访问即清除脚本可写存储"（ITP 7-day cap，localStorage/IDB 对无站点交互的源过期清除），Chrome 按 LRU 配额压力淘汰、无固定 7 天策略；Safari 的 IDB 配额较保守（约 1GB 量级、按磁盘比例），Cache API 与 IDB 共享池。iOS 全系 WebKit，策略随版本变化大，必须 runtime 探测而非硬编码。
- 稳妥策略：① 不假设持久——关键数据服务端有副本，本地只做"缓存/草稿"；② persist 申请后验证 persisted() 结果，失败即启动"短命缓存"模式（TTL 缩短、用量预算减半）；③ 存储不可用时全量降级内存缓存（运行时可用的兜底）；④ 版本探测：estimate() 失败/无 StorageManager 直接走保守路径。
- 7 天 cap 的对策：对"必须存活超过 7 天"的数据——服务端同步（登录后拉取）、或引导用户 PWA 安装（安装的 PWA 豁免 ITP 7 天 cap）；业务上把 localStorage 的会话性当成设计前提。

```javascript
// 跨浏览器探测与分级策略
async function storageTier() {
  if (!navigator.storage?.estimate) return 'minimal';       // 老浏览器：内存缓存为主
  const { usage, quota } = await navigator.storage.estimate();
  const persisted = await navigator.storage.persisted?.() ?? false;
  if (persisted) return 'persistent';                        // 可长期存
  if (quota > 500 * 1048576) return 'generous';              // 大配额（Chrome 桌面）
  return 'conservative';                                     // Safari/移动：短 TTL + 小预算
}
// 各档位配置：
// persistent: 离线包预算 200MB, TTL 30 天
// generous:   预算 100MB, TTL 14 天
// conservative: 预算 30MB, TTL 3 天（对齐 ITP 7 天 cap 的安全边距）
// minimal:    内存 Map 缓存，页面刷新即失效
```
