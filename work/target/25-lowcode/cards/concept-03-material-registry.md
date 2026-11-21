---
title: 物料体系与组件注册表
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 概念, 物料, 组件注册表]
---

## 物料体系与组件注册表

物料 = 平台可复用资产的统称，分三层：**基础物料**（input/image/text 等原子组件）、**业务物料**（组合块）、**页面模板**。物料体系的最小可行实现是**组件注册表模式**：`Record<type, Component>` 映射表，新增物料 = 登记，编辑器与渲染器自动感知。

**本项目实例**：share 包 15 种组件（text/swiper/list/image/video/card/split/richText/qrcode/alert/input/textArea/radio/checkbox/empty），统一从 `componentExport/componentList` 导出；渲染侧 `getComponentByType(type)` 工厂按 type 取组件；属性面板侧 `getComponentPropsByType` 按类型映射配置组件——"视图映射放 share、配置映射只放 client"。

新增一个组件必改三处：①组件 index.ts 导出、②types.ts 加类型、③componentExport 注册；漏一处会触发遍历断链 + TS 警告。每个物料自带编辑态（画布可选中拖拽）与渲染态（发布页纯展示）两套消费方式，这正是"编辑端/发布页复用同一套组件"的实现基础。

出处「课程25 · 14-7、14-9、15-1~16-7；scan3」
