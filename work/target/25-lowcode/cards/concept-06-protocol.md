---
title: 低代码协议与标准化
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 概念, 协议, 标准化]
---

## 低代码协议与标准化

协议回答四个问题：**物料如何描述**（让属性面板自动生成）、**Schema 如何描述**（跨端可渲染）、**事件/逻辑如何表达**（扩展性）、**版本如何演进**（兼容性）。

业界参照：阿里 LowCodeEngine 的《低代码引擎搭建协议规范》《物料描述协议》、Amis 的 JSON Schema 渲染格式。协议没定就写渲染器，后面必然推倒重来。

**本项目实例**：课程版虽未引入正式协议文档，但契约实践是协议的雏形——组件 type 枚举（TComponentTypes）、每个 type 的属性三件套（value/defaultValue/isHidden）、share 包作为唯一契约真源、入参类型用 Omit 收敛。自研参考实现更进一步：PageSchema JSON（version/title/nodes 递归嵌套）与 WorkflowContract（节点 NodeContract {type, category, label, version, inputs, outputs} + 图 DSL，契约与执行器分离：NODE_CONTRACTS / NODE_REGISTRY）双契约放在 shared 包，前后端同源消费，前端画布直接读 NODE_CONTRACTS 渲染端口。

课程自缺的一层是版本演进：Schema 无版本号、组件 type 发布后改名即破坏存量页面——商用化必须补 version + 迁移脚本。

出处「课程25 · 14-2；scan4 §2/§5；scan3」
