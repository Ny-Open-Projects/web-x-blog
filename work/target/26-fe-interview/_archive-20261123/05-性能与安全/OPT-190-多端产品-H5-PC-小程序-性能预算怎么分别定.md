---
title: [OPT-190] 多端产品（H5/PC/小程序）性能预算怎么分别定标？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-190：多端产品（H5/PC/小程序）性能预算怎么分别定标？

**答**：
- 预算必须按端差异化：H5 弱网+低端机多（LCP ≤ 2.5s、JS ≤ 200KB gzip）；PC 网络好但用户期望更高（LCP ≤ 2s、JS ≤ 300KB，因为 PC 页面更重）；小程序有包体硬限制（主包 ≤ 2MB，首屏启动分包策略）。
- 每端预算维度统一：体积（JS/CSS/图片）、指标（LCP/INP/CLS）、接口（首屏 API 时延）、数量（请求数/第三方脚本数），数值按端标定。
- 预算推导方法：以当前 P75 基线 + 竞品对标 + Core Web Vitals 达标线三方取严；预算写进 size-limit/CI 按端独立配置。
- 定期校准：每半年按设备分布变化（新 iPhone 普及、低端安卓占比）重标，预算是活的。

```yaml
# 一一对应：多端性能预算矩阵（size-limit 按端分文件校验）
budgets:
  h5:
    metrics: { lcp_p75: 2.5s, inp_p75: 200ms, cls_p75: 0.1 }   # CWV 达标线
    size: { js_gzip_total: 200KB, css_gzip: 50KB, img_first_screen: 300KB }
    api: { first_screen_p75: 800ms, max_requests_first_screen: 25 }
    note: 弱网+低端机占比高，指标按 75 分位在 4G 语义下标定
  pc:
    metrics: { lcp_p75: 2.0s, inp_p75: 200ms, cls_p75: 0.1 }
    size: { js_gzip_total: 300KB, css_gzip: 70KB, img_first_screen: 500KB }
    api: { first_screen_p75: 600ms, max_requests_first_screen: 30 }
    note: 页面更重但网络优，用户耐心低
  miniprogram:
    package: { main: 1.5MB, total: 12MB }    # 微信硬限：主包 2M 总包 20M，留余量
    metrics: { first_render_p75: 1500ms, data_ready_p75: 2500ms }  # 启动口径
    api: { first_screen_p75: 1000ms }
    note: 小程序无 CWV，用启动与数据就绪自定义口径，分包按需注入

ci:
  size-limit-config: .size-limit-h5.json + .size-limit-pc.json   # 按端独立阻塞
  rum_alert: 每端独立基线，劣化 15% 告警
  review_cadence: 每半年按设备分布重标定
```
