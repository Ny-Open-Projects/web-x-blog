---
title: "[SP-071] Boot·nested jar（可执行 jar）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · nested jar（可执行 jar）

- **事实**：Spring Boot 可执行 jar 用嵌套 jar 结构由 LaunchedURLClassLoader 加载
- **原理**：依赖打进 BOOT-INF/lib 内部 jar，启动类 JarLauncher 引导，解法解决了"fat jar 在容器内 classpath 问题"，代价是类加载稍慢
- **常见误区**：
  1. Boot jar 与普通 jar 结构相同（错）
  2. 外部容器部署与可执行 jar 类加载一致（错）
  3. BOOT-INF 是可选目录（错）
- **工程用法**：理解 fat jar 加载原理
- **版本锚点**：Boot 文档
