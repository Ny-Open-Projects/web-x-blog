---
title: Schema 与 DSL：低代码的数据契约层
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 概念, Schema, DSL, 契约]
---

## Schema 与 DSL：低代码的数据契约层

Schema 是平台所有端共同遵守的**数据契约**：约定组件 type 枚举、每个 type 的 props 规范、页面结构的表达方式。DSL 是更广义的"领域专用语言"，JSON Schema 直驱是其中最简单直接的形态。

**本项目实例**：契约收敛在 pnpm workspace 的 share 包——组件类型用 `TComponentTypes` 字面量映射，options 用 `Record<string,any>`，入参类型放 `share/src/types/request/`（如 PostReleaseRequest 用 `Omit` 排除 account_id/id）。编辑端（client）、发布端（release）、服务端（server）三端引用同一个 `@lowcode/share`，改契约要 `pnpm build:share` 后其他包才能生效。

设计要点：①先固化协议再写渲染器；②Schema 要版本化，破坏性变更走 version + 迁移；③契约唯一真源在共享包，任何端不得私自加字段。

业界参照：Amis 的 JSON Schema、阿里 LowCodeEngine 的物料/搭建协议。

出处「课程25 · 8-5、14-2；scan4」
