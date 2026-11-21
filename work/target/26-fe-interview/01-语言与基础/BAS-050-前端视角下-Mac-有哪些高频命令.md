---
title: [BAS-050] 前端视角下 Mac 有哪些高频命令？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-050：前端视角下 Mac 有哪些高频命令？
**答**：
- 目录与查找：ls -la、pwd、find、tree；`open .` 用 Finder 打开当前目录、`code .` 用 VS Code 打开。
- 文本搜索：`grep -rn "keyword" src` 递归搜代码，排查最常用。
- 端口与进程：`lsof -i:3000` 查端口占用、`kill -9 <pid>` 结束进程；brew 管理软件。

```bash
grep -rn "TODO" src/            # 递归搜索代码
lsof -i:3000                    # 查看 3000 端口被哪个进程占用
kill -9 12345                   # 结束占用端口的进程
open http://localhost:5173      # 用默认浏览器打开本地服务
code .                          # VS Code 打开当前目录
brew install node               # Homebrew 安装软件
```

## 七、HTML 补充
