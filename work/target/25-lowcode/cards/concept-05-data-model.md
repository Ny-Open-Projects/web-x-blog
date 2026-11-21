---
title: 五张核心表与关系化 Schema 存储
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 概念, 数据模型, ER]
---

## 五张核心表与关系化 Schema 存储

课程平台用五张核心表撑起全部业务：**user / page / component / component_data / resources**。关系：user:page 1:1，user:component、user:resources、page:component、page:component_data 均 1:n。

关键设计：
- component 的属性统一以 JSON 存 `options` 字段（TypeORM `simple-json` 列类型）——**组件类型不用加列，属性自由扩展**。
- page.components 存组件 id 顺序串（simple-array），这是画布排序的持久化形态，与前端 store 的"排序数组"一一对应。
- component_data 四列 `id/page_id/user/props`：`user` 是 MD5(ip+ua) 访客匿名标识（非登录用户），组件 id 存在 `props[].id` 里（无 componentId 列）。
- resources 只存 OSS 返回的 URL，不存文件本体。

组件表（存配置：type 列 + options，title 在 options 内）与组件数据表（存用户填写内容）的区分是统计模块的地基——前者出表头，后者出表格行。

对比：自研参考实现用"整页 PageSchema JSON 存 text 列"的 DSL 式存储。关系化利于按组件粒度统计，整页 JSON 利于迁移与 diff。

出处「课程25 · 6-4、14-2、20-1；scan3」
