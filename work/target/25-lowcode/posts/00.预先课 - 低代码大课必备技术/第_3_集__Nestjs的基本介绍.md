---
title: "NestJS 的基本介绍：为什么全栈项目要选它"
date: 2026-11-17 03:15
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# NestJS 的基本介绍：为什么全栈项目要选它

> **导语**：在低代码平台这套全栈项目里，后端为什么不用 Express 或 Koa，而选 NestJS？本文从官网定义出发，讲清它「构建高效、可扩展 Node.js 服务端应用」的定位、对 TypeScript 的原生支持、基于 Express / Fastify 的兼容层，以及控制反转与依赖注入这两个核心设计思想。读完你会明白它热度从哪来、适合什么规模的工程。

## 前置知识

建议先读《Nestjs框架课程介绍+适合人员+学后水平》，了解本课程后端部分的整体定位。读过 Express 或 Koa 的接口开发会更容易对照理解；另外需要一点 ES6 `class` 的基础，NestJS 里几乎处处是类与装饰器。配套资料：全栈多端低代码平台项目大课.html / .pdf。

## 正文

### 官网定义：一个 Node.js 服务端框架

NestJS 官网有一句很标准的表述：它是一个用于构建**高效、可扩展的 Node.js 服务端应用程序**的框架。它和 Express、Koa 一样都属于 Node.js 框架，区别在于 NestJS 提供了更高层的架构约束。

它采用**渐进式**设计——这个词学 Vue 时应该见过，意思是项目可以从一个很小的骨架起步，随着业务迭代逐步加模块、加逻辑，而不是一开始就被迫接受一整套重结构。

### 语言与编程范式：TypeScript 优先

NestJS 本身用 TypeScript 开发，也完全支持你在项目里使用 TypeScript 的静态类型约束；同时也允许纯 JavaScript 编写。它把几种范式揉在一起：

- OOP 面向对象编程：模块、控制器、服务都是类；
- FP 函数式编程：类似 React 的写法思路；
- FRP 函数式响应编程：内置对 RxJS 的支持。

如果还没建立「类」的概念，建议先补一下 ES6 `class` 与 `constructor`，不然后面读控制器代码会很吃力。

### 底层兼容：Express 与 Fastify 二选一

NestJS 默认基于 Express，也可以切换到 Fastify——后者是速度最快的 Web 框架之一。这意味着你既能用 NestJS 自己的 API，也能无缝使用 Express 或 Fastify 生态里的中间件与库，兼容性更好。对全栈项目来说，这类「不推翻已有生态」的设计，迁移成本要低得多。

### 为什么要选 NestJS

**热度**：NestJS 2017 年 11 月才发布，是 Node.js 框架里较晚的一个，到课程录制的 2023 年不过六年，却是 GitHub 上 Star 增长最快的 TypeScript 后端框架，Star 数快速逼近老牌 Express。阿里云（云函数计算）、滴滴出行、蚂蚁金服等团队的项目中都有使用。

**可伸缩性**：模块化架构让应用拆分更容易，配合控制反转与依赖注入，模块之间高度解耦，维护与测试都更轻松，应用也因此更容易扩展。

**TypeScript 友好**：静态类型检查加上丰富的面向对象特性，直接提升代码的可读性、可维护性与可扩展性。

**中间件与生态**：异常处理、统一响应格式、身份验证（JWT）、跨域（CORS）都可以做成中间件。比如希望所有接口统一返回 `{ code, data, message }`，写一个响应拦截器就能全局生效，不必在每个控制器里重复拼装。

### 控制反转与依赖注入

这两个词第一次听会陌生，开发过 Spring 的同学则很熟悉。一句话概括：**控制反转（IoC）是思想，依赖注入（DI）是它的实现**，目的都是降低类与类之间的耦合度。

先看不用框架时的问题：

```ts
class A {
  private b = new B();
}
```

`A` 内部自己 `new B()`，两者强耦合。一旦 `B` 的构造逻辑变了，`A` 里也要跟着改。

依赖注入的做法是把实例化交给外部，通过构造函数传进去：

```ts
class A {
  constructor(public b: B) {}
}

const b = new B();
const a = new A(b);
```

NestJS 把这套动作完全接管了：你只需要在构造函数里声明「我要用哪个类」，框架扫描到后自动实例化并注入。比如用户控制器里：

```ts
@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post('register')
  register() {
    return this.userService.register();
  }
}
```

`UserService` 从没被 `new` 过，直接以声明的方式使用。于是控制器专心接 HTTP 请求、取参数、返结果，注册逻辑全放在 Service 里；别处要用 `UserService` 也注入同一个实例，改 Service 内部实现不影响调用方。解耦带来的可测试性与可维护性，正是大型项目选它的关键理由。

### 配套工程说明

本阶段练习代码见 `代码（已8期）/代码（已8期）/8-2/lowcode/`，其中 `pnpm-workspace.yaml` 声明了多包工作空间：

```yaml
packages:
  - "packages/*"
```

后续低代码平台会把 client、server、share、release 拆成独立子包，正是这种模块化思路在工程结构上的体现。

## 小结

- NestJS 是构建高效、可扩展 Node.js 服务端应用的渐进式框架，与 Express、Koa 同属 Node.js 生态。
- 原生 TypeScript 支持，融合 OOP、FP、FRP 三种范式。
- 底层基于 Express / Fastify，可复用两者中间件与库，兼容性好。
- 热度高、模块化架构、中间件与拦截器完善，适合中大型全栈工程。
- IoC 是思想、DI 是实现，由框架负责实例化与注入，让类之间充分解耦。

## 下一步

概念铺垫完毕，接下来动手。建议接着看《Nestjs环境搭建和项目创建》，把 Node.js、pnpm 与 NestJS 项目真正跑起来；随后建议接着看《Nestjs初始化目录结构介绍》，对照本文讲的模块与依赖注入，逐一认识脚手架生成的文件。
