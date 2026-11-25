---
title: [MFW-258] 图片优化器的容量与成本治理
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-258：图片优化器容量治理

**答**:
- 成本结构：on-demand 转换（CPU 密集）× 唯一 URL 数（尺寸×格式×图数）——长尾图首次访问打满 CPU，缓存命中率决定成本曲线
- 治理四招：①deviation 预算：deviceSizes 裁到真实断点（默认 8 档太宽——每种尺寸都是独立缓存键）②预热：发布后对热门图预拉全尺寸（首访不发转换）③offload：大图/动态图外移专用服务（imgproxy）——next/image 只管站内小图 ④命中率监控（优化器缓存命中 P95）
- 安全面：remotePatterns 白名单 + 内容类型校验（防开放代理——图片优化器会被当 SSRF 跳板）

```text
四招：断点裁剪（8→3 档） / 热门预热 / 大图 offload / 命中率监控
安全：remotePatterns 白名单 + content-type 校验（防 SSRF 跳板）
```
