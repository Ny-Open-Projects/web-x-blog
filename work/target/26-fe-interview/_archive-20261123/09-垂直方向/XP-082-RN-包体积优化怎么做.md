---
title: [XP-082] RN 包体积优化怎么做？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-082：RN 包体积优化怎么做？
**答**：
- 先拆构成再治理：**原生 so 与引擎（Hermes）、JS bundle（.hbc）、assets 图片、三方原生库**四大头，用 apk-analyzer / bloaty / bundle-report 建体积清单。
- so 治理：按 ABI 拆分（App Store/Google Play 均支持 per-abi 分发）、R8/ProGuard 收缩 Java 层、去除冗余架构（x86 仅保留在模拟器变体）。
- bundle 治理：Hermes 字节码（比源码包更小且执行更快）、inline-requires 移除启动期引用、三方依赖审计（moment→dayjs、lodash 全量→按需）、拆 bundle（XP-077）。
- 资源治理：PNG→WebP/SVG（react-native-svg）、图片走 CDN 下发不进包、语言资源子集化、字体子集。
- 门禁：CI 体积预算（超阈值阻断合并）+ 体积 diff 报告到 PR（治理口径与 XP-116 跨端包体积看板对齐）。

```text
RN 包体积治理清单（Android APK 为例，iOS 同思路）
构成拆解：
  lib/**/**.so           ~40-60%   Hermes 引擎 + 三方原生库（按 ABI 拆分后单架构统计）
  assets/bundle .hbc     ~15-25%   JS 字节码与图片资源
  classes.dex            ~10-15%   Java/Kotlin 层（R8 收缩）
  res                    ~5-10%    壳资源

手段与预期收益：
  per-abi 拆分           总包 -40%+（用户实际下载单架构）
  Hermes 字节码          bundle 更小 且启动更快（XP-077 联动）
  R8 minify+shrink       dex -30%~50%
  依赖瘦身               moment/lodash 类替换，bundle -5%~15%
  图片 WebP/SVG + CDN    assets -50%+（运营图一律 CDN 下发不进包）
  拆 bundle 按需加载     基座只含首屏（XP-077）

CI 门禁（口径对齐 XP-116）：
  budget: { androidApkMB: 45, iosIpaMB: 55, diffLimitKB: 200 }
  超预算 → CI fail，附体积 diff 明细，需平台组审批豁免
```
