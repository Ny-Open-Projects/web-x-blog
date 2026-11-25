---
title: [AIC-095] 让 Agent 自由执行命令前，「安全沙箱」至少要做到哪几层？容器/Docker 方案的取舍？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-095：让 Agent 自由执行命令前，「安全沙箱」至少要做到哪几层？容器/Docker 方案的取舍？
**答**：
- 至少三层：① 进程层——容器/VM 隔离（文件系统只挂载工作区、无网络或白名单网络、无敏感 env 注入）② 权限层——以低权限用户运行、命令白名单（AIC-009）③ 数据层——工作区不含真实凭据（用 mock env）、产物导出走审查通道。
- 容器方案的取舍：Docker 隔离好但启动慢、调试麻烦、IDE 集成成本高；本地裸跑效率高但风险大。折中方案是「本地开发裸跑 + CI/自动任务容器化」，越自动化的场景隔离越强。
- 网络默认关：agent 执行命令大多数场景不需要外网；需要时（装依赖）用代理白名单并记录域名——防「prompt 注入 → curl 外传代码」这条最危险的链路。
- 资源限制：CPU/内存/时长限额，防 agent 写出死循环拖垮宿主。
- 追问钩子：安全设计的验证方式是「注入测试」——故意在仓库里埋一条诱导外传的文本，看沙箱能不能拦住。

```javascript
// 沙箱配置示意（agent 任务执行环境）
const sandbox = {
  image: 'node:20-slim',
  mounts: [{ src: './workspace', dst: '/repo', mode: 'rw' }],   // 只挂工作区
  network: { mode: 'none', allowProxy: ['registry.npmjs.org'] },
  user: 'agent',            // 非 root
  limits: { cpu: 2, mem: '2g', timeoutMs: 600_000 },
  env: { NODE_ENV: 'sandbox' }, // 不注入任何真实密钥
};
```
