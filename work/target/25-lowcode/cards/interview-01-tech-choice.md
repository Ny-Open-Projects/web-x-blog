---
title: 面试卡：技术选型话术
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 面试, 选型]
---

## 面试卡：技术选型话术

面试官考察点四件：**选择依据、决策过程、可替换方案对比、可持续性**。

**三维度框架**：①项目——周期长短、规模、是否 SEO（→Next.js/Nuxt）、是否跨端（→Uni App/Flutter/RN）；②团队——成员技术栈、要有"兜底人"、招聘成本与冷门技术风险；③技术——GitHub star/npm 下载量、生态维护状态、兼容性。

**本项目话术样例**：
- 状态管理选 MobX 不选 Redux：配置更简单，响应式适合编辑器频繁局部更新（注意坑：Vuex 默认响应式而 MobX 必须 observer）。
- 后端选 NestJS：内置 DI/Pipe/Guard，TS 优先，适合中大型项目；与 Express（轻量）/Koa（极简需自行组装）对比。
- 发布端选 Next.js：SSR 直出 HTML 利于 SEO；注意别把 Next.js（React SSR 框架）误说成 NestJS（Node 后端框架）——名词错误一票否决。

**经典面试案例**（课程给的两份简历亮点）：①图形验证码+短信验证码+Redis 原子性防重提交；②DevOps CI/CD 一键部署。每个亮点要能讲清"为什么做"。

出处「课程25 · 2-3~2-9、31-1」
