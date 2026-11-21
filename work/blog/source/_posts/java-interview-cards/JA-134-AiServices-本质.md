---
title: "[JA-134] LangChain4j·AiServices 本质（装配）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · AiServices 本质（装配）

- **事实**：AiServices 本质是动态代理工厂：接口调用被拦截转为 LLM 请求+工具循环
- **原理**：理解代理本质才能定制（拦截/包装/测试桩），与 AOP 动态代理知识（SP-037）同构
- **常见误区**：
  1. AiServices 用了字节码生成库（错）
  2. 代理只能返回字符串（错）
  3. 拦截过程不可观测（错）
- **工程用法**：框架机制理解
- **版本锚点**：LangChain4j 1.0
