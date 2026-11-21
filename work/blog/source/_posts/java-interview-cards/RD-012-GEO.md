---
title: "[RD-012] 扩展类型·GEO（GEO）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 扩展类型 · GEO（GEO）

- **事实**：GEO 用 ZSet 编码（GeoHash 打进 score）实现地理位置搜索
- **原理**：GEOADD/GEOSEARCH（6.2 命令化），附近的人/门店搜索场景，底层是 52 位 GeoHash 编码
- **常见误区**：
  1. GEO 是独立存储引擎（错）
  2. GeoHash 是字符串前缀匹配（错）
  3. GEO 支持多边形查询（错）
- **工程用法**：LBS 功能实现
- **版本锚点**：Redis 6.2
