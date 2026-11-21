---
title: "[话术AD-147] 工程·续跑（体验）· 7 问"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 工程 · 续跑（体验）—— 7 类问法与标准话术

**Qagent-dev-1023（概念考察·P4-P6）**
【面试官】请谈谈你对「手写」中「类设计」的理解。
【标准回答话术】手写 Agent 的类结构设计：AgentExecutor（循环）/ToolRegistry（注册表 AD-051）/Message（AD-062）/ModelClient（抽象 AD-189）/TrajectoryRecorder（AD-040）五类，类图即架构。背后的原理是：五类划分是手写 Agent 的最小架构（每类单一职责 JA-051 注册表），类设计先于编码（面试手写先画类图），与面向对象设计联动。
【评分点】① 准确说出核心机制（类设计）；② 能带出原理层而非背结论。 ③ 版本锚点：实战共识

---

**Qagent-dev-1024（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「手写 Agent 一个类搞定」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：手写 Agent 的类结构设计：AgentExecutor（循环）/ToolRegistry（注册表 AD-051）/Message（AD-062）/ModelClient（抽象 AD-189）/TrajectoryRecorder（AD-040）五类，类图即架构。原因是：五类划分是手写 Agent 的最小架构（每类单一职责 JA-051 注册表），类设计先于编码（面试手写先画类图），与面向对象设计联动。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（实战共识）。

---

**Qagent-dev-1025（原理深挖·P5-P7）**
【面试官】「类设计」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：五类划分是手写 Agent 的最小架构（每类单一职责 JA-051 注册表），类设计先于编码（面试手写先画类图），与面向对象设计联动。落到结论：手写 Agent 的类结构设计：AgentExecutor（循环）/ToolRegistry（注册表 AD-051）/Message（AD-062）/ModelClient（抽象 AD-189）/TrajectoryRecorder（AD-040）五类，类图即架构。
【评分点】① 讲出结构层面的机制；② 结论与机制对应不脱节。

---

**Qagent-dev-1026（工程落地·P7-P9）**
【面试官】在你带过的项目里，「类设计」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：手写 Agent 的类结构设计：AgentExecutor（循环）/ToolRegistry（注册表 AD-051）/Message（AD-062）/ModelClient（抽象 AD-189）/TrajectoryRecorder（AD-040）五类，类图即架构。补充要点：手写类设计。常见误区要规避：手写 Agent 一个类搞定。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qagent-dev-1027（结论依据·P8-P10）**
【面试官】关于「类设计」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：实战共识。事实与结论：手写 Agent 的类结构设计：AgentExecutor（循环）/ToolRegistry（注册表 AD-051）/Message（AD-062）/ModelClient（抽象 AD-189）/TrajectoryRecorder（AD-040）五类，类图即架构。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qagent-dev-1028（边界追问·P6-P9）**
【面试官】「类设计」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「手写 Agent 一个类搞定」是常见误区。正确的边界：手写 Agent 的类结构设计：AgentExecutor（循环）/ToolRegistry（注册表 AD-051）/Message（AD-062）/ModelClient（抽象 AD-189）/TrajectoryRecorder（AD-040）五类，类图即架构。使用要点：手写类设计。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qagent-dev-1029（追问链·P5-P8）**
【面试官】追问：如果有人按「五类是过度设计」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：手写 Agent 的类结构设计：AgentExecutor（循环）/ToolRegistry（注册表 AD-051）/Message（AD-062）/ModelClient（抽象 AD-189）/TrajectoryRecorder（AD-040）五类，类图即架构。原理：五类划分是手写 Agent 的最小架构（每类单一职责 JA-051 注册表），类设计先于编码（面试手写先画类图），与面向对象设计联动。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
