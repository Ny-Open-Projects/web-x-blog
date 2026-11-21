---
title: [AGT-392] 浏览器插件 Agent——伴生型助手的工程要点？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-392：做浏览器插件形态的 AI 助手，工程要点有哪些？

**答**:
- 架构要点：content script（页面感知/注入 UI）+ background service worker（LLM 调用/状态——SW 会被休眠，长任务要保活策略或迁移到 offscreen）、侧边栏 UI（不侵入页面样式）、跨域与权限声明最小化（host_permissions 只声明需要的域——商店审核与安全双要求）。
- 页面感知：读取 DOM/accessibility tree（AGT-332 感知层同款）+ 页面语义识别（当前页是什么：商品页/文档页——路由意图）+ 用户选中内容捕获（用户选中文本即上下文——伴生助手的最低摩擦入口）。
- 隐私与信任：用户浏览数据敏感——本地处理优先（端侧小模型做轻任务）、上传最小化（只传用户显式请求的内容）、权限提示透明（AGT-355 合规）。
- 与页面冲突治理：注入 UI 的样式隔离（Shadow DOM）、SPA 路由变化的监听适配、页面 CSP 与插件脚本的兼容、性能影响控制（长任务页面感知的节流）。

```text
插件 Agent 架构：
content script（感知/注入 UI，Shadow DOM）
  + background SW（LLM 调用，休眠保活）
  + 侧边栏 UI
感知：a11y tree + 页面语义识别 +
  用户选中即上下文
隐私：本地优先 / 上传最小化 /
  权限最小声明
兼容：SPA 路由 / CSP / 节流。
```
