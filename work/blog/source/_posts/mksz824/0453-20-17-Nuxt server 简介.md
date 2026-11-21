---
disableNunjucks: true
title: 20-17 Nuxt server 简介
date: 2026-11-17 11:33:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

这节课进入一个新的基础知识模块：server 服务器端。之前提到过，Nuxt 3 是一个全栈框架，不仅能构建前端页面和应用，做后端也不在话下。

后端相信大家已经很熟悉了。我们之前使用 Nest.js 深入了解并创建了整个 OpsFlow 项目的后端。Nuxt 3 同样可以完成 Nest.js 能做的任务，比如连接并操作数据库、创建 API 文件、上传等等。和之前不一样的是：过去前后端分离，前端一个代码库、后端一个代码库，现在通过 Nuxt 3 可以在一个代码库中完成，这是比较大的优势。

由于前面已经深入了解了后端功能的原理，Nuxt 部分的讲解不会特别深入。虽然 API 不同，但道理是一样的，到具体功能点时我会让大家回顾之前的内容。

先来熟悉 Nuxt 后端的架构，它是一个三层模型。最外层是 Nuxt，往下一层是 server engine，也就是后端引擎，这里使用的是一个叫 Nitro 的框架。它最初是为 Nuxt 诞生的，现在已经发展成一个优秀的独立项目，GitHub 上有 4.4k 个 star。它是后面要密切接触的框架，看几个特点：

1. 支持极速开发和 HMR（Hot Module Replacement），后端也支持热替换，不用每次都重启，非常方便。
2. 文件系统路由（file system routing）。前端通过 pages 目录生成路由，后端同样可以根据不同文件生成 API 节点，是很统一的设计思想。
3. TypeScript 支持，它是全 TS 编写的。
4. Auto Imports 自动导入，一系列内置全局函数可以直接使用。
5. 图层（layers）设计，内置了很多存储工具可以直接使用。
6. Cache API 缓存设计，还有部署（Deploy）、可移植（Portable）相关的特性等等，之后的学习中会一一接触。

再往下是更底层、更基础的框架，叫 H3。它是一个高性能、极简的 Node.js HTTP 框架，主要为 Nitro 提供 API 路由以及中间件功能。想做一个简单的 Web 服务器，也可以直接用它，方便快捷。它有几个特性：第一，提供一系列内置帮助函数，处理服务端的日常情况，比如 Cookie、Body 数据、Headers 以及 request、response 的各种数据；第二，设计了很贴心的返回类型，直接返回 object 或 array 时会生成 JSON，还可以直接返回 Promise，框架会自动等待 Promise 完成后再返回数据。想了解更多可以直接去看它的文档。

最后是文件夹的位置。和其他功能一样，Nuxt 为后端服务器设置了一个特殊文件夹，叫 server。server 文件夹中的内容会根据文件名称和规则直接生成 API endpoints 以及一系列事件处理。举个简单例子：在 server 下建 api 文件夹，里面放一个 hello.ts，就会生成 /api/hello 这样的 endpoint。如果想生成根目录层级的 API，不能直接放在根目录，需要放到一个特殊的文件夹 routes 里；另外还有放置 middleware 的特殊文件夹等等，下节课详细接触。

这节课简单介绍了 server 的架构以及它内部使用的两个工具（Nitro 和 H3），下节课我们就要重度使用它了。
