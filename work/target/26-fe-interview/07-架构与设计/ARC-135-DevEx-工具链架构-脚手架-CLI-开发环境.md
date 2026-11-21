---
title: [ARC-135] DevEx 工具链架构（脚手架/CLI/开发环境一键启动）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-135：DevEx 工具链架构（脚手架/CLI/开发环境一键启动）如何设计？
**答**：
- 目标定义：新成员从 clone 到本地跑起第一个页面的时间（onboarding time）是 DevEx 北极星，目标是 30 分钟内。
- 一键启动：`dev up` 编排全部依赖（本地 mock 服务/依赖容器/env 注入/端口检测），失败给出可操作的修复建议（doctor 子命令体检：node 版本、代理、端口占用、依赖完整性）。
- CLI 分层：内核（参数解析/插件机制/日志）+ 命令插件（create/dev/deploy/check），团队各平台以插件形式接入，避免 CLI 变成大泥球。
- 度量反馈内建：启动时长/失败率匿名上报，DevEx 改进有据可依；CLI 版本与模板版本联动，防止环境漂移。

```yaml
# dev up 编排配置（CLI 消费）
devex:
  north_star: "新成员 clone → 首页可访问 ≤ 30min"
  up:
    steps:
      - name: 环境体检
        run: dev doctor                  # node 版本/镜像源/磁盘/端口检查
      - name: 依赖安装
        run: pnpm install
      - name: 依赖服务
        compose: docker-compose.dev.yml  # mock server / redis / db
        healthcheck: [mock:3001, db:5432]
      - name: 启动应用
        run: turbo dev --parallel
        wait_for: "http://localhost:3000 → 200"
    on_fail:
      suggest: "运行 dev doctor 查看体检报告；常见问题见 docs/troubleshooting"   # 报错必须可操作
  metrics:                               # 匿名上报
    - up_duration_ms
    - up_fail_step
    - onboarding_time（新人首次成功运行）
  cli_structure:
    core: [parse, plugin-host, logger]
    plugins: [create, dev, deploy, check, doctor]   # 平台团队以插件接入
```
