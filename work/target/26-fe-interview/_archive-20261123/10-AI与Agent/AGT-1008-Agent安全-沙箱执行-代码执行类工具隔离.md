---
title: [1008] Agent 要执行生成的代码，沙箱怎么做
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 沙箱]
type: 面试题
---

## 1008：Agent 要执行生成的代码，沙箱怎么做

**答**：
- 隔离等级递进：进程级（子进程 + 资源限额）→ 容器级（独立镜像、无网络或白名单网络）→ 微 VM 级（Firecracker 类，最强隔离）；执行不可信代码至少容器级。
- 资源与时间双限：CPU/内存限额 + 墙钟超时强杀，防止死循环与资源耗尽攻击；输出截断防「刷屏攻击」撑爆内存。
- 文件系统只给临时目录白名单，网络默认全禁、按需开白名单域名——Agent 生成的代码默认视为攻击者代码。
- 追问钩子：为什么不能「模型说安全就跑」？——模型输出可被注入操纵，信任锚必须在沙箱配置而不是模型自评。

```ts
async function runCode(code) {
  return sandbox.run({
    image: 'agent-sandbox:latest',        // 无网络基础镜像
    code, timeoutMs: 10000,               // 墙钟强杀
    limits: { cpu: 0.5, mem: '256m', pids: 64 },
    fs: { tmp: '/sandbox/tmp' },          // 只给临时目录
    net: 'none',                          // 默认断网
    outputMax: 10000,                     // 输出截断
  });
}
```
