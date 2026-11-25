---
title: [MFW-235] Next.js 图片字体优化的深水配置
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-235：图片与字体优化深水

**答**:
- next/image 的深水：remotePatterns 精确白名单（协议/端口/路径——宽松 hostname 是 SSRF 面）、sizes 属性必须与布局匹配（否则拉错尺寸——最大 CLS 与流量来源）、priority 只给 LCP 图（多个 priority 互相挤）、unoptimized 场景（自建 CDN 已处理时关优化器省 CPU）
- 图片优化器的代价：按需转换的 CPU 成本与缓存命中率——高流量站预生成（构建期 export 全尺寸）或换第三方图片服务（imgproxy）+ 简单 img
- next/font：构建期子集化 + 自托管（零外部请求防隐私 GDPR）+ 零布局偏移（size-adjust 自动算）——换掉手写 @font-face 的理由
- 组合验收：Lighthouse 图片审计全绿 + CLS 图片贡献 = 0

```javascript
images: {
  remotePatterns: [{ protocol: 'https', hostname: 'cdn.example.com', pathname: '/img/**' }],
  formats: ['image/avif', 'image/webp'], deviceSizes: [...], // 按真实断点裁剪
}
// fonts: next/font/google（构建期子集+自托管）→ className 直用
```
