---
title: "掌握 RxJS 和在 NestJS 中的应用"
date: 2026-11-17 06:06
categories: [低代码大课, 低代码预备]
tags: ["低代码", "React", "NestJS", "全栈", "25-lowcode"]
source: 25.xiaodi-lowcode
---

# 掌握 RxJS 和在 NestJS 中的应用

> **导语**：初始化 NestJS 项目时，RxJS 就已经作为依赖被装好了，写拦截器、包装异步响应时几乎绕不开它。这一集从 Observable 的发布/订阅讲起，把 interval、take、of、map、filter 几个高频操作符和主动取消订阅一次梳理清楚。读完后你能看懂拦截器里那个 Observable 返回值的来龙去脉，也为后面低代码平台后端的异步处理打好底子。

## 前置知识

- 已经能创建并运行一个 NestJS 项目，清楚 Controller 与 Service 的分工，可回顾《Nestjs环境搭建和项目创建》和《什么是装饰器和Nestjs中的应用》。
- 熟悉 JavaScript 的异步、回调与 setTimeout，对 TypeScript 装饰器有基本印象。
- 用过观察者模式或发布-订阅（例如 Vue 的全局事件总线）会更轻松，但不是硬性要求。

## 正文

### 为什么 NestJS 里要专门学 RxJS

RxJS 是一个基于观察者模式的响应式编程库，用简洁、直观的方式处理异步操作与事件流。关键一点：它**随 NestJS 项目自带**，不需要额外安装——在工程 `packages/server` 的依赖清单里能看到 `rxjs`，这也是 NestJS 拦截器、守卫等能力默认返回 Observable 的原因。

服务端拿不到 DOM 节点，所以 NestJS 场景里没有浏览器那种事件流，RxJS 主要承担的是**异步操作的编排**。它的思路和 Vue 的全局事件总线很像：一方发布任务，另一方通过订阅 API 拿到发布出来的内容。放到本项目里，低代码平台后端要统一包装接口响应、串联多个异步数据源，靠的正是这套模型。

> 工程里可对照 `代码（已8期）/8-5/lowcode/packages/server/package.json` 的依赖声明，以及 `代码（已8期）/8-5/lowcode/package.json` 的 monorepo 启动脚本。

### 核心模型：Observable 发布，subscribe 订阅

一切的起点是 `new Observable(subscriber => {...})`。传入的回调函数拿到一个 `subscriber`，通过 `subscriber.next(...)` 推值、`subscriber.complete()` 结束；另一端用 `subscribe` 订阅，在 `next` 回调里拿到每一次发布的值。

```ts
import { Observable } from 'rxjs';

const observable = new Observable<number>((subscriber) => {
  subscriber.next(1);
  subscriber.next(2);
  subscriber.next(3);

  setTimeout(() => {
    subscriber.next(4);   // 两秒后才发布
    subscriber.complete();
  }, 2000);
});

observable.subscribe({
  next: (value) => console.log(value),
});
```

请求这个接口后会先打印 `1、2、3`，等两秒再打印 `4`，随后流被 complete 终止。这里最值得记住的是：**订阅是持续的**，哪怕发布发生在订阅之后，两秒后推的值依然会送进 `next` 回调——这正是它和普通回调、Promise 一次性的区别。

### 高频操作符：interval、take 与 of

手动 `new Observable` 比较繁琐，日常更多用操作符创建流：

- `interval(ms)`：每隔指定毫秒不停地产值，从 `0` 开始；
- `take(n)`：限制只取前 `n` 个值，取满自动停止；
- `of(...values)`：用自定义数据创建流，不必依赖自增数字。

```ts
import { interval, of, take } from 'rxjs';

// 每秒输出一个值，取 6 个后停止：0 1 2 3 4 5
interval(1000)
  .pipe(take(6))
  .subscribe((value) => console.log(value));

// 自定义字符串数据，只取 2 个
of('一', '二', '三', '四')
  .pipe(take(2))
  .subscribe((value) => console.log(value));
```

`interval` 接收的参数是毫秒；把 `take(6)` 改成 `take(10)`，就会一路输出到 `9` 才停。实际开发里按场景选：需要定时轮询用 `interval`，需要限量用 `take`，需要塞自己的数据用 `of`。

### 用 pipe 串起 map 与 filter

`pipe` 就是「管道」，可以把多个操作符按顺序接在一条流上。`map` 把值转换形态（例如把 number 包成对象），`filter` 只放行满足条件的值：

```ts
import { interval, map, filter } from 'rxjs';

interval(1000)
  .pipe(
    map((num) => ({ num })),
    filter((item) => item.num % 2 === 0),
  )
  .subscribe((item) => console.log(item));
```

这样输出的不再是裸 number，而是 `{ num: 0 }`、`{ num: 2 }`、`{ num: 4 }`…… 且只有能被 2 整除的值才会放行。要注意：这段没有 `take`，所以流**不会自己停**，会一直输出下去。

### 如何提前终止：unsubscribe

想在中途停掉，就保存 `subscribe` 返回的订阅对象，调用它的 `unsubscribe()`。讲师演示的是「输出到 10 就收手」：

```ts
import { interval } from 'rxjs';

const subscription = interval(1000).subscribe((num) => {
  console.log(num);
  if (num === 10) {
    subscription.unsubscribe();
  }
});
```

`take(n)` 本质上也是帮你在取满后自动退订，只是条件由操作符替你写好了。

### 放回 NestJS 工程里看

本节是在干净的 Controller/Service 里演示的：保留一个接口，请求它时跑一遍上面的流。真正到项目里，RxJS 会出现在两个地方：一是拦截器（响应拦截器、异常拦截器）的方法签名返回 `Observable`，二是异步数据的组合与转换。工程用 pnpm-workspace 管理 `client / server / share / release` 多个子包，`代码（已8期）/8-5/lowcode/package.json` 里的 `run:server`、`build:server` 等脚本就是按包过滤启动后端，和本节的练习接口是同一套工程结构。

## 小结

- RxJS 随 NestJS 项目自带，服务端主要用来处理异步，而不是 DOM 事件流。
- `Observable` 负责发布（`next` / `complete`），`subscribe` 负责订阅取值，订阅是持续性的。
- `interval` 定时产值、`take` 限量、`of` 自定义数据，三者常一起用。
- `pipe` 里串 `map` / `filter` 可做转换与筛选；没有 `take` 的流不会自动停止。
- 保存订阅对象并调用 `unsubscribe()` 可在任意条件下主动终止。

## 下一步

建议接着看《Nest的响应拦截器》——拦截器方法返回的就是 Observable，本节这些操作符会在那里真正落地到接口响应包装上。也可以先看《项目需求分析—前端页面需求分析》，从预备技术自然过渡到低代码平台的需求梳理。
