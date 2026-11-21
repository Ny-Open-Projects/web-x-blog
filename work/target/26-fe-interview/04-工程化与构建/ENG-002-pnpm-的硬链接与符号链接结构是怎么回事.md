---
title: [ENG-002] pnpm 的硬链接与符号链接结构是怎么回事？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-002：pnpm 的硬链接与符号链接结构是怎么回事？
**答**：
- 所有包的真实文件保存在全局内容寻址 store 中，同一版本的全局只存一份。
- 项目的 node_modules/.pnpm 目录下，每个包通过硬链接指向 store，不复制文件。
- 项目根的 node_modules 里，直接依赖以符号链接指向 .pnpm 中的对应目录，形成严格层级。
- 收益：安装快、磁盘占用低、依赖结构严格，未声明的包 import 不进来。

```bash
# 查看全局 store 位置
pnpm store path

# 直接依赖以符号链接形式平铺在 node_modules
ls -la node_modules | head

# .pnpm 目录存放实际包，内部再硬链接到全局 store
ls node_modules/.pnpm | head

# 确认 store 被多项目共享
du -sh $(pnpm store path)
```
