---
title: [XP-105] Electron 应用的安全审计清单应包含哪些项？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-105：Electron 应用的安全审计清单应包含哪些项？
**答**：
- 渲染进程基线：`contextIsolation: true`、`nodeIntegration: false`、`sandbox: true`、`webSecurity: true`——四项为默认红线，任何窗口（含内嵌第三方页）不得关闭。
- preload 纪律：只通过 `contextBridge` 暴露**白名单化、最小粒度** API，绝不透传 `ipcRenderer` 全量对象；渲染侧禁 Node 痕迹（require/process 全量）。
- IPC 加固：每个 handle 校验 `event.senderFrame` 来源与参数 schema（zod），写操作区分窗口权限；禁止把主进程对象/函数直接传给渲染进程（原型污染）。
- Web 内容防线：CSP（禁 inline/eval、限 connect-src）、`will-navigate`/`setWindowOpenHandler` 拦截外部导航、自定义协议白名单（注册标准 scheme 禁 file:// 访问）、`permissionRequestHandler` 按来源放行摄像头/通知等。
- 数据与供应链：密钥走 safeStorage 不进代码、`npm audit`/lockfile 审计进 CI、更新链路签名校验（XP-101）、剪贴板/录屏等敏感权限用后即关；审计按此清单季度化执行 + 自动化扫描。

```text
Electron 安全审计清单（季度执行 + CI 自动化项）
A 渲染进程基线（自动化扫描 main 进程代码）
  [ ] contextIsolation=true  [ ] nodeIntegration=false  [ ] sandbox=true
  [ ] webSecurity=true       [ ] 全项目 grep 无 allowRunningInsecureContent
B contextBridge 暴露面
  [ ] preload 只暴露白名单方法，无 ipcRenderer 对象直传
  [ ] 每个 API 最小粒度，敏感操作（fs/shell/exec）不在暴露面
C IPC 加固（自动化：所有 handle 必须注册 schema 校验）
  [ ] event.senderFrame 校验来源（防 iframe/子窗口伪造）
  [ ] 参数 zod schema 校验；写操作按窗口角色鉴权
D Web 内容防线
  [ ] CSP：default-src self；禁 unsafe-inline/eval；connect-src 白名单
  [ ] will-navigate 拦截 + setWindowOpenHandler 强制外链走系统浏览器
  [ ] 自定义协议 standard+secure 注册，禁 file:// 通配；permissionRequestHandler 按来源放行
E 数据与供应链
  [ ] 密钥 safeStorage；日志/崩溃上报脱敏（路径/token）
  [ ] npm audit + lockfile diff 进 CI；原生模块来源审计
  [ ] 自动更新签名校验开启（XP-101）；devtools 生产禁用
F 演练与追踪
  [ ] 渗透样例：渲染进程被注入 XSS 后能否逃逸（预期：被 A-D 全链拦死）
  [ ] 审计结论归档，风险项进 XP-137 发布门禁
```

---

## 十三、跨端一致性专项（106-112）
