---
title: [BAS-116] tsconfig 的 include/exclude 怎么配？报错怎么排查？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-116：tsconfig 的 include/exclude 怎么配？报错怎么排查？
**答**：
- include/exclude 决定哪些文件参与编译；exclude 排不掉被 include 文件 import 进来的文件，files 可精确指定入口。
- 报错排查三步：看错误码定位类型不匹配 → 检查 target/module/lib 与 strict 配置 → `tsc --noEmit` 单独跑类型检查。
- 常见坑：装了包仍报"找不到模块"，多半缺 @types 声明或 moduleResolution 配置不当。

```json
{
  "compilerOptions": {
    "strict": true,
    "noEmit": true,
    "moduleResolution": "bundler"
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```
