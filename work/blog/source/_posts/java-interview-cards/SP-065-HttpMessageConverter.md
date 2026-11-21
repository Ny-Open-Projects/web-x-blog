---
title: "[SP-065] Boot·HttpMessageConverter（web）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · HttpMessageConverter（web）

- **事实**：@RequestBody/@ResponseBody 由 HttpMessageConverter 完成 JSON 与对象转换
- **原理**：默认 Jackson，配置 ObjectMapper 定制（时间格式、null 处理、Long 转字符串防前端精度丢失）
- **常见误区**：
  1. @RequestBody 由反射解析（错）
  2. Jackson 不可定制（错）
  3. Long 转 String 没有必要（前端 JS Number 超过 2^53 会丢精度所以必要）（错）
- **工程用法**：统一响应与序列化定制
- **版本锚点**：Spring MVC 文档
