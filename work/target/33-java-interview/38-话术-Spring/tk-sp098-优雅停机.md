---
title: "[话术SP-098] 容器·优雅停机（关闭）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 容器 · 优雅停机（关闭）—— 7 类问法与标准话术

**Qspring-680（概念考察·P1-P3）**
【面试官】请谈谈你对「容器」中「优雅停机」的理解。
【标准回答话术】Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。背后的原理是：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep。
【评分点】① 准确说出核心机制（优雅停机）；② 能带出原理层而非背结论。 ③ 版本锚点：Boot 2.3

---

**Qspring-681（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「默认就是优雅停机」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。原因是：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（Boot 2.3）。

---

**Qspring-682（原理深挖·P5-P7）**
【面试官】「优雅停机」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep。落到结论：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。
【评分点】① 讲出关闭层面的机制；② 结论与机制对应不脱节。

---

**Qspring-683（工程落地·P7-P9）**
【面试官】在你带过的项目里，「优雅停机」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。补充要点：发布零中断的基础配置。常见误区要规避：默认就是优雅停机。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-684（版本演进·P8-P10）**
【面试官】关于「优雅停机」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：Boot 2.3。事实层面：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qspring-685（边界追问·P6-P9）**
【面试官】「优雅停机」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「默认就是优雅停机」是常见误区。正确的边界：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。使用要点：发布零中断的基础配置。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-686（追问链·P5-P8）**
【面试官】追问：如果有人按「SIGTERM 会被忽略直接杀」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：Boot 2.3+ 优雅停机：server.shutdown=graceful 等待请求完成再关容器。原理：K8s 删除 Pod 时先 SIGTERM，停机期 Tomcat 停接新请求等存量完成（超时 spring.lifecycle.timeout-per-shutdown-phase），配合 preStop sleep。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
