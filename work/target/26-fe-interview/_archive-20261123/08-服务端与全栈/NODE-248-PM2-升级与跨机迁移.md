---
title: [NODE-248] PM2 升级与跨机迁移？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-248：PM2 升级与跨机迁移？
**答**:
- 状态持久化：pm2 save（进程表 → ~/.pm2/dump.pm2）+ pm2 startup（开机自启脚本）——机器重启后进程恢复。
- 跨机迁移：dump 文件含脚本路径/env——迁移要同步 ecosystem.config.js 与目录结构；密钥类 env 从配置中心拉（NODE-150）不进 dump。
- PM2 自身升级：npm i -g pm2 后旧 dump 兼容性一般 OK；正式升级流程 = save → 新版 → resurrect → 验证健康。
- 蓝绿迁移（物理机到容器）：新旧环境并行，网关按比例切流（NODE-176 灰度服务端版），稳定后旧机下线。

```bash
# 迁移流程
pm2 save                                        # 1) 保存进程表
scp ~/.pm2/dump.pm2 new-host:~/.pm2/            # 2) 同步（env 密钥剔除）
# new-host:
pm2 startup systemd -u app --hp /home/app       # 3) 开机自启
pm2 resurrect                                   # 4) 恢复
curl -f http://new-host:3000/health             # 5) 验证 → 网关切流
# 升级 PM2 自身：
pm2 save && npm i -g pm2@latest && pm2 update && pm2 resurrect
```
