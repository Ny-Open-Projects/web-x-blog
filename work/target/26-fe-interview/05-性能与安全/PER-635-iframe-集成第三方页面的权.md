---
title: [PER-635] iframe 集成第三方页面的权限最小化怎么做？Permissions-Policy 与 sandbox 的组合拳
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-635：iframe 集成第三方页面的权限最小化怎么做？Permissions-Policy 与 sandbox 的组合拳

**答**：
- 权限最小化三层：**sandbox 属性**（无 allow 值=最严格，逐项放开 allow-scripts/allow-forms/allow-same-origin——注意 allow-scripts + allow-same-origin 同时给等于没沙箱）、**Permissions-Policy**（页面级声明摄像头/麦克风/定位/剪贴板等能力的可用性，`camera=()` 全禁，iframe 的 `allow` 属性做按帧放行）、**CSP frame-src**（限制能嵌哪些域）。
- 常见错误：图省事 `sandbox="allow-scripts allow-same-origin"`（第三方若被攻破可反制父页面）；允许 fullscreen/payment 但业务根本用不到。
- 落地策略：从全禁开始，按第三方实际需要逐项放开并记录为什么放开"；Permissions-Policy 在响应头统一配置（`camera=(), microphone=(), geolocation=(self)`），iframe 级用 allow 属性覆盖更窄范围。
- 验证：集成测试断言第三方 iframe 内 getUserMedia 被拒绝、无法访问父页面存储。

```javascript

// 第三方 iframe 权限最小化模板
const iframePolicy = {
  html: `<iframe src="https://partner.com/widget"
    sandbox="allow-scripts allow-forms"          <!-- 最小集：脚本+表单 -->
    allow="fullscreen"                            <!-- 按帧放行，仅声明用到的 -->
    referrerpolicy="strict-origin-when-cross-origin"
    loading="lazy"></iframe>`,
  headers: {
    // 页面级全局收敛：所有人（含自己）默认禁用高危能力
    'Permissions-Policy': 'camera=(), microphone=(), geolocation=(self), usb=(), clipboard-write=(self)',
  },
  rules: [
    '禁止 allow-scripts + allow-same-origin 组合（等于无沙箱）',
    '每个 allow 项都要有业务理由记录',
    'frame-src 限定第三方域，禁止 *',
  ],
};
console.log(iframePolicy.rules.join('；'));
```
