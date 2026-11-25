---
title: [PER-1104] 如何应对"前端被嵌入恶意环境"（WebView 注入/劫持网络）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1104：如何应对"前端被嵌入恶意环境"（WebView 注入/劫持网络）

**答**：
- 环境检测：检测 WebView 是否被注入（window 对象异常属性）、代理/VPN（结合 App 上报）、证书校验失败（App 层）。
- 响应：检测到异常环境降级功能（只读模式/拒绝敏感操作）、上报环境指纹辅助风控。
- 数据保护：敏感操作走 App 原生通道（不经过可能被劫持的 WebView JS 环境）。
- OTA 对抗：热修通道本身要签名校验（1099），防止"修复通道"被劫持成攻击通道。

```javascript
// WebView 环境体检
function webviewAudit() {
  const anomalies = [];
  const known = new Set(Object.keys(window));
  if (known.has('__ injected_hook__')) anomalies.push('hook 检测');
  if (navigator.userAgent.includes('Xposed') ||
      navigator.userAgent.includes('Frida')) anomalies.push('UA 特征');
  if (!window.crypto?.subtle) anomalies.push('crypto 被替换');
  return { anomalies,
    policy: anomalies.length ? 'deny-sensitive' : 'normal' };
}
// policy=deny-sensitive 时支付/实名入口隐藏，仅保留浏览
```
