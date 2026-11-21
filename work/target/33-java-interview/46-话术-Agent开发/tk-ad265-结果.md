---
title: "[话术AD-265] 手写·结果（包装）· 7 问"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 手写 · 结果（包装）—— 7 类问法与标准话术

**Qagent-dev-1849（概念考察·P1-P3）**
【面试官】请谈谈你对「手写」中「清单」的理解。
【标准回答话术】Agent 依赖注入清单：ModelClient/ToolRegistry/TrajectoryRecorder/BudgetCounter/Config 五依赖构造器注入（AD-186 类图的实例化清单），构造器注入便于测试（AD-189 mock）。背后的原理是：依赖注入清单是可测试性的保障（每依赖可 mock），字段注入（@Autowired 字段）不利于测试（SP-023 构造器推荐），与 Spring 集成（AD-280）联动。
【评分点】① 准确说出核心机制（清单）；② 能带出原理层而非背结论。 ③ 版本锚点：实战共识

---

**Qagent-dev-1850（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「依赖字段注入即可」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：Agent 依赖注入清单：ModelClient/ToolRegistry/TrajectoryRecorder/BudgetCounter/Config 五依赖构造器注入（AD-186 类图的实例化清单），构造器注入便于测试（AD-189 mock）。原因是：依赖注入清单是可测试性的保障（每依赖可 mock），字段注入（@Autowired 字段）不利于测试（SP-023 构造器推荐），与 Spring 集成（AD-280）联动。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（实战共识）。

---

**Qagent-dev-1851（原理深挖·P5-P7）**
【面试官】「清单」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：依赖注入清单是可测试性的保障（每依赖可 mock），字段注入（@Autowired 字段）不利于测试（SP-023 构造器推荐），与 Spring 集成（AD-280）联动。落到结论：Agent 依赖注入清单：ModelClient/ToolRegistry/TrajectoryRecorder/BudgetCounter/Config 五依赖构造器注入（AD-186 类图的实例化清单），构造器注入便于测试（AD-189 mock）。
【评分点】① 讲出注入层面的机制；② 结论与机制对应不脱节。

---

**Qagent-dev-1852（工程落地·P7-P9）**
【面试官】在你带过的项目里，「清单」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：Agent 依赖注入清单：ModelClient/ToolRegistry/TrajectoryRecorder/BudgetCounter/Config 五依赖构造器注入（AD-186 类图的实例化清单），构造器注入便于测试（AD-189 mock）。补充要点：注入清单。常见误区要规避：依赖字段注入即可。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qagent-dev-1853（结论依据·P8-P10）**
【面试官】关于「清单」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：实战共识。事实与结论：Agent 依赖注入清单：ModelClient/ToolRegistry/TrajectoryRecorder/BudgetCounter/Config 五依赖构造器注入（AD-186 类图的实例化清单），构造器注入便于测试（AD-189 mock）。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qagent-dev-1854（边界追问·P6-P9）**
【面试官】「清单」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「依赖字段注入即可」是常见误区。正确的边界：Agent 依赖注入清单：ModelClient/ToolRegistry/TrajectoryRecorder/BudgetCounter/Config 五依赖构造器注入（AD-186 类图的实例化清单），构造器注入便于测试（AD-189 mock）。使用要点：注入清单。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qagent-dev-1855（追问链·P5-P8）**
【面试官】追问：如果有人按「五依赖清单是负担」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：Agent 依赖注入清单：ModelClient/ToolRegistry/TrajectoryRecorder/BudgetCounter/Config 五依赖构造器注入（AD-186 类图的实例化清单），构造器注入便于测试（AD-189 mock）。原理：依赖注入清单是可测试性的保障（每依赖可 mock），字段注入（@Autowired 字段）不利于测试（SP-023 构造器推荐），与 Spring 集成（AD-280）联动。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
