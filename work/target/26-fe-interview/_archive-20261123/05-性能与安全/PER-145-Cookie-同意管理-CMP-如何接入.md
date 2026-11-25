---
title: [PER-145] Cookie 同意管理（CMP）如何接入？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-145：Cookie 同意管理（CMP）如何接入？

**答**：
- 接入三步：**页面头部同步 stub**（同意未就绪时第三方 SDK 调用先入队，防未同意即采集）→ **渲染分类开关**（必要/分析/营销三类，必要类不可关闭）→ **同意后按类加载**（未同意的脚本一个字节都不下载）。
- 与 Google Consent Mode 联动：默认 `denied`，用户同意后 `update`，SDK 内部自行控制采集粒度。
- 同意状态要**可撤回**：页脚常驻"Cookie 设置"入口，撤回后立即停对应 SDK 并清其 Cookie。
- 同意记录上送留痕（谁、何时、哪个版本、哪些类目），满足审计要求。

```html
<!-- CMP 接入：stub 占位 -> 分类开关 -> 同意后按类加载 -->
<script>
  // 1. 页面头部同步 stub：同意未就绪时 gtag 调用先入队，防未同意即采集
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  gtag('consent', 'default', { analytics_storage: 'denied', ad_storage: 'denied' }); // 默认全拒
</script>

<div id="cmp-banner" hidden>
  <p>我们使用 Cookie 提供基础功能与改进体验</p>
  <label><input type="checkbox" checked disabled> 必要 Cookie（始终开启）</label>
  <label><input type="checkbox" id="cmp-analytics"> 分析统计</label>
  <label><input type="checkbox" id="cmp-ads"> 营销推广</label>
  <button onclick="saveConsent()">保存选择</button>
</div>

<script>
  function saveConsent() {
    const analytics = document.getElementById('cmp-analytics').checked;
    const ads = document.getElementById('cmp-ads').checked;
    // 2. Consent Mode 更新：SDK 收到后自行控制采集粒度
    gtag('consent', 'update', { analytics_storage: analytics ? 'granted' : 'denied', ad_storage: ads ? 'granted' : 'denied' });
    localStorage.setItem('cmp-consent', JSON.stringify({ analytics, ads, ts: Date.now(), v: '2026-05-01' }));
    document.getElementById('cmp-banner').hidden = true;
    // 3. 未同意的脚本一个字节都不下载
    if (analytics) loadScript('/vendor/analytics.js');
    if (ads) loadScript('https://ads.example.com/sdk.js');
  }
  if (!localStorage.getItem('cmp-consent')) {
    document.getElementById('cmp-banner').hidden = false; // 无记录必须先询问
  }
</script>
```
