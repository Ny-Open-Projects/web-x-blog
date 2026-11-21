---
title: 面试卡：低代码项目亮点话术
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 面试, 项目亮点]
---

## 面试卡：低代码项目亮点话术

**项目一句话**：非开发人员也能零代码发布官网与问卷系统，降门槛、加速交付、易应对变更。

**六大亮点及展开点**：
1. **pnpm workspace 最大复用**：share 包统一放 AntD 组件/types 类型/utils 工具，编辑端与发布页复用同一套 15 种组件（unbuild 打 ESM/CJS/d.ts 三产物）；
2. **组件数据结构设计**：配置字典（id→配置）+ 排序数组（表达画布顺序）分离，一切画布操作 = 对这两份数据的增删改查；
3. **拖拽+键盘双交互**：dnd-kit 拖拽本质是 arrayMove 索引交换，与键盘上移/下移共用同一 action；mobx-shallow-undo 撤销重做；
4. **一键部署**：云效 CI/CD + Docker 四镜像 + 双 Nginx + React 上 OSS（部署位置区分能讲清）；
5. **验证码防刷**：图形验证码+短信验证码+Redis 自定义 key+原子性防重提交（动机 = 短信成本）；
6. **数据侧**：在线 Excel/压缩包导出 + ECharts 动态图表 + Next.js SSR 优化 SEO。

**追问预案**：时间戳取舍逻辑（storeTime vs releaseTime）、事务化发布为什么开事务、草稿机制存了什么。

出处「课程25 · 1-2、31-4」
