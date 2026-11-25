---
title: [AIC-008] Agent 模式允许自动执行终端命令，风险是什么？如何设计权限边界？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-008：Agent 模式允许自动执行终端命令，风险是什么？如何设计权限边界？
**答**：
- 风险分级：读命令（cat/ls/git status）低危；写命令（rm/git commit/pnpm publish/curl 下载执行）高危；带变量的复合命令（`rm -rf $DIR`）最危险，因为变量可能被上一轮输出污染。
- 权限设计三件套：白名单（lint/test/build 自动放行）、黑名单（rm -rf、git push --force、publish 一律拦截）、逐次确认（白名单外命令弹窗人审）。
- 环境隔离：让 Agent 在容器/沙箱里跑，宿主机只挂载项目目录，即使删库也只删容器内的。
- 命令注入的典型路径：Agent 读了网页或 issue 内容后把内容拼进命令，所以「外部内容不可信」要作为规则写进规则文件。
- 追问钩子：能提到 `--auto-run` 类开关要按项目分级（个人 demo 全开、公司仓库全关）是加分项。

```jsonc
// .cursor/settings.json 示意：分级权限
{
  "agent.autoRun": {
    "allow": ["pnpm lint", "pnpm test*", "pnpm tsc --noEmit", "git status", "git diff*"],
    "deny": ["rm *", "git push*", "* publish*", "curl * | sh", "sudo *"],
    "ask": true // 其余命令逐次确认
  }
}
```
