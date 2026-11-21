---
title: "[JA-003] Spring AI·entity（结构化）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · entity（结构化）

- **事实**：ChatClient 结构化输出：.call().entity(MyDto.class) 直接得到 Java 对象
- **原理**：框架把目标类型转成 JSON Schema 注入提示词，返回 JSON 后反序列化，业务免手写解析
- **常见误区**：
  1. entity 返回 JSON 字符串（错）
  2. entity 只支持 String 类型（错）
  3. 结构化输出不需要提示词工程（框架内部做了约定注入）（错）
- **工程用法**：下游强类型消费（报表/工单结构）
- **版本锚点**：Spring AI 1.0 GA
