---
title: [PER-396] 首屏图片策略的动态选择：按设备/网络/角色（首图 vs 配图）分配不同的加载策略？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-396：首屏图片策略的动态选择：按设备/网络/角色分配不同的加载策略？

**答**：
- 图片角色分型：Hero（LCP 候选，必须最高优先）、内容图（首屏可见但非最大）、次屏图（懒加载）、装饰图（可省略）。策略按"角色 × 设备 × 网络"三维决定——同一张图在不同象限走完全不同的加载路径。
- 策略矩阵（示例）：Hero × 弱网 → 预览图（10KB LQIP）先占位 + 渐进替换；Hero × 快网 → AVIF 原图 fetchpriority=high；内容图 × 任意 → srcset + loading=lazy + rootMargin 200px；装饰图 × 弱网 → 直接不加载。
- 动态选择实现：SSR 输出时根据请求头（Save-Data/User-Agent/视口 hints）选择初始策略；客户端接管后按 runtime 信号（网络档位/内存 deviceMemory）二次调整；CSS 的 image-set 与 HTML srcset 双轨。
- 验收：各象限的图片流量与 LCP 贡献分别度量（弱网 Hero 预览图让 LCP 提前 1.2s 的实测数据），避免"一刀切高清"或"一刀切低清"两个极端。

```javascript
function pickImageStrategy({ role, tier, deviceMemory }) {
  if (role === 'hero') {
    if (tier === 'slow') return { src: 'hero-lqip.avif', fetchpriority: 'high', upgrade: true };   // 先占位后升级
    return { src: 'hero.avif', fetchpriority: 'high', sizes: '100vw' };
  }
  if (role === 'content') return { srcSet: SRCSET, loading: 'lazy', rootMargin: '200px' };
  if (role === 'decor') return tier === 'fast' && deviceMemory > 4
    ? { src: 'decor.avif', loading: 'lazy' } : { skip: true };              // 弱网/低端机：装饰图不加载
  return { srcSet: SRCSET, loading: 'lazy' };
}
// LCP 贡献验收：弱网象限 Hero 预览图 → LCP -1.2s；图片流量分象限监控防"全体高清"
```
