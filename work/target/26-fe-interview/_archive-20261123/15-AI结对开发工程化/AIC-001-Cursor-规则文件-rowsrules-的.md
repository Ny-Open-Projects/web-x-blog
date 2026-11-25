---
title: [AIC-001] Cursor 的 .cursor/rules 规则文件应该写什么？和旧的 .cursorrules 有什么区别？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-001：Cursor 的 .cursor/rules 规则文件应该写什么？和旧的 .cursorrules 有什么区别？
**答**：
- `.cursor/rules` 是新版目录式规则系统：每个规则一个 `.mdc` 文件，支持 front-matter 指定 `globs`（命中哪些文件才生效）与 `alwaysApply`，旧的 `.cursorrules` 是单文件全局规则，已标记废弃。
- 规则内容写「项目约定」而非通用常识：技术栈版本、目录结构、命名规范、禁止事项（如禁止引入新依赖）、组件/接口的固定写法模板。
- 按 glob 拆分规则：`components/**/*.tsx` 一条、`server/api/**` 一条，避免一次塞进所有上下文挤占 token。
- 规则要短且可验证，写「必须用 arrow function + 显式返回类型」而不是「代码要优雅」这类模型无法执行的软要求。
- 追问钩子：规则文件太多会导致每次对话注入膨胀，需要定期清理与合并。

```markdown
<!-- .cursor/rules/frontend-style.mdc -->
---
description: 前端组件规范
globs: src/components/**/*.tsx
alwaysApply: false
---
- 组件一律函数式 + TypeScript，禁止 class 组件。
- 样式使用 CSS Modules，禁止全局 className。
- Props 必须定义 interface 并导出，事件回调命名 onXxx。
- 引入新 npm 依赖前必须在对话中说明理由并等待确认。
- API 请求统一走 src/lib/request.ts，禁止直接 fetch。
```

```markdown
<!-- .cursor/rules/api-style.mdc -->
---
description: 服务端接口规范
globs: server/api/**/*.ts
alwaysApply: false
---
- 所有 handler 用 defineEventHandler（Nitro）。
- 响应统一 { code, data, message } 结构，错误用 createError。
- 禁止在 handler 内写业务逻辑，抽到 server/services/ 下。
```
