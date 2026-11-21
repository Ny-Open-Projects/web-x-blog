---
title: [ARC-439] 微前端的 CSS 隔离与运行时共享的演进方案如何选？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-439：微前端 CSS 隔离与运行时共享的演进
**答**:
- CSS 隔离方案谱系：Shadow DOM（强隔离但样式穿透难、Portal 兼容麻烦）、CSS Modules/命名空间约定（弱隔离、成本低）、构建期 scoped + CSS 变量 token（推荐基线）、运行时 scoper（qiankun 动态样式改写，有性能成本）。
- 演进策略：新建子应用直接 token + scoped；老应用接入先命名空间改造（自动加前缀工具）；仅真正冲突难治的用 Shadow DOM。
- 运行时共享演进：externals（全局变量，粗暴但稳）→ import map（浏览器原生，现代基线）→ Module Federation（构建期声明共享，ARC-201）→ 运行时容器协议（主应用提供 service registry，子应用消费）。
- 公共依赖版本策略：React/框架类不共享（各版本自持防冲突），工具类（lodash/dayjs）共享 + 版本协商；共享依赖的升级由主应用统一节奏。
- 隔离验证：样式冲突扫描（选择器碰撞检测脚本）进 CI。
```html
<!-- import map：现代微前端共享基线 -->
<script type="importmap">
{ "imports": { "react": "https://cdn.example.com/react@18.3.1/react.js",
               "shared/": "https://cdn.example.com/shared/" } }
</script>
<!-- 子应用构建 external: react → 命中 import map，版本由主应用统一定 -->
```
