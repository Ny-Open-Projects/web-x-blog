---
title: "[JA-015] Spring AI·api-key（配置）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · api-key（配置）

- **事实**：OpenAI 模型接入配置属性以 spring.ai.openai 前缀：api-key 配密钥，chat.options.model 配默认模型
- **原理**：自动装配依据这些属性构建 ChatModel bean，密钥必须走环境变量或配置中心不入库
- **常见误区**：
  1. 密钥直接写在 application.yml 提交仓库（错）
  2. 属性前缀是 spring-ai（点号无）（错）
  3. 配置只在启动时读取且不能换模型（错）
- **工程用法**：OpenAI 接入标准配置
- **版本锚点**：Spring AI 1.0 GA
