---
title: [ENG-234] 微前端与 monorepo 的构建边界（共享依赖/独立部署）怎么处理？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-234：微前端构建边界怎么处理？
**答**：
- 共享依赖三策略：externals+运行时共享（单例 React，防双实例）、import map 版本协商、模块联邦 shared 配置——关键决策是「哪些必须单例」（React/DOM 相关全部单例）。
- 独立部署契约：子应用产物带版本清单，宿主加载时按清单取最新（或指定版本回滚）；发布互不阻塞。
- 构建隔离：子应用独立构建独立 CI（monorepo 内独立 project），共享包（utils/tokens）走包发布——子应用不直接 import 宿主代码。
- 兼容性验证：宿主升级 React 大版本时，自动跑「所有子应用在宿主新版本下的冒烟」——跨应用兼容矩阵进 CI。
- 追问钩子：为什么共享依赖宁少勿多——每多一个 shared 依赖，子应用间的隐式耦合就多一分（版本协商失败全挂）；只有框架与全局单例类（React/router/状态单例）值得共享，业务工具各自打包。

```javascript
// 模块联邦 shared 配置
shared: {
  react: { singleton: true, requiredVersion: deps.react },
  'react-dom': { singleton: true },
  '@org/utils': { singleton: false },        // 业务工具不共享
}
// 子应用版本清单（独立部署契约）
{ "name": "cart", "version": "1.4.0", "entry": "cdn/.../cart@1.4.0/index.js" }
```
