---
title: [ENG-072] CLI 工具怎么发布与全局安装？bin 字段和权限有哪些坑？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-072：CLI 工具怎么发布与全局安装？bin 字段和权限有哪些坑？
**答**：
- package.json 的 bin 字段把命令名映射到脚本，npm install -g 时自动在全局 bin 目录建符号链接。
- 脚本必须带 shebang（#!/usr/bin/env node），且 files 字段要包含 bin 与 templates，否则发布缺文件。
- scoped 包（@myorg/cli）全局安装要带域：npm i -g @myorg/cli；常用做法是提供短别名 bin。
- 权限坑：不要 sudo npm i -g，用 nvm 管理的 node 则写入用户目录无需 root；EACCES 优先检查 node 版本路径。

```json
{
  "name": "@myorg/create-app",
  "version": "2.1.0",
  "type": "module",
  "bin": {
    "@myorg/create-app": "bin/cli.js",
    "my-create": "bin/cli.js"
  },
  "files": ["bin", "templates", "README.md"],
  "engines": { "node": ">=18" },
  "publishConfig": { "access": "public" }
}
```

---

## 第十八章 代码规范深化（ENG-073 ~ ENG-079）
