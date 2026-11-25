---
title: [BAS-187] nvm 和 nrm 有哪些高频操作？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-187：nvm 和 nrm 有哪些高频操作？
**答**：
- nvm 管 Node 版本：install 装、use 切、alias default 设默认、ls 列表。
- nrm 管 npm registry：ls 列源、use 切源、test 测速。
- 注意：nvm 的版本是按 shell 生效的，`nvm alias default` 才是新终端的默认版本。

```bash
nvm install 22                  # 安装指定版本
nvm alias default 22            # 设为新终端默认版本
nvm use 20                      # 当前 shell 临时切换
nvm ls                          # 查看已装版本
nrm ls                          # 列出可用镜像源
nrm use taobao                  # 切换 registry
```
