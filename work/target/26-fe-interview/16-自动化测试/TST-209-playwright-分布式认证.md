---
title: [TST-209] 分布式下登录态（storageState）如何复用而不必每用例登录？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-209：分布式下登录态（storageState）如何复用而不必每用例登录？
**答**：
- project.dependencies：auth 项目先跑 setup（登录存 storageState），依赖它的项目注入复用。
- 多角色（买家/卖家）各建独立 auth project，storageState 分文件管理。
- 分布式下 storageState 是文件，随 artifact 分发或每 shard 现场生成（避免过期）。
- 长跑套件注意会话过期：setup 里同时写入刷新令牌或按需重登。

```javascript
export default defineConfig({
  projects: [
    { name: 'setup-buyer', testMatch: /auth-buyer\.setup\.ts/ },
    { name: 'buyer', dependencies: ['setup-buyer'],
      use: { storageState: 'state/buyer.json' } },
  ],
});
r
```
