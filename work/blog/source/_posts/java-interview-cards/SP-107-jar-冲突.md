---
title: "[SP-107] IoC·jar 冲突（坑）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · jar 冲突（坑）

- **事实**：依赖冲突是 Boot 项目第一大故障源（mvn dependency:tree 排查）
- **原理**：同一库多版本导致 NoSuchMethodError/ClassNotFoundException，用 dependencyManagement 统一版本、BOM 管理第三方（如 spring-cloud-bom）
- **常见误区**：
  1. Maven 自动选最优版本无冲突（错）
  2. 冲突报错都发生在启动时（错）
  3. exclude 不是标准解法（错）
- **工程用法**：依赖治理是 Boot 工程师基本功
- **版本锚点**：实战共识
