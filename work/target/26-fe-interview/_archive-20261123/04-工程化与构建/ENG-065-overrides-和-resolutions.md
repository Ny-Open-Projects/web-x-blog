---
title: [ENG-065] overrides 和 resolutions 怎么做依赖仲裁？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-065：overrides 和 resolutions 怎么做依赖仲裁？
**答**：
- overrides（npm 8.3+ / pnpm 同名字段）与 resolutions（yarn）用于强制整棵依赖树中某包的版本。
- 典型场景：修一个无法等待上游发版的安全漏洞（CVE）、消除重复依赖、锁定被劫持的版本。
- 支持精确覆盖：可以只针对某个父依赖下钻（bar 只在 foo 里被替换成指定版本）。
- 它是临时止血手段，要登记技术债，等上游修复后移除，否则长期掩盖真实的版本漂移。

```json
{
  "overrides": {
    "lodash": "4.17.21",
    "semver": "^7.6.0",
    "some-lib": {
      "axios": "1.7.9"
    }
  }
}
```
