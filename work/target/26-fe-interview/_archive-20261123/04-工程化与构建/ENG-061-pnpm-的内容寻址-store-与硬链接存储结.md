---
title: [ENG-061] pnpm 的内容寻址 store 与硬链接存储结构是怎样的？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-061：pnpm 的内容寻址 store 与硬链接存储结构是怎样的？
**答**：
- store 按文件内容 hash 存储在全局目录（pnpm store path 可查），同一文件全机只存一份。
- 项目的 node_modules/.pnpm 下每个包版本一个目录，包内文件通过硬链接指向 store，零复制。
- 根 node_modules 里直接依赖是符号链接，指向 .pnpm 中的真实包，依赖闭包在 .pnpm 内自洽。
- 收益：安装快（硬链接近乎瞬时）、磁盘占用低、结构严格；注意硬链接跨磁盘分区会失效退化为复制。

```bash
# 查看全局 store 位置与占用
pnpm store path
du -sh $(pnpm store path)

# 验证硬链接：node_modules 中的文件与 store 中的文件 inode 相同
ls -i node_modules/.pnpm/lodash@4.17.21/node_modules/lodash/lodash.js
find $(pnpm store path) -name lodash.js -exec ls -i {} \;

# 定期清理 store 中不再被任何项目引用的包
pnpm store prune
```
