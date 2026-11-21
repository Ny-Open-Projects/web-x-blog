---
title: "[SP-003] Bean 生命周期·BeanPostProcessor（扩展点）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Bean 生命周期 · BeanPostProcessor（扩展点）

- **事实**：BeanPostProcessor 在初始化前后对每个 Bean 加工
- **原理**：postProcessBeforeInitialization 在 init 回调前、After 在之后，AOP 代理、@Autowired 填充、@PostConstruct 全靠它实现
- **常见误区**：
  1. BeanPostProcessor 只处理一次（错）
  2. BPP 前后处理都在初始化之后（错）
  3. BPP 不能修改 Bean（错）
- **工程用法**：Spring 扩展机制核心，插件体系的基石
- **版本锚点**：Spring 源码
