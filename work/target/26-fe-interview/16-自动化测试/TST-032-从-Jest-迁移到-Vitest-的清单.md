---
title: [TST-032] 从 Jest 迁移到 Vitest 的实操清单和常见坑有哪些？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-032：从 Jest 迁移到 Vitest 的实操清单和常见坑有哪些？
**答**：
- 第一步配置替换：jest.config → vitest.config（transform/babel 相关配置直接删掉，alias 从 moduleNameMapper 换成 resolve.alias，格式 `'^@/(.*)$': '/src/$1'` 改成 `'@': '/src'`）。
- import 替换：`jest.fn → vi.fn`、`jest.spyOn → vi.spyOn`、`jest.mock → vi.mock`；`globals: true` 开启后 describe/it/expect 免 import，但 vi.* 建议仍显式导入。
- 定时器 API：`jest.useFakeTimers/advanceTimersByTime` → `vi.*`；新版 Vitest fake timers 默认不劫持 process.nextTick（参数 toFake 控制）。
- 常见坑：① `testEnvironment: 'jest-environment-jsdom'` 换成 `environment: 'jsdom'`；② ESM-only 包在 Jest 需 transformIgnorePatterns 白名单，Vitest 天然支持，直接删；③ snapshot 文件兼容，一般可直接复用；④ ESLint 插件从 eslint-plugin-jest 换 eslint-plugin-vitest。
- 追问钩子：迁移策略是「新模块 Vitest、存量 Jest 共存期」，用 vitest.workspace 把两套 runner 并进一个命令，最后逐步切换。

```bash
# 迁移脚本示例：批量替换 API 前缀
grep -rl "jest\.fn\|jest\.mock\|jest\.spyOn\|jest\.useFakeTimers" src --include="*.test.ts" \
  | xargs sed -i '' 's/jest\.fn/vi.fn/g; s/jest\.mock/vi.mock/g; s/jest\.spyOn/vi.spyOn/g; s/jest\.useFakeTimers/vi.useFakeTimers/g'
# 然后按文件头补 import { vi } from 'vitest'（或开 globals: true）
```
