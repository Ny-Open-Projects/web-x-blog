---
title: [XP-089] Flutter 包体积优化怎么做？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-089：Flutter 包体积优化怎么做？
**答**：
- 体积大头：**引擎与 framework（双端各 ~10MB+ 级）、AOT 产物（libapp.so / App.framework）、字体与图片资源、图标树**；先 `flutter build apk --analyze-size` / DevTools 体积视图拆构成。
- 编译期手段：`--obfuscate --split-debug-info`（混淆并把符号表外置缩小产物）、`--split-per-abi`（so 按架构拆分）、Android `deferred components`（动态 feature 下发 Dart 产物，iOS 受限）。
- 资源治理：字体子集化（fonttools 按实际字符裁剪，中文字体收益巨大）、图片 WebP/压缩、`flutter_tree_shake_icons`（Material 图标按使用裁剪）、未引用资产清理（CI 脚本比对资产清单）。
- 依赖治理：pubspec 依赖审计，砍掉只为一个小工具引入的整包；平台侧 Android 用 R8、iOS 检查无用 framework。
- 门禁与口径：CI 记录双端体积趋势，diff 超 200KB 报警；基线口径与 XP-116 跨端包体积对比统一，防止"优化了 A 端把资产塞进 B 端"。

```yaml
# .github/workflows/flutter-size.yml —— 体积门禁与产物分析
name: flutter-size-guard
on: [pull_request]
jobs:
  size:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
      - name: build with size analysis
        run: |
          flutter build apk --release \
            --obfuscate --split-debug-info=build/symbols \  # 混淆+符号外置（崩溃还原用）
            --split-per-abi \                               # so 按 abi 拆分
            --analyze-size \                                # 产出体积构成报告
            --target-platform android-arm64
      - name: budget gate
        run: dart run tool/size_gate.dart --budget 45 --diff-limit 200
        # budget: 单架构 apk 上限 45MB；diff-limit: 相对 main 超 200KB 报警阻断
      - name: asset audit
        run: dart run tool/asset_audit.dart   # 未引用资产/超大图片/未子集化字体 清单
# 资源治理配套：中文字体 fonttools 子集化后体积常从 8MB 级降到 1MB 级
```
