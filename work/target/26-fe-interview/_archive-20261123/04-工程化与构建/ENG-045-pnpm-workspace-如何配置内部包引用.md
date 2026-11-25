---
title: [ENG-045] pnpm workspace 如何配置内部包引用？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-045：pnpm workspace 如何配置内部包引用？
**答**：
- pnpm-workspace.yaml 声明 workspace 范围：apps/*、packages/*。
- 包之间用 workspace 协议引用：`"@repo/ui": "workspace:*"`，永远指向本地包而不是 npm。
- --filter 按包名执行脚本；-r 递归所有包。
- 内部包通常配 exports 字段暴露入口，构建方式可选源码直出或预构建。

```yaml
# pnpm-workspace.yaml
packages:
  - "apps/*"
  - "packages/*"

# apps/web/package.json 中引用内部包
# "dependencies": {
#   "@repo/ui": "workspace:*",
#   "@repo/utils": "workspace:^"
# }
```
