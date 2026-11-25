---
title: [RBL-339] 构建系统的 OS 差异与路径处理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-339：构建系统的 OS 差异与路径处理

**答**:
- 差异清单：路径分隔符（win \ vs unix /）、大小写敏感（mac 不敏感 linux 敏感——import 大小写错误本地正常 CI 炸）、换行符（CRLF/LF 影响内容 hash）、文件锁与长路径（win 260 字符限制）
- 治理：路径一律用 path.join/url（不手拼字符串）、eslint 大小写强制规则、editorconfig LF 统一 + git autocrlf input、产物路径归一化（统一 /）——hash 稳定性的跨平台基础
- CI 验证：linux runner 是事实标准——本地 windows/mac 开发必须 CI 兜底；跨平台产物 hash 一致性测试（见 RBL-282 矩阵）

```text
差异四项：分隔符 / 大小写 / 换行 / 长路径
治理：path API / 大小写 lint / editorconfig+autocrlf / 产物路径归一化
```
