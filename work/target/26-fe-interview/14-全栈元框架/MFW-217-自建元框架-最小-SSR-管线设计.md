---
title: [MFW-217] 自建元框架实践：最小 SSR 管线的设计决策
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-217：自建元框架的最小 SSR 管线

**答**:
- 自建动机：深度定制渲染策略（如特定行业的模板缓存）而主流框架扩展点不够——自建是「扩展点不足」的最后选择，优先想办法用扩展点
- 最小管线组成：构建期（RSC 编译器用 react-server-dom-webpack 插件 or 干脆放弃 RSC 用纯 SSR——自建第一刀砍掉 RSC 复杂度）+ 服务端（renderToString/renderToPipeableStream + 路由匹配）+ 客户端 hydration（同构入口）
- 逐层自建清单（由易到难）：路由（自写简单）/状态（不做，用外部库）/数据获取（自写 fetch 包装）/RSC（不建议自建）/编译（直接用 Vite/esbuild）
- 判断标准：团队要维护的是「业务」不是「框架」——自建框架每年吞掉的人力要有明确预算（通常 1-2 人年/年）

```text
自建最小 SSR 决策树：
① 放弃 RSC（用纯 SSR + islands 思路）——砍最大复杂度
② Vite/rollup 做构建（不自建编译）
③ 自写：路由匹配 + renderToPipeableStream 包装 + hydration 入口
④ 数据层：外部库（Query）不自建
预算：1-2 人年/年，团队 ≤ 5 人不建议启动
```
