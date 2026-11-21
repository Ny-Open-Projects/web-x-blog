---
title: JMeter 压测实战：从线程组到聚合报告
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, JMeter, 性能]
---

## JMeter 压测实战：从线程组到聚合报告

**关键认知**：JMeter 是 Apache 基于 Java 的开源性能测试工具，**不是浏览器**——协议层工作，不执行 JS、不渲染 HTML，适合压测后端异步接口，不适合 UI 功能测试。与 Postman 的分工：性能压测 vs 接口功能调试。

**环境**：必须 JDK 8（高版本有兼容问题）；永久汉化改 `jmeter.properties` 的 `language=zh_CN`；中文乱码改 `sampleresult.default.encoding=UTF-8`。

**四件套**：线程组（线程数 × Ramp-Up × 循环次数）+ HTTP 请求默认值 + 信息头管理器 + 监听器。带鉴权接口加 `Authorization: Bearer <token>` 头；POST+JSON 必须设 `Content-Type: application/json`（否则 text/plain 后端解析失败）。

**读报告**：90% Line = 90% 请求响应时间低于该值（不是 90% 不出错，错误率看异常%）；聚合报告看 Throughput/Error%；跑前用扫把清空旧数据；调试先 10 线程/1s/循环1 跑通。

**进阶**：响应断言校验业务字段防"假成功"（高并发下少用正则，开销大拖垮压测机）；集合点（Synchronizing Timer）模拟秒杀瞬时高压，超时设 >0 防个别线程卡死整组；setUp/tearDown 线程组做前置登录拿 token 与清理。

出处「课程25 · 28-1~29-3」
