---
title: [SCN-568] 验证 SDK 的版本管理与灰度发布怎么做？SDK 升级怎么不炸业务？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-568：验证 SDK 版本管理与灰度怎么做？
**答**：
- 版本策略：SDK 提供 stable/beta 双通道，业务声明兼容范围（semver）；重大 API 变更提前一个 minor 弃用告警。
- 灰度：按业务流量百分比 + 白名单设备灰度新版本；SDK 上报版本号，监控分版本看错误率与通过率，异常自动回切。
- 契约保护：SDK 对外接口不变式（onPass/onFail 语义）用契约测试守护；验证器插件接口版本化（v2 并存 v1）。
- 兜底开关：每个业务可配置「最低可用版本」——低于它时走降级验证，防止坏版本扩散。
- 追问钩子：SDK 与业务不同发版节奏怎么对齐——SDK 自更新（CDN 动态脚本）+ 业务声明区间，解耦发布。

```html
<!-- 动态加载 + 版本通道 -->
<script>
  const CHANNEL = flag('risk_sdk_channel') || 'stable';
  loadScript(`https://cdn.example.com/risk-sdk/v2/${CHANNEL}/index.js`)
    .then(() => window.RiskSDK.init({
      version: window.RiskSDK.version,
      minVersion: '2.3.0',                        // 业务声明的最低可用版本
      onDeprecate: (api) => report({ type: 'SDK_DEPRECATE', api }),
    }));
</script>
```
