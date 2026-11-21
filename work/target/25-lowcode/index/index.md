---
title: 全栈低代码平台大课（小滴课堂）
date: 2026-11-17
categories: [课程]
tags: [25-lowcode, 低代码, 课程导航]
---

<h1 style='margin-bottom:6px'>全栈低代码平台大课</h1>
<p style='color:#666'>从零做一个可上线、可压测的低代码平台：Schema 驱动渲染、拖拽编辑器、发布链路、问卷统计、Docker + 云效流水线。共 <b>229</b> 篇笔记（预先课 40 + 主课 8 期 189）+ <b>35</b> 张知识卡。点期目录进入，再点单篇看细节；知识卡按「概念 → 原理 → 实战 → 面试」四类组织。</p>

## 阅读顺序（预先课 → 8 期）

<div style='display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-top:18px'>
  <a href='/categories/低代码大课/低代码预备/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>00 · 预先课（必备技术）</div><div style='color:#888;font-size:13px;margin-top:6px'>40 篇 · NestJS / TypeORM / React 三件套打底</div></a>
  <a href='/categories/低代码大课/低代码第一期/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>01 · 第一期（导学与需求）</div><div style='color:#888;font-size:13px;margin-top:6px'>24 篇 · 技术选型 / Next.js / 需求文档</div></a>
  <a href='/categories/低代码大课/低代码第二期/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>02 · 第二期（架构与数据）</div><div style='color:#888;font-size:13px;margin-top:6px'>26 篇 · 系统架构 / ER 图 / Monorepo / TypeORM</div></a>
  <a href='/categories/低代码大课/低代码第三期/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>03 · 第三期（账户体系）</div><div style='color:#888;font-size:13px;margin-top:6px'>23 篇 · 验证码防刷 / 注册登录 / 微信扫码</div></a>
  <a href='/categories/低代码大课/低代码第四期/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>04 · 第四期（编辑器与组件）</div><div style='color:#888;font-size:13px;margin-top:6px'>24 篇 · 发布接口 / 画布布局 / 组件成对开发</div></a>
  <a href='/categories/低代码大课/低代码第五期/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>05 · 第五期（资源与发布）</div><div style='color:#888;font-size:13px;margin-top:6px'>26 篇 · OSS / 拖拽排序 / 草稿发布 / 发布页渲染</div></a>
  <a href='/categories/低代码大课/低代码第六期/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>06 · 第六期（统计与部署）</div><div style='color:#888;font-size:13px;margin-top:6px'>25 篇 · 问卷统计 / Excel 导出 / Dockerfile / Compose</div></a>
  <a href='/categories/低代码大课/低代码第七期/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>07 · 第七期（流水线上线）</div><div style='color:#888;font-size:13px;margin-top:6px'>22 篇 · 云效流水线 / 上线确认与 BUG 修复 / JMeter 入门</div></a>
  <a href='/categories/低代码大课/低代码第八期/' style='display:block;border:1px solid #e3e8ef;border-radius:10px;padding:14px 16px;text-decoration:none;color:inherit'><div style='font-weight:700;font-size:16px'>08 · 第八期（压测与面试）</div><div style='color:#888;font-size:13px;margin-top:6px'>19 篇 · JMeter 压测实战 / 压测优化 / 简历面试</div></a>
</div>

## 知识卡（35 张，进站后与笔记互链）

- **概念（是什么，11 张）**：元信息驱动 / Schema 与 DSL / 物料与组件注册表 / 渲染引擎 / 五张核心表 / 低代码协议 / 权限模型 / 发布三态 / 沙箱 / 工作流 DAG / 低代码 vs 零代码选型
- **原理（为什么，6 张）**：Schema→UI 驱动机制 / 拖拽=数组索引交换 / 事务化发布 / Redis 缓存与 QPS / JWT 鉴权链路 / 撤销重做快照
- **实战（怎么做，12 张）**：NestJS 要点 / TypeORM 坑 / 验证码防刷 / 微信扫码 / OSS 资源 / Excel 导出 / Docker 部署 / JMeter / Redis 封装 / 编辑器交互 / 统计前端 / 组件开发五步范式
- **面试（怎么讲，6 张）**：技术选型 / 安全 / 性能 / 项目亮点 / 简历铁律 / 踩坑谈资

## 前置与后续

- **前置**：会 React + Node/MySQL 基础即可；不熟 NestJS/TypeORM 先看 00 预先课（对应实战卡 practice-01/02）。
- **快速通道**：只要低代码本质 → 概念卡「元信息驱动」→「渲染引擎」→ 原理卡「Schema→UI」→ 第五期 20-6 篇；只要面试 → 面试六卡 + 第八期 31-1~31-4。
- **后续阅读**：部署上线后可接站内《自主开发PaaS平台》（云原生方向延伸）与《云原生CI/CD实战》（流水线深化）。

> 备注：第三期 13-4 集课程未录制（内容并入 13-3）；工作流/沙箱相关卡片来自课程配套参考实现，非课程原始代码，引用见课程图谱标注。
