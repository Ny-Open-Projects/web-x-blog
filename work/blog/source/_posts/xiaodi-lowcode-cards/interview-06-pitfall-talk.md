---
title: 面试卡：踩坑谈资合集（真实 BUG 叙事）
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 面试, 踩坑, 排错]
---

## 面试卡：踩坑谈资合集（真实 BUG 叙事）

踩坑叙事的答法公式：**现象 → 定位过程 → 根因 → 修复 → 沉淀**。以下每条都可按此展开：

1. **数据库连不上**：`database` 填了 Docker 容器名而不是数据库名；顺带 mysql2 驱动漏装。
2. **发布接口"成功"但数据错**：事务内混用普通 repository 脱离事务管辖；catch 忘 rollback 留半成品；finally 不 release 连接泄漏。
3. **MobX 改了没反应**：组件没包 `observer`、列表没 `toJS`——Vuex 默认响应式而 MobX 必须 observer，迁移思维差异。
4. **轮播多图改第二张总改到第一张**：没维护当前展开项索引，补 itemExpandIndex + useEffect 同步修复。
5. **粘贴组件后行为异常**：复制粘贴必须 ulid 重新分配 ID。
6. **富文本样式全失效**：Tailwind base 重置了 h1~h6/ol/ul 默认样式，全局样式补回且放在 Tailwind 之后。
7. **CI 流水线三连败**：Dockerfile `FROM nginx:` 多冒号、文件名多字母、tar `-C` 误写 `-c`（创建归档）——修完三阶段全通。
8. **JMeter 乱码/假成功**：`sampleresult.default.encoding=UTF-8`；HTTP 200 不代表业务成功，要加响应断言。

出处「课程25 · 10-8、18-3、16-1、27-2~27-4、28-7；scan2 §面试汇总」
